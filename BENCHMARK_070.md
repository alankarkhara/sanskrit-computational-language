# SCL 0.7.0 — comparative ambiguity benchmark

This controlled experiment compares three algorithms with the same nominal morphology inventory. **It does not benchmark Python, Rust, or Haskell as whole languages.**

- SCL evidence gate: existing `resolve_nominal` implementation.
- Conventional first-match parser: intentionally commits to the first admissible parse.
- Typed-constraint baseline: independently enumerates all parses and applies type-like feature constraints; uses the same lexical engine as SCL.
- Gold cases are internally constructed and require independent Sanskrit-specialist review.

## Measured results

| Algorithm | Correct | False unique acceptance | Missed ambiguous cases | Median ns/case |
|---|---:|---:|---:|---:|
| SCL evidence gate | 17/18 | 0 | 0 | 1,075,277 |
| First-match parser | 11/18 | 6 | 6 | 523 |
| Typed constraint parser | 17/18 | 0 | 0 | 1,280 |


The valid instrumental singular `rāmeṇa` is not recognized by the current morphology engine; both exhaustive systems miss it. This is a discovered coverage defect. The first-match parser fails to flag six genuinely ambiguous cases, demonstrating a weakness of that chosen parser policy—not a limitation of Python or established languages.

SCL and the typed-constraint baseline produce identical decisions: **no measured uniqueness advantage**. SCL takes more time in this microbenchmark because it builds extensive evidence records and reconstructs an engine per request, rather than because of any inherent grammatical complexity. Timing values are environment-specific.

## Reproduce

`python -m benchmarks.ambiguity_benchmark --rounds 50 > BENCHMARK_RESULTS_070.json`

`python -m unittest discover -s tests -q`

## Integrity

All 157 inherited non-cache paths retained: True. Changed inherited bytes: 0.
New benchmark files only; the inherited interpreter and modules have not been altered.

## Conclusions

1. SCL improves over an intentionally naive first-match policy by detecting ambiguity rather than accepting the first parse.
2. Equivalent ambiguity detection can be implemented in conventional programming environments; no superiority has been established.
3. Grammar coverage and verification need improvement; external expert review and a larger adversarial corpus are outstanding.
4. This is not a comparative runtime benchmark against production parsers or proof assistants.
