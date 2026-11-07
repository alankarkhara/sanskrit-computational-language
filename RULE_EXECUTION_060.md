# SCL 0.6 — Bounded Pāṇinian rule execution architecture

This release adds a **separate typed rule-execution laboratory** to SCL 0.5.9. Previous source files remain unchanged. The module models rule identifiers, complete-term rewrites, context-bound inherited conditions, exception overrides, phase gating, exhaustive finite-state exploration, normal-form comparison, divergence, and replay certificates.

## Formal contract

A state is `(term, phase, context)`. A rule is `(id, phase, lhs, rhs, inherits, guard, overrides, source)`. A rule is eligible precisely when its phase and left-hand term match and each explicit inherited/guard token is in the context. Applicable exceptional rules suppress the named general rule. Distinct remaining rules are **not** ordered arbitrarily: both transitions remain in the graph. Phase advances only when no rule is eligible. At the final phase, no rule means a normal form.

For a supplied starting state, a finite reachable graph is enumerated. Termination is reported only if this graph has no cycles. Each immediate fork is considered joinable when its two successor states have a common reachable normal form. Confluence **from this start state** is reported only when this finite graph is acyclic and all reachable forks join. This is not a global proof for every input, and does not implement arbitrary first-order unification or classical *vipratiṣedha*.

The certificate stores exact rules, starting context, exploration outcomes, fork evidence and a checksum. Verification reconstructs the system and recomputes its exploration, rather than trusting certificate fields. This is stronger integrity replay, but the verifier is not formally verified and certificates do not independently certify classical Sanskrit rule interpretations.

The included joinable, divergent, and exception examples are **abstract symbolic demonstrations**, not claimed Aṣṭādhyāyī derivations. Authentic rule application requires a validated Sanskrit ontology and sūtra-scoped context conditions before incorporation.

## Pending requirements

1. Map real sūtras and all inherited conditions into audited structured rules, and check them with expert-reviewed examples.
2. Extend to term trees, substitution, and critical pairs, integrating the existing limited rewrite checker.
3. Implement a faithful treatment of *adhikāra*, *anuvṛtti*, *asiddhatva*, *apavāda* and *vipratiṣedha* by grammatical domain; current phases are only a model.
4. Link grammar certificates with source-to-IR compiler certificates; currently separate by design.
5. Run independent Lean 4 verification and obtain external Sanskrit-scholar review.

## Commands

`python rule_execution_cli.py --case joinable`

`python rule_execution_cli.py --case divergent`

`python rule_execution_cli.py --case exception`

`python rule_execution_cli.py --case joinable > cert.json`

`python rule_execution_cli.py --verify cert.json`

`python -m unittest discover -s tests -q`
