# Governance

Earthforge is open to contribution from anyone. The core — ontology, provenance model, and public interfaces — changes through a versioned, reviewable process so the project does not fragment into incompatible forks.

## Principles

- **Open by default.** Design discussion happens in public issues and pull requests.
- **Rough consensus, recorded decisions.** Every core decision has a linked rationale.
- **The data model is load-bearing.** Core changes require an RFC, not just a PR.
- **No single point of failure.** At least two maintainers must be able to merge.
- **Everything is reversible.** Any decision can be revisited by a later RFC.

## Roles

| Role | Who | Rights |
|---|---|---|
| **User** | anyone | use the project, open issues |
| **Contributor** | anyone with a merged PR | submit PRs, comment on RFCs |
| **Reviewer** | regular contributors granted review rights | approve PRs, block on quality |
| **Maintainer** | trusted long-term contributors | merge rights, decide RFCs, release |

The ladder is earned by sustained, quality contribution. Removal is by a two-thirds vote of maintainers, for inactivity (6 months) or Code of Conduct violations.

## Decision making

### Routine changes
Lazy consensus. A PR merges after review, green CI, and no blocking objection within a stated window (default 5 days for non-core code, 7 days for docs).

### Core changes
Anything touching L0 (ontology), L5 (provenance/uncertainty), or a public API (Query / Step / Agent) requires an **RFC**:

1. Open an RFC issue using the template.
2. Comment period of at least 7 days.
3. Maintainers decide by rough consensus; if split, a simple majority; a tie keeps the status quo.
4. The decision and rationale are recorded in the RFC thread and `CHANGELOG.md`.

### Core invariants (high bar to change)
These cannot be changed by a normal RFC. Changing any requires an RFC with an explicit migration plan and a two-thirds supermajority of maintainers.

1. Every persisted fact carries provenance.
2. Every numeric value carries a unit.
3. Missing data is `unknown`, never a default.
4. History is append-only; corrections are new facts.
5. Bitemporality is preserved.

## Becoming a maintainer

- Sustained contributions over at least three months, **or** a major accepted RFC/implementation.
- Nominated by a maintainer and approved by two-thirds of maintainers.
- Recorded publicly in `MAINTAINERS.md`.

## Conflict resolution

Escalate to maintainers. If unresolved, an independent mediator agreed by both sides. Code of Conduct issues follow [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
