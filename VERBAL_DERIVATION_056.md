# SCL v0.5.6 — Restricted verbal derivation specification

This release introduces `grammar/verbal.py`, a typed finite-state trace for four explicitly declared consonant-final class-1 lexical roots and a third-person singular present active parasmaipada form. The older v0.5.5 compiler, modules, tests and user-facing commands remain unchanged.

## Source-backed operations

- 3.2.123 (*vartamāne laṭ*): select present lakāra given the present-time semantic premise.
- 3.4.78 with inherited 3.4.77: select `tip` for the fixed prathama/ekavacana/parasmaipada case.
- 1.3.3 and 1.3.9: recognize and elide final `p` of `tip`.
- 3.1.68 (*kartari śap*), conditioned by 3.4.113: select `śap` as a thematic affix for the explicitly supported class and construction.
- 1.3.8, 1.3.3 and 1.3.9: recognize and remove `ś` and `p` of `śap`, leaving `a`.
- `LINEARIZE` concatenates the residual pieces; it is an administrative action, not an authenticated Sanskrit grammatical rule.

Sources: https://www.learnsanskrit.org/vyakarana/tinanta/prakriya/ ; https://brijs.github.io/ashtadhyayi-explorer/sutra/3.1.68/ ; https://sanskritdictionary.com/panini/1-3-8 ; https://www.sanskritdictionary.com/panini/3-2-123 .

The traditional account also involves lexical dhātu identification, lakāra markers, inherited conditions, pada selection and other grammatical operations. These are represented as **explicit premises**, not claimed as completely derived. Support is restricted to paṭh, likh, vad, pac with expected third-person singular surface forms. The root-class assumptions have not received independent linguistic review. No general inference of arbitrary dhātu class or exception behavior is made.

## Assurance

The certificate records source links, stage invariants and explicit operations. The verifier recomputes the trace and checks the entire payload, not just its hash. This is computational replay, not an independently checked formal proof or external philological certification.

Run `python verbal_cli.py paṭh` or redirect the JSON certificate to a file and execute `python verbal_cli.py --verify file.json`.
