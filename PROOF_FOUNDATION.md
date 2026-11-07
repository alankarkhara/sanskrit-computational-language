# SCL 0.4.3 — Machine-checkable proof foundation

## Status

This release contains an **executable proof checker with human-readable inductive arguments**. It is NOT a proof encoded in Lean, Coq, or Isabelle, nor a verified implementation of the full SCL interpreter. `scl.py`, its default rewrite policy, and all prior files remain unchanged from v0.4.2. The new `proof_kernel/` is opt-in and separately testable.

## F0 syntax and typing

Closed terms: `e ::= integer | true | false | neg e | not e | e + e | e - e | e * e | e < e | e == e | e and e | e or e`.

Types `τ ::= Int | Bool`. `integer : Int`; Boolean literal `: Bool`; `neg : Int→Int`, `not : Bool→Bool`, arithmetic `Int×Int→Int`, comparisons `Int×Int→Bool`, Boolean operators `Bool×Bool→Bool`. There are **no** variables, exceptions, floats, division, function calls or I/O. Boolean operators are **strict** in F0 (not short-circuit); this differs from full SCL and is not silently substituted into it.

F0 is call-by-value, left-to-right: reduce the operand on the left first, then the operand on the right, then the total primitive operation. Evaluation uses exact, unbounded mathematical integers (modeled via Python int), subject in practice to machine resource limits.

## Theorems and proof sketches

**Canonical forms.** Any closed value of type `Int` is `Num(n)`; any closed value of type `Bool` is `Bool(b)`. By inspection of constructors and typing rules.

**Progress (F0).** If `⊢ e : τ`, either `e` is a value or there exists `e′` with `e → e′`. Structural induction on typing. Unary and binary operands step by the induction hypothesis; if operands are values, canonical forms give a defined primitive reduction. Each primitive operation is total on its declared domain.

**Preservation (F0).** If `⊢ e : τ` and `e → e′`, then `⊢ e′ : τ`. Structural induction on the reduction rule. Congruence steps retain operand type by induction; primitive rules return the result type of their typing rule.

**Termination (F0).** Every well-typed reduction strictly decreases AST node count: congruence decreases its operand; a primitive replaces an operator-plus-value-children by one literal. Natural numbers are well founded. Together with progress, every F0 expression reaches a value, ignoring physical runtime limits.

`numeric.check_derivation` replays each reduction and checks a type invariant and strict node-size decrease. The test suite checks 250 seeded random arithmetic expressions as well as specific Boolean and ill-typed cases. Finite testing is evidence about the implementation, not the general proof.

## First-order rewrite theory

Terms are made of declared fixed-arity function symbols and variables; rules `l → r` are first-order. The certified subset imposes: (1) a non-variable LHS, (2) LHS left-linearity, (3) `Vars(r) ⊆ Vars(l)`, (4) no variable gains multiplicity in RHS, and (5) the number of function nodes in `l` exceeds that of `r`.

**Termination proof.** For any substitution σ, `|lσ| − |rσ|` equals the positive difference in function-node skeletons plus nonnegative contributions from variables removed or reduced in multiplicity. Thus every rewrite in every context strictly decreases total term size. This proves strong normalization for finite terms.

**Critical-pair generation.** For each ordered pair of rules, rename variables apart; unify the first rule's LHS with each non-variable subterm of the second rule's LHS; instantiate both peak branches. Trivial identical-rule root self-overlaps are omitted. Generated pairs are checked for joinability by exploring reachable terms; both witness paths are checked step by step. State-exploration limits raise an error and must NEVER be interpreted as either certification or nonconfluence.

**Confluence theorem for this subset.** Left-linear first-order rewrite systems satisfy the critical-pair lemma (every critical pair joinable implies local confluence). The checked strict size decrease supplies termination, so Newman's lemma yields global confluence. This is a conventional mathematical proof argument, not a foundational proof assistant certificate. A witnessed unjoinable peak implies non-confluence **for these terminating systems**, since the reachable sets are exhaustive when no resource bound is hit.

Rule priority is **not** considered in this system, which checks nondeterministic rewriting (a stronger condition than one fixed priority execution strategy).

## Scope exclusions / bridging obligation

These rewrites operate on first-order algebraic terms and do not automatically certify the existing SCL `niyama` AST. The SCL compiler must first supply a semantics-preserving translation, a type/effect judgment and a proof that its optimization rules preserve values and traces. Symbolic confluence by itself does not prove that a rule such as `x*0→0` preserves observable failures or effects. Morphological and kāraka checks are outside F0 and still use the distinct evidence/context interfaces from v0.4.2.

## Replication

Run `python -m unittest discover -s tests -v` in this directory. Run `python proof_demo.py` for concrete numeric and critical-pair reports. `proof_kernel/` has no third-party dependencies. Do not rename or replace `scl.py` as part of this release.
