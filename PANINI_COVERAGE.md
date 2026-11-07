# Pāṇinian Rule Coverage and Generative Derivations — v0.5.3

This additive milestone retains the v0.5.2 interpreter unchanged. Four authentic sūtra references are recorded with individual provenance; only two have **bounded executable** subcases. The other two supply contextual/interpretive dependencies. This is not coverage of every phonetic context or a full generative Sanskrit morphology system.

| Sūtra | Role | Executable coverage |
|---|---|---|
| 1.3.10 yathāsaṃkhyam anudeśaḥ samānām | ordered correspondence | interpretive dependency only |
| 6.1.72 saṃhitāyām | continuous context | contextual dependency only |
| 6.1.77 iko yaṇ aci | i/u/ṛ/ḷ family substitution before unlike vowels | bounded |
| 6.1.101 akaḥ savarṇe dīrghaḥ | homogeneous vowel contraction | bounded |

**Rules and precedence:** overlapping candidate substitutions are not resolved by an arbitrary priority. The explicit homogeneous-vowel condition routes the derivation to 6.1.101; 6.1.77 is restricted to unlike vowel families. Unsupported boundaries fail closed. These are local eligibility decisions and do not implement Pāṇini's complete precedence mechanisms.

**Proof boundary:** Certificates carry full input, output, source-registry hash, one step, dependency IDs, and a content digest. Verification repeats derivation against the installed rule implementation. This provides deterministic replay and tamper detection, not an independently checked proof of grammatical correctness or historical completeness.

**Expert review:** source URLs allow philological review; scholarly signoff is not claimed. These specific rules have not been exhaustively implemented, and generation is only for a single word-boundary vowel transformation. Full nominal/verbal derivations, it-marker handling, saṃjñā, anuvṛtti, adhikāra scoping, asiddhatva, and exceptions remain open.

Run `python derivation_cli.py dadhi indraḥ`, `python derivation_cli.py --coverage`, or `python -m unittest discover -s tests -q`.
