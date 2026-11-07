# SCL Formalization, version 0.4.2

## Status and scope

This is a **restricted executable formal model**, not a machine-checked proof, a verified compiler, or a complete account of Sanskrit grammar. The previous SCL 0.4.1 AST schema remains unchanged. The added `formal` IR metadata is versioned independently as `SCL-Formal/0.4.2`. Legacy mode is intentionally preserved to avoid silently changing prior programs. For security-sensitive/scientific programs use `--rewrite-policy formal` (equivalent to the `checked` rewrite admission criterion in 0.4.1).

## Small-step intentions and operational rules

Runtime configurations are `(statement/expression, environment, store, function table, trace, fuel)` with a left-to-right call-by-value evaluation order. The current interpreter concretely implements these rules via Python evaluation. `trace` records externally observable `darśaya` output and errors; fuel bounds statement/loop execution.

Expression evaluation is specified inductively:

- `⟨literal(v), σ⟩ ⇓ (v, ε)`.
- `⟨name(x), σ⟩ ⇓ (σ(x), ε)` if bound, otherwise raises `Undefined variable`.
- For strict binary `⊕`, evaluate `e₁` then `e₂`; compute `v₁ ⊕ v₂` or produce an error. The ordering matters even for commutative numeric operators.
- For `ca` and `vā`, evaluate the left operand first and conditionally skip the right operand (short circuit).
- For `call(f,a₁,…,aₙ)`, evaluate arguments from left to right, then evaluate named arguments in insertion order, bind by parameter name or unique declared kāraka annotation, evaluate the callee body, then return; `darśaya` appends output to the trace.
- `yadi` evaluates its condition once; `yāvat` reevaluates the condition before each iteration. `pratyāvartaya` exits its current function.
- Out-of-fuel is an observable termination-with-error condition. Python-native floating point operations, unbounded integers, and implementation recursion constraints are part of the current interpreter's execution model, rather than an abstract hardware-independent numeric specification.

These evaluation rules describe the implementation; exact trace equivalence beyond the restricted arithmetic fragment is not proven.

## Typed effect judgment

`Γ;Σ ⊢ e : τ ! ε`, where `Γ` gives variable types and `Σ` gives function signatures, `τ ∈ {saṅkhyā, pāṭha, tarka, ?}`, and `ε ⊆ {read, raise, call, io}`. The `?` type is unknown and must not be interpreted as type safety. `read` denotes a variable lookup, `raise` possible evaluation failure, `call` a function invocation, and `io` observable output. Every binary/unary operation conservatively carries `raise` because its dynamic implementation may fail. A user-defined function invocation is conservatively assigned all possible effects; the report does **not** infer interprocedural purity. Short-circuit expressions are upper-bounded by effects on either branch, whether evaluated or not. The executable APIs `typed_expression_judgment`, `expression_effects`, and `effect_report` produce conservative, JSON-compatible reports.

**Limitation:** this is a conservative *type-and-effect analysis*, not a proof of type soundness. Flow-sensitive types, polymorphism, exceptions as first-class values, whole-program effects, and user-defined function effect annotations remain open.

## Restricted rewrite preservation theorem

Let `E` be an expression in grammar `e ::= n | -e | e+e | e-e | e*e`, where `n` is an integer literal. Suppose both `e` and replacement `e′` can be evaluated by the exact mathematical-integer evaluator, and `value(e)=value(e′)`. Then, *in that exact-integer mathematical fragment*, replacing `e` with `e′` preserves its integer value, has no variable lookups or I/O, and terminates at that redex. Proof: induction on expression structure; each primitive integer operation is total and effect-free in the mathematical model; substitution of equal integer results into a pure integer arithmetic context preserves the context result.

The actual implementation realizes the criterion through `checked_rewrite`. It excludes division, remainder, floats, booleans, calls, symbolic names, and short-circuit expressions. **Caveat:** its evaluation uses Python arbitrary-precision ints and imposes no explicit arithmetic gas budget; resource consumption and Python implementation exceptions are not included in the theorem. No global observational-equivalence guarantee for arbitrary enclosing SCL contexts is claimed. The original program is statically checked before rewriting, and the rewritten program is checked again.

## Confluence and termination criteria

A rewrite system is confluent iff for all `s →* a` and `s →* b`, there exists `c` with `a →* c` and `b →* c`. For a terminating rewrite system, local confluence suffices for global confluence (Newman's lemma); in a suitable first-order term-rewriting system, joinability of all critical pairs provides a practical local-confluence check, subject to the usual formal hypotheses.

Priority-based winner selection only provides **deterministic selection under the implemented strategy**, not mathematical confluence. Detection of repeated terms and rewrite budgets does **not** prove termination. Existing rule-level skeleton-size certificates apply only under their stated variable multiplicity assumptions and do not establish termination of arbitrary collections of rules or evaluation. `rule_confluence_report` marks only the empty rule set globally certified. Nonempty systems remain unproved pending critical-pair generation and joinability proof with a terminating reduction measure.

## Vibhakti and kāraka: separate sorts

**Vibhakti:** morphosyntactic case evidenced by a word's inflection (e.g. `rāmeṇa` → instrumental/tṛtīyā in the closed singular `rāma` paradigm). **Kāraka:** semantic-syntactic relation in a construction (e.g. `karaṇa`, `kartā`), which cannot in general be inferred from surface case alone. The `grammatical_evidence` output therefore sets `semantic_role: null` and gives a *candidate* role set rather than an inferred role. `validate_contextual_karaka(evidence, declared_role)` checks a contextually declared role against a conservative teaching table. E.g. `tṛtīyā` currently licenses both `kartā` and `karaṇa`. This is a licensing check, **not** proof that a particular sentence realizes that role. The closed paradigm does not generalize to other stems, genders, numbers, constructions, or all Sanskrit case usages. The runtime continues to allow unmarked ordinary strings for backward compatibility; strict grammatical evidence requirements will require an explicitly opt-in future mode.

## Outstanding proof obligations

1. Give a full language-independent dynamic semantics for SCL numbers and errors; prove progress/preservation for a well-typed fragment.
2. Prove operational trace preservation for a stated effect-safe rewrite class, including contextual substitution and resource limits.
3. Implement unification/critical-pair enumeration and joinability certificates for nonempty rewrite rule sets.
4. Separate morphology, syntactic dependency, and compositional semantic kāraka inference in a broader Sanskrit corpus.
5. Establish formal IR migration guarantees and property-based/differential verification across all releases.
