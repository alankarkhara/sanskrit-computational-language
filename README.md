# Sanskrit Computational Language (SCL)

**Status:** v1.0 release candidate (research software); **not** certified as v1.0 stable.  
**License:** Apache License 2.0 (Apache-2.0). See [LICENSE](LICENSE) and [docs/LICENSING.md](docs/LICENSING.md). Third-party provenance and patent/ownership clearance should be checked before public distribution.

SCL is an experimental Sanskrit-inspired computational language and bounded agent-communication research programme. Its implemented subsystems include a native grammatical layer, constrained execution and certificates, clarification workflows and an experimental canonical JSON frame protocol. These are research mechanisms, **not** general AI-agent authorization or comprehensive Pāṇinian grammar.

## What works and what has not been demonstrated

- The engineering-audit package reported 556 passing unit tests, a passing inherited-integrity release gate, and 4,000 fixed-seed malformed wire inputs without uncaught failures. See `V1_RELEASE_READINESS.md` for scope and reproduction.
- A deterministic two-process test is distinct from testing **two actual inference-running local language models**; the latter remains unverified.
- No complete formal proof, independent linguistic certification, external penetration test, durable authenticated distributed permissions system, or production safety guarantee is claimed.
- Experimental wire frames do not confer authorization; model output is untrusted.

## Reproduce the available checks

Use Python 3.11+ from the repository root:

```bash
python -m unittest discover -s tests -q
python -W error::ResourceWarning -m unittest discover -s tests -q
python publication/release_gate.py
```

The optional local-model adapter is documented in `V1_RELEASE_READINESS.md`; it requires users to start and configure two model-serving endpoints and **does not execute tasks**.

## Repository guidance

Read [docs/PROTOCOL_V1_RC.md](docs/PROTOCOL_V1_RC.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md), [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md) before integrating SCL. The historical README is archived at [docs/archive/README_pre_v1_release.md](docs/archive/README_pre_v1_release.md); the release documentation takes precedence for current claims.

## Academic attribution

See [CITATION.cff](CITATION.cff) and [docs/CITATION_GUIDE.md](docs/CITATION_GUIDE.md). Citation metadata is not evidence of licensing permission or independently peer-reviewed acceptance.

## Notice

Do not deploy for untrusted production execution, financial transfers, medical decisions or critical infrastructure. No implied warranty or security certification.
