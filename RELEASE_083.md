# SCL v0.8.3 — Formal Unambiguity Audit

- **Result:** 405/405 Python unittest tests passed, including six new tests.
- **Finite audit:** 153 distinct source-level expressions, all 153 produced equivalent value-or-error observations with 100000 fuel before and after optimizer rewriting; each triggered at least one rewrite.
- **Counterexample:** Same-fuel execution is not semantics-preserving: `0+1` vs `1` at two execution steps.
- **Proof assistant:** No Lean / Coq / Z3 executable installed; no machine-checked theorem claimed.
- **Continuity:** All inherited v0.8.2 archive members verified byte-for-byte in the new ZIP by SHA-256, except for no modifications (the release is additive).
- **Detailed definition and remaining obligations:** See `FORMAL_UNAMBIGUITY_083.md`.

Use `python formal083.py` and `python -m unittest discover -s tests -q` from the extracted archive root.
