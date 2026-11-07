# SCL v0.8.7 — Typed task dialogues

## Design goal
Formalise who requests what action, on which uniquely named target, with which output, constraints and authority. This is *task-contract determinism* over a fixed vocabulary, not proof that arbitrary natural-language goals are fully unambiguous.

The parser requires the exact roles `kartṛ`, `pratigrahītṛ`, `viṣaya`, `kriyā`, `lakṣya`, `pariṇāma`, `maryādā`, `anumati`. Missing, duplicated, unknown or unsupported fields fail closed. Only `gaṇaya`, `parīkṣaya`, `saṃkṣip`, and `racaya` are recognised action labels; this module does not execute actions. Values `anirdiṣṭa` (unspecified) and `na` (explicitly none) are distinct. Targets/output cannot be unspecified.

## Protocol phases
- `ādeśa`: request; stable task ID and explicit request contract.
- `spaṣṭīkaraṇa`: assignee seeks clarification of one scoped field.
- `uttara`: original requester resolves that precise field.
- `anumodana`: original requester authorises a task marked `bāhya_anumati`.
- `pratigraha`: assignee acknowledges/accepts the task only after all clarifications and permissions.
- `nirākaraṇa`: assignee declines with stated reason.

## Security/semantics limitations
- This is a scripted **native SCL dialogue**, not a network transport between independent models. No operations run, no messages leave the process.
- Symbolic target names are not globally resolvable resource identifiers. A production deployment needs an authenticated object registry, effect typing, explicit budgets and deadlines, provenance, identity signatures, delegated authority, and actual execution receipts.
- Hash-linked transcripts establish reproducible integrity only; they do not authenticate speakers or prevent an attacker from rewriting a whole transcript.
- A `pratigraha` confirms acceptance of the stated task **not completion**, user satisfaction, or factual correctness.
- The grammar is Pāṇinian-inspired via kāraka-labelled roles, scoped condition inheritance (explicit contract), and exception/authorisation checks. It does not implement all of the Aṣṭādhyāyī.
- Python, Java, Rust, JSON Schema and protobuf can implement equivalent checks. Comparative advantage is a hypothesis requiring controlled baselines.

## Execution
`python tasks087_cli.py core080/examples/task_user_agent_087.scl`
`python tasks087_cli.py core080/examples/task_agent_agent_087.scl`

`--verify transcript.json` recomputes the conversation from the SCL source and compares the exact canonical result.
