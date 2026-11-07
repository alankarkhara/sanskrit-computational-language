# SCL 0.9.2 — Clarification & Contract Completion

Machine-executable **restricted task negotiation kernel**. `Session.ask()` produces all currently identifiable missing or conflicting fields, with no guessed values. Only the declared owner may fill requested fields, followed by independent explicit proposal and approval. Typed operations and object references are checked against the existing 0.9.1 closed ontology. Certificates hash-link all events.

## Scope and limitations
* The interface is Python-hosted runtime logic; **not yet a unified native SCL dialogue compiler**.
* The verifier checks structural integrity, **not cryptographic signatures or an independent re-execution of semantic validity**. Hashes alone do not authenticate agents.
* No general natural-language-to-SCL transformation or spontaneous LLM questioning, no external actions, no formal theorem kernel.
* A contract can be syntactically complete while misconstruing human intent.
* Existing 0.9.1 compiler/policies are preserved, not redefined.

Run `python -m unittest discover -s tests -q` from release directory.
