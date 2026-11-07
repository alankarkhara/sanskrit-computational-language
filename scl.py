#!/usr/bin/env python3
"""SCL 0.4 reference interpreter. Python >= 3.10; standard library only."""
from __future__ import annotations
import argparse
import ast
import dataclasses
import json
import pathlib
import re
import sys
import unicodedata
from morphology import MorphologyEngine, MorphologyError
from grammar import ContextEngine, ContextError

class SCLError(Exception):
    pass

class InflectedForm(str):
    """Validated lexical provenance survives variables and function returns."""
    def __new__(cls, surface):
        obj = super().__new__(cls, unicodedata.normalize('NFC', surface))
        obj.analysis = analyze_form(str(obj))
        return obj



ROLES = {'kartā', 'karma', 'karaṇa', 'sampradāna', 'apādāna', 'adhikaraṇa'}
# Closed, documented teaching paradigm; NOT an unrestricted Sanskrit morphological analyzer.
# Case does not uniquely determine semantic role. The mapping below is a set of
# admissible candidate roles, not a linguistic equivalence.
CASE_ROLES = {
    'prathamā': {'kartā'}, 'dvitīyā': {'karma'},
    'tṛtīyā': {'karaṇa', 'kartā'}, 'caturthī': {'sampradāna'},
    'pañcamī': {'apādāna'}, 'ṣaṣṭhī': set(),
    'saptamī': {'adhikaraṇa'}, 'sambodhana': set()
}
RAMA_FORMS = {
    'rāmaḥ': 'prathamā', 'rāmam': 'dvitīyā', 'rāmeṇa': 'tṛtīyā',
    'rāmāya': 'caturthī', 'rāmāt': 'pañcamī', 'rāmasya': 'ṣaṣṭhī',
    'rāme': 'saptamī', 'rāma': 'sambodhana'
}
def analyze_form(form):
    form=unicodedata.normalize('NFC',form)
    if form not in RAMA_FORMS:
        raise SCLError(f'Unsupported Sanskrit form {form!r}; v0.4 supports rāma singular paradigm only')
    case=RAMA_FORMS[form]
    return {'lemma':'rāma','case':case,'number':'ekavacana','gender':'puṃliṅga',
            'candidate_roles': sorted(CASE_ROLES[case])}

# Formal analysis is deliberately conservative. Effects are possible effects,
# not a promise that a runtime exception or call will occur.
EFFECTS = frozenset({'read', 'raise', 'io', 'call'})
BUILTIN_EFFECTS = {
    'darśaya': frozenset({'io'}),
    'padam': frozenset({'raise'}),
    'vibhakti': frozenset({'raise'}),
    'mūlarūpa': frozenset({'raise'}),
    'rūpam': frozenset({'raise'}),
    'rūpasaṅkhyā': frozenset({'raise'}),
    'kārakasaṅkhyā': frozenset({'raise'}),
    'kārakaparīkṣā': frozenset({'raise'}),
}

def expression_effects(node, function_effects=None):
    """Soundly overapproximates reads, known calls and runtime failure sites.

    Unknown user calls conservatively have all possible effects. The result is
    suitable for rewrite exclusion, not detailed interprocedural optimization.
    """
    function_effects = function_effects or {}
    tag = node[0]
    if tag == 'literal': return frozenset()
    if tag == 'name': return frozenset({'read', 'raise'})
    if tag == 'unary': return expression_effects(node[2], function_effects) | frozenset({'raise'})
    if tag == 'binary':
        eff = expression_effects(node[2], function_effects) | expression_effects(node[3], function_effects)
        # Python numeric operations, comparisons and dynamic typing may raise;
        # / and % also have zero-divisor exceptional behavior.
        return eff | frozenset({'raise'})
    if tag == 'call':
        name = node[1][1] if node[1][0] == 'name' else None
        eff = BUILTIN_EFFECTS.get(name, function_effects.get(name, EFFECTS))
        for child in node[2]: eff = eff | expression_effects(child, function_effects)
        for child in node[3].values(): eff = eff | expression_effects(child, function_effects)
        return eff | frozenset({'call'})
    raise SCLError(f'Unknown node for effect analysis: {tag}')

def typed_expression_judgment(checker, node):
    """Conservative type-and-effect judgment Γ ⊢ e : τ ! ε.

    Type '?' is a top/unknown approximation, not proof of a specific type.
    Any static-check error is propagated. The analysis is intentionally
    context-sensitive to checker scopes and registered signatures.
    """
    typ=checker.expr(node)
    return {'type':typ, 'effects':sorted(expression_effects(node)),
            'type_certainty':'known' if typ!='?' else 'unknown'}

