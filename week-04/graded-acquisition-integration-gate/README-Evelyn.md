## Part 3 — Create your working notes
1. Who is the decision-maker?
The decision-maker is the facilities-maintenance team.

2. What action might they take?
If the provided facility and service area data pass the required checks, the decision-maker may use this data for a limited data integration and planning review.

3. What area or spatial unit are you checking?
The spatial units currently being analyzed are Facilities and Service zones.

4. What geographic area do the supplied data cover?
From the layer information, the Facilities are found to be located approximately within the longitude range of -113.806 to -113.773 and the latitude range of 52.240 to 52.254. The Service zones are located approximately within the longitude range of -113.815 to -113.764 and the latitude range of 52.235 to 52.262.

5. What scale is appropriate for interpreting the results?
The result is appropriate for interpreting the supplied facility and service-zone study area only.

6. What date or time limitation applies?
The facility_points dataset has a retrieval date of August 13, 2026, while the legacy_access_paths source has no documented retrieval date. 

7. Is your decision ready, conditional, quarantine, or reject?
My decision is conditional because the facility and service-zone data passed the required checks, but the legacy_access_paths source has incomplete metadata and missing geometry and should remain quarantined.

8. Why is your decision limited to this fictional learning example?
As the data is fictional—generated for the course—rather than actual operational data, it does not represent real residents or service demands.

## Part 4 — Project and layer CRS
Project CRS: No CRS
Facilities layer CRS: EPSG:4326
Service zones layer CRS: EPSG:4326

## Part 6 — Facility layer check
- Feature count: 5
- Stable ID field: feature_id
- Duplicate IDs: none
- Blank IDs: none
- Geometry type: Point
- Layer CRS: EPSG:4326

## Part 7 — Service-zone validity check
- Valid features: 3
- Invalid features: 0
- Errors: 0
- Invalid feature IDs: none

## Part 8 — CRS, units, and area of use
at metadata.json
storage: EPSG:4326
analysis: EPSG:32612 where metric distance or area is required
warning: Verify area of use and units before analysis.
1. Record the storage CRS.
EPSG:4326

2. State whether it uses degrees or metres.
degrees

3. State the analysis CRS you selected, if a projected copy is needed.
EPSG:32612，if metric distance or area is required

4. State the units of the analysis CRS.
metres

5. Explain why the CRS area of use matters.
Because a projected CRS is designed for a specific geographic area. Using it outside that area may reduce the accuracy of distance or area measurements.

6. & 7. No projected layer was created

## Part 9 — Produce one reproducible QGIS result
I created a facility-to-zone spatial relationship using Join attributes by location. The result was saved as `outputs/facilities_with_zones.gpkg`.

## Part 10 — Changed-variable comparison
I changed the spatial predicate from `within` to `intersects` while keeping the other settings are same.
Both settings produced 5 matched facility features, and no facility IDs were affected. Therefore, this change did not affect my integration decision.