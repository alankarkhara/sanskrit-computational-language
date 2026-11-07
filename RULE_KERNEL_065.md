# SCL v0.6.5 — 36 source-linked structured-condition subcases

**Scope:** This release adds 36 distinct sūtra-ID-indexed *bounded premise recognizers* (1.1.1–1.1.36), NOT 36 complete classical sūtra implementations. Inputs are typed feature maps supplied by an upstream grammatical analyzer. The recognizers do not prove that a feature label is linguistically justified, derive Sanskrit word forms, or implement the full inherited environments/exception and visibility mechanisms. The registry records every entry as `bounded_recognizer` to prevent inflated coverage claims.

Source edition: https://www.learnsanskrit.org/texts/ashtadhyayi/book1-1/ ; source semantics require independent Sanskrit-specialist review, especially contextual rules and optional interpretations.

The established v0.6.4 compiler is retained without modification; there is **no automatic binding** from these recognizers to all source-level AST nodes. New integration must use the existing native certificate chain and establish that evidence comes from authenticated typed grammatical states.

Run `python coverage065_cli.py 1.1.1 --field sound --value ā` or `python -m unittest discover -s tests -q`.

**Acceptance gate not met for 36 fully executable grammatical transformations.** This release only meets 36 unique executable, independently testable *guarded classifications*. Real Pāṇinian transformations, general applicability, inherited rules, formal proofs, and independent expert validation remain outstanding.
