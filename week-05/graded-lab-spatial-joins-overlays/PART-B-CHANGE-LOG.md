## Issue or question
R-05 is on the boundary between AREA-A and AREA-B.
I tested if `touch` can find requests that are on service-area boundaries.

## Exact setting changed
I used the same settings as Part A:
- Input layer: service_requests
- Join layer: service_areas
- Join type: one-to-many
- Unmatched requests were kept
I only changed the spatial predicate to: touch
The new result was saved as:`outputs/requests_touch.gpkg`

## Before and after results
### Before
Using `within`:
- 4 matched rows
- 1 unmatched request
- R-05 did not match any area

Using `intersects`:
- 6 matched rows
- R-05 matched AREA-A and AREA-B

### After
Using `touch`:
- 2 matched rows
- R-05 matched AREA-A
- R-05 matched AREA-B
- R-01, R-02, R-03, and R-04 did not match
## What changed
`touch` only found the boundary request.

R-05 matched because it is on the boundary. The other requests did not match because they are inside the service areas.

## Trade-off or limitation
`touch` is useful for finding boundary points, but it cannot be used for normal area assignment because points inside a polygon do not match.

## Recommendation
I recommend using `within` for normal requests and `touch` to check boundary requests.
This makes it easier to find special cases like R-05.