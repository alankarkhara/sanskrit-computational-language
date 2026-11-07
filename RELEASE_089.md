# SCL v0.8.9 — Authenticated Grounded Document Tasks (research prototype)

## Three requested directions

1. **Identity and authorization:** Ed25519 requester signatures, independently signed scoped authority grants, expiry checks, one-use nonces, executor-specific public-key grants and signed result messages. Cryptographically proven identity means possession of a key, **not** real-world identity; production needs credential provisioning/revocation.
2. **General task grounding:** immutable content-addressed UTF-8 document references; an explicit pure word-count task whose output has deterministic reference semantics, plus byte-bound verification and output certificate. This extends 0.8.8 beyond Int64 inputs, **not** to all possible task types.
3. **Formal verification:** added proof obligations and paper-level proof sketches, tests for malformed contracts/signatures and result replay. **A machine-checked proof was not achieved** (no Lean/Coq installed); the general soundness milestone remains open.

## Compatibility

Additive extension. Previous code from 0.8.8 preserved byte-for-byte; historical release gate and test suite executed. The baseline 0.8.6 feature set was role typing, restricted optimizer, certificate verifier, and scripted native agent conversation. 0.8.8 introduced grounded Int64 addition over loopback TCP. 0.8.9 adds key-bound authorization and byte-grounded document counting over two independent processes, while retaining prior behavior.

## Run

```
python -m unittest discover -s tests -q
python publication/release_gate.py
python demo089.py
```

Requires `cryptography` (tested 46.0.4) and Python 3.13. The previous core continues to run without the `cryptography` dependency.

## Limitations

Not a general-purpose remotely secure distributed agent platform. In demo the private worker key is passed to its isolated child over an inherited IPC channel as test configuration. Do not emulate this in production; use protected private-key storage. Signatures are not independently proof-checked by a formal kernel. `gaṇaya_śabdān` is a deterministic token count, **not** verified natural-language comprehension. No open-source license decision is made here.
