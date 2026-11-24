# 00 — Scope

## What problem this solves

"Digitize all matter and knowledge into an Earth environment" is not one problem. It is a hundred thousand digitization efforts that already exist in fragments. The missing piece is a **composition layer**: one ontology, one provenance model, one addressing scheme, one simulation interface, so that a terrain tile, a building footprint, a species observation, and a climate reanalysis can be queried and stepped as one world.

Earthforge builds that layer and proves it on a small patch first.

## Two orthogonal products

### A. Earth Knowledge Graph (`ekg`)
A bitemporal, provenance-tracked graph of entities and facts, spatially and temporally indexed.

- Question it answers: *"What is at this place, at this time, according to which source, with what confidence?"*
- Does not simulate. Does not predict. Stores and serves what is known or asserted.

### B. Earth Simulator (`sim`)
A steppable world model that advances physical and agent state forward in time.

- Question it answers: *"Given this state and these forces, what is the next state?"*
- Does not claim truth. Claims a **model** with stated assumptions and error.

They share L0 (ontology) and L5 (provenance). They must stay separable: a knowledge graph with no simulator is useful; a simulator with no grounding is a toy.

## What "data-ize" decomposes into

| Phrase | Actual technical content |
|---|---|
| "data-ize matter" | geometry (where) + material/attributes (what) + physical parameters (how it behaves) |
| "data-ize knowledge" | entities + relations + text + grounding of symbols to geometry/time |

The join point is the **entity**: a thing with a spatial extent, a temporal extent, attributes, relations, and provenance. Both products operate on entities.

## Level of detail (LOD)

Fidelity is a function of the question, not a global constant.

| LOD | Spatial | Typical content | Cost |
|---|---|---|---|
| L0 | ~10 km | global terrain, land cover, climate means | cheap |
| L1 | ~1 km | hydrology, roads, settlements | medium |
| L2 | ~100 m | buildings, parcels, vegetation | expensive |
| L3 | ~1 m | facades, materials, individual trees | very expensive |
| L4 | sub-cm | surface texture, microstructure | research-only |

A query declares the LOD it needs; the system serves the cheapest layer that satisfies it. **No fact is stored without a declared LOD.**

## Reference use cases (drive fidelity)

1. **Agent sandbox** — a physically plausible world for embodied agents to act in.
2. **What-if analysis** — flood, land-use change, infrastructure placement at L1–L2.
3. **Knowledge grounding** — attach text claims to places and times for retrieval and verification.
4. **Education / visualization** — explorable Earth at L0–L2.

If a proposed feature serves none of these, it is out of scope for now.

## Explicit non-goals

- Photorealistic rendering (we produce *state*, not *pixels*; a renderer is a downstream consumer).
- Atomic/subatomic or full continuum physics (we use reduced models with stated validity domains).
- Real-time global high-resolution weather (we integrate reanalysis and reduced models).
- "All knowledge" in the philosophical sense (we scope knowledge to grounded, sourced assertions).
- A single monolithic database of everything (we federate; see architecture).

## Success criteria

- **M1:** one 1 km² tile is queryable end-to-end across ≥4 data layers with full provenance.
- **M2:** that tile can be stepped forward by a reduced physical model, reproducibly.
- **M3:** every fact in the tile is bitemporal and carries a calibrated uncertainty.
- **M4:** an external agent can query and act in the tile through a stable API.
- **M5:** the same pipeline runs on ≥100 tiles with streaming and LOD selection.
