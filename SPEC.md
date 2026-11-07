# SCL 0.4 technical specification (prototype)

All constructs from SCL 0.3 are retained. Lexical input is NFC normalized UTF-8 IAST.

## Morphological subset

Builtin `vibhakti(pāṭha)->pāṭha` returns the grammatical case name; `mūlarūpa(pāṭha)->pāṭha` returns `rāma`; `padam(pāṭha)->pāṭha` verifies a recognized surface form and returns it. Recognized singular masculine lemma rāma forms: rāmaḥ/prathamā, rāmam/dvitīyā, rāmeṇa/tṛtīyā, rāmāya/caturthī, rāmāt/pañcamī, rāmasya/ṣaṣṭhī, rāme/saptamī, rāma/sambodhana. Unsupported forms are errors rather than guesses.

## Case and role

Prototype licensing relation: prathamā→kartā; dvitīyā→karma; tṛtīyā→karaṇa OR kartā (instrument or passive-agent contexts); caturthī→sampradāna; pañcamī→apādāna; saptamī→adhikaraṇa; ṣaṣṭhī and sambodhana→none. This is neither a complete Pāṇinian grammar nor a one-to-one semantic mapping. A direct `padam("…")` argument to a typed `@role` parameter triggers a runtime check against that relation. No check is performed on unmarked strings or numeric parameters.

## Rewrite safety

A subtree with a `call` node is never substituted by a user rule. This conservatively avoids erasing, duplicating, or reordering observable effects through call-bearing expressions. The compiler also emits `structural_termination_certificate`, computed using a syntactic size decrease and metavariable occurrence multiplicities. This is a sufficient condition for a single rule to reduce AST size under arbitrary finite captures, but is **not a global rewrite-termination proof** when an uncertified rule is present. For certified rules only, the measure decreases at every rewrite, so termination holds for finite input expressions (provided the implementation preserves the stated measure). Runtime step budget and rewrite budget remain.

## Open formal obligations

Type preservation for user rewrites; general purity/effect typing; morphology outside the listed paradigm; morphological ambiguity resolution; lexical scope in guard patterns; formal treatment of all Pāṇinian meta-rules; compiler correctness relative to operational semantics.
