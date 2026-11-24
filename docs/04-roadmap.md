# 04 — Roadmap

Each milestone is a working, demonstrable slice. No milestone is "infrastructure with nothing to show."

## M0 — Foundation (current)
- [x] Scope, architecture, ontology v0.1, data-source inventory.
- [x] Core schema as machine-readable JSON Schema.
- [x] One worked example entity, validated in CI.
- [x] CI: schema validation, contract tests, DCO sign-off.
- **Acceptance:** schema validates the example; docs are self-consistent.

## M1 — The hello-world tile
Pick one 1 km² patch with good data coverage.
- Ingest ≥4 layers: elevation, land cover, roads/buildings, hydrography.
- Normalize into entities with full provenance and LOD.
- Stand up the Query API: `query(bbox, time, lod, types)`.
- **Acceptance:** a single query returns a coherent, provenance-complete description of the tile; every fact traces to a source snapshot.

## M2 — It moves
- Implement one reduced physical model on the tile (start with surface hydrology or a simple energy balance).
- Deterministic, seeded stepping via the Step API.
- **Acceptance:** same seed → identical trajectory; state snapshots round-trip exactly.

## M3 — It's honest
- Make every fact bitemporal.
- Add calibrated uncertainty to every property (or explicit `unknown`).
- **Acceptance:** the graph answers "what did we believe at transaction-time T about valid-time V?" correctly for the tile.

## M4 — Agents can live in it
- Agent API: observe/act, sandboxed, no direct writes.
- Reference agent runs in the tile.
- **Acceptance:** an external process can perceive and act through the API alone; simulation stays deterministic under a recorded action log.

## M5 — It scales
- Tiling + LOD resolver across ≥100 tiles; streaming reads.
- Federation: reference remote snapshots instead of copying.
- **Acceptance:** a multi-tile query returns consistent LOD-selected results within a latency budget.

## Beyond
- More reduced models (climate, vegetation, erosion).
- Richer knowledge grounding.
- Reproducible benchmark suites for agent research.
