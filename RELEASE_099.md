# SCL v0.9.9 — Persistent replay integrated into unified execution

## What changed
- `core080.bridge097.run_verified_durable` uses v0.9.8 SQLite transaction-backed nonce registry to execute the supported SCL `gaṇaya_śabdān` document-token-count task through the unified v0.9.4 task lifecycle.
- Each completed pure task checks owner approval, authority grant, object digest, interpreter operation mapping, executor signature and independent computation of result.
- Tests cover successful execution, replay after a new kernel/session, forged approval, tampered input, rejected effect and attempted execution before approval.
- `tests/test_independent_peers088.py` explicitly closes both subprocess pipes after use, removing prior ResourceWarning output.

## Reproduce
`python -W error::ResourceWarning -m unittest discover -s tests -q`

## Guarantees and limits
This release covers the restricted pure UTF8Document token-count task only. SQLite nonce consumption survives process restarts when all participants use the same protected database. It does not provide crash-atomic coordination between the SQLite transaction and the in-memory Kernel state, nor secure identity onboarding, key rotation, distributed consensus or side-effecting tool execution. A crash after execution can consume the nonce before the result is delivered: the requester must reconcile pending work, not blindly retry using a new grant. A grant can be used on another uncoordinated database, so deployments must share a single trusted replay authority.

This is executable validation, not Lean/Coq formal proof, nor a two-live-LLM acceptance test. Human usability research remains open. The project remains experimental research software, subject to licensing and provenance review before publication.
