# Security policy

## Reporting a vulnerability

Do **not** open a public issue for a security problem. Email `security@earthforge.dev` with:

- what you found and where,
- a reproduction or proof of concept,
- the impact you believe it has.

We aim to acknowledge within 72 hours and to publish a coordinated disclosure after a fix. Credit is given unless you ask otherwise.

## In scope

- Code execution in ingestion adapters (untrusted datasets are a real attack surface).
- Path traversal or injection in the Query / Step APIs.
- Denial of service via crafted tiles, geometries, or queries.
- Sandbox escape from the Agent API.
- Supply-chain issues in the ingestion toolchain.

## Out of scope

- Data inaccuracies or disagreements — use the data-source issue template.
- License disputes — see [`docs/05-licensing.md`](docs/05-licensing.md).
- Vulnerabilities in third-party datasets or their servers.
