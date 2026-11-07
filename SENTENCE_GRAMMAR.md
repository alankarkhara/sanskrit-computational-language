# SCL v0.5 — bounded sentence grammar and source audit

## Exact implementation boundary

This is an **additive** module (`grammar/sentence.py`); the historical SCL interpreter and grammar APIs were left unchanged. It checks whitespace-separated nominal surface forms followed by **one final finite verb** and returns alternative dependency analyses. It supports only third-person, active, present-tense (laṭ), parasmaipada surface forms in an explicit nine-form table (paṭh-, gam-, dā- across singular/dual/plural). It does **not** derive those nine forms using the full succession of Pāṇini's operations. The present inventory is pedagogical, not exhaustive.

SCL uses a closed, documented mini-lexicon for nominal forms (`morphology/engine.py`) with six lemmas. The solver rejects unsupported verbal forms, agentless clauses, active-voice case patterns outside its local licensing policy, role duplication, agreement disagreement, unknown words, and exhaustion of the analysis budget. A rejection means **outside SCL's supported fragment**, not necessarily ungrammatical Sanskrit. No sandhi splitting, null subject inference, pronouns, relative clauses, coordination, compounds, passive voice, semantic selection, or long-distance dependencies.

## Layer separation

1. **Form recognition:** attested-looking surface inflections are stored as explicit `VERBS` entries. Each records root label, predicate label, number, and construction frame. A table entry is *not* a derivation from the Aṣṭādhyāyī.
2. **Nominal morphology:** `MorphologyEngine` supplies every recognized lemma/case/number reading; syncretism is retained.
3. **Local contextual policy:** only nominative-as-agent, accusative-as-object, and dative-as-recipient active constructions are admitted where the predicate frame allows them; these mappings are not claimed to be universally valid Sanskrit laws.
4. **Agreement:** one overt nominated agent must match the finite verb's number. Third person is fixed by this prototype's verb inventory; gender agreement with a finite verb is not imposed.
5. **Dependency analysis:** each licensed nominal is linked to the finite verb with its role. Duplicate-role assignments are disallowed in this simple-frame subset. All complete assignments are returned.
6. **Certificate replay:** a deterministic JSON payload is hashed and replayed by recomputing the parse from the recorded input, with the same local implementation. This is not independent logical proof or expert review.

## Source-traceable *relevant* sūtras — not full derivations

| Sūtra | Reference relevance | What SCL actually does |
|---|---|---|
| 1.4.54 *svatantraḥ kartā* | Defines agent | Links eligible nominative argument to agent under local active policy |
| 1.4.49 *kartur īpsitatamaṃ karma* | Defines object | Uses an explicit accusative-object policy without proving the semantic criterion |
| 1.4.32 *karmaṇā yam abhipraiti sa sampradānam* | Recipient relation | Local dative recipient in a giving frame |
| 1.4.108 *śeṣe prathamaḥ* | Third-person verbal ending category | Fixed third-person finite verb inventory |
| 3.4.78 *tip-tas-jhi ...* | Enumerates verbal endings | Inventory is tagged by number; no actual suffix derivation performed |

Source records:
- https://www.sanskritlibrary.org/grammatical/data/A.1.4.108.html
- https://ashtadhyayi.com/sutraani/3/4/78
- https://learnsanskrit.org/vyakarana/subanta/karaka/
- https://www.bodharesearch.in/library/sections/ashtadhyayi/1.4.32

These citations establish that the *referenced sūtras exist and are relevant*, not that they completely derive SCL outputs. The independent human review required by `GRAMMAR_REVIEW_PROTOCOL.md` is **pending**.

## Run

```sh
python sentence_cli.py 'rāmaḥ phalam paṭhati'
python sentence_cli.py 'rāmau gacchataḥ'
python -m unittest discover -s tests -q
```

Interpretations such as “Rāma reads a fruit” are syntactically analyzable in the simplified grammar but pragmatically unusual. The analyzer is **not** a semantic plausibility checker.

## Acceptance evidence

Use the automated tests in `tests/test_sentence.py` for nominal-role ambiguity, agreement, dependency edges, unsupported constructions, tampered certificates, and order-insensitivity. Inherited regression tests cover unchanged interpreter modules. The tests do not establish completeness or full correctness for Sanskrit.

## What remains for genuine Pāṇinian coverage

A machine-readable **complete sūtra corpus**, structured anuvṛtti and adhikāra scopes, it-markers, pratyāhāra interpretation, root/affix derivations, ordered phonological changes, sandhi, kāraka/vibhakti and prayoga choices, nontrivial precedence/exception/asiddhatva mechanisms, and an independently reviewed set of derivation traces are all missing. Full implementation concerns roughly four thousand interconnected sūtras and associated traditional interpretations; this module references only a handful.
