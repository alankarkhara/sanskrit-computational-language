# SCL 0.7.5 — External Sanskrit treebank evaluation harness

## What is implemented

* Strict ten-column CoNLL-U reader; distinguishes syntactic words from multiword-token and empty-node rows.
* Reproducible evaluation command `python -m benchmarks.treebank075 path/to/sa_ufal-ud-test.conllu --out results.json`.
* Fail-closed abstention for sentences outside the finite SCL grammar; no partial analyses are scored as successful.
* No invented dependency metrics: UD relations (e.g., `nsubj`, `obj`) are NOT automatically equivalent to semantic kārakas; LAS/UAS intentionally `null` until validated mapping and compatible segmentation exist.
* Eight new unit/property/metamorphic checks, including word-order invariance, certificate tampering, constraint monotonicity, invalid data handling.

## How to obtain a real independent corpus

Download the original `sa_ufal-ud-test.conllu` from https://github.com/UniversalDependencies/UD_Sanskrit-UFAL . Corpus is CC BY-SA 4.0: preserve attribution and comply with reuse license.

Do not interpret self-generated nominal and sentence cases as held-out linguistic validation. This release was built in a restricted environment which could not retrieve the raw treebank file. Accordingly **no measured external parsing accuracy** is reported.

## Remaining proof obligations

* A verified transliteration conversion and token alignment between external corpus and the IAST-only SCL analyzer.
* Independently justified mappings between Universal Dependencies relation labels and SCL dependency/kāraka labels.
* Reproducible corpus-specific abstention, precision, recall and coverage measurements.
* Authentic multi-rule asiddhatva implementation with externally reviewed derivations.
* Lean 4 kernel-checked semantic theorems (Lean unavailable here).
