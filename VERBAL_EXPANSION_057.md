# SCL v0.5.7 — bounded verbal derivation extension

## Scope and guarantees
- Preserves all 0.5.6 files. New module is `grammar/verbal_expanded.py`; old `grammar/verbal.py` is unchanged.
- laṭ, kartari, parasmaipada; first/second/third person **singular** only; limited bhvādi lexicon.
- Explicit sources 3.2.123, 3.4.77–78, 3.1.68, 1.3.3/8/9, 7.3.84 and 6.1.78, with inherited `aci` (6.1.77) described as rule context.
- `bhū → bho → bhav`, independently logged for 7.3.84 and 6.1.78. Compound `bhavati` then linearized.
- `gam → gacch` is a *lexical exception premise*, **not** an authenticated Pāṇinian derivation. This distinction is machine readable.
- Class membership, formal tiṅ position and thematic selection depend on explicit table/premises, not complete sūtra derivations.
- Request is rejected for other lakāras, padas, persons/numbers, roots rather than silently guessing.
- Replay certification is deterministic recomputation, not a proof-assistant-checked theorem.

## Example
`python verbal_expanded_cli.py bhū` and `python verbal_expanded_cli.py bhū --person 2`.

## Research gaps
General lakāra support, dual/plural tiṅ substitutions, dhātu-pāṭha integration, irregularity licensing, conflict/visibility semantics, expert Sanskrit review, independent proof assistant checking.

## Sources
- https://www.bodharesearch.in/library/sections/ashtadhyayi/3.4.78
- https://brijs.github.io/ashtadhyayi-explorer/sutra/7.3.84/
- https://sanskritdictionary.com/panini/6-1-78
- https://www.premabase.com/siddhanta-kaumudi/p44/textbook/index.html
