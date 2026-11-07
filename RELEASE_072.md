# SCL 0.7.2 — Sentence dependencies and rewrite interaction benchmark

## Scope

This additive research release benchmarks SCL's finite active-voice sentence analyzer against two comparative implementations. The benchmark uses 28 curated sentence inputs and tests exact sets of dependencies, not merely acceptance/rejection. An independent constraint solver uses a separately hand-written surface-form feature map, without importing the SCL nominal morphology analyzer. A Lark Earley parser is also exercised, but semantic features are supplied by the same independent finite solver.

The curated corpus is **not** independently reviewed by a Sanskrit grammarian. Shared restrictions include a finite noun vocabulary, overt kartā, present-tense active predicates and a local nominative/accusative/dative role policy. This benchmark does not evaluate unlimited Sanskrit parsing, sandhi segmentation, or a full Aṣṭādhyāyī implementation.

## Results

See `BENCHMARK_RESULTS_072.json` for machine-readable outputs, per-case mismatches and environment-dependent timing. All 28 sentence inputs produced exact matches among the three systems. Four abstract rewrite-interaction tests (joinable, divergent, overriding, cyclic) produced the expected classifications; these are synthetic and **not source-reviewed Pāṇinian critical pairs**.

All 339 automated tests passed. The baseline had 333 tests; six tests were added in `tests/test_sentence072.py`.

## Release continuity

`INTEGRITY_072.json` compares inherited non-cache files against v0.7.1 by SHA-256. No preexisting source file was intentionally modified. New work is contained in `benchmarks/sentence072.py`, `tests/test_sentence072.py`, benchmark output and this report. The package retains the historical codebase.

## Limits and next acceptance gate

1. Obtain an external, independently annotated Sanskrit sentence corpus, including commentary on semantic plausibility and alternative analyses.
2. Replace synthetic rewrite systems with genuinely overlapping, source-traceable sandhi and verbal rules, with full inherited contexts.
3. Benchmark against production grammatical analysis systems, with equivalent grammar coverage and cached initialization.
4. Continue Lean kernel checking and general rule-visibility formalization. No independent proof or Sanskrit expert approval is claimed in this release.
