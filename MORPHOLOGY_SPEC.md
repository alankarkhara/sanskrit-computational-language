# SCL v0.5-alpha nominal morphology specification

Scope: six lexical entries, three **regular** nominal paradigms: masculine -a, neuter -a, feminine -ā. The eight traditional case labels and three numbers are enumerated. These are finite pedagogical tables **not** a complete Pāṇinian rule system and not authenticated sūtra-level derivations.

- `MorphologyEngine.generate(lemma, case, number)` returns one structured `Analysis` and an explicit table-rule derivation trace.
- `MorphologyEngine.analyze(surface)` returns **all** matching analyses in stable order. Empty result is not evidence that the word is ungrammatical Sanskrit.
- Lemma entries: `rāma`, `deva`, `phala`, `vana`, `sītā`, `latā`.
- SCL v0.5-alpha introduces `rūpam(lemma,case,number): pāṭha` and `rūpasaṅkhyā(surface): saṅkhyā`. The first returns a generated surface word; the second returns the count of potential morphological analyses, not kāraka assignments.
- Legacy `vibhakti`, `mūlarūpa`, `padam` retain their v0.4-era limited, single-form semantics for compatibility. A later explicitly versioned API may replace these with ambiguity-aware results, **not** a silent change.
- Case (`vibhakti`) is a morphosyntactic feature. Semantic kāraka remains `None`, requiring syntactic and predicate context. No case-to-role equation is implied.
- `NOM-*` provenance IDs reference internal paradigm rows and do **not** claim to be Pāṇini sūtra IDs.
- NFC normalization is mandatory. No sandhi, dialect variation, inflectional alternations outside selected paradigms, syntax-driven disambiguation, agreement, or true rule precedence is implemented.

CLI: `python -m morphology.cli analyze rāmābhyām`; `python -m morphology.cli generate sītā saptamī ekavacana`.
