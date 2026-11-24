# 05 — Licensing policy

Earthforge mixes three kinds of material, and they must not be licensed as one:

| Kind | License | Why |
|---|---|---|
| **Code** | Apache-2.0 | permissive, explicit patent grant, standard for infrastructure |
| **Documentation** | CC BY 4.0 | permissive, attribution only |
| **Data** | per-source | it is not ours to relicense |

## Code: Apache-2.0

Permissive, includes a patent grant, compatible with DCO sign-off. See [`../LICENSE`](../LICENSE).

## Documentation: CC BY 4.0

Prose, diagrams, and specs may be reused with attribution.

## Data: the hard part

### Share-alike is contagious

OpenStreetMap is **ODbL 1.0**. ODbL distinguishes two things:

- **Derivative Database** — a database made by combining or adapting OSM data with other data. If you publicly use it, it must be offered under ODbL.
- **Produced Work** — a result generated from the database (a rendered map, a computed answer) that is not itself a database. Only attribution is required.

A queryable knowledge graph that stores OSM-derived entities alongside other sources is almost certainly a **Derivative Database**, not a Produced Work. That means the aggregated *data* layer is ODbL, not Apache-2.0. This is a legal requirement, not a preference.

### Consequences

- The **code** stays Apache-2.0.
- The **aggregated data store** must be released under ODbL (or a compatible share-alike) if it contains OSM or other ODbL-derived content.
- **Per-source provenance is what lets downstream users comply.** This is why L5 is mandatory and per-fact, not optional and document-level.
- **Non-commercial sources** (e.g., GADM) must never enter the permissive core. Isolate them in an optional, clearly labeled `nc` pack that users opt into explicitly.

### Practical structure

1. Keep source datasets **referenced by external ID** wherever possible; do not bake them into the core.
2. Every entity or tile derived from a share-alike source carries a machine-readable `license` field in its provenance.
3. Ship a `licenses/` manifest mapping every source to its license and obligations.
4. Downstream users receive: code (Apache-2.0) + data (ODbL/share-alike per source) + the manifest telling them what to attribute and what to share.

### Never

- Re-license someone else's data as Apache-2.0.
- Mix non-commercial data into a permissively licensed dataset.
- Ship data without its license recorded in provenance.

## Open source, cleanly

"Fully open" means: anyone can read, use, modify, and redistribute the code and docs, and anyone can reuse the data under its source's terms with attribution. It does **not** mean pretending all data is Apache-2.0. The manifest is what makes open source legally coherent for a project built from other people's datasets.
