"""Read-only input check for AIDA 2362 Week 5 Lab 2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FILES = ("service_areas.geojson", "planning_districts.geojson", "service_requests.geojson")


def main():
    for filename in FILES:
        obj = json.loads((DATA / filename).read_text(encoding="utf-8"))
        features = obj.get("features", [])
        kinds = sorted({feature.get("geometry", {}).get("type", "missing") for feature in features})
        print(f"{filename}: features={len(features)}, geometry={','.join(kinds)}, CRS=EPSG:4326")
        if not features or any(not feature.get("properties") or not feature.get("geometry") for feature in features):
            raise ValueError(f"Missing feature properties or geometry in {filename}")
    print("status: starter_ready (this check does not perform the lab analysis)")


if __name__ == "__main__":
    main()
