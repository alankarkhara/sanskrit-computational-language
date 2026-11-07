# SCL v0.8.1 — Restricted certified rule compiler

## Scope
This is a *programming-language* rewrite engine, not Sanskrit text analysis. Its nomenclature is inspired by four Pāṇinian control mechanisms; its semantics are deliberately explicit and narrower than their classical counterparts.

- **Adhikāra (scope):** `scopes` intersect enabled rewrite identifiers at the `global` or `function:name` boundary.
- **Anuvṛtti (inheritance):** `inherited.enabled` and `inherited.phases` set global policy for downstream optimization passes.
- **Apavāda (exception):** an active matching winner suppresses listed matching general alternatives. Circular mutual suppression is rejected.
- **Asiddhatva-inspired visibility:** two named phases, `initial` and `simplified`. A rule is only eligible in its declared phase. This is not a complete model of classical asiddhatva.

All supplied policy fields are validated. The rewrite set is fixed and consists of:
`add-zero-left`, `add-zero-right`, `sub-zero`, `mul-one-left`, `mul-one-right`, `if-true`, and `if-false`.

## Restricted semantic-preservation argument
For 64-bit operands, `0+x=x`, `x+0=x`, `x-0=x`, `1*x=x`, `x*1=x`; if the other operand would fault under eager evaluation, the transformed term still evaluates it. No integer overflow is induced by the dropped neutral arithmetic operation. For `if(true,a,b)` and `if(false,a,b)`, evaluation is already lazy in v0.8.0, so elimination of the unselected branch preserves program results and exceptions. There is *no* general assumption that `0*x=0` is a safe optimization because it could discard errors in `x`. Therefore zero multiplication is not offered.

The source and rewritten programs preserve values or computational errors in this supported fragment, under ordinary unbounded step allowances. Exact instruction counts and step-budget exhaustion are *not* preserved. The compiled IR is re-created from the original typed v0.8.0 IR, restricting rules to typed nodes. The certificate verifier independently reruns the same implementation, but is not a separate trusted proof checker or a Lean theorem.

## Rule conflicts
When multiple rules match the same node, declared active exceptions suppress lower-priority alternatives. If the remaining rules have structurally identical results, the match is joinable. If none remain, the compiler rejects the configuration. If incompatible results remain, compilation rejects rather than choosing an arbitrary interpretation. The present whitelist has no distinct incompatible outcomes, so this last defensive path has not yet been exercised against authentic conflicting identities.

## Example

```sh
python core081_cli.py core080/examples/semantic_core_080.scl
python core081_cli.py core080/examples/semantic_core_080.scl --certify > certificate.json
python core081_cli.py core080/examples/semantic_core_080.scl --verify certificate.json
python -m unittest discover -s tests -q
```

Optional config JSON:

```json
{
  "inherited":{"enabled":true,"phases":["initial","simplified"]},
  "rules":["add-zero-left","add-zero-right","if-true"],
  "scopes":{"function:calc":["add-zero-left"]},
  "visibility":{"if-true":"simplified"},
  "exceptions":{"add-zero-left":["add-zero-right"]},
  "max_passes":24
}
```

## Limits and research obligations
The v0.8.1 compiler does not provide full classical grammatical semantics, arbitrary formally certified user-defined rewrite rules, mechanically kernel-checked preservation, optimization of recursive programs, or full semantics-preserving machine code. Full semantic equivalence for finite-resource behaviors (including step budgets) is not claimed. Current testing is an implementation and restricted identity audit, not a proof of general program equivalence or competitive superiority.
