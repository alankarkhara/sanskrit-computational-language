# SCL v0.7.1 — Correctness and controlled parser comparison

## Completed

- Corrected bounded ṇatva handling for selected instrumental singular nominal forms. `rāma → rāmeṇa`, while `deva → devena`, `phala → phalena`, `vana → vanena` remain distinct.
- Implemented a module-local reusable morphology engine in the evidence gate to reduce repeated initialization overhead.
- Added a 360-case mechanically derived adversarial consistency suite, comparing SCL, a typed-constraint implementation, and the real **Lark Earley** parser library combined with the same morphology inventory.
- Fixed historical benchmark regression expectations explicitly, rather than quietly suppressing the discovered failure.
- Preserved all prior non-cache paths. Exact per-file changes recorded in `FILE_INTEGRITY_071.json`.

## Tests and measured results

333/333 automated unit tests pass. All three comparator systems classify 360/360 generated test instances correctly. Median processing times are environment-specific and not representative of cross-language speed. See `BENCHMARK_RESULTS_071.json`.

## Scientific validity limits

- The corpus is mechanically generated from the same lexicon, so 360/360 **does not constitute independent linguistic validation**.
- Lark Earley is a production parsing library, but the nominal paradigm logic is shared; the experiment does not compare complete language front ends.
- A full Sanskrit expert-reviewed adversarial sentence corpus has **not** been obtained. That requires an independent reviewer.
- Formal Lean 4 proof checking is still outstanding.
- The implemented ṇatva condition covers supported finite lexemes only, not Pāṇini's general rule system.
- SCL does not eliminate intrinsic linguistic ambiguity, nor does this benchmark establish superiority over existing programming languages.

## Reproduce

```bash
python -m unittest discover -s tests -q
python -m benchmarks.ambiguity_benchmark --rounds 10
python -m benchmarks.expanded071
```

## Sources for bounded ṇatva

Pāṇini 8.4.1–2, with the relevant `rāmena → rāmeṇa` example: https://learnsanskrit.org/vyakarana/sounds/satvam-and-natvam/ and https://www.sanskritlibrary.org/grammatical/data/A.8.4.1.html.
