# SCL v0.8.5 — Native agent communication

- Automated suite: **425/425 passed**.
- Inherited non-cache files: **222**, missing **0**, modified **0**.
- Native SCL source example: `core080/examples/native_agents_085.scl`.
- CLI: `native085_cli.py`.
- Accepted operations: propose, challenge, accept and reject of bounded typed arithmetic claims.
- Source-bound independent replay of the transcript via native source recompilation.
- Scope limits: messages are compiled in a single scripted conversation. The actual agents are not independently networked processes; there is no cryptographic agent authentication, no arbitrary typed AST transfer, no Lean soundness proof, and no machine learning.
