# SCL v0.9.3 — Native clarification and live-process demonstration

## Implemented
- Native SCL `spaṣṭa_saṃvāda` grammar for role declarations, typed objects, initial contracts, clarification request, answer, proposal, approval and rejection.
- Rejects duplicate fields, unauthorized answers, unknown objects, unmet requirements, invalid approvers and altered transcripts.
- Uses the v0.9.2 clarification state machine through a native SCL compiler, with deterministic replayed transcript certificates.
- Runs a message-driven demonstration across two independent OS processes and assembles/replays the actual exchange as native SCL source; **both participants are deterministic rule-driven programs**, not language models.

## Validation
- 501 Python unittest cases passed (493 inherited plus 8 new).
- Five missing-field questions and five dynamic answers from separate processes; final contract approved and native SCL transcript verification VALID.
- All 0.9.2 inherited non-cache files retained byte-for-byte (see COMPARISON_093.json).

## Boundaries
- Demonstration does **not** prove human-intent fidelity, live LLM reasoning, or semantic grounding outside the restricted task ontology.
- The certificate is hash-linked and independently recomputed from native SCL source, but not digitally signed, and mathematical soundness has not been checked by Lean/Coq.
- The approved task is **not executed**; an approval record is not a completion certificate.
- Real independently hosted conversational AI models and human usability experiments require model connections and controlled user trials.
- Not yet publication-grade for claims of general semantic unambiguity. Suitable as a reproducible experimental software prototype, subject to IP/licensing and independent review.

## Reproduce
```bash
python -m unittest discover -s tests -q
python native093_cli.py core080/examples/native_clarification_093.scl > cert.json
python native093_cli.py core080/examples/native_clarification_093.scl --verify cert.json
python live093_demo.py
python native093_cli.py LIVE093_TRANSCRIPT.scl --verify LIVE093_CERTIFICATE.json
```