def effect_report(statements):
    """A conservative effect upper bound for every expression-bearing statement."""
    reports=[]
    def visit(stmts, path):
        for i, node in enumerate(stmts):
            tag=node[0]; here=path+[i]
            if tag in ('declare','assign','return','expression'):
                reports.append({'path':here,'kind':tag,'effects':sorted(expression_effects(node[-1]))})
            elif tag=='function': visit(node[-1],here)
            elif tag=='if':
                reports.append({'path':here,'kind':'condition','effects':sorted(expression_effects(node[1]))})
                visit(node[2],here+[0]); visit(node[3],here+[1])
            elif tag=='while':
                reports.append({'path':here,'kind':'condition','effects':sorted(expression_effects(node[1]))})
                visit(node[2],here+[0])
    visit(statements,[])
    return reports

def rule_confluence_report(rules):
    """Only certifies a narrow sufficient non-overlap criterion.

    Identical root operators may overlap. Distinct roots may still overlap in
    nested contexts, so this report does NOT infer global confluence from roots.
    A single rule also can overlap with itself at proper subexpressions.
    We certify only the empty rule set; other sets need explicit proof.
    """
    return {'globally_certified': not bool(rules),
            'criterion':'empty rewrite relation (trivially confluent)' if not rules else 'unproved: root, nested, and self critical pairs not discharged',
            'potential_root_conflicts':[
              [a[1],b[1]] for i,a in enumerate(rules) for b in rules[i+1:]
              if a[3][:2]==b[3][:2]],
            'note':'Priority and cycle/budget checks do not imply confluence.'}

def grammatical_evidence(surface):
    """Morphological evidence: syntactic case, not a semantic kāraka claim."""
    a=analyze_form(surface)
    return {'surface':unicodedata.normalize('NFC',surface), 'lemma':a['lemma'],
            'vibhakti':a['case'], 'vacana':a['number'], 'liṅga':a['gender'],
            'semantic_role':None, 'candidate_roles':a['candidate_roles']}

def validate_contextual_karaka(evidence, requested_role):
    """Check a declared role against a provisional licensing table.

    Evidence alone never infers a unique semantic role. Licensing is necessary
    for this teaching grammar, not a full Sanskrit parse or semantic proof.
    """
    if requested_role not in ROLES: raise SCLError(f'Unknown kāraka: {requested_role}')
    if requested_role not in CASE_ROLES[evidence['vibhakti']]:
        raise SCLError(f"Grammatical role mismatch: {evidence['vibhakti']} does not license @{requested_role}")
    return True

def expr_may_raise(node):
    """Conservative check for potentially exceptional arithmetic expressions."""
    if node[0] == 'binary' and node[1] in ('/', '%'):
        return True
    if node[0] in ('binary', 'unary'):
        return any(expr_may_raise(ch) for ch in node[2:])
    if node[0] == 'call':
        return True
    return False

def named_captures(node):
    if node[0] == 'name':
        return {node[1]: 1}
    result = {}
    if node[0] in ('binary', 'unary'):
        for ch in node[2:]:
            for k, v in named_captures(ch).items(): result[k] = result.get(k, 0) + v
    return result

def rewrite_is_safe(rule, captures):
    """Do not erase/repeat potentially failing computations (conservative)."""
    lhs, rhs = named_captures(rule[3]), named_captures(rule[4])
    for name, tree in captures.items():
        if lhs.get(name, 0) != rhs.get(name, 0) and expr_may_raise(tree):
            return False
    return True

def expr_effectful(node):
    if node[0]=='call': return True
    if node[0] in ('binary','unary'): return any(expr_effectful(ch) for ch in node[2:])
    return False

def tree_size(n):
    return 1+sum(tree_size(ch) for ch in n[2:]) if n[0] in ('binary','unary') else 1

def rule_certificate(rule):
    # Conservative syntactic certificate: each occurrence of any metavariable
    # contributes one node; proves a decrease only if all capture sizes obey it.
    p,r=rule[3],rule[4]
    def skeleton(n):
        if n[0]=='name': return (0,{n[1]:1})
        if n[0] not in ('binary','unary'): return (1,{})
        count=1; vars={}
        for ch in n[2:]:
            a,b=skeleton(ch); count+=a
            for k,v in b.items(): vars[k]=vars.get(k,0)+v
        return count,vars
    pc,pv=skeleton(p); rc,rv=skeleton(r)
    return rc < pc and all(rv.get(k,0)<=v for k,v in pv.items())

KEYWORDS = {'mūlyam','parivartya','kāryam','pratyāvartaya','yadi','anyathā','yāvat','satya','asatya','ca','vā','na','niyama','prādhānya'}
TYPES = {'saṅkhyā','pāṭha','tarka'}
TOKEN_RE = re.compile(r'(?P<SPACE>\s+)|(?P<COMMENT>\#.*)|(?P<NUMBER>\d+(?:\.\d+)?)|(?P<STRING>"(?:\\.|[^"\\])*" )|(?P<IDENT>[^\W\d]\w*)|(?P<OP>==|!=|<=|>=|->|=>|[+*/%(){}:;,@=<>\-])',re.UNICODE|re.VERBOSE)
# Regex verbose mode: string pattern uses an explicit trailing space; grammar handles IAST identifiers.
@dataclasses.dataclass(frozen=True)
class Token:
    value:str
    line:int
    col:int

