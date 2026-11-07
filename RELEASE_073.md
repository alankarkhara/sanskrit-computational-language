# SCL v0.7.3 — Source-attributed linguistic audit and authentic rule overlap

## Tested deliverables
- The complete v0.7.2 archive was extracted as the source baseline; all non-cache inherited files preserved, see `INTEGRITY_073.json`.
- A first source-attributed sandhi fixture set uses public grammatical descriptions of Aṣṭādhyāyī 6.1.77 and 6.1.101, with the input, expected form, rule identity and citation URL in each fixture.
- The audit explicitly reports the raw syntactic competition at `dadhi + indraḥ`: 6.1.77 would yield `dadhyindraḥ` if improperly applied, but 6.1.101 requires `dadhīndraḥ`, suppressing 6.1.77 in that homogeneous vowel context.
- All 343 tests pass (339 inherited + 4 new). `EXTERNAL_AUDIT_073.json` contains individual results.

## Evidence boundary
These source-attributed examples were drawn from published instructional descriptions, not downloaded from an independently annotated dependency treebank and not signed off by an independent Sanskrit scholar. The UD Sanskrit-UFAL public treebank is identified for the independent evaluation phase, but its raw CoNLL-U data could not be retrieved in this offline runtime. **No independent sentence-level accuracy score is claimed.** Nor is this a proof of global confluence or general Pāṇinian correctness.

## Next gating tasks
- Import the actual UD Sanskrit-UFAL test split with pinned version/hash/license, align tokenization, and publish coverage, LAS/UAS and abstention measures without excluding unsupported sentences.
- Build authenticated multi-step Pāṇinian critical-pair examples, covering asiddhatva and inherited applicability, with scholarly interpretation.
- Run a Lean toolchain on a faithful formal model of sorted rewriting and executable semantics, and obtain independent scholarly review.
