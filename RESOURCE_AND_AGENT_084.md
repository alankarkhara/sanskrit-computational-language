# SCL v0.8.4 — Resource observation and agent exchange

## Resource model

`core080.resource084.observe(ir, fuel)` defines an **AST-entry fuel counter**. Every invocation of the expression evaluator consumes one fuel unit, including literals, variables, calls, conditionals and binary operators. Once fuel is exhausted the evaluation returns an explicit `fuel_exhausted` error. Sequential program definitions and outputs share one fuel budget. A partial output prefix remains observable if a later expression fails. The record contains `status`, `output`, `error`, `fuel_limit`, `fuel_used`, `fuel_remaining`, and `event_trace`.

A certificate names a **set of observable fields** and **a finite list of fuel budgets**. For each budget it supplies the source and target observations and an explicit Boolean preservation result. The quantification claim is only over the enumerated budgets. The certificate may validly report failed preservation; the verifier does not confuse a verified failure report with successful preservation. `verify` validates the source-bound rewrite proof using the separate v0.8.2 checker and independently recomputes the resource observations. It does not establish a universal semantic preservation theorem.

Example: `(krama (darśaya (yoga 0 1)))`. The source evaluates three AST nodes; the optimized target evaluates one. At fuel 2 the source exhausts but the optimized target succeeds. At fuel 3 both produce 1, but their `fuel_used` differs. Therefore the compiler must distinguish **value/error preservation under specified budgets** from **resource-trace preservation**.

## Agent communication model

`core080.agents084.Channel` is a closed, deterministic wire protocol for **exactly two named participants**, not a natural-language interpreter. A message has exactly the keys `schema`, `sequence`, `previous`, `sender`, `recipient`, `kind`, `claim_id`, `claim`, and `references`. Canonical JSON serialization and SHA-256 hashes bind a message to the prior message. Duplicate identifiers, wrong sequence, altered predecessor hash, wrong peer, missing claim reference, unauthorized decision or repeated decision are rejected.

Claims have a closed schema: `operator` (`add`, `subtract`, `multiply`, `equal`), `lhs`, `rhs`, `expected`. Inputs are signed 64-bit integers and results must not overflow. Proposals may be wrong. Only the opposing participant can accept a correct claim or reject a false claim; a challenge is also permitted. All validation is deterministic, subject to the implemented protocol. No unconstrained prose fields are admitted.

**Security:** hashes are integrity mechanisms, not digital signatures. A malicious party that can rewrite the full transcript can recompute every hash. Authenticate actors and protect the transcript with a signed transport or hardware-backed keys before using this across a trust boundary. Python's runtime and verifier remain in the trusted computing base.

**Research limitations:** the agent protocol supports only this small arithmetic proposition fragment, no general SCL program AST exchange, no signatures, no network transport, no agent learning, no belief state, and no proof-assistant certification. No claim is made of universal AI-to-AI semantic unambiguity.

## Reproduce

From the release root:

```bash
PYTHONPATH=. python -m unittest discover -s tests -q
```

Illustration:

```python
from core080.resource084 import certify, verify
from core080.agents084 import Channel, verify_transcript
source='(krama (darśaya (yoga 0 1)))'
cert=certify(source,[1,2,3,4],fields=['status','output','error','fuel_used'])
assert verify(source,cert)
assert not cert['preserved_on_declared_budgets']
ch=Channel()
p={'operator':'add','lhs':3,'rhs':5,'expected':8}
ch.append(ch.make('AgentA','propose','p1',p))
ch.append(ch.make('AgentB','challenge','p1'))
ch.append(ch.make('AgentB','accept','p1'))
assert verify_transcript(ch.log)
```
