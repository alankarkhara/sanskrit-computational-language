# SCL v0.5 stable-candidate: grammatical integrity and evidence

## Four obligations and their precise status

1. **Sourced sūtras:** verified IAST text/numbering for semantic definitions 1.4.24, 1.4.32, 1.4.42, 1.4.45, 1.4.49 and 1.4.54 against GRETIL Pāṇini and secondary commentary. These are *definitions*, not a derivation or proof that case suffixes realize the role. The paradigm tables remain `NOM-*` teaching rules.
2. **Dependencies and precedence:** dependency DAG checker and local explicit-exception-over-general precedence with equal-rank conflict rejection. This is NOT a full reconstruction of Pāṇini's rule ordering, apavāda, vipratiṣedha, or asiddhatva.
3. **Certificates:** cryptographic digest of canonical grammatical output, and independent replay from surface token(s) against morphology and context registry. This rejects naive tampering but is *not* a theorem prover or cryptographically authenticated issuer; source-to-compiler-IR linkage remains an open extension. Existing numeric proof certificates are untouched.
4. **Complete short sentences:** finite whitespace-separated nominal token samples anchored to a supplied predicate. The example `rāmaḥ phalam paṭhati` is supported (predicate passed separately). There is no verb morphology parser, sandhi splitter, agreement checking, or expert-reviewed annotated corpus. Linguist review is **not completed**.

## Example

```
python grammar_cli.py paṭhati rāmaḥ phalam
python grammar_cli.py dadāti rāmābhyām
python grammar_cli.py --registry
python -m unittest discover -s tests -q
```

`analyse_sentence` preserves all locally licensed analyses per token without deciding a global parse. Each semantic role is tagged with a sourced definition, and each licensing rule is marked `local_policy`. The tokens have no automatic syntactic attachment, and unmatched tokens are reported rather than invented.

## Independent review required

Have a trained Pāṇinian grammarian check sūtra applicability, linguistic examples, morphology, role restrictions and any purported exception before a stable grammatical release. For production-grade source-to-IR verification, bind canonical grammatical certificate digests into the program IR and verify that association independently.

Sources: https://www.gretil.uni-goettingen.de/gretil/corpustei/transformations/html/sa_pANini-aSTAdhyAyI.htm ; https://learnsanskrit.org/vyakarana/subanta-1/karaka/
