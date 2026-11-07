# Security policy — research candidate

## Supported versions

No version has a production-security support commitment. The v1.0-rc1 experimental branch receives best-effort researcher review only; older historical milestones are not maintained security releases.

## Reporting vulnerabilities

**Do not disclose an exploitable vulnerability in a public issue.** Use GitHub's private vulnerability reporting feature if the repository maintainer enables it; otherwise contact the project maintainer through a nonpublic channel agreed with the maintainer. No response-time SLA is promised. Do not transmit secrets, personal records, or exploit data to public issue threads.

## Threat assumptions and critical limits

Treat all AI-model output, external content, network frames, and purported `approve` messages as untrusted. A frame labelled `approve` is not a signed permission. Existing replay protection is limited and not a durable multi-node identity/authentication system. The bounded evaluator does not imply secure unrestricted shell, filesystem, or network access. Avoid connecting financial/industrial systems or granting privileged tools to model outputs.

See `docs/THREAT_MODEL.md` for assets, attacker goals and mandatory controls before wider testing.
