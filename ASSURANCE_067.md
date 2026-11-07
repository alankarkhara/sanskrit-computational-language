# SCL v0.6.7 — authenticated grammatical evidence gate

This **additive** release introduces `grammar.assurance067`, retaining inherited tools.

## Implemented
- Finite nominal evidence by two-way analysis/generation consistency, retaining all ambiguities. Table rule IDs are local SCL rules, not authenticated Pāṇinian derivations.
- Finite laṭ parasmaipada verbal evidence via full previous stepwise derivation replay. Remaining `BOUNDARY_A` in the legacy verbal engine is not externally justified and MUST NOT be promoted to proof.
- Explicit 169-case vowel-boundary interaction audit, including the 6.1.101 override of 6.1.77, with a stable digest of the decision table.
- Versioned, recomputable certificate chain covering source, certified-policy IR, native grammar IR and exact requested evidence. Sandhi requires unique source AST occurrence; **nominal and verbal evidence remain auxiliary requests not yet source-attached**.
- Fail-closed invalid premises and certificate tampering detection.

## Not completed / independent obligations
- No Lean/Coq checker was available or run. Previous F0 Lean sources remain unchecked; no new mechanically proven substitution/preservation theorem is claimed.
- No independent Sanskrit grammarian or externally reviewed derivation corpus is available in this build; cited sūtras are source-linked, not expert-reviewed step sequences.
- General anuvṛtti, adhikāra, asiddhatva and pan-Pāṇinian rule interaction correctness are not established.
- The 36 existing recognizers are **not** 36 fully integrated transformative rules.
- Arbitrary nominal and verbal AST-node binding is not yet established.

## Run
`python -m unittest discover -s tests -q`

`python assurance067_cli.py examples/namaste.scl --requests examples/assurance067_requests.json > cert.json`

`python assurance067_cli.py examples/namaste.scl --requests examples/assurance067_requests.json --verify cert.json`
