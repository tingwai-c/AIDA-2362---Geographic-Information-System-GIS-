# AIDA 2362 — Week 5 Graded Lab 2: Spatial Joins and Overlays

**Individual | One submission | 5% total (Part A 3% + Part B 2%)**

## Purpose

Use QGIS to combine fictional community-service request points with service-area and planning-district polygons. Check how the spatial predicate affects boundary cases, perform a polygon overlay, and make a bounded evidence-based recommendation. The data are synthetic and are not suitable for real decisions.

## Start here

1. Copy this entire `graded-lab-spatial-joins-overlays` folder from the instructor's **AIDA_2362_Graded_Labs** repository into `week-05/` in your assigned private AIDA 2362 repository. Keep this folder name.
2. Open your **private repository** in VS Code. In its terminal, run:

   ```powershell
   py week-05/graded-lab-spatial-joins-overlays/starter_check.py
   ```

3. The check reports layer names, feature counts, geometry types, and CRS. It does not perform the lab analysis.
4. Open QGIS. Add the GeoJSON files from this lab's `data/` folder using **Layer → Add Layer → Add Vector Layer**. Do not edit the supplied data.
5. Confirm that every input layer uses EPSG:4326. If you create an output layer, keep its CRS documented.

## Part A — Guided spatial analysis (3%)

Create the following evidence in this lab folder. You may use QGIS tools and its attribute tables; save your project as `outputs/lab2_project.qgz`.

### A1. Inspect and validate the inputs

1. Record the feature count, geometry type, CRS, and important fields for all three input layers.
2. Check for empty geometries, missing IDs, duplicate IDs, and features outside the supplied area.
3. State that the data are fictional and identify their supplied source and limits.

### A2. Join request points to service areas

1. Open **Processing Toolbox** and search for **Join attributes by location**.
2. Set `service_requests` as the input layer and `service_areas` as the join layer.
3. Choose the **intersects** predicate and the one-to-many output option (one output row for every match). Keep unmatched input records if the tool offers that option. Save the output as `outputs/requests_intersects.gpkg`.
4. Repeat with **within**, using the same join/output settings; save as `outputs/requests_within.gpkg`.
5. Compare the number of joined records, unmatched requests, and requests with multiple matches.
6. Identify request `R-05`, which is deliberately located on a shared boundary. Explain how the predicate changes its assignment.
7. Create `outputs/comparison.csv` with these columns, filling in the counts from your two output tables:

   ```text
   predicate,input_request_count,matched_output_rows,unmatched_request_count,multiple_match_request_count
   ```

### A3. Overlay the polygon layers

1. Search the Processing Toolbox for **Intersection**.
2. Use `service_areas` and `planning_districts` as the two polygon inputs.
3. Save the result as `outputs/area_intersections.gpkg`.
4. Record how many output polygons are created and which input IDs each output retains.
5. Explain in plain language how this overlay differs from joining a request point to a polygon.

### A4. Report the evidence

Create `PART-A-REPORT.md` with the question, input checks, CRS, both join predicates and counts, the boundary-case result, overlay result, one limitation, and one practical next validation step. Include a small table of the `intersects` versus `within` results.

## Part B — Independent extension (2%)

Choose one meaningful extension, such as comparing a third predicate, testing a documented boundary-assignment rule, or changing one overlay assumption. Keep Part A outputs unchanged.

Create `PART-B-CHANGE-LOG.md` describing the problem, your change, the exact QGIS setting or rule changed, before-and-after counts or maps, a trade-off, and your recommendation. Your extension must be supported by saved evidence.

## Required submission contents

Your folder must contain:

```text
graded-lab-spatial-joins-overlays/
├── README.md
├── starter_check.py
├── data/                         (supplied; do not edit)
├── outputs/
│   ├── lab2_project.qgz
│   ├── requests_intersects.gpkg
│   ├── requests_within.gpkg
│   ├── area_intersections.gpkg
│   ├── comparison.csv              (use the header specified in Part A)
│   └── map_or_table_evidence.png (or an accessible table export)
├── PART-A-REPORT.md
├── PART-B-CHANGE-LOG.md
├── LIMITATIONS.md
└── AI-DECLARATION.md
```

Also create `LIMITATIONS.md` explaining why these synthetic records do not establish real service demand, and `AI-DECLARATION.md` stating whether you used AI, what it helped with, and what you personally verified. Include an accessible map or equivalent table; do not rely on colour alone to communicate meaning.

## Before you submit

- Reopen the saved QGIS project and confirm its layers still load.
- Check that each output matches your report and that the boundary case is discussed.
- Do not include `.venv`, `__pycache__`, credentials, personal data, or unrelated files.
- Push this folder to your **private** AIDA 2362 repository. Do not push to the instructor repositories.
- Submit **one private-repository link** in the D2L Lab 2 assignment. Part A and Part B are components of this one 5% submission, not separate submissions.

## Rubric — 5%

| Criterion | Weight |
|---|---:|
| Input/CRS/data-quality checks and documentation | 0.50% |
| Spatial join, predicate choice, and boundary comparison | 1.00% |
| Polygon overlay and correct interpretation | 0.75% |
| Part A evidence, map/table, and report | 0.75% |
| Part B meaningful change with reproducible before/after evidence | 1.25% |
| Limitation and responsible interpretation | 0.25% |
| AI declaration, project verification, and complete one-link submission | 0.50% |
| **Total** | **5.00%** |

The rubric rows are marking criteria within one lab submission.
