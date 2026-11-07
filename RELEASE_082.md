# SCL v0.8.2 — Independent executable certificate checker and programming benchmark

## Scope
This release extends v0.8.1 additively. Its new `core080/independent082.py` implements rewrite recognition, phase traversal, scope/exception resolution, replay-trace reconstruction, hash verification, and output checking without importing the v0.8.1 optimizer. It still shares the v0.8.0 parser, typed IR definitions, evaluator and digest function: it is **not** independent of the entire language implementation, nor a formal proof assistant.

## Observed results
- `python -m unittest discover -s tests -q`: **399 tests passed**.
- `python benchmark082.py`: **8/8 task expectations matched**.
- CPython and Node executed equivalent named-role subtraction demonstrations and both output `5`. Their process-start timings are not a normalized language benchmark and are not evidence of SCL superiority.
- `INTEGRITY_082.json` compares inherited v0.8.1 ZIP members against this release. No inherited files were missing or altered.
- Seven limited rewrite identities checked: addition/subtraction by zero, multiplication by one, and constant Boolean conditional selection. `0*x -> 0` is intentionally rejected because it can remove errors.

## What is NOT proved
1. No Lean/Coq theorem was kernel-checked (toolchains unavailable in this environment).
2. Checker and optimizer both reuse v0.8.0 parser/typed IR/evaluator, so the trusted base remains substantial.
3. Exact step-budget semantics are not preserved by these reductions. Value/error behavior is tested for a bounded fragment; no universal observational equivalence is claimed.
4. No statistically powered language comparison has been performed. The benchmark is a preliminary acceptance matrix, not proof of a quantitative advantage over Python, JavaScript, Rust, or Haskell.

## Usage
```sh
python -m unittest discover -s tests -q
python benchmark082.py
```
Python library:
```python
from core080.rules081 import certify_081
from core080.independent082 import check
s = '(krama (darśaya (yoga 0 12)))'
assert check(s, certify_081(s))
```

## Next acceptance gates
- Extract formal small-step semantics that model errors and fuel explicitly; prove all seven identities preserve their specified observations.
- Compile the theorem sources using an installed Lean/Coq kernel, recording version and complete logs.
- Expand comparative benchmark using like-for-like language tasks, held-out cases, typing/error policies, and separated execution/compile-time measurements.
