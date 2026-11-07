# SCL v0.4.5: symbolic and confluence integration

**New compiler modes:** `--rewrite-policy symbolic` and `symbolic-confluent`.

`symbolic` admits local rewrites if both AST expressions denote identical integer polynomials, under all assignments of their free variables to mathematical integers. This is a sound identity decision for the stated language fragment (+,-,*, unary -, integer constants and variable references) *provided* variable reads are total, stable, integer-valued and without effects. SCL has mutable variables and runtime typing, so the current interpreter cannot guarantee all those premises globally: **these certificates are conditional, not end-to-end observational-equivalence proofs**. A proof for expression ASTs is not a proof of binding-type or effect invariants in arbitrary SCL contexts.

`symbolic-confluent` additionally requires a restricted syntactic first-order critical-pair confluence certificate. Left-linear and strictly skeleton-decreasing rewrite systems with joinable critical pairs are admitted. The checker ignores priority semantics and built-in arithmetic evaluation; the result is *not* a confluence theorem for the combined evaluator or full Pāṇinian rule engine. Unsupported systems are rejected in this mode, but remain available under legacy policies.

`verify_source_ir(source,ir)` recompiles and matches the entire IR, and replays local certificates. This defends against unsynchronized IR edits given a trusted source and trusted compiler implementation. It is **not independent proof checking**.

Lean 4 and Lake are not installed in the build environment, so no kernel-verified theorem is claimed. The earlier mathematical induction arguments and Python checking remain independent-formalization obligations.

## Remaining before v0.5

1. Type-and-effect tracked integer binding semantics and typed symbolic substitution theorem, including mutation and evaluation-order restrictions.
2. Trusted independent Lean 4 proof of F0 progress and preservation, followed by translation correctness.
3. Morphological lexicon/rule framework with ambiguity, vibhakti–kāraka contextual inference, sandhi boundaries, and derivation trace certificates.
4. Formal grammatical rule precedence, exceptions, asiddha domains and ordering, with versioned provenance.
5. Integrated differential tests against real Sanskrit paradigms and backward-compatibility suite.

This release completes the planned integration *prototype*, not a proof of a fully verified optimizing compiler.
