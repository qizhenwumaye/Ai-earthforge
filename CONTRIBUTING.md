# Contributing

Earthforge is open to contributions from anyone — data sources, adapters, models, docs, and code. Three documents govern how:

- [`GOVERNANCE.md`](GOVERNANCE.md) — roles, decision making, RFC lifecycle.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — expected behavior.
- [`SECURITY.md`](SECURITY.md) — report vulnerabilities privately; do not open a public issue.

Licensing obligations for data are in [`docs/05-licensing.md`](docs/05-licensing.md). Read it before adding a source.

## Ways to contribute

1. **Data-source proposals** — a new dataset to compose (use the issue template).
2. **RFCs** — changes to ontology, architecture, or interfaces.
3. **Adapters** — ingestion code for a source, conforming to the schema.
4. **Models** — reduced physical models with stated validity domains.
5. **Docs and examples** — worked tiles, notebooks, validation.

## The RFC process

- Open an RFC issue using the template.
- Core changes (L0 ontology, L5 provenance, public interfaces) require an RFC, not just a PR.
- RFCs have a comment period of at least 7 days; maintainers decide by rough consensus and record the decision and rationale.
- Ontology changes require a version bump, a migration note, and an updated schema.
- The full lifecycle is in [`GOVERNANCE.md`](GOVERNANCE.md).

## Non-negotiables

- Every persisted fact has provenance. No exceptions.
- Every numeric value has a unit.
- Missing data is `unknown`, never a default.
- Source licenses are recorded and respected. No ingestion of a source whose license forbids the intended use.
- History is append-only; corrections are new facts.

## Code

- Language: Python for ingestion, models, and API (pragmatic default; revisit if a component needs otherwise).
- Formatting and linting enforced in CI.
- Tests required for schema validation, unit handling, and determinism.
- Commit sign-off (DCO): `git commit -s`.

## Data licensing

Every ingested dataset's license must be recorded in provenance. Share-alike sources (ODbL, CC BY-SA) and non-commercial sources have real obligations — read [`docs/05-licensing.md`](docs/05-licensing.md) before adding a source.

## Naming and identity

- Prefer external stable IDs; mint internal UUIDs only when no external ID exists.
- Use `same_as` to link duplicate representations, never to overwrite.
