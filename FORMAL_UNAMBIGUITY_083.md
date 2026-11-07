# SCL v0.8.3 — Formal unambiguity audit

## Scope and claim status

This is an **executable bounded audit**, not a kernel-checked proof of full language correctness. The package keeps SCL v0.8.2 and extends it with `formal083.py`, six regression tests, and a JSON finite-model report. No Lean, Coq, or Z3 executable was available. All inherited files have been retained byte-for-byte.

## Four distinct proof obligations

**Parsing.** The reader is a deterministic, single-pass recursive descent parser of fully parenthesized S-expressions. For every successfully tokenized well-formed input, the implementation constructs one syntactic tree. Ambiguous quotation/Unicode normalization and external file encoding are outside the present formalization; it does not implement arbitrary reader macros.

**Typing.** `expression(exp,env,functions)` computes a single pair `(type, typed_tree)`, or throws `SclError`. Disjoint operator syntax and exact role matching establish a plausible structural-induction uniqueness argument for the restricted trusted syntax and environments. The source code has not been translated into a proof assistant to check its assumptions; ill-formed manually constructed environments and IR are outside this judgment.

**Evaluation.** `evaluate` is a deterministic Python procedure on valid typed IR and acyclic functions, given a concrete environment and budget. It may return a value or error; it has no intended scheduling nondeterminism. Full progress/preservation theorems require a formal specification of runtime errors, uninitialized variables, Unicode semantics, integer operations, and resource bounds. The interpreter assumes that IR comes from the compiler; direct arbitrary IR may not satisfy typing.

**Rewrite observational equivalence.** Seven rewrite identities are admitted. With sufficiently large fuel and within the supported typed expression fragment, algebraic neutral-element rewrites and lazy conditional branch selection preserve values and normal error outcomes. The finite audit exercised 153 supported expressions including division by zero, overflow, nested expressions and unreachable branches, finding zero mismatches with fuel=100000. This is **not** a universal proof. 

## Discovered finite-fuel counterexample

Source `(krama (darśaya (yoga 0 1)))` has a different outcome from its rewrite `(krama (darśaya 1))` at fuel=2: source exhausts step budget, target returns `[1]`.

Thus the proposition `forall P, fuel: observe(P,fuel)=observe(optimize(P),fuel)` is **false** for the present runtime. Correct next choices are either (a) define semantics that abstract from step-count resource limits and clearly state a high-enough-fuel assumption, or (b) instrument optimization with source-cost simulation / accounting so exact cost-sensitive observations are preserved. Do not call the existing optimizer *fully semantics-preserving* under current fuel semantics.

## Implemented audit

`python formal083.py > FINITE_AUDIT_083.json`

`python -m unittest discover -s tests -q`

## Proof-assistant acceptance gate (still open)

1. Specify typed syntax, contexts, error outcomes, evaluation derivations and a fuel-independent observation relation.
2. Prove uniqueness of parsing and typing judgments, deterministic evaluation and rewrite preservation for each permitted identity.
3. Establish a mechanized correspondence theorem or certified parser/compiler translation from actual Python-executed SCL semantics to the formal model.
4. Execute the proof files with a real kernel, record toolchain version/logs, ensure no `sorry`/unproved axioms, and rerun all regression tests.

No external Sanskrit text evaluation is needed for this programming-language milestone.
