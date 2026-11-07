# SCL v0.9.5 — Model Communication Gateway (research prototype)

## Scope and honest acceptance status

- A provider-neutral OpenAI-compatible HTTPS chat-completions adapter has been added. The adapter needs a configured external endpoint, model, and credentials. **No model was connected or called during this release**.
- The unified 0.9.4 task kernel is now usable behind a fail-closed task dialogue gateway. The gateway emits requested missing fields, accepts only authorized owner answers, keeps model suggestions untrusted, records approval, and exposes a hash-linked integrity transcript.
- The new offline example was executed. It requests five clarification fields, supplies owner answers, and reaches `approved`; **it does not execute any action**.
- Seven new tests pass, with the preexisting regression suite: **520 / 520**.
- All files inherited from v0.9.4 remain byte-identical; see INTEGRITY_095.json.
- Inherited tests still emit unclosed-file ResourceWarnings. These should be corrected in a future release with explicit, audited changes to older tests.

## Security and semantics

The model is not an authority. A model-supplied JSON update is logged as a *proposal* and is never merged directly into the canonical contract. Only an explicit owner answer can change missing fields, and only an explicit owner approval can change the state to `approved`. The runtime accepts only a declared, fixed ontology of operations. Hash-linked logs are integrity records, **not** digital signatures or authentication evidence. This gateway does not add a live authorization path or arbitrary tool execution.

## Acceptance gate — v0.9.5

| Condition | Result |
|---|---|
| Generic model transport adapter | Implemented, untested with external model |
| Two actual AI models exchange messages | **NOT ACHIEVED** |
| Unseen real-model tasks: missing fields, contradictions, delegation, rejection | **NOT ACHIEVED** |
| Offline deterministic gateway tests | Passed |
| Automatic approved task execution with tool verification | **NOT ACHIEVED** |
| Historical source retention | Passed |
| Independent machine-checked formal proof | **NOT ACHIEVED** |

## Next acceptance requirements

1. Configure two independently operating model providers or instances; retain raw redacted transcripts and model IDs; evaluate held-out cases. Model-generated requests must be validated before owner approval or any side effect.
2. Bind approval and signed scoped grants to exact canonical contract digests at the execution boundary. Verify results with a separate checker and least-privilege tool adapter; never accept a Boolean authorization verdict as cryptographic proof.
3. Construct and check a small formal model of the task states, authority, delegation and immutable restrictions in Lean/Coq or a comparable kernel; validate implementation correspondence.
4. Compare *ordinary AI task requests* versus *SCL-mediated AI task requests* using matched models and tools, and run nonprogrammer human comprehension studies.

## Commands

```bash
python -m unittest discover -s tests -q
python demo_gateway095.py
```

This is an **experimental gateway development release**, not a completed v0.9.5 inter-model acceptance milestone or a complete, formally verified AI communication standard.
