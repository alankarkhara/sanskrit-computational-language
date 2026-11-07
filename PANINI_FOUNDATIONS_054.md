# SCL v0.5.4 — Bounded Pāṇinian foundations

## Scope and release decision
This is an additive research release of v0.5.3. The earlier `scl.py`, `grammar.derivation.derive()`, proof modules, morphology, and CLI remain unchanged. This release is **not** a comprehensive Aṣṭādhyāyī implementation or a grammar certified by an outside scholar.

## Implemented
- A tokenized 14-row Māheśvara inventory and *selected* pratyāhāras `ac`, `ik`, `yaṇ`, `hal`, `aṇ`. Repeated markers are identified by their row. Phonetic class expansion to long vowel allophones is a separate future operation.
- A bounded `1.3.3` then `1.3.9` example for the attested `tiP` ending, represented as `tip` in IAST. General `it` inference is **deliberately rejected**. This prevents incorrectly removing final consonants of ordinary roots or surface forms. Nasalized-vowel markers and other technical cases are not supported.
- New, explicitly restricted vowel-sandhi instances: `6.1.87` a/ā + i/ī -> e, a/ā + u/ū -> o, and a/ā + ṛ/ṝ -> ar; `6.1.88` a/ā + e/ai -> ai and + o/au -> au. Existing 6.1.77 and 6.1.101 subcases use the previous engine untouched.
- A generic **local modeling tool** for scopes, explicit exceptions, equal-priority conflicts, and visibility. It is **not** an implementation of Pāṇini's general precedence, *asiddha*, or *anuvṛtti* semantics.
- A provenance trace data structure. The `local_chain` structural check only ensures steps connect, not that the rules are linguistically sound.

## Sources and evidence boundaries
- Aṣṭādhyāyī 1.1.71: pratyāhāra construction; 1.3.3 and 1.3.9: *it* designation and deletion. Background: https://sanskritdictionary.com/panini/1-3-9 and https://web.stanford.edu/~kiparsky/Papers/hyderabad.pdf
- 6.1.87, 6.1.88 and their overlap: https://sanskritdictionary.com/panini/6-1-87 and https://www.cam.ac.uk/system/files/rajpopat_phd_thesis_15_dec_2022.pdf
- Rule conflicts 1.4.2 and its interpretive controversies: https://sanskritdictionary.com/panini/1-4-2 and https://api.repository.cam.ac.uk/server/api/core/bitstreams/4f4bd11c-da22-4baf-84c8-d4ed1ba19a4f/content

The sources establish identifiable rules, not independent validation of this software's completeness or accuracy. Editorial choices should be reviewed by a qualified Sanskrit grammarian.

## Commands
```bash
python grammar_cli_054.py pratyahara ac
python grammar_cli_054.py it tip --category affix
python grammar_cli_054.py sandhi rāma iti
python grammar_cli_054.py sandhi rāma eva
python -m unittest discover -s tests -q
```

## Acceptance status
- Original regression suite retained. 199 automated tests passed at development time.
- Existing CLI and compiler modules not modified. Cross-version behavioral equivalence beyond the inherited tests is unproven.
- Independent expert approval: **pending**.
- Independent Lean/Coq check: **pending**.
- General affix/root morphology, anuvṛtti, adhikāra, vipratiṣedha, apavāda, asiddhatva: **not implemented generally**.

## Next engineering gate
Introduce an actual derivation-state algebra `(dhātu, pratyaya, it-markers, phonemes, features, rule history, visibility)`; allow only source-mapped typed transitions; implement a small authoritative dhātu+tiṅ derivation with attested intermediate stages and expert-reviewed gold traces. Do not use local string transformations as evidence of full grammatical fidelity.
