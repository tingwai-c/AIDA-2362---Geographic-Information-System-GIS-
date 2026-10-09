# Data documentation

- **Dataset:** fictional access-index values for six illustrative service zones.
- **Geometry:** polygons; coordinates supplied in GeoJSON CRS84 / EPSG:4326.
- **Fields:** `zone_id` and `zone_name` identify each polygon; `access_index` is a fictional relative index on a 0–100 teaching scale; `locations_reviewed` is the denominator for that zone; `period` is the fictional reporting period.
- **Provenance:** deterministic synthetic course data; no real residents, addresses, facilities, or service records.
- **Use limit:** the index is not a measured resident-access rate and is not a basis for actual resource allocation.
- **Projection note:** if making a measured scale bar or area calculation, create and document an appropriate projected working copy. Do not overwrite the supplied EPSG:4326 source.
