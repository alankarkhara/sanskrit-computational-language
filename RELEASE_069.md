# SCL 0.6.9 — evidence and ambiguity gate

- Conservative finite-state nominal ambiguity preservation; reject nonunique requests unless explicitly allowed.
- Explicit separation between syntactic case and semantic kāraka.
- Replay accepted verbal forms through the 0.5.9 restricted derivation engine; reject legacy `BOUNDARY_A` steps.
- Sandhi verification limited to the declared vowel-boundary fragment.
- Versioned source/IR-bound certificates with full deterministic replay.
- Older interpreter files remain unchanged; new module, CLI, test suite and documentation are additive.

## Not completed

- No independent Lean kernel run: executable Lean is not available in this environment.
- No independent Sanskrit specialist review, and no universal classical asiddhatva semantics.
- Finite paradigm reconstruction remains; nominal generation is not yet derived exclusively from Paninian sutras.
- No claim that SCL eliminates all ambiguity or surpasses established languages in formal safety.

## Run

`python -m unittest discover -s tests -q`

`python ambiguity069_cli.py examples/namaste.scl --requests examples/ambiguity069_requests.json > cert.json`

`python ambiguity069_cli.py examples/namaste.scl --requests examples/ambiguity069_requests.json --verify cert.json`
