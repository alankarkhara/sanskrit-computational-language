# SCL v0.4.1 Integrity Profile

This patch is derived from audited v0.4; it is not a full verification of compiler semantics.

## Preservation and semantic contract
- **Legacy default**: `compile_source(source)` and `run(source)` retain original v0.4 rewrite behavior and IR version `SCL-IR/0.4` for compatibility. Previously accepted examples and tests remain usable. This mode permits unproven user rewrite rules and must not be advertised as formally semantics-preserving.
- **Checked opt-in**: `compile_source(source, rewrite_policy="checked")` (also `run`) admits a rewrite only when the entire before/after subtree is a closed expression of *integer literals* using `+`, `-`, `*`, unary negation, and both sides evaluate to exactly the same mathematical integer. Rewrites with variables, calls, division, modulo, booleans, floats and unknown operations are skipped. This establishes equality of mathematical integer results for accepted local rewrites; it is not a complete compiler correctness proof (e.g. resource budgets or AST evaluation costs may differ).
- **Morphological provenance**: `padam(text)` returns `InflectedForm`, a `str` subtype bearing its validated lexical analysis. Grammatical checks now occur on actual bound values, surviving aliases and function returns. Untagged strings preserve previous permissive behavior. Operations that yield ordinary strings discard provenance rather than invent it.
- **Termination**: Existing syntactic decreasing-rule certificates remain per-rule sufficient conditions. `max_rewrites` and cycle detection remain operational controls. There is no total proof of termination for arbitrary legacy rule sets.
- **IR**: `version` remains `SCL-IR/0.4`; optional `ir_schema` and `rewrite_policy` keys are added. Consumers should ignore unknown fields, validate `version`, and never treat AST tuples as cross-version stable binary formats. No migration of arbitrary external IR consumers is guaranteed.
- **Compatibility**: Old grammar and APIs remain. New role checks intentionally reject tagged `padam()` values whose grammar is incompatible even when passed via alias. Legacy unmarked strings remain accepted. Python and IAST Unicode behavior otherwise unchanged.

## Unresolved formal obligations
General user rewrite observational equivalence, a sound static effect system, a full operational semantics and preservation proof, global rewrite confluence, general morphology/case-to-role disambiguation, and formally proven compiler correctness are still open. `checked` is a restricted safety profile, not a full formal-verification system.