def lex(source:str)->list[Token]:
    source=unicodedata.normalize('NFC',source)
    tokens=[]; i=0; line=1; col=1
    while i<len(source):
        m=TOKEN_RE.match(source,i)
        if not m: raise SCLError(f'Line {line}, column {col}: unexpected character {source[i]!r}')
        value=m.group(); kind=m.lastgroup
        if kind not in ('SPACE','COMMENT'):
            tokens.append(Token(value,line,col))
        newlines=value.count('\n')
        if newlines: line+=newlines; col=len(value.rsplit('\n',1)[-1])+1
        else: col+=len(value)
        i=m.end()
    tokens.append(Token('<EOF>',line,col))
    return tokens

class Parser:
    def __init__(self,tokens): self.ts=tokens; self.i=0
    def peek(self): return self.ts[self.i].value
    def pop(self): t=self.ts[self.i]; self.i+=1; return t.value
    def take(self,x):
        if self.peek()==x: self.pop(); return True
        return False
    def expect(self,x):
        if not self.take(x):
            t=self.ts[self.i]; raise SCLError(f'Line {t.line}, column {t.col}: expected {x!r}, got {t.value!r}')
    def ident(self):
        t=self.ts[self.i]; v=t.value
        if not v.isidentifier() or v in KEYWORDS: raise SCLError(f'Line {t.line}, column {t.col}: expected identifier, got {v!r}')
        self.pop(); return v
    def program(self):
        nodes=[]
        while self.peek()!='<EOF>': nodes.append(self.statement())
        return nodes
    def block(self):
        self.expect('{'); nodes=[]
        while self.peek()!='}':
            if self.peek()=='<EOF>': self.expect('}')
            nodes.append(self.statement())
        self.expect('}'); return nodes
    def statement(self):
        v=self.peek()
        if v=='niyama':
            self.pop(); name=self.ident(); self.expect('prādhānya')
            priority=self.pop()
            if not priority.isdecimal(): raise SCLError('Rule priority must be a nonnegative integer')
            self.expect(':'); pattern=self.expr(); self.expect('=>')
            replacement=self.expr(); self.take(';')
            return ('rule',name,int(priority),pattern,replacement)
        if v in ('mūlyam','parivartya'):
            mode=self.pop(); name=self.ident(); annotation=None
            if self.take(':'): annotation=self.ident(); self.checktype(annotation)
            self.expect('='); expression=self.expr(); self.take(';')
            return ('declare',mode,name,annotation,expression)
        if v=='kāryam':
            self.pop(); name=self.ident(); self.expect('('); params=[]
            if self.peek()!=')':
                while True:
                    role_or_name=self.ident(); role=None; pname=role_or_name
                    if self.take(':'):
                        typ=self.ident(); self.checktype(typ)
                    else: raise SCLError('Function parameters require explicit type annotations')
                    if self.take('@'):
                        role=self.ident()
                    if role is not None and role not in ROLES: raise SCLError(f'Unknown kāraka role: {role}')
                    params.append((pname,typ,role))
                    if not self.take(','): break
            self.expect(')'); ret=None
            if self.take('->'): ret=self.ident(); self.checktype(ret)
            return ('function',name,params,ret,self.block())
        if v=='yadi':
            self.pop(); cond=self.expr(); yes=self.block(); no=[]
            if self.take('anyathā'): no=self.block()
            return ('if',cond,yes,no)
        if v=='yāvat':
            self.pop(); cond=self.expr(); return ('while',cond,self.block())
        if v=='pratyāvartaya':
            self.pop(); e=self.expr(); self.take(';'); return ('return',e)
        if v.isidentifier() and self.ts[self.i+1].value=='=':
            name=self.pop(); self.pop(); e=self.expr(); self.take(';'); return ('assign',name,e)
        e=self.expr(); self.take(';'); return ('expression',e)
    def checktype(self,t):
        if t not in TYPES: raise SCLError(f'Unsupported type {t!r}; choose {sorted(TYPES)}')
    BP={'vā':1,'ca':2,'==':3,'!=':3,'<':4,'>':4,'<=':4,'>=':4,'+':5,'-':5,'*':6,'/':6,'%':6}
    def expr(self,minbp=0):
        tok=self.pop()
        if tok=='-': left=('unary','-',self.expr(7))
        elif tok=='na': left=('unary','na',self.expr(7))
        elif tok=='(':
            left=self.expr(); self.expect(')')
        elif tok in ('satya','asatya'): left=('literal',tok=='satya')
        elif tok.startswith('"'):
            try: left=('literal',ast.literal_eval(tok))
            except (SyntaxError,ValueError): raise SCLError('Invalid string literal')
        elif tok[0].isdigit(): left=('literal',float(tok) if '.' in tok else int(tok))
        elif tok.isidentifier() and tok not in KEYWORDS: left=('name',tok)
        else: raise SCLError(f'Invalid expression starting with {tok!r}')
        while True:
            if self.peek()=='(' and 8>=minbp:
                self.pop(); args=[]; kwargs={}
                if self.peek()!=')':
                    while True:
                        if self.peek().isidentifier() and self.ts[self.i+1].value=='=':
                            key=self.pop(); self.pop()
                            if key in kwargs: raise SCLError(f'Duplicate named argument {key}')
                            kwargs[key]=self.expr()
                        else: args.append(self.expr())
                        if not self.take(','): break
                self.expect(')'); left=('call',left,args,kwargs); continue
            op=self.peek(); bp=self.BP.get(op,0)
            if bp<minbp or bp==0: break
            self.pop(); right=self.expr(bp+1); left=('binary',op,left,right)
        return left

