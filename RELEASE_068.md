# SCL v0.6.8 — Native grammatical certification and archive integrity

## Implemented
- New `tiṅrūpam(root, person, number)` typed SCL built-in using the v0.5.9 restricted laṭ parasmaipada generator.
- Compiler native grammatical IR automatically binds literal `rūpam`, `rūpasaṅkhyā`, `tiṅrūpam`, and `sandhi_pramāṇa` calls to individual parsed AST nodes, with paths and hashes.
- Nominal claims are regenerated from the finite paradigms, preserving ambiguity; verbal claims are regenerated using v0.5.9 traces and reject the legacy `BOUNDARY_A` step and unsourced grammatical rule steps. Structural `LINEARIZE` is explicitly classified as compiler operation, not a classical sūtra.
- Source, complete AST and compiler-IR digests are replay-checked. Tampering, unsupported arguments and nonliteral evidence requests fail closed. Earlier v0.6.7 verification remains available.

## Verified tests and archives
- 316 Python unit tests passed (311 inherited and 5 added).
- 32 historical release ZIP archives checked for file-path retention; every archived file path occurs in this release. Refer to `ZIP_FILE_RETENTION_068.json`.
- The prior v0.6.7 source tree is fully retained by path. Only `scl.py` was modified among its preexisting files.
- The local v0.6.7 example comparison appears in `EXECUTABLE_COMPATIBILITY_068.json`; complete historical behavioral replay was attempted but timed out, hence it is not claimed.

## Remaining proof and review boundaries
- Lean and Lake executables were unavailable: no kernel-checked theorem was produced.
- No independently reviewed Sanskrit derivation corpus is supplied: no external linguistic approval is claimed.
- Nominal morphology remains finite-table driven; verbal derivations still assume inherited grammatical conditions. This certificate guarantees reproducibility in the supported model, not universal Pāṇinian correctness.
- Literal arguments are necessary for native certificates; dynamic grammatical calls can execute but are not fully certified.
- General *anuvṛtti*, *adhikāra*, *apavāda*, and *asiddhatva* remain outside the verified bounded model.

## Commands
```sh
python -m unittest discover -s tests -q
python scl.py examples/native_068.scl
python native068_cli.py examples/native_068.scl > cert.json
python native068_cli.py examples/native_068.scl --verify cert.json
```
