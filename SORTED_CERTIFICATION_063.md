# SCL 0.6.3: Sorted unification, conditional overlap checks, source-bound compiler chain

## Scope

An additive module to v0.6.2. Historical interpreter and legacy execution modes remain unchanged. This is an **executable validation kernel**, not an independently kernel-checked theorem proving system, and it does not implement the full Aṣṭādhyāyī.

## Mathematical model

A many-sorted signature Σ consists of constructors `f:s₁×⋯×sₙ→s` and a context Γ mapping variables to sorts. Well-formedness is inductive:

* Γ(x)=s implies Γ ⊢ x:s.
* Σ(f)=(s₁,...,sₙ)→s and Γ ⊢ tᵢ:sᵢ imply Γ ⊢ f(t₁,...,tₙ):s.

A well-sorted substitution σ satisfies Γ ⊢ σ(x):Γ(x) for every variable in its domain. **Substitution lemma:** if Γ ⊢ t:s and σ is well sorted, then Γ ⊢ tσ:s. Proof by induction on term structure: variable case follows from the assumption on σ; constructor case applies the inductive hypotheses to all arguments and then the constructor signature. This is a mathematical proof sketch, not Lean-checked source.

**Unification invariant:** each new variable binding has equal sorts and passes the occurs check; after each binding, substitution composition preserves sort. Hence whenever unification succeeds, both instantiated input terms are well sorted and equal. This implementation checks the invariant operationally; no independent proof assistant certification is claimed.

**Rewrite preservation:** if l→r has equal sorts, Var(r)⊆Var(l), the matched substitution is well sorted and its runtime guards hold, then replacing a matched subterm of sort s by rσ preserves the sort of the enclosing expression. This follows from the substitution lemma and a structural induction on the one-hole context. Rule type declarations and actual reductions are both checked.

## Conditional critical pairs

Rules are renamed apart, a sorted most general unifier is computed for each nonvariable overlap, and residual variables are instantiated from finite declared domains. Guards are checked after instantiation; suppressed rules are removed, and surviving competing paths are explored. The result `exhaustive-finite-domains` means that candidate ground instantiations were exhausted under the maximum assignment limit. Joinability exploration has a separate state bound and may return `unknown-bound`. This is **not universal confluence**, particularly for infinite sorts, unenumerated contexts, or classical Pāṇinian meta-rules.

## Source associations

* 6.1.77 `iko yaṇ aci`: vowel to corresponding semivowel before a vowel; implementation models an **i-boundary subcase**.
* 6.1.101 `akaḥ savarṇe dīrghaḥ`: same-class vowels produce a long vowel; the restricted model suppresses 6.1.77 for i + i/ī.
* 7.3.101 `ato dīrgho yañi`: a thematic-stem vowel lengthening context before first-person m/v-initial endings; the verifier tests applicability conditions but **does not itself construct full verbal surface forms**.

Source links: https://brijs.github.io/ashtadhyayi-explorer/sutra/6.1.77/ ; https://sanskritdictionary.com/panini/6-1-101 ; https://brijs.github.io/ashtadhyayi-explorer/sutra/7.3.101/ .

The sandhi model's `resolved` term records a *boundary result marker*, not an independently validated full phonetic surface form. The `inherited` declarations are executable prerequisite identifiers, not a general reconstruction of *anuvṛtti* or *adhikāra*. Phase ordering approximates restricted visibility; it is not full *asiddhatva*.

## Compiler certificate

`chain063_cli.py` compiles a supplied source file using `certified` policy, computes its IR digest, enumerates finite-domain conditional pairs and records the source digest, rule-registry digest, selected grammatical rule, resulting typed term, and witness terms in a versioned certificate. Verification **recomputes** the compilation and the grammatical checks rather than trusting stored digests. Such certificates show consistent execution by the supplied trusted Python checker, not independent soundness of the compiler, nor automatic grammatical analysis of source expressions. The sandhi request is explicitly provided; it is not inferred from an arbitrary source program.

## Remaining requirements

Actual many-sorted grammatical intermediate representation and linking of each source AST node to each grammatical derivation; complete inherited grammatical environments, general constraints and phases; source-scholarly derivation review; external Lean/Coq progress and preservation proofs; termination bounds or proofs for production rule sets; independent checking of the compiled IR semantics.