@dataclasses.dataclass
class Binding:
    value:object
    mutable:bool
    declared_type:str|None

@dataclasses.dataclass
class Function:
    params:list
    ret:str|None
    body:list

class Returned(Exception):
    def __init__(self,value): self.value=value

def validate_params(params):
    names=[p for p,_,_ in params]
    roles=[r for _,_,r in params if r]
    if len(names)!=len(set(names)): raise SCLError('Duplicate parameter names')
    if len(roles)!=len(set(roles)): raise SCLError('Duplicate kāraka roles')
    # A role alias may not collide with another parameter's name.
    for p,_,r in params:
        if r in names and r!=p: raise SCLError(f'Ambiguous role alias: {r}')

# Explicit, deterministic, first-order expression rewriting. Not Sanskrit morphology.
def _match(pattern, tree, captures):
    if pattern[0]=='name':
        key=pattern[1]
        if key in captures: return captures[key]==tree
        captures[key]=tree; return True
    if not isinstance(tree,tuple) or pattern[0]!=tree[0] or len(pattern)!=len(tree): return False
    if pattern[0]=='literal': return pattern==tree
    if pattern[0] in ('binary','unary') and pattern[1]!=tree[1]: return False
    if pattern[0] not in ('binary','unary'): return pattern==tree
    return all(_match(a,b,captures) for a,b in zip(pattern[2:],tree[2:]))

def _substitute(template,captures):
    if template[0]=='name': return captures[template[1]]
    if template[0] in ('binary','unary'):
        return (template[0],template[1],*(_substitute(x,captures) for x in template[2:]))
    return template

def _variables(node):
    if node[0]=='name': return {node[1]}
    if node[0] in ('binary','unary'): return set().union(*(_variables(x) for x in node[2:]))
    return set()

def _validate_rules(nodes):
    rules=[]; names=set()
    for n in nodes:
        if n[0]!='rule': continue
        _,name,priority,pattern,replace=n
        if name in names: raise SCLError(f'Duplicate rule name: {name}')
        names.add(name)
        if pattern[0] not in ('binary','unary'): raise SCLError(f'Rule {name}: pattern must start with operator')
        if _variables(replace)-_variables(pattern): raise SCLError(f'Rule {name}: unbound replacement variable')
        rules.append(n)
    return rules

from proof_kernel.integration import certify_local, verify_ir_certificates
from proof_kernel.symbolic import certify_symbolic
from proof_kernel.confluence import analyze_rules

class Rewriter:
    def __init__(self,rules,max_rewrites=1000, rewrite_policy='legacy'):
        self.rules=rules; self.max_rewrites=max_rewrites; self.count=0; self.rewrite_policy=rewrite_policy; self.certificates=[]
    def rewrite(self,tree):
        seen=set()
        while True:
            marker=repr(tree)
            if marker in seen: raise SCLError('Rewrite cycle detected')
            seen.add(marker)
            new=self._pass(tree)
            if new==tree: return tree
            tree=new
    def _pass(self,n):
        kind=n[0]
        if kind in ('binary','unary'):
            n=(kind,n[1],*(self.rewrite(x) for x in n[2:]))
        elif kind=='call':
            n=('call',n[1],[self.rewrite(x) for x in n[2]],{k:self.rewrite(x) for k,x in n[3].items()})
        # Do not apply user rewrite rules across calls: preserving effects requires
        # an effect system. Pure subtrees without calls are eligible.
        if expr_effectful(n): return n
        matches=[]
        for rule in self.rules:
            captures={}
            if _match(rule[3],n,captures) and rewrite_is_safe(rule,captures):
                candidate=_substitute(rule[4],captures)
                if self.rewrite_policy in ('checked','formal') and not checked_rewrite(n,candidate):
                    continue
                if self.rewrite_policy=='certified' and certify_local(n,candidate) is None:
                    continue
                if self.rewrite_policy in ('symbolic','symbolic-confluent') and certify_symbolic(n,candidate) is None:
                    continue
                matches.append((rule[2],rule[1],candidate))
        if not matches: return n
        priority=max(x[0] for x in matches)
        winners=[x for x in matches if x[0]==priority]
        if any(x[2]!=winners[0][2] for x in winners[1:]):
            raise SCLError('Ambiguous rewrite at priority '+str(priority)+': '+', '.join(x[1] for x in winners))
        replacement=winners[0][2]
        if replacement==n: return n
        if self.rewrite_policy=='certified':
            cert=certify_local(n,replacement)
            if cert is None: raise SCLError('Internal proof certificate failure')
            self.certificates.append({**cert,'rule_names':[x[1] for x in winners]})
        if self.rewrite_policy in ('symbolic','symbolic-confluent'):
            cert=certify_symbolic(n,replacement)
            if cert is None: raise SCLError('Internal symbolic certificate failure')
            self.certificates.append(cert)
        self.count+=1
        if self.count>self.max_rewrites: raise SCLError('Rewrite budget exceeded')
        return replacement

