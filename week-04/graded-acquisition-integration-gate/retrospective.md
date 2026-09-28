# Week 4 retrospective

1. What changed between your Part A checkpoint and final Part B result?
The Part A checkpoint established the planned inspection and analysis steps. To arrive at the Part B final result, I completed the validity check output, the spatial join between facilities and service zones, the comparison of variable changes, the map layout, and the text equivalent.

2. Which reviewer observation did you accept, reject, or defer? Why?
- 

3. Which parameter or assumption most changed the result?
I only changed the spatial predicate from `within` to `intersects`. Both settings yielded five matching facility features, so the change did not affect the final result. Consequently, I cannot determine which parameter had the greatest impact.

4. What could still make the output look plausible while being wrong?
Incorrect Coordinate Reference Systems (CRS), incomplete metadata, missing geometry data, or erroneous spatial relationships.

5. What evidence is still missing before operational use?
The data currently used is dummy data. Before actual operational use, current business data, appropriate authorizations, and other real-world inputs would be required.

6. How did you consider accessibility, location privacy, community impact, and Indigenous data authority?
I created a text equivalent so the result can be understood without relying only on colour or map interaction. I used only the supplied fictional locations and did not add any real sensitive locations. The facilities-maintenance team may benefit from better-organized spatial information, while communities could be harmed if incomplete or inaccurate data were used for real decisions. Any real community or Indigenous data would require the relevant Nation or community authority and locally specific protocols before use.


7. What AI assistance, if any, was used? How did you verify it?
I used AI assistance to interpret the README instructions and outline the necessary steps. Before adopting any suggestions, I cross-verified them against the provided README, QGIS results, and output files.