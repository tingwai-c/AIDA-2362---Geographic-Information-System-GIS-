"""Read-only starter check for AIDA 2362 Week 6 Lab 3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "access_zones.geojson"


def main():
    obj = json.loads(DATA.read_text(encoding="utf-8"))
    features = obj.get("features", [])
    required = {"zone_id", "zone_name", "access_index", "locations_reviewed", "period"}
    for feature in features:
        missing = required - set(feature.get("properties", {}))
        if missing or not feature.get("geometry"):
            raise ValueError(f"Feature missing fields or geometry: {missing}")
    if len(features) != 6:
        raise ValueError(f"Expected six zones, found {len(features)}")
    print(f"status: starter_ready | zones: {len(features)} | CRS: EPSG:4326")
    print("Fields:", ", ".join(sorted(required)))
    print("This check does not create or grade your map.")


if __name__ == "__main__":
    main()
