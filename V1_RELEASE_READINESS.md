# SCL v1.0 release-readiness evidence (2026-10-24)

Status: **v1.0 NOT CERTIFIED**. This is an additive release-candidate engineering package, not a stable 1.0 release.

## Five release obligations

1. **Real local AI-agent interoperability: PARTIAL.** `local_agents100.py` implements a bounded 3-message, two-endpoint adapter for OpenAI-compatible local chat services, carrying strictly validated v1 wire frames. No local model runtime or weights were available in the checking environment; **no real LLM inference was run**. Adapter transcripts do not produce SCL certificates or signed permission grants. Run with `python local_agents100.py --a-url http://127.0.0.1:11434/v1/chat/completions --a-model MODEL_A --b-url http://127.0.0.1:1234/v1/chat/completions --b-model MODEL_B` after starting your two local services. The script intentionally does not execute tasks.
2. **Protocol stability: PARTIAL.** `core080/wire100.py` specifies a byte-bounded six-field canonical JSON envelope, version match, duplicate-key rejection, finite JSON, message-kind whitelist, sender/session syntax, and monotonic per-sender sequence validation. It is **experimental**: no vendor-independent wire conformance test, release compatibility promise, authenticated sender identity, or complete SCL semantics mapping.
3. **Security hardening: PARTIAL.** Added strict negative cases, replay/order checks and 4,000 fixed-seed malformed-input fuzz attempts. This is NOT comprehensive security fuzzing; endpoint allowlisting is not sandboxing, replay sequence registry is in-memory, model text is untrusted. Existing SQLite nonce durability applies only to pure executions, not side-effectful tools. No external penetration test completed.
4. **Independent validation: OPEN.** Existing 550-test baseline plus 6 new tests run locally. An independent linguistic reviewer, external security audit, independent replication and a Lean toolchain run are still needed. Existing formal artifacts have NOT been upgraded to independent executable verification.
5. **Licensing/publication: OPEN.** `LICENSE-DECISION-REQUIRED.md` still applies. This engineering package grants no new distribution permissions, cannot elect a license on behalf of rightsholders or resolve patent/third-party questions, and has not been deposited with a DOI or publicly released.

## Wire v1.0-rc1 contract

Every frame has EXACT keys `version`, `session`, `sequence`, `sender`, `kind`, `payload`. Version is `1.0-rc1`. Sequence begins at zero for each (session,sender) and increments by 1. Supported kinds: `request`, `clarify`, `answer`, `propose`, `approve`, `reject`, `result`, `error`. Payload is a JSON object; model-authored `approve` is merely untrusted text, **not** an authorization and must never trigger execution. Canonical UTF-8 output uses sorted keys, compact separators, Unicode preservation and nonfinite-value rejection. Frames max 65536 bytes. Strict readers reject duplicate keys; unknown version and extra fields fail closed. Ordering is scoped to an in-memory receiver, not a distributed or restart-durable identity protocol. The JSON object payload is not a security certificate.

## Reproduction

`python -m unittest discover -s tests -q`

`python publication/release_gate.py`

`python -W error::ResourceWarning -m unittest discover -s tests -q`

## Remaining 1.0 release gates

- Execute a real pair of isolated local language model inference servers; capture reproducible, independently checked multi-turn SCL-native messages, intentional ambiguity and rejection cases.
- Bind authenticated principals and grants to protocol frame/session/task digests; implement resilient transport, authorization and error handling.
- Define and test semantic mappings from the model messages to the native language grammar; never treat LLM prose as a trusted instruction.
- Stress and independently fuzz all parser surfaces, grant/certificate decoders and recovery paths, not only the wire envelope.
- Independent linguistic review and formal proof checks; third-party rights audit, rights-holder's license choice, and public archival steps.
