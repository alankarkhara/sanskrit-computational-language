# SCL v0.8.5 — Native two-agent language

Agent interaction is now authored **entirely as SCL source** using `saṃvāda`, `abhikartṛ`, `prastāva`, `pratipraśna`, `svīkāra`, `asvīkāra`.

Run: `python native085_cli.py core080/examples/native_agents_085.scl > transcript.json`

Verify: `python native085_cli.py core080/examples/native_agents_085.scl --verify transcript.json`

Supported proposition forms are `(pratijñā (samāna (yoga A B) C))`, `vyavakalana`, `guṇana`, or `(sama A B)` with `satya` or `asatya`. All integers are 64-bit signed. The validator rejects an invalid acceptance or incorrect rejection. Participants are logical identities, NOT cryptographically authenticated. Message order follows source order; no asynchronous network transport is claimed. The Python implementation is hidden behind SCL source syntax. The transcript is a deterministic compiled output, not an interactive external AI runtime. Formal Lean soundness is still pending.

This release deliberately adds new files without modifying any inherited source files.
