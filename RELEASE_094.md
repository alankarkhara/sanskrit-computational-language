# SCL 0.9.4 — Unified semantic kernel (experimental)

## What is implemented
- Canonical normalized task contracts (`core080/unified094.py`) backed by v0.9.2 validation.
- Native v0.9.3 SCL clarification source ingestion via `compile_native` and deterministic certificate replay.
- Explicit lifecycle: draft → clarifying → pending_approval → approved → executing → completed/failed. Cancel/reject also supported.
- Execution is prohibited before approval. Generic `Kernel.begin` accepts an **application-supplied authorization verdict**, not independent cryptographic authentication. Do not expose it to untrusted callers as an authentication mechanism.
- The bounded `execute_signed_document` adapter integrates v0.8.9 Ed25519 signed document-count task execution and verification, binding the task identity, roles, action, target and output to the approved contract. This adapter covers **only** UTF-8 whitespace-token counting.
- Exact underlying earlier language files are retained and existing APIs are unchanged.

## Limitations / publication gating
- No general-purpose natural-language understanding; v0.9.0 natural-language recognition remains narrow.
- No autonomous LLM-to-LLM interoperability test; existing separate-process demonstrations are protocol demos.
- No machine-checked proof of protocol invariants or proof assistant integration.
- No general authenticated tool or multi-step delegation execution; effect enforcement is restricted.
- The signed adapter executes and verifies an operation before recording the unified lifecycle atomically. It does not provide crash-safe atomic transactions across remote systems.
- Adversarial security audit, nonprogrammer usability study, licenses and intellectual-property clearance remain incomplete.
- A result verification replay does not prove real-world factual correctness for arbitrary text tasks.

## Reproduce
```
python -m unittest discover -s tests -q
python -m unittest tests.test_unified094 tests.test_signed094 -v
```

## Publication verdict
Suitable as **experimental research artifact / preprint candidate** with explicit limitations; not publication-grade for universal semantic unambiguity, formally verified multi-agent execution, or mature user usability.
