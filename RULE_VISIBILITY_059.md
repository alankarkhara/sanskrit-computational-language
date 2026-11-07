# SCL v0.5.9 — Inheritance and visibility gate

## Scope
Additive module `grammar/verbal_059.py` and CLI; v0.5.8 and earlier files retained. Scope is six declared class-1 roots, laṭ kartari parasmaipada, 3 persons × 3 numbers. Other constructions fail closed.

## New authenticated boundary operation
`6.1.97 ato guṇe` applies to `a + anti` yielding `anti` via *para-rūpa* (following form). Context: non-pada-final `a`, following guṇa vowel `a`, continuous phonological domain. Its interpretation includes inherited `6.1.84 ekaḥ pūrvaparayoḥ`, and `6.1.72 saṃhitāyām`. Earlier `BOUNDARY_A` was a locally defined operation. This release encodes 6.1.97 and applies explicit checks before surface linearization.

## Inheritance and rule-visibility gate
Machine-readable RULE_MODEL states scope, dependencies, applicability and limited visibility phase for 6.1.97, 7.1.3, 7.3.101 and 8.3.15. The replay verifier checks chain integrity and deterministic regeneration, not a fully independent Sanskrit grammar kernel.

## Explicit limits
The simplified finite phase sequence is NOT universal Pāṇinian `asiddhatva`; several roots and affix operations still encode assumptions; sources are references requiring human scholarly evaluation. Full classical `anuvṛtti`, `adhikāra`, `vipratiṣedha`, `apavāda`, and `asiddhatva` across ~4000 sutras remain unsupported.

## External sources
- https://learnsanskrit.org/vyakarana/tinanta/prakriya/ — 6.1.97, 7.1.3, 7.3.101 and inherited conditions
- https://sanskritdictionary.com/panini/6-1-101 — 6.1.101 and 6.1.84 inheritance

## Validation
Run `python -m unittest discover -s tests -q` and `python verbal_059_cli.py bhū --person 3 --number pl`. Independent Sanskrit scholarly review remains pending.
