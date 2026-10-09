# AIDA 2362 — Week 6 Graded Lab 3: Cartography and Visual Hierarchy

**Individual | One submission | 5% total (Part A 3% + Part B 2%)**

## The task

Create an accessible, decision-useful QGIS map of fictional neighbourhood access indicators. Make the main pattern easy to see without hiding the counts or limitations, then test how one cartographic choice changes the message.

## Start here

1. Copy this whole `graded-lab-cartography-visual-hierarchy` folder from the instructor's **AIDA_2362_Graded_Labs** repository into `week-06/` of your assigned private AIDA 2362 repository. Keep the folder name.
2. Open your **private repository** in VS Code. In its terminal, run:

   ```powershell
   py week-06/graded-lab-cartography-visual-hierarchy/starter_check.py
   ```

3. Confirm the check reports six polygon features and the expected fields. It checks the supplied files; it does not create your map.
4. Open QGIS and add `data/access_zones.geojson` using **Layer → Add Layer → Add Vector Layer**. Do not change the supplied data or labels.
5. Confirm the layer CRS is EPSG:4326. For a scale bar and local map layout, export a working copy in EPSG:32612; keep the original unchanged and record the transformation.

## Part A — Guided map (3%)

### A1. Inspect and understand the data

1. Record the six zone names, the `access_index` values, `locations_reviewed` counts, reporting period, and CRS.
2. Check for missing values, duplicate zone IDs, and invalid or empty geometries.
3. Explain what the index measures according to the supplied data note. Do not interpret it as a percentage of residents served.

### A2. Create the main thematic map

1. Open **Layer Styling** and choose **Graduated** symbology.
2. Set the value field to `access_index` and use **3 classes**. Choose and document a classification method (equal interval is a suitable starting point).
3. Choose a sequential, colour-blind-considerate colour ramp. Use labels as well as colour to distinguish zones; avoid a red/green-only distinction.
4. Label polygons with `zone_name`. Keep labels legible and avoid covering boundaries.
5. Create a QGIS Print Layout with a descriptive title, legend containing numeric class breaks, reporting period, data-source note, scale bar, and north arrow where appropriate.
6. Include a small table listing each zone, index, and number of locations reviewed. Do not make the map the only way to access the results.
7. Export the main map as `outputs/access_map_part_a.pdf` or `.png` and save the project as `outputs/lab3_project.qgz`.

### A3. Explain the map

Create `PART-A-REPORT.md`. State the audience and decision question, explain what the index does and does not mean, list the CRS and transformation, document the class method and exact breaks, identify the high/low zones, and explain how the counts affect interpretation. Include one limitation and one next validation step.

## Part B — Independent cartographic comparison (2%)

Choose one consequential map choice to test, such as using 3 versus 5 classes, changing the class method, or revising a colour/label choice. Do not alter the source data.

1. Save the alternative map as `outputs/access_map_part_b.pdf` or `.png`; do not overwrite Part A.
2. Create `PART-B-CHANGE-LOG.md` with the issue, exact map setting changed, class breaks before and after, what pattern became more or less visible, accessibility trade-off, and which version you recommend for the stated audience.
3. Support your comparison with a short table listing zone values, counts, and class assignment in both versions.

## Required files

```text
graded-lab-cartography-visual-hierarchy/
├── README.md
├── starter_check.py
├── data/                         (supplied; do not edit)
├── outputs/
│   ├── lab3_project.qgz
│   ├── access_map_part_a.pdf or .png
│   ├── access_map_part_b.pdf or .png
│   └── map_comparison.csv
├── PART-A-REPORT.md
├── PART-B-CHANGE-LOG.md
├── LIMITATIONS.md
└── AI-DECLARATION.md
```

Also create `LIMITATIONS.md` explaining sample-size, measurement, classification, and geographic-scale limits. Create `AI-DECLARATION.md` stating whether AI tools were used, what they helped with, and what you personally checked. Your map must include an equivalent text/table summary and must not rely on colour alone.

## Before submitting

- Reopen your saved QGIS project and verify that all layers load.
- Check that the map title, legend breaks, period, source note, and table match your analysis.
- Do not include `.venv`, `__pycache__`, credentials, personal data, or unrelated files.
- Push the complete folder to your **private** AIDA 2362 repository, not the instructor repositories.
- Submit **one private-repository link** in the D2L Lab 3 assignment. Both parts belong to this one 5% submission.

## Rubric — 5%

| Criterion | Weight |
|---|---:|
| Data understanding, source/CRS and quality checks | 0.50% |
| Accurate, readable Part A thematic map and required map elements | 1.25% |
| Table-equivalent evidence and interpretation that respects counts | 0.50% |
| Part A report, limitation, and next validation step | 0.75% |
| Part B meaningful design comparison with reproducible evidence | 1.00% |
| Accessibility, trade-off, recommendation, and complete submission | 1.00% |
| **Total** | **5.00%** |

This rubric marks components within one lab; it does not create separate submissions.
