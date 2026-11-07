# SCL v0.5.5 — Typed Derivation State

The new `grammar.typed_state` module implements an immutable, checked state with fields for a **dhātu**, **pratyaya**, inflectional features, derivational phase, **it** marker, residual ending, surface form, and rule visibility. Each transition has its own guard, and every state enforces phase invariants. Certificates are replayed by a separate call to the deterministic generator and compared byte-for-byte at the structured JSON level.

## Covered derivation

Input: `paṭh` + explicitly supplied `tip` and features `laṭ / parasmaipada / prathama / ekavacana`.

1. `1.3.3` identifies final `p` as an indicatory marker in **this specific upadeśa**.
2. `1.3.9` removes the marked final `p`, leaving `ti`.
3. `SCL.AFFIX_ATTACH` combines `paṭh + a + ti -> paṭhati`. The intervening `a` is a **local, explicitly assumed operation**, not a certified classical derivation from the Aṣṭādhyāyī.

The example demonstrates a typed transition architecture **but is not a full traditional derivation of paṭhati**. In particular, lakāra-based affix selection, vikaraṇa selection, full metarules, and global rule visibility remain future obligations. Refuse unsupported roots/affixes instead of silently producing forms.

## Verification guarantees

- Dataclass instances are immutable, validated, and phase-constrained.
- The verifier recomputes the entire derivation; a matching hash alone is insufficient.
- Certificate validation is **not** proof-assistant verification or independent scholarly review.
- Existing compiler modules and entry points are copied unchanged. Full compatibility is established only for exercised tests.

Run `python typed_derivation_cli.py paṭh tip`, or write JSON to `cert.json` and run `python typed_derivation_cli.py --verify cert.json`.
