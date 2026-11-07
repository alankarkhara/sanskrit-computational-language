# SCL v0.9.7 — Restricted Integration & Research Validation

## Scope
- Added an explicit, fail-closed translation from the unified SCL task `gaṇaya_śabdān` / `śuddha` to the signed execution perimeter `count_tokens` / `pure`.
- Binding is restricted to an approved `UTF8Document -> Int64` token-count task with `no_modify`, `internal` permission and an independently signed owner approval and signed scoped grant.
- The evidence verifier recomputes results before the kernel transitions to executing/completed. Unsupported operations are rejected instead of being guessed.
- The translation is a checked implementation, **not** a machine-checked formal equivalence proof. Legacy source is retained unchanged.

## Non-claims / gaps
- This does NOT close the generic addition (`yoga` is not the same type shape as `add_int64` with `Int64Pair`), general effects, durable replay persistence, distributed atomicity, key management, live two-model testing, or human participant study.
- No installed Lean/Coq checker; exhaustive finite test cases are not a universal proof. Real-model study and independent human replication remain unperformed.
- The gateway model adapter still requires independently provided API credentials and a connected live model endpoint; all included tests are offline.
- External and state-changing actions are not supported by this new bridge.

## Run
`python -m unittest discover -s tests -q`
`python -m unittest tests.test_bridge097 -v`

## Publication
This is an engineering research artifact suitable for reproducible prototype publication subject to license/IP review; **not** a validated universal AI-semantic communication system.
