import csv
import math
import requests

FUEL_FILE = "C:/Users/DELL/Desktop/Spotter/Assessment/fuel_route_clean/fuel_data/fuel_prices.csv"

MAX_RANGE_MILES = 500
MPG = 10


def haversine(lat1, lon1, lat2, lon2):
    R = 3958.8
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


# Load fuel stations (simulated coordinates)
def load_fuel_stations():
    stations = []

    with open(FUEL_FILE, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):
            try:
                price = float(row["price"])

                # Spread data better to reduce duplicates
                lat = 25 + ((i * 3) % 25)
                lon = -125 + ((i * 5) % 50)

                stations.append({
                    "lat": lat,
                    "lon": lon,
                    "price": price,
                    "city": row.get("city", "")
                })
            except:
                continue

    return stations


# Get real route from OSRM
def get_route(start, end):
    url = f"http://router.project-osrm.org/route/v1/driving/{start['lon']},{start['lat']};{end['lon']},{end['lat']}?overview=full&geometries=geojson"

    response = requests.get(url)
    data = response.json()

    route = data["routes"][0]

    distance_miles = route["distance"] / 1609.34
    geometry = route["geometry"]["coordinates"]

    return distance_miles, geometry


# Filter stations near route
def find_stations_along_route(stations, route_coords):
    filtered = []

    for station in stations:
        for lon, lat in route_coords[::50]:
            dist = haversine(lat, lon, station["lat"], station["lon"])

            if dist < 100:
                filtered.append(station)
                break

    return filtered


# MAIN FUNCTION
def optimize_fuel_route(start, end):
    stations = load_fuel_stations()

    if not stations:
        return {
            "total_distance": 0,
            "fuel_stops": [],
            "total_gallons": 0,
            "total_cost": 0,
        }

    total_distance, route_coords = get_route(start, end)

    route_stations = find_stations_along_route(stations, route_coords)

    num_segments = max(1, int(total_distance // MAX_RANGE_MILES))

    fuel_stops = []

    for i in range(1, num_segments + 1):
        idx = int(len(route_coords) * (i / (num_segments + 1)))
        lon, lat = route_coords[idx]

        nearby = sorted(
            route_stations,
            key=lambda s: haversine(lat, lon, s["lat"], s["lon"])
        )[:15]

        if nearby:
            fuel_stops.append(min(nearby, key=lambda x: x["price"]))

    # ✅ FINAL DEDUP (GUARANTEED UNIQUE)
    unique = []
    seen = set()

    for stop in fuel_stops:
        key = (stop["lat"], stop["lon"], stop["price"], stop["city"])

        if key not in seen:
            unique.append(stop)
            seen.add(key)

    fuel_stops = unique[:6]

    total_gallons = total_distance / MPG
    gallons_per_stop = MAX_RANGE_MILES / MPG

    total_cost = sum(stop["price"] * gallons_per_stop for stop in fuel_stops)

    return {
        "total_distance": round(total_distance, 2),
        "fuel_stops": fuel_stops,
        "total_gallons": round(total_gallons, 2),
        "total_cost": round(total_cost, 2),
    }