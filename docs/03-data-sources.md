# 03 — Data sources

Priority: compose what exists. Verify the license of each snapshot before ingestion; licenses change.

## L1 — Static world

| Layer | Source | Format | License |
|---|---|---|---|
| Elevation | Copernicus DEM GLO-30 | raster (COG) | Copernicus |
| Elevation (coarse) | SRTM 1/3 arc-sec | raster | public domain |
| Land cover | ESA WorldCover 10 m | raster | CC BY 4.0 |
| Land cover (built) | GHSL built-up | raster | CC BY 4.0 |
| Buildings | OSM / Microsoft Global ML Building Footprints | vector | ODbL |
| Roads | OSM | vector | ODbL |
| Hydrography | HydroSHEDS / OSM water | vector+raster | free / ODbL |
| Coastline | Natural Earth / OSM | vector | public domain / ODbL |
| Admin boundaries | Natural Earth / GADM | vector | public domain / NC |

## L2 — Physical / dynamic

| Layer | Source | Notes |
|---|---|---|
| Climate reanalysis | ERA5 (Copernicus C3S) | hourly, ~31 km, 1940–present |
| Climate normals | WorldClim | ~1 km monthly means |
| Hydrology model | HydroSHEDS + reduced routing | derived |
| Soil | SoilGrids | 250 m |

## L3 — Knowledge

| Layer | Source | License |
|---|---|---|
| General entities | Wikidata | CC0 |
| Scholarly graph | OpenAlex | CC0 |
| Common-sense concepts | ConceptNet | CC BY-SA 4.0 |
| Biodiversity occurrences | GBIF | per-record |
| Place names | GeoNames | CC BY 4.0 |

## Ingestion rules

1. Record source URL, snapshot date, license, and checksum in provenance.
2. Never overwrite a fact from one source with another; link with `same_as` and let the resolver choose by confidence/LOD.
3. Prefer stable external IDs over names.
4. Keep raw payloads content-addressed and immutable.
