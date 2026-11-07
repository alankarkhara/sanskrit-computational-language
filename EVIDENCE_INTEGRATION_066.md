# SCL 0.6.6 — Evidence provenance and native certificate gate

## What is implemented

The 0.6.5 registry of 36 bounded recognizers remains unchanged. `grammar/evidence066.py` adds:

1. An immutable phoneme sequence and a typed boundary, parsed directly from normalized IAST strings. Invalid segments are rejected.
2. State-derived applicability subcases for IDs 1.1.1, 1.1.2, 1.1.3, 1.1.7, and 1.1.21. These do not claim complete coverage of the cited sūtras. In particular, 1.1.3 is a membership precondition, not the complete semantic force of *iko guṇavṛddhī*.
3. Reuse of the existing native 6.1.77 / 6.1.101 vowel-boundary transformations and documented exception suppression. These operations are restricted to the prior sandhi model and are not fresh whole-sūtra implementations.
4. A certificate gate joining a literal `sandhi_pramāṇa` AST node, its digest and path, its input-specific rule result, original source digest, and certified-policy compiler IR digest. Unsupported or missing AST evidence fails closed.
5. Exhaustive enumeration of the **169 ordered boundary pairs** from the declared thirteen-vowel inventory: **60** use 6.1.77, **16** use 6.1.101 and **93** are unsupported. These counts are implementation results, *not* proof of all classical sandhi possibilities. Finite enumeration only.
6. Replay of the complete requested certificate and mutation detection.

## Explicit limits

- The 36 recognizers are not 36 complete transformations. Five identifiers now receive state-derived phonological evidence; the other 31 still need authenticated syntactic or lexical context. This release adds no independently certified complete sūtra.
- A typed Python dataclass does not constitute a proof-assistant type-preservation theorem.
- Source-linked is not independent expert-reviewed. No external scholar has reviewed this version.
- Native certificate integration covers **literal sandhi calls** only, not general SCL program semantics or all grammatical expressions.
- `AffixState` authenticates only the supported `tip` input category; no general affix semantics are inferred.
- No automatic general *anuvṛtti*, *adhikāra* or *asiddhatva* proof is claimed.

## Run

```bash
python -m unittest discover -s tests -q
python evidence066_cli.py --audit
python evidence066_cli.py examples/native_sandhi_064.scl --requests examples/evidence066_requests.json > cert.json
python evidence066_cli.py examples/native_sandhi_064.scl --requests examples/evidence066_requests.json --verify cert.json
```

## Next acceptance gate

Carry explicit grammatical provenance through nominal and verbal states; add an independent checker for typed transitions, critical-pair witnesses with grammar environments, external review corpus and formally kernel-checked substitution lemmas. Do not count a classification rule as a transformation until the actual derivation and failure conditions are implemented.
