# SCL 0.8.8 — Grounded executable task contracts (experimental)

## Supported SCL source

`core080/examples/grounded_agents_088.scl` defines two participants, typed `Int64` objects, one explicit *authority grant* (`adhikāra`), and one executable `yoga` task (`ādeśa`). Supported elements:

- `(vastu (id ...) (prakāra Int64) (mūlya ...))`: immutable integer object, canonical SHA-256 identity over typed content and identifier.
- `(adhikāra (kartṛ ...) (kriyā yoga) (prabhāva śuddha))`: closed-world role grant.
- `(ādeśa ...)`: typed task referencing both existing objects; action `yoga`, expected type `Int64`, effect `śuddha` (pure), permission `antarika` (internal).
- Result observations always include `status`, `steps` and `value`; errors `out_of_fuel` and `overflow` are explicit. Fuel accounting uses one semantic operation per addition (not physical CPU steps).
- Execution certificate binds contract digest, individual object digests, executor/requester, task, supported effect and exact observations; the requester recomputes the result without trusting certificate claims.

## Running

```
python grounded088_cli.py core080/examples/grounded_agents_088.scl
python -m unittest discover -s tests -q
```

Two real independent operating-system processes can communicate through `agent088_peer.py`: start `server --port 38088` and run `client --port 38088 --source core080/examples/grounded_agents_088.scl`. The client verifies the returned certificate. A process-level integration test runs this automatically on an ephemeral local port.

## Scope and limitations

The protocol is **not a proof of complete unambiguity for general AI communication**. It is an executable, deterministic, sharply restricted typed arithmetic fragment. The authority model operates over logical participant labels and predeclared grants, **not cryptographically authenticated identities**. Both processes receive the request source; no signed external authorization, protected trust anchor, TLS, agent discovery or transport replay protection is supplied. TCP loopback is a demonstration transport, not a production security boundary. No remote tools, files or side effects are executed. A certificate is independently replayable evidence that this arithmetic computation and these symbolic authority checks were performed, **not external-world evidence or a formal proof-kernel theorem**. SCL natural-language-to-contract conversion is outside the implemented guarantee, and a sender can lie in the source unless a trusted authority binds the grant to a real identity.

The earlier `tasks087` negotiation API remains available and is preserved byte-for-byte. This module adds a separate execution contract and does not yet translate all v0.8.7 task-vocabulary operations or negotiation states into executable plans. General typed documents, reference resolvers, effects and runtime provenance remain future work.
