# SCL v0.9.1 — Pāṇinian-inspired task policy implementation

## Coverage accounting

**Not a claim of implementing all relevant Aṣṭādhyāyī sūtras.** SCL is a formal AI-task language; direct Sanskrit phonology and morphology rules are mostly not necessary for its purposes. No complete, objectively enumerable set of applicable sūtras has been established.

The two legacy registries in v0.9.0 contained **10** unique authentic sūtra IDs: **2** had bounded executable sandhi cases, **6** were kāraka source definitions only, and **2** were contextual source references. This is not an exhaustive repository-wide count and none of those ten is demonstrated as a complete executable AI-task sūtra.

### Eight mechanism families — release status

| Family | v0.9.1 operational support | Boundary |
|---|---|---|
| Saṃjñā | Closed operation/object/effect glossary and type checking | No general ontology or dependent type theory |
| Kāraka | Explicit requester, assignee, input and result relationships | No independent inference of real-world semantic roles |
| Adhikāra | Executor operation/effect grants and requester-only approval | Grants are symbolic; no cryptographic trust root in this module |
| Anuvṛtti | Constraint inheritance across parent/child delegation | Fixed two-level test; general graph limited to acyclic chains |
| Apavāda | Authorized, recorded constraint exception; `no_external` non-exceptable | Restricted exception vocabulary, not general default-rule theorem |
| Vipratiṣedha | Conflicting competing tasks explicitly marked and cannot be accepted | Reject-only; no confluence / intelligent precedence resolution |
| Asiddhatva | Proposed task states cannot be treated as accepted; parent must commit before child | Not transactional isolation of distributed agents |
| Paribhāṣā | Deterministic fixed meta-policies: reject missing authorities, explicit approval and non-delegable prohibitions | Meta-policies coded in trusted interpreter, not independently certified |

This extension executes all **eight scoped computational adaptations** to varying bounded degrees; none should be counted as a complete directly implemented historical numbered sūtra. True semantic grounding, user intent interpretation, distributed authorization and machine-checked formal proofs remain open.

### CLI

```bash
python policy091_cli.py core080/examples/paninian_policy_091.scl > policy_certificate.json
python policy091_cli.py core080/examples/paninian_policy_091.scl --verify policy_certificate.json
python -m unittest discover -s tests -q
```

### Safety and nonprogrammer experience

A user should not need to type this syntax. Existing v0.9.0 guided interface covers only a narrow counted-token request; this extension adds policy semantics, **not** a general conversational interface. A future guided UI must expose inherited constraints and delegation scope and obtain approval for ambiguity or external effects. Comparing SCL to natural-language AI task requests requires prospective controlled user research.
