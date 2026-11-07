# SCL v0.9.8 — Durable Replay Hardening (bounded)

Implements a SQLite-backed nonce-consumption store for the existing two pure verified operations. SQLite `BEGIN IMMEDIATE` provides serialized nonce checks and commits with certificate digests; previous v0.9.7 source files are preserved byte-for-byte (except Python bytecode caches omitted). Each call remains subject to all existing cryptographic, scope, object, result, and expiry checks in `verified096`.

## Reproduce
`python -m unittest discover -s tests -q`

## Limits
No actual neural-model endpoints were available for live two-model trials; adapters remain unvalidated with external models. No Lean/Coq kernel was run, hence no machine-checked universal soundness theorem. No human-subject usability study was performed. Process crashes after computing a pure operation but before commit may lead to a harmless recomputation; external effects remain unsupported. SQLite storage integrity depends on OS permissions and operator-managed database security. The new wrapper has not yet been wired into the v0.9.7 `bridge097.run_verified` lifecycle; callers use `DurableReplayStore.execute_once` explicitly.

This is an engineering validation candidate, not a claim of complete SCL correctness or publication-grade AI interoperability.
