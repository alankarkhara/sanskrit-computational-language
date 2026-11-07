# SCL v0.6.2 — Typed Grammatical Unification and Conditional Critical Pairs

## Trust boundary
This is a **restricted finite-domain analyzer** and is additive to the v0.6.1 compiler. Its demonstration rules for nominative/accusative licensing are **SCL-local assumptions**, not authenticated Pāṇinian derivations. No external grammatical expert approval is claimed.

## Term signature and typing
A signature maps each constructor to argument sorts and its result sort. A variable context assigns every metavariable a sort. The constructor check is inductive: `Γ ⊢ f(t₁,…,tₙ):τ` requires `f:τ₁×…×τₙ→τ` and `Γ⊢tᵢ:τᵢ`. Rules must have equal LHS/RHS sorts; RHS variables must occur in LHS. The rule validator also checks conditions and declared domain membership.

## Conditional rewrite relation
For a term `t`, a rule `l→r [C]` is applicable at position `p` if first-order matching yields σ with `t|p=lσ`, each case/feature guard in `Cσ` holds, prerequisites are present in the enabled rule environment, and the rule's phase is visible. If an applicable competing rule explicitly overrides it, it is suppressed. The rewrite yields `t[rσ]p` and checks sort equality again.

## Critical-pair method
For every ordered rule pair, variable names are standardized apart; every non-variable position in the first LHS is unified with the second LHS. Remaining variables range over a **declared finite set of ground feature constants**. Ground instances that satisfy both guards and allow both rules under the explicit override policy are considered realizable overlaps. Reachable descendant state graphs are explored under a configurable bound.

- `joinable`: two branches share a reachable descendant within exhausted graphs.
- `divergent`: two exhausted finite graphs have disjoint reachable sets and each has a terminal state.
- `unknown-bound`: graph exploration exceeded the bound.
- `unknown-cycle`: a non-terminating, unproven situation requiring additional proof.
- `unknown-assignment-bound`: enumeration exceeded its assignment budget.

A report marked `exhaustive-declared-ground-domains` covers only these finite domains, guarded first-order rules, and checked visibility environment. It does **not** prove universal confluence for arbitrary Sanskrit terms or all Aṣṭādhyāyī rules.

## Mathematical obligations
1. **Type preservation for generated steps:** follows inductively from the sorted constructor signature and rule-side sort equality, provided ground matching respects declared sorts. The implementation checks sorts on completed ground terms. The current unifier is inherited and untyped; only grounded instantiations that pass checking can be trusted.
2. **Termination:** not established for general rules. Bounded state exploration is not a substitute for a reduction ordering.
3. **Confluence:** conditional critical-pair joinability alone is not a global theorem without additional hypotheses (e.g., appropriate termination and conditional critical-pair criteria). This module reports finite-state evidence rather than a universal theorem.
4. **Grammatical authenticity:** guard examples must be independently sourced, and actual Pāṇinian inherited contexts must be modeled before linguistic certification.
5. **Compiler integration:** module is callable from Python/CLI, not yet on the main SCL compilation path.

## Usage
`python typed_conditional_cli.py` — show that disjoint guards do not cause a realizable critical pair.

`python typed_conditional_cli.py --conflict` — inject a synthetic contradictory rule, identify divergent branches.

`python -m unittest discover -s tests -q` — run inherited and new tests.
