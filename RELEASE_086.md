# SCL v0.8.6-rc1 — publication readiness

**Status: candidate for researcher review; not legally cleared for open-source publication or marketed as a fully verified language.**

## Measured checks
- Base artifact: `scl_v0_8_5_native_agents.zip`.
- All **229 inherited archive members** retained byte-identically, as verified by `publication/release_gate.py`.
- **425/425 Python unittest cases passed**, measured on Python 3.13.5 in this build environment.
- **10 historical legacy SCL programs** execute via `scl.py`. New core executes using `core080_cli.py`. Native scripted agent dialogue executes in native SCL with `native085_cli.py`.
- Strict-core and scripted agent certificates were generated, replay-verified and checked against an extra-field tampering attempt.
- A CI workflow checks supported Python versions, but the workflow has not yet run on the GitHub service.

## Research commitment
SCL is a Sanskrit-grammar-*inspired programming language*, not a Sanskrit corpus, transcription or morphology research programme. `publication/GOALS_AND_NON_GOALS.md` is the mission statement; `publication/CLAIMS_REGISTER.md` is the requirement-versus-evidence ledger. The strict `core080/` and legacy linguistic `grammar/` modules are **distinct**. No legacy module was removed.

## No overstated claims
SCL cannot yet claim machine-checked global type-safety/determinism proofs, universal observational compiler equivalence, networked independent AI-agent communication, production-grade security, or performance superiority over existing languages. In particular, finite-budget fuel observations can change under valid mathematical simplifications; the verifier must name preserved observations/budgets. Hash chains do not authenticate agents. The native SCL example models **scripted agents** and a restricted arithmetic language.

## Distribution gate
The rights holder must approve licensing, third-party dependencies, patent disclosures and code provenance. `LICENSE-DECISION-REQUIRED.md` is **not** a license. Until rights approval, this is a controlled review artifact, not a fully open-source release.

## Reproducibility
See `publication/REPRODUCE.md`, run `python -m unittest discover -s tests -q` and `python publication/release_gate.py`. The file hashes and test results are in `publication/`. Formal and security obligations remain listed in `publication/PUBLICATION_CHECKLIST.md`.
