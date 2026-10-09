# Part A Report — Access Index Map

## 1. Audience and Decision Question

**Audience:** Students and planning staff reviewing fictional service-zone data.

**Decision question:** Which service zones have higher or lower access index values, and how should the number of locations reviewed affect our interpretation?

## 2. Data and Access Index

The dataset contains six fictional service zones for September 2026.

The access index is a fictional relative index on a 0–100 scale. A higher value means a higher index score.

It does not represent the percentage of residents who have access to services.

The data are synthetic and cannot be used for real resource-allocation decisions.

## 3. CRS and Transformation

- Original CRS: EPSG:4326 — WGS 84
- Working CRS: EPSG:32612 — WGS 84 / UTM zone 12N

I exported the original GeoJSON as a projected GeoPackage for the map layout and scale bar.

The original dataset was not modified.

## 4. Classification Method

- Field: `access_index`
- Method: Equal Interval
- Number of classes: 3
- Colour ramp: Light blue to dark blue

**Class breaks:**

- 34–52
- 52–70
- 70–88

Darker colours represent higher access index values.

## 5. Results

| Zone | Access Index | Locations Reviewed |
|---|---:|---:|
| Northwest | 34 | 4 |
| North Central | 48 | 9 |
| Northeast | 53 | 6 |
| Southwest | 67 | 8 |
| South Central | 71 | 5 |
| Southeast | 88 | 10 |

**Highest index:** Southeast (88), with 10 locations reviewed.

**Lowest index:** Northwest (34), with 4 locations reviewed.

The number of locations reviewed differs between zones. For example, Northwest has only 4 locations reviewed, while Southeast has 10.

This means the scores should be interpreted carefully. The map does not show equal amounts of supporting information for every zone.

## 6. Limitation

The dataset is fictional and contains only six zones. The number of locations reviewed also differs between zones.

The index is not a measured resident-access rate, so the map cannot support real planning decisions.

## 7. Next Validation Step

Before making a real decision, I would collect actual service-location data and check how the index was calculated.

I would also review more locations in each zone to better understand the differences between areas.