def _rewrite_stmt(n,rewrite):
    k=n[0]
    if k in ('declare','assign','return','expression'):
        return (*n[:-1],rewrite(n[-1]))
    if k=='function': return (*n[:-1],[_rewrite_stmt(x,rewrite) for x in n[-1]])
    if k=='if': return ('if',rewrite(n[1]),[_rewrite_stmt(x,rewrite) for x in n[2]],[_rewrite_stmt(x,rewrite) for x in n[3]])
    if k=='while': return ('while',rewrite(n[1]),[_rewrite_stmt(x,rewrite) for x in n[2]])
    return n

def checked_rewrite(original, replacement):
    """Admit only ground integer transformations that can be evaluated exactly.

    This is a deliberately narrow decidable subset. No variables, calls, floating
    point values, booleans, exceptions, division, or short-circuit expressions.
    """
    def integer_value(node):
        if node[0]=='literal' and type(node[1]) is int: return node[1]
        if node[0]=='unary' and node[1]=='-': return -integer_value(node[2])
        if node[0]=='binary' and node[1] in ('+','-','*'):
            a=integer_value(node[2]); b=integer_value(node[3]);
            return {'+':lambda:a+b,'-':lambda:a-b,'*':lambda:a*b}[node[1]]()
        raise ValueError('non-ground or non-integer expression')
    try:
        return integer_value(original)==integer_value(replacement)
    except (ValueError,TypeError,RecursionError):
        return False


def compile_source(source,max_rewrites=1000,rewrite_policy='legacy'):
    if rewrite_policy not in ('legacy','checked','formal','certified','symbolic','symbolic-confluent'):
        raise SCLError('Unknown rewrite policy; choose legacy, checked, formal or certified')
    ast_nodes=Parser(lex(source)).program()
    rules=_validate_rules(ast_nodes)
    # Check original program too: rewriting must not conceal undefined names/types.
    StaticChecker().check([n for n in ast_nodes if n[0]!='rule'])
    confluence=analyze_rules(rules)
    if rewrite_policy=='symbolic-confluent' and not confluence['confluence_certified']:
        raise SCLError('Rule set lacks restricted first-order confluence certificate')
    rw=Rewriter(rules,max_rewrites,rewrite_policy)
    original=[n for n in ast_nodes if n[0]!='rule']
    lowered=[_rewrite_stmt(n,rw.rewrite) for n in original]
    StaticChecker().check(lowered)
    # JSON-serializable, explicit intermediate representation (tree-form IR).
    return {'version':'SCL-IR/0.4','rules':[{'name':r[1],'priority':r[2],'structural_termination_certificate':rule_certificate(r)} for r in rules],
            'rewrite_count':rw.count,'certificates':rw.certificates,'statements':lowered, 'rewrite_policy':rewrite_policy,
            'ir_schema':{'major':0,'minor':4,'patch':1},
            'formal':{'analysis_schema':'SCL-Formal/0.4.2', 'effects_before':effect_report(original), 'effects_after':effect_report(lowered),
                      'confluence':confluence,
                      'rewrite_guarantee':('integer polynomial identity for all typed integer assignments' if rewrite_policy in ('symbolic','symbolic-confluent') else 'SCL-F0 closed pure total local equivalence with replayable certificates' if rewrite_policy=='certified' else ('ground exact-integer arithmetic equality at accepted redexes' if rewrite_policy in ('checked','formal') else 'no universal semantic guarantee')),
                      'morphology_policy':'case evidence separate from contextual semantic role licensing'}}

