# SCL 0.4.4 — certified compiler integration

## Exact guarantee

With `--rewrite-policy certified`, an accepted *local* transformation must have
both source and target expressible in SCL-F0, the closed pure total integer/Boolean
fragment, with equal types and equal evaluated values. The compiler emits a
`SCL-LocalProof/1` record containing original AST, resulting AST, inferred F0 type,
value, and step counts. `proof_kernel.integration.verify_ir_certificates(ir)`
recomputes all local certificates and verifies the accepted rewrite count.

The kernel is implemented in Python and **not independently verified by Lean/Coq**.
The guarantee is scoped to F0-local replacements, assuming the interpreter's
corresponding arithmetic and evaluation semantics coincide with the F0 model.
A separate independent proof of full compiler correctness is still outstanding.

## Safety boundaries

Uncertifiable rewrites are skipped; no open metavariable identity receives a
universal certificate merely because a single closed instance is equal.
No calls, floating-point values, names, partial division, modulo, mutable state,
exceptional operations or side-effect expressions are accepted as F0 redexes.
The existing `legacy`, `checked` and `formal` policies remain unchanged.

Confluence certificates of `proof_kernel.rewrites` remain separate from local
semantic proof records. Local equivalence does **not** prove global confluence.

## Usage

`python scl.py examples/niyama.scl --rewrite-policy certified --emit-ir`

`python -m unittest discover -s tests -v`

## Next proof obligations

1. Independently formalize a typed SCL-to-F0 simulation theorem (Lean/Coq).
2. Certify open-term rewrites through symbolic identities under type/effect assumptions.
3. Integrate TRS critical-pair certificates with runtime algebraic rewrite admission.
4. Establish observational equivalence of the complete language with exceptions and effects.
