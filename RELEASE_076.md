# SCL v0.7.6 — independent published excerpt audit

Source: UniversalDependencies/UD_Sanskrit-UFAL, `sa_ufal-ud-test.conllu` (CC BY-SA 4.0). The `external/ufal_published_excerpt_076.conllu` file is a *manually transcribed, limited excerpt* from the public source (3 sentences); it is **not** the full test set and must not be described as such. Gold edges are reference annotations. None are SCL predictions.

Run `python -m benchmarks.external076` and `python -m unittest discover -s tests -q`.

The corpus's original Devanagari form cannot be sent directly through SCL's limited IAST grammar; neither treating `nsubj` as kartṛ nor `obj` as karman in all contexts would be justified. SCL reports abstention on unsupported inputs. LAS, UAS, precision, recall, and independent grammatical accuracy are deliberately unreported. A full-treebank score requires actual corpus retrieval, verified transliteration/segmentation, a justified annotation crosswalk, and a compatible full-coverage parser. See `EXTERNAL_RESULTS_076.json`.

Integrity file: `INTEGRITY_076.json` enumerates byte-identical inherited file retention.