class StaticChecker:
    """Conservative compile-time checks; unknown inferred types defer to runtime."""
    def __init__(self): self.signatures={}; self.scopes=[{}]; self.return_type=None
    def lookup(self,name):
        for scope in reversed(self.scopes):
            if name in scope: return scope[name]
        raise SCLError(f'Undefined variable: {name}')
    def expr(self,node):
        tag=node[0]
        if tag=='literal':
            v=node[1]; return 'tarka' if type(v) is bool else 'pāṭha' if type(v) is str else 'saṅkhyā'
        if tag=='name': return self.lookup(node[1])[0]
        if tag=='unary':
            typ=self.expr(node[2]); expected='tarka' if node[1]=='na' else 'saṅkhyā'
            self.compat(expected,typ); return expected
        if tag=='binary':
            op=node[1]; a=self.expr(node[2]); b=self.expr(node[3])
            if op in ('ca','vā'):
                self.compat('tarka',a); self.compat('tarka',b); return 'tarka'
            if op in ('==','!='):
                if a!='?' and b!='?' and a!=b: raise SCLError(f'Incompatible comparison: {a} and {b}')
                return 'tarka'
            if op in ('<','>','<=','>='):
                self.compat('saṅkhyā',a); self.compat('saṅkhyā',b); return 'tarka'
            if op=='+':
                if a!='?' and b!='?' and a!=b: raise SCLError(f'Incompatible addition: {a} and {b}')
                if a not in ('saṅkhyā','pāṭha','?') or b not in ('saṅkhyā','pāṭha','?'): raise SCLError('Invalid addition operands')
                return a if a==b else '?'
            self.compat('saṅkhyā',a); self.compat('saṅkhyā',b); return 'saṅkhyā'
        if tag=='call':
            callee=node[1]
            if callee[0]!='name': raise SCLError('Only named functions can be called')
            name=callee[1]; args=node[2]; kwargs=node[3]
            if name=='sandhi_pramāṇa':
                if kwargs or len(args)!=2: raise SCLError('sandhi_pramāṇa requires two text arguments')
                for a in args:self.compat('pāṭha',self.expr(a))
                return 'pāṭha'
            if name=='tiṅrūpam':
                if kwargs or len(args)!=3: raise SCLError('tiṅrūpam requires root, person, number')
                self.compat('pāṭha',self.expr(args[0])); self.compat('saṅkhyā',self.expr(args[1])); self.compat('pāṭha',self.expr(args[2])); return 'pāṭha'
            if name=='rūpam':
                if kwargs or len(args)!=3: raise SCLError('rūpam requires lemma, case, number')
                for a in args: self.compat('pāṭha',self.expr(a))
                return 'pāṭha'
            if name in ('kārakasaṅkhyā','kārakaparīkṣā'):
                arity=2 if name=='kārakasaṅkhyā' else 3
                if kwargs or len(args)!=arity: raise SCLError(f'{name} requires {arity} text arguments')
                for a in args: self.compat('pāṭha',self.expr(a))
                return 'saṅkhyā' if name=='kārakasaṅkhyā' else 'tarka'
            if name=='rūpasaṅkhyā':
                if kwargs or len(args)!=1: raise SCLError('rūpasaṅkhyā requires one surface text')
                self.compat('pāṭha',self.expr(args[0])); return 'saṅkhyā'
            if name in ('vibhakti','mūlarūpa'):
                if kwargs or len(args)!=1: raise SCLError(f'{name} requires one positional argument')
                self.compat('pāṭha', self.expr(args[0])); return 'pāṭha'
            if name=='padam':
                if kwargs or len(args)!=1: raise SCLError('padam requires one positional argument')
                self.compat('pāṭha', self.expr(args[0])); return 'pāṭha'
            if name=='darśaya':
                if kwargs: raise SCLError('darśaya does not accept named arguments')
                for a in args: self.expr(a)
                return '?'
            if name not in self.signatures: raise SCLError(f'Undefined function: {name}')
            params,ret=self.signatures[name]
            if len(args)>len(params): raise SCLError(f'Too many arguments for {name}')
            bound={}
            for (p,t,_),val in zip(params,args): bound[p]=val
            for key,val in kwargs.items():
                matches=[p for p,_,r in params if p==key or r==key]
                if len(matches)!=1: raise SCLError(f'Unknown or ambiguous argument/role {key}')
                p=matches[0]
                if p in bound: raise SCLError(f'Duplicate argument or role {key}')
                bound[p]=val
            if len(bound)!=len(params): raise SCLError(f'Missing function arguments for {name}')
            for p,t,_ in params: self.compat(t,self.expr(bound[p]))
            return ret or '?'
        raise SCLError(f'Unsupported expression: {tag}')
    @staticmethod
    def compat(expected,actual):
        if expected not in (None,'?') and actual!='?' and expected!=actual:
            raise SCLError(f'Static type error: Expected {expected}, got {actual}')
    def block(self,statements,scoped=False):
        if scoped: self.scopes.append({})
        try:
            for node in statements:
                kind=node[0]
                if kind=='function':
                    continue
                if kind=='declare':
                    _,mode,name,t,e=node
                    if name in self.scopes[-1]: raise SCLError(f'Duplicate declaration: {name}')
                    inferred=self.expr(e); self.compat(t,inferred)
                    self.scopes[-1][name]=(t or inferred,mode=='parivartya')
                elif kind=='assign':
                    _,name,e=node; typ,mutable=self.lookup(name)
                    if not mutable: raise SCLError(f'Cannot assign immutable variable: {name}')
                    self.compat(typ,self.expr(e))
                elif kind=='if':
                    self.compat('tarka',self.expr(node[1])); self.block(node[2]); self.block(node[3])
                elif kind=='while':
                    self.compat('tarka',self.expr(node[1])); self.block(node[2])
                elif kind=='return':
                    if self.return_type is None: raise SCLError('pratyāvartaya outside function')
                    self.compat(self.return_type,self.expr(node[1]))
                elif kind=='expression': self.expr(node[1])
                else: raise SCLError(f'Unsupported statement: {kind}')
        finally:
            if scoped: self.scopes.pop()
    def check(self,nodes):
        # Collect signatures before checking expressions: forward references supported.
        for node in nodes:
            if node[0]=='function':
                _,name,params,ret,body=node; validate_params(params)
                if name in ('darśaya','padam','vibhakti','mūlarūpa','rūpam','rūpasaṅkhyā','tiṅrūpam','kārakasaṅkhyā','kārakaparīkṣā') or name in self.signatures: raise SCLError(f'Duplicate or reserved function: {name}')
                self.signatures[name]=(params,ret)
        # Check function bodies with parameter bindings and globals already declared.
        self.block(nodes)
        for node in nodes:
            if node[0]=='function':
                _,name,params,ret,body=node
                old=self.return_type; self.return_type=ret or '?'
                self.scopes.append({p:(t,False) for p,t,_ in params})
                try: self.block(body)
                finally: self.scopes.pop(); self.return_type=old

