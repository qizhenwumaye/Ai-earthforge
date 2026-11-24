# 01 — Architecture

## Layer model

Each layer is a separate package with a narrow interface. Layers may be used independently; the contract is the interface, not the implementation.

### L0 — Ontology & Schema
The spine. Defines:
- core primitives: `Entity`, `Property`, `Relation`, `SpatialExtent`, `TemporalExtent`, `Provenance`
- units and coordinate reference systems
- the LOD declaration
- the uncertainty model

See [`02-ontology.md`](02-ontology.md) and [`../ontology/core.schema.json`](../ontology/core.schema.json).

### L1 — Static World
Slowly-changing physical and built structure.
- terrain / elevation
- land cover
- hydrography (rivers, lakes, basins)
- built environment (buildings, roads, parcels)
- administrative boundaries

Interface: `get(entity_id) -> Entity`, `query(bbox, time, lod, types) -> Entity[]`, `tile(x, y, z, lod) -> TileBundle`.

### L2 — Physical / Dynamic
State that evolves: climate, hydrology, and the physics an agent experiences.
- reduced models with declared validity domains
- deterministic, seeded stepping
- state snapshots and deltas

Interface: `step(state, dt, forces) -> state'`, `snapshot(t) -> State`, `restore(snapshot)`.

### L3 — Knowledge
Grounding of symbols to the world.
- entity/relation store (the `ekg` product)
- text→entity grounding
- concept/ontology alignment (e.g., to Wikidata/OSM tags)

Interface: `entities(place, time)`, `facts(entity)`, `resolve(text) -> EntityRef[]`.

### L4 — Interface
The stable surface everything else codes against.
- **Query API** — read the EKG and current sim state.
- **Step API** — advance the simulator.
- **Agent API** — a restricted, sandboxed view for embodied agents: observe, act, no direct write.

### L5 — Provenance & Uncertainty (cross-cutting)
Not a stage in the pipeline — a constraint on every stage.
Every persisted fact carries:
`source`, `method`, `confidence`, `valid_time`, `transaction_time`, `lod`, `units`.

## Data flow

```
external datasets
      │  (ingest + harmonize)
      ▼
L0 normalize ──► L1 static ──► L2 dynamic ──► L4 API
                    │              │
                    └──► L3 knowledge ◄──┘
      ▲
L5 stamps every record at every hop
```

## Tiling, LOD, and federation

- **Spatial addressing:** hierarchical tiles (e.g., a quadtree over an equal-area projection). Every entity sits in one or more tiles.
- **LOD selection:** queries request a target resolution; the resolver returns the coarsest layer that meets it.
- **Federation over centralization:** source datasets are referenced by stable IDs and cached, not blindly copied. A central store holds *indexes, normalized entities, and provenance*, not necessarily all raw payloads.
- **Storage split:**
  - spatial/relational index: PostGIS or DuckDB+Spatial
  - entity/relation graph: a property graph or relational triple store
  - time series / raster: columnar + tiled raster formats (COG/Zarr)
  - blobs: object storage, content-addressed

## Module boundaries (planned packages)

| Package | Layer | Responsibility |
|---|---|---|
| `core` | L0/L5 | schema, entity model, provenance, validation |
| `ingest` | L1/L3 | dataset adapters, harmonization |
| `world` | L1 | static world store + tiling |
| `sim` | L2 | reduced models, stepping |
| `ekg` | L3 | knowledge graph store |
| `api` | L4 | query/step/agent APIs |
| `tile` | cross | LOD/tile addressing |

## Design constraints

- **Determinism:** simulation is seeded and reproducible; provenance records the seed.
- **Immutability of history:** facts are appended, not overwritten; corrections are new facts with new transaction times.
- **No silent defaults:** missing data is `unknown`, never zero/false.
- **Unit safety:** every numeric value carries a unit; conversion at boundaries only.
