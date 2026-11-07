# SCL v0.5.2 — Remaining architectural obligations: execution ledger

## Implemented and reproducibly tested
- Original 0.5.1 interpreter and historical runtime defaults retained without edits.
- Explicit **reject-unknown** schema migration policy: same-schema round-trip only, no invented cross-schema conversions.
- Open-expression evidence gate records necessary obligations but **does not authorize code generation based on untrusted Boolean attestations**. Open symbolic program rewrites remain uncertified.
- Expanded pending-review sentence corpus from 7 to 11 samples; negative and structurally ambiguous cases are annotated rather than declared correct.
- Lean 4 source candidate of *a smaller total intrinsically typed Nat/Bool F0 language*, with progress-by-total-evaluation and canonical algebraic identities; NOT executed by Lean here.

## Remain external / open
- Lean toolchain execution and independent proof assistant checking; independently validated small-step progress/preservation for the real F0 syntax and exceptional semantics.
- General source-to-IR typing and effect proof for open symbolic programs; observational equivalence for effectful contexts.
- Actual migration mappings from historical IR formats, including migration correctness tests; currently fail closed.
- A linguist's independent signed review of Sanskrit case analyses and sūtra citations; none obtained.
- Full derivations for Pāṇini's Aṣṭādhyāyī, with phonology, affix rules, precedence, anuvṛtti and exceptions.

## Release criterion
Do not call the whole SCL compiler verified or its Sanskrit analyses scholarly approved. The current package is a **soundness-gated development candidate**, not a completed formal proof of the compiler. All older features must continue to pass inherited regression and golden compatibility tests.
