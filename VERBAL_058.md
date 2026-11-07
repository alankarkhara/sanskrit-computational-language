# SCL v0.5.8 — bounded present verbal paradigm and verification contract

Scope: **laṭ, kartari, parasmaipada only**; six roots (`paṭh`, `likh`, `vad`, `pac`, `bhū`, `gam`); nine person–number cells. No other lakāras, padas, semantic valencies, or dhātu classes are newly accepted. Earlier interpreter and public CLI remain unchanged. New API: `grammar.verbal_058.derive`, `verify`; command `python verbal_058_cli.py gam --person 3 --number pl`.

## Executed operations and evidence classification

* 3.4.78 supplies tiṅ upadeśa items: `tip/tas/jhi`, `sip/thas/tha`, `mip/vas/mas`.
* 1.3.3 and 1.3.9 remove upadeśa `p` in `tip/sip/mip`. 3.1.68 selects `śap` within the bounded class-1 premise and 1.3.8/1.3.3/1.3.9 yield `a`.
* 7.3.101 lengthens thematic `a` to `ā` before first-person m/v-initial endings. 7.1.3 handles third-person plural `jhi` to `anti` under limited inherited conditions. For the third plural, thematic `a` is eliminated at the vowel boundary by a **local rule**, which is NOT certified as a complete sutra-level derivation.
* Dual and first-person plural final `s` runs through `s → ru` (8.2.66), `ru → r` (indicatory `u` deletion) and pause `r → ḥ` (8.3.15). These operations are modeled on the bounded grammatical path and do not claim complete pada-level rule visibility.
* `bhū`: 7.3.84 then 6.1.78, yielding `bhav` before thematic `a`. `gam`: 7.3.77 substitutes `ch` for root-final `m` before śit `śap`; 6.1.73 inserts `tuk` in the short-vowel environment, modeled as `gach → gacch`. This is no longer an unproved lexical base lookup, but the rule-inheritance and visibility model is still restricted.

## Limitations

All affix selection relies on declared root-class, voice/pada and inherited conditions. It is **not a full Pāṇinian prakriyā**. The derivation certificate is deterministic Python replay and digest comparison, **not** an independently checked mathematical proof or Sanskrit scholar certification. `BOUNDARY_A`, `LINEARIZE` and phase ordering are local implementation mechanisms, not invented Pāṇinian sūtras. External scholarship is required before labeling a chain linguistically certified.

This is an additive compatibility release. Running inherited tests establishes the covered regression behavior, not equivalence for all source programs.

## Reference sources

- Aṣṭādhyāyī 7.3.101: https://brijs.github.io/ashtadhyayi-explorer/sutra/7.3.101/
- Aṣṭādhyāyī 7.3.77: https://brijs.github.io/ashtadhyayi-explorer/sutra/7.3.77/
- Aṣṭādhyāyī 6.1.73: https://brijs.github.io/ashtadhyayi-explorer/sutra/6.1.73/
- Aṣṭādhyāyī 7.1.3: https://sanskritdictionary.com/panini/7-1-3
- Aṣṭādhyāyī 8.3.15: https://sanskritdictionary.com/panini/8-3-15
- Ending overview: https://www.premabase.com/siddhanta-kaumudi/p44/textbook/index.html
