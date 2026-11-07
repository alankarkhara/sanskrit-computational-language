# SCL v0.5.1 — Compatibility and Soundness Gate

- Original interpreter and legacy modes are *preserved* for historical compatibility.
- `gate_cli.py` is a separate **opt-in fail-closed certification interface**; it accepts only `certified` policy, without fallback to legacy. This gate does not change original `scl.py` defaults.
- `gate/trusted.py` is a small independent Python checker for **closed, pure, total F0** arithmetic/Boolean rewrite claims. It does not import compiler code, but is **not** a proof-assistant-verified or formally verified kernel.
- Source, policy, IR and explicitly requested grammar analyses are recompiled/recomputed for certificate replay. Unknown artifact schemas are rejected.
- Grammar requests outside the finite supported grammar fail closed. No sentence is claimed to be approved by an external expert.
- `GRAMMAR_REVIEW_REGISTER.json` lists pending independent philological review.
- `run_gate.py` compares archived example outputs, stderr and exit statuses with per-process timeouts. Its evidence is bounded to the examples; it is not exhaustive program equivalence.
- Versioned *gate envelope* only: historic IR/grammar formats are retained, not universally migrated.
- Symbolic/open rewriting, full language type-soundness, full Pāṇinian derivations, universal grammar certification, external expert review, and independently mechanized Lean proofs are **out of scope** of this release gate.

Run: `python -m unittest discover -s tests -q`, `python run_gate.py`, `python gate_cli.py examples/namaste.scl > cert.json`, `python gate_cli.py examples/namaste.scl --verify cert.json`.

## Observed gate results (2026-10-14)

- 161/161 tests passed on the current Python environment.
- 26/26 archived example comparisons matched output, stderr and exit code; sampled at most two examples per archived release, not all possible programs.
- Certificate creation and verification passed for `examples/namaste.scl`.
- Release **remains a candidate**: independent Lean/Coq verification and external Sanskrit philological review remain open.