class Runtime:
    def __init__(self,output=print,max_steps=100000):
        self.output=output; self.max_steps=max_steps; self.steps=0
        self.frames=[{}]
        self.functions={}
    def tick(self):
        self.steps+=1
        if self.steps>self.max_steps: raise SCLError('Execution step limit exceeded')
    def locate(self,name):
        for frame in reversed(self.frames):
            if name in frame: return frame[name]
        raise SCLError(f'Undefined variable: {name}')
    @staticmethod
    def matches(value,annotation):
        if annotation=='saṅkhyā': return type(value) in (int,float)
        if annotation=='pāṭha': return isinstance(value,str)
        if annotation=='tarka': return type(value) is bool
        return True
    def ensure(self,value,annotation):
        if annotation and not self.matches(value,annotation): raise SCLError(f'Expected {annotation}, received {type(value).__name__}')
    def evaluate(self,n):
        kind=n[0]
        if kind=='literal': return n[1]
        if kind=='name': return self.locate(n[1]).value
        if kind=='unary':
            x=self.evaluate(n[2]); return -x if n[1]=='-' else not x
        if kind=='binary':
            op=n[1]; x=self.evaluate(n[2])
            if op=='ca': return bool(x) and bool(self.evaluate(n[3]))
            if op=='vā': return bool(x) or bool(self.evaluate(n[3]))
            y=self.evaluate(n[3])
            try:
                return {'+':lambda:x+y,'-':lambda:x-y,'*':lambda:x*y,'/':lambda:x/y,'%':lambda:x%y,'==':lambda:x==y,'!=':lambda:x!=y,'<':lambda:x<y,'>':lambda:x>y,'<=':lambda:x<=y,'>=':lambda:x>=y}[op]()
            except (TypeError,ZeroDivisionError,OverflowError) as exc: raise SCLError(str(exc)) from exc
        if kind=='call':
            callee=n[1]
            if callee[0]!='name': raise SCLError('Only named functions can be called')
            name=callee[1]
            args=[self.evaluate(a) for a in n[2]]
            kwargs={k:self.evaluate(v) for k,v in n[3].items()}
            if name=='sandhi_pramāṇa':
                if kwargs or len(args)!=2 or any(type(a) is not str for a in args):raise SCLError('sandhi_pramāṇa needs two strings')
                try:
                    from grammar.native064 import derive
                    return derive(*args)['output']
                except ValueError as exc:raise SCLError(str(exc)) from exc
            if name in ('kārakasaṅkhyā','kārakaparīkṣā'):
                arity=2 if name=='kārakasaṅkhyā' else 3
                if kwargs or len(args)!=arity or any(type(a) is not str for a in args):
                    raise SCLError(f'{name} expects {arity} text arguments')
                try:
                    found=ContextEngine().candidates(args[0],args[1],args[2] if arity==3 else None)
                    return len(found) if arity==2 else bool(found)
                except ContextError as exc: raise SCLError(str(exc)) from exc
            if name=='tiṅrūpam':
                if kwargs or len(args)!=3 or type(args[0]) is not str or type(args[1]) is not int or type(args[2]) is not str: raise SCLError('tiṅrūpam expects root, integer person, number')
                try:
                    from grammar.verbal_059 import derive
                    return derive(args[0],args[1],args[2])['payload']['result']
                except ValueError as exc: raise SCLError(str(exc)) from exc
            if name in ('rūpam','rūpasaṅkhyā'):
                if kwargs: raise SCLError(f'{name} does not accept named arguments')
                if any(type(a) is not str for a in args): raise SCLError('Morphology requires Sanskrit text')
                try:
                    engine=MorphologyEngine()
                    return engine.generate(*args).surface if name=='rūpam' and len(args)==3 else (len(engine.analyze(args[0])) if name=='rūpasaṅkhyā' and len(args)==1 else (_ for _ in ()).throw(SCLError(f'Wrong argument count for {name}')))
                except MorphologyError as exc: raise SCLError(str(exc)) from exc
            if name in ('vibhakti','mūlarūpa','padam'):
                if kwargs or len(args)!=1: raise SCLError(f'{name} requires one positional argument')
                if type(args[0]) is not str: raise SCLError(f'{name} expects Sanskrit text')
                analysis=analyze_form(args[0]); return (analysis['case'] if name=='vibhakti' else analysis['lemma'] if name=='mūlarūpa' else InflectedForm(args[0]))
            if name=='darśaya':
                if kwargs: raise SCLError('darśaya does not accept named arguments')
                self.output(*args); return None
            if name not in self.functions: raise SCLError(f'Undefined function: {name}')
            fn=self.functions[name]; params=fn.params
            if len(args)>len(params): raise SCLError('Too many positional arguments')
            values={}
            for (p,_,_),v in zip(params,args): values[p]=v
            for k,v in kwargs.items():
                matches=[p for p,_,role in params if k==p or k==role]
                if len(matches)!=1: raise SCLError(f'Unknown or ambiguous argument/role {k}')
                target=matches[0]
                if target in values: raise SCLError(f'Duplicate argument or role {k}')
                values[target]=v
            if len(values)!=len(params): raise SCLError('Missing function arguments')
            frame={}
            for p,t,_ in params:
                self.ensure(values[p],t)
                # Lexical provenance is attached to the value, not to call syntax.
                # It survives immutable/mutable bindings, aliases, and returns.
                role=next((rr for pp,_,rr in params if pp==p),None)
                if role and isinstance(values[p],InflectedForm):
                    validate_contextual_karaka(grammatical_evidence(str(values[p])),role)
                frame[p]=Binding(values[p],False,t)
            if len(self.frames)>128: raise SCLError('Maximum recursion depth reached')
            self.frames.append(frame)
            try:
                try: self.execute(fn.body); result=None
                except Returned as returned: result=returned.value
            finally: self.frames.pop()
            self.ensure(result,fn.ret)
            return result
        raise SCLError(f'Unknown AST node {kind}')
    def execute(self,stmts):
        for stmt in stmts:
            self.tick(); kind=stmt[0]
            if kind=='declare':
                _,mode,name,typ,exp=stmt
                if name in self.frames[-1]: raise SCLError(f'Duplicate declaration: {name}')
                value=self.evaluate(exp); self.ensure(value,typ)
                self.frames[-1][name]=Binding(value,mode=='parivartya',typ)
            elif kind=='assign':
                _,name,exp=stmt; bind=self.locate(name)
                if not bind.mutable: raise SCLError(f'Cannot assign immutable variable: {name}')
                value=self.evaluate(exp); self.ensure(value,bind.declared_type); bind.value=value
            elif kind=='function':
                _,name,params,ret,body=stmt
                if name in self.functions: raise SCLError(f'Duplicate function: {name}')
                validate_params(params)
                self.functions[name]=Function(params,ret,body)
            elif kind=='if': self.execute(stmt[2] if self.evaluate(stmt[1]) else stmt[3])
            elif kind=='while':
                while self.evaluate(stmt[1]): self.tick(); self.execute(stmt[2])
            elif kind=='return': raise Returned(self.evaluate(stmt[1]))
            elif kind=='expression': self.evaluate(stmt[1])
            else: raise SCLError(f'Invalid statement: {kind}')

