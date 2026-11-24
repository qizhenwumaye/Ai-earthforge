# Earthforge

> An open research project to build a single, queryable, simulatable, provenance-tracked model of Earth by composing existing data — not by re-collecting it.

**Status: pre-alpha (M0).** This repo currently contains the ontology, scope, architecture, and roadmap. No ingestion pipeline yet.

## The thesis

Nobody can "data-ize reality" in one project. Earth's data already exists — in thousands of disconnected datasets, formats, coordinate systems, licenses, and levels of accuracy. The unsolved problem is **integration**: a common spine that lets those datasets compose into one coherent, queryable, steppable world.

Earthforge is that spine, plus a thin reference implementation that proves it works end-to-end on a small patch of the planet.

We are explicitly **not** building another map, another climate model, or another knowledge graph. We are building the layer that makes all of them addressable as one world.

## Two goals, one ontology

| Goal | Module | Answers |
|---|---|---|
| **Earth Knowledge Graph** | `ekg` | "What is here, and what is true about it?" |
| **Earth Simulator** | `sim` | "If I change this, what happens next?" |

They share one ontology (L0) and one provenance model (L5). They are otherwise independent — you can use either alone.

## Architecture

```
L5  Provenance & Uncertainty   (cross-cutting: every fact carries source, method, confidence, time)
L4  Interface                  Query API · Step API · Agent API
L3  Knowledge                  entities · relations · text grounding · concepts
L2  Physical / Dynamic         climate · hydrology · physics stepping
L1  Static World               terrain · built environment · land cover · hydrography
L0  Ontology & Schema          entity · property · relation · time · units · uncertainty
```

See [`docs/01-architecture.md`](docs/01-architecture.md).

## Repo map

```
docs/              design documents (start here)
ontology/          the core schema (v0.1)
examples/          worked entities, validated in CI
scripts/           standalone validation
tests/             schema contract tests
data/              local only, never committed
.github/workflows/ CI: validate · test · DCO
```

Ingestion, storage, API, and simulator code land in M1+ (see [`docs/04-roadmap.md`](docs/04-roadmap.md)).

## Principles

1. **Compose, don't recollect.** Prefer an existing authoritative dataset over new collection.
2. **Level-of-detail is a contract, not an afterthought.** Every fact declares the resolution it is valid at.
3. **Provenance is mandatory.** A fact with no source is not a fact.
4. **Uncertainty is data.** Store error bars, not just point estimates.
5. **Use-case driven.** Fidelity is set by the question being asked, not by an abstract ideal.
6. **Bitemporal by default.** Distinguish *when something was true* from *when we learned it*.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Start with an RFC issue. The ontology is versioned and changes through a review process.

## Community

- [`GOVERNANCE.md`](GOVERNANCE.md) — roles, RFC process, decision making
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to contribute
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) · [`SECURITY.md`](SECURITY.md)

## License

- **Code:** [Apache-2.0](LICENSE).
- **Documentation:** CC BY 4.0.
- **Data:** per-source. The aggregated store may be ODbL/share-alike because of OSM-derived content. See [`docs/05-licensing.md`](docs/05-licensing.md) and [`docs/03-data-sources.md`](docs/03-data-sources.md).
