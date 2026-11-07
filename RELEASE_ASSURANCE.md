# SCL v0.5 — Integrity candidate acceptance report

## Scope
This is a conservative additive release on top of the v0.5 stable candidate. Legacy compiler/grammar APIs are unchanged. No independent expert signoff or Lean verification is claimed.

## Deliverables
1. `grammar/review_corpus.json`: seven annotated, reproducible grammatical examples. All carry explicit **PENDING_EXTERNAL_SANSKRIT_EXPERT** status, named reviewer absent. This is a review-ready corpus, not a reviewed corpus.
2. `grammar/assurance.py`: finite declarative grammatical-policy checker for duplicate IDs, cyclic/missing dependencies, integer priorities, and conflicting decisions at the same maximal priority for **identical predicate/role/case keys**. An explicit higher-priority exception can shadow a general policy. It does not implement Pāṇini's complete vipratiṣedha, apavāda or asiddhatva mechanisms.
3. Source/IR/grammar certificate bundles, revalidated by recompiling from the original text, regenerating grammatical analyses and recomputing the registry digest. This verifies reproducibility/tamper detection in the *trusted Python runtime*. It does not prove formal compiler correctness or that the supplied grammar analysis is linguistically correct.
4. Additional tests plus inherited regression suite.

## Independent review acceptance gate (OPEN)
A qualified Sanskrit grammarian must confirm each corpus row's morphological accuracy, frame interpretation, cited sūtra applicability, exception scope and linguistic naturalness. Reviewer identity, date, issues and approved evidence must be recorded; corrections must generate a new corpus revision. No automated system may mark this gate complete.

## Certificate usage
`python certify_program.py examples/namaste.scl --policy certified --requests grammar/requests_example.json > certificate.json`
`python certify_program.py examples/namaste.scl --policy certified --verify certificate.json`

## Trust boundaries
Python reference evaluator, lexer/parser, arithmetic proof kernel, morphology and contextual frames remain trusted assumptions. SHA-256 binds bytes and detect modifications, not a mathematical proof. Users must not interpret rule references labelled `definition-only` as derivational authority.