def run(source:str, output=print, max_steps:int=100000, rewrite_policy='legacy'):
    ir=compile_source(source,rewrite_policy=rewrite_policy)
    runtime=Runtime(output,max_steps)
    try: runtime.execute(ir['statements'])
    except Returned: raise SCLError('pratyāvartaya outside function')
    return runtime

def main():
    ap=argparse.ArgumentParser(description='SCL 0.4 IAST Sanskrit interpreter')
    ap.add_argument('file',type=pathlib.Path)
    ap.add_argument('--max-steps',type=int,default=100000)
    ap.add_argument('--emit-ir',action='store_true',help='Print lowered JSON IR without executing')
    ap.add_argument('--max-rewrites',type=int,default=1000)
    ap.add_argument('--rewrite-policy',choices=('legacy','checked','formal','certified','symbolic','symbolic-confluent'),default='legacy')
    args=ap.parse_args()
    try:
        source=args.file.read_text(encoding='utf-8')
        if args.emit_ir:
            print(json.dumps(compile_source(source,args.max_rewrites,args.rewrite_policy),ensure_ascii=False,indent=2))
        else:
            ir=compile_source(source,args.max_rewrites,args.rewrite_policy)
            runtime=Runtime(max_steps=args.max_steps)
            runtime.execute(ir['statements'])
    except SCLError as exc:
        print('SCL error:',exc,file=sys.stderr); return 1
    return 0

if __name__=='__main__': raise SystemExit(main())
