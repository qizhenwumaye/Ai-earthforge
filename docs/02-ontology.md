# 02 — Ontology (v0.1)

The ontology is deliberately small. Everything is built from six primitives.

## Primitives

| Primitive | Meaning |
|---|---|
| `Entity` | a thing that exists in space and time (a mountain, a building, a river, a species occurrence) |
| `Property` | an attribute of an entity with a value, unit, and uncertainty |
| `Relation` | a typed, directed link between entities |
| `SpatialExtent` | geometry + CRS + LOD |
| `TemporalExtent` | valid-time interval (+ optional transaction-time) |
| `Provenance` | source, method, confidence, timestamps |

## The atomic fact

Everything reduces to a **quad**:

```
(entity, property, value, provenance)
```

with `value` carrying `unit` and `uncertainty`, and `provenance` carrying `source`, `method`, `confidence`, `valid_time`, `transaction_time`, `lod`.

A relation is the same shape with a relation predicate and an entity-valued target.

## Time is bitemporal

Two independent time axes:

- **valid time** — when the fact was true in the world.
- **transaction time** — when the system recorded it.

This lets the graph answer "what did we believe in 2020 about 1990?" and "what do we now believe about 1990?" without conflict.

## Uncertainty is mandatory

`uncertainty` is one of:
- `interval {low, high}` — bounded error
- `distribution {kind, params}` — e.g., normal, uniform
- `categorical {probabilities}` — for discrete values
- `unknown` — explicitly not quantified (still recorded)

`confidence` is a calibrated probability that the assertion is correct, where calibration is possible; otherwise `null` with a reason.

## LOD is part of every extent

`SpatialExtent.lod` declares the resolution at which the geometry is meaningful. A building footprint at L3 is a different object from the same building at L1 (a point). The resolver decides which to serve.

## Identity

- Each entity has a stable `id` (UUID) and zero or more **external ids** (OSM way id, Wikidata Q-id, GBIF taxon key, etc.).
- External ids are the bridge to source datasets.
- The same real-world thing may be represented by several entities at different LODs or from different sources; `same_as` relations link them.

## Example

```json
{
  "id": "7f3c1e2a-0000-4000-8000-000000000000",
  "type": "water.body",
  "name": "Lake X",
  "external_ids": { "osm": "way/123456", "wikidata": "Q789" },
  "spatial": {
    "geometry": { "type": "Polygon", "coordinates": [[[0.0, 0.0], [0.01, 0.0], [0.01, 0.01], [0.0, 0.0]]] },
    "crs": "EPSG:4326",
    "lod": "L1"
  },
  "temporal": { "valid_from": "1990-01-01", "valid_to": null },
  "properties": [
    {
      "key": "surface_area",
      "value": 12.4,
      "unit": "km2",
      "uncertainty": { "kind": "interval", "low": 12.1, "high": 12.7 },
      "provenance": {
        "source": "OpenStreetMap",
        "method": "geometry area",
        "confidence": 0.8,
        "valid_time": "2024-03-01",
        "transaction_time": "2026-11-24T00:00:00Z",
        "lod": "L1"
      }
    }
  ],
  "relations": [
    { "predicate": "within", "target": "admin/region/0000", "provenance": { "source": "Natural Earth", "method": "point-in-polygon", "valid_time": "2020-01-01", "transaction_time": "2026-11-24T00:00:00Z", "lod": "L1" } }
  ]
}
```

## Versioning

The ontology is versioned (`v0.1`). Breaking changes require an RFC and a migration note. Additive changes are minor versions.
