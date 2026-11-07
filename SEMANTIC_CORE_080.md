# SCL 0.8.0 — Strict Semantic Core (research milestone)

## Mission
This is a programming language, NOT a classical Sanskrit text interpreter. `core080/` is a standalone, dependency-free, statically typed programming language fragment inspired by selected Pāṇinian structural principles. Legacy Sanskrit morphology and parsing live in the inherited modules and are not imported by this new core.

## Grammar
```
program ::= (krama declaration*)
declaration ::= (kārya identifier ((role type)*) type expression)
              | (mūlya identifier type expression)
              | (darśaya expression)
type ::= Int | Bool | String
expression ::= integer | satya | asatya | identifier
             | (pāṭha "text")
             | (yoga e e) | (vyavakalana e e) | (guṇana e e)
             | (bhāga e e) | (sama e e) | (laghu e e)
             | (yadi e e e) | (sthāna identifier e e)
             | (āhvāna function (role expression)*)
```
Semicolon comments; single, parenthesized parse; there is no operator precedence ambiguity. Every role must appear exactly once, order-independent; no overload or implicit coercion. Repeated declarations, shadowing of an existing local name, and recursion are rejected. Function definitions cannot read top-level globals; named global values are permitted in output expressions and subsequent value definitions. Forward references to functions are allowed. Global values are computed in source order. Outputs are evaluated after definitions.

## Precise supported semantics
- Int: signed 64-bit with checked overflow; division by zero and nonintegral division are explicit runtime errors.
- Bool: `satya`/`asatya`; expressions `sama` and `laghu`.
- String: explicit `(pāṭha "...")`.
- Functions: pure, nonrecursive, first-order, expression-valued; parameters bound by *semantic roles*. Calls use canonical role order in the IR.
- `yadi` is non-strict in the nonselected branch. No concurrent, random, nondeterministic or mutable operations.
- Bounded evaluation uses a decrementing step counter and rejects excess computation.
- Static acceptance establishes a unique typed AST in the specified language fragment, because each expression constructor has exactly one typing rule and the lexical grammar is unambiguous.
- The evaluator is deterministic for this fragment. **It does not guarantee every well-typed program runs without error**, nor does it establish full language or compiler soundness.

## Evidence
`certify` records SHA-256 of exact source and canonical JSON IR, plus outputs. `verify` recompiles and re-evaluates; it checks byte-for-byte equality of certificate content. This is a replay certificate, NOT a cryptographic signature, proof-assistant certificate, or externally trusted proof.

## Running
```
python core080_cli.py core080/examples/semantic_core_080.scl
python core080_cli.py core080/examples/semantic_core_080.scl --certify > core080_cert.json
python core080_cli.py core080/examples/semantic_core_080.scl --verify core080_cert.json
python -m unittest discover -s tests -q
```

## Scope boundaries / next obligations
General rewriting and rule precedence are still maintained by inherited modules; **not integrated** into this new core. SCL v0.8.1 must add well-scoped typed rewrite declarations, overlap/confluence checking and phase visibility with source-linked derivations. There is no proof-assistant-checked soundness theorem, general semantic-preserving optimizer, mutable state, data structures, recursion or loops in this strictly bounded fragment. Legacy `scl.py` remains available and unchanged.
