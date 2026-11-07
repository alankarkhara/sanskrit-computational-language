# SCL v0.9.6 — Verified Execution (restricted research release)

## Results
- All **532** Python regression tests pass, including 12 new v0.9.6 tests.
- 316 inherited files retained without changing content (see comparison report).
- Two signed pure operations: `count_tokens` on UTF-8 text and `add_int64` on typed integer pairs, including explicit overflow.
- Ed25519 root-signed, expiring, scoped grants; Ed25519 owner approval for the exact canonical task hash; executor-signed evidence and an independent verifier.
- Nonce reuse is blocked while using the provided persistent nonce registry; an ephemeral set does **not** provide restart-safe replay defense.
- The verifier checks actual result values as well as the cryptographic bindings.

## Hard limits
1. **Not full completion of v0.9.6 roadmap.** The v0.9.4 kernel's existing operation vocabulary is incompatible with the two v0.9.6 operation names; these verified adapters are not yet end-to-end integrated through its state machine. No claim of general tool dispatch.
2. Execution is pure and in-process, with no filesystem writes, network actions, payments, email, or arbitrary AI-generated code.
3. The trust anchors and owner/executor private keys are passed by caller. Key custody, principal-to-key registration, durable revocation and atomic persistent nonce reservation require a production implementation.
4. Signed evidence does not prove that a remote agent followed an arbitrary instruction; supported results are independently recomputed.
5. No Lean/Coq proofs or live two-model gateway tests; research and validation stages remain pending.
6. Legacy tests still report inherited ResourceWarnings for unclosed streams.

## Commands
```sh
python -m unittest discover -s tests -q
python -m unittest tests.test_verified096 -v
```

## Research claim
This release provides a separately verifiable and cryptographically bound execution perimeter for two explicitly specified, pure task operations. It **does not** yet provide verified generic AI-to-AI task execution.
