"""Finite-model semantic audit for SCL 0.8.3. Not a proof assistant.

Exercises all seven rewrite identities against the real SCL evaluator, including
error behavior, lazy branches, nested terms and explicit finite-fuel differences.
"""
import json
from itertools import product
from core080.language import compile_program,run_ir,SclError
from core080.rules081 import compile_081,DEFAULT_RULES

VALUES = ('0','1','-1','2','-2','9223372036854775807','-9223372036854775808')
RIGHTS = ('0','1','-1','2','(bhāga 1 0)','(yoga 9223372036854775807 1)')

def observation(ir, fuel):
    try: return ('value', tuple(run_ir(ir,steps=fuel)))
    except (SclError,OverflowError,ZeroDivisionError) as err:
        return ('error',str(err))

def program(e): return '(krama (darśaya '+e+'))'

def audit():
    cases=[]
    for op,neutral,side in (('yoga','0','left'),('yoga','0','right'),('vyavakalana','0','right'),('guṇana','1','left'),('guṇana','1','right')):
        for e in RIGHTS + VALUES:
            expression='('+op+' '+neutral+' '+e+')' if side=='left' else '('+op+' '+e+' '+neutral+')'
            cases.append((op+'-'+side,expression))
    for condition, branch in (('satya',2),('asatya',3)):
        for a,b in product(RIGHTS, repeat=2):
            cases.append(('if-'+condition,'(yadi '+condition+' '+a+' '+b+')'))
    for a,b in product(('0','1','(yoga 0 2)','(bhāga 1 0)'),repeat=2):
        cases.append(('nested','(yoga 0 (yadi satya '+a+' '+b+'))'))
    outcomes=[]; differences=[]; nontrivial=0
    for category,e in cases:
        src=program(e)
        initial=compile_program(src)
        comp=compile_081(src)
        target=comp['target_ir']
        if comp['steps']: nontrivial+=1
        before=observation(initial,100000)
        after=observation(target,100000)
        if before!=after: differences.append({'category':category,'expression':e,'before':before,'after':after})
        outcomes.append({'category':category,'observation':before[0], 'rewrite_steps':len(comp['steps'])})
    fuel_counterexample='(krama (darśaya (yoga 0 1)))'
    aa=compile_program(fuel_counterexample); bb=compile_081(fuel_counterexample)['target_ir']
    budget={'source':observation(aa,2),'target':observation(bb,2)}
    return {'schema':'scl-finite-model-083','scope':'finite selected expressions; not mathematical proof',
            'rewrite_rules':list(DEFAULT_RULES),'cases':len(cases),'cases_with_rewrites':nontrivial,
            'observational_differences_high_fuel':differences,'exact_fuel_counterexample':budget,
            'fuel_equivalence':budget['source']==budget['target'],'outcomes':outcomes}

if __name__=='__main__':
    print(json.dumps(audit(),indent=2,ensure_ascii=False))
