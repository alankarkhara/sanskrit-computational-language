# SCL v0.5-beta: Contextual Grammar Contract

The system implements a bounded pedagogical grammar model. It does **not** implement or quote authentic Aṣṭādhyāyī sūtras. Rule IDs `CTX-*` are SCL-local, and registry entries disclose that no primary-source attribution has been verified. Morphological trace `NOM-*` is retained.

- `MorphologyEngine.analyze(surface)` yields zero or more case/number/lemma analyses, **without** inferred semantic kāraka.
- `ContextEngine.candidates(surface, predicate, role=None)` filters all analyses by an explicitly declared predicate frame and (optionally) the intended role. No confidence ranking or first-match choice.
- Predicate frame assertions are pedagogical licensing constraints. For example `dadāti` admits `sampradāna` with `caturthī`; `gacchati` admits `apādāna` with `pañcamī`. This is not a universal vibhakti-to-kāraka law.
- If a role is absent from a predicate's frame, raise an error; if no known surface-form analysis qualifies, return the empty tuple. Never invent morphology.
- `kārakasaṅkhyā(surface, predicate)` returns the candidate count in SCL; `kārakaparīkṣā(surface, predicate, role)` returns whether at least one analysis is licensed.
- These two builtins are classified as potentially raising (effectful), therefore not admitted into the pure symbolic optimization fragment.

## Rule registry, precedence and exceptions

The v0.5-beta registry records model provenance, scope, status and an explicit `sutra_reference: null`. Derivation traces append frame, licensing and ambiguity policy identifiers. The frame lookup is deterministic and introduces no non-confluent rewrite choices. **Full Pāṇinian rule ordering, apavāda, asiddhatva and authentic sūtra-dependency graphs remain unimplemented**; none are claimed.

## Integrity

v0.5-alpha interpreter, morphology API, numerical proof kernel, and rewrite strategies are retained. The new contextual layer is opt-in, invoked through its new API or two builtins; no previous syntax is repurposed. Automated tests are regression evidence, not a compiler-soundness proof.
