import math
import pandas as pd

# Load fuel data once (CSV must exist)
FUEL_DATA = pd.read_csv("fuel_data/fuel_prices.csv")


# =========================
# Distance Calculation
# =========================
def haversine(lon1, lat1, lon2, lat2):
    R = 3958.8  # miles

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


# =========================
# Move towards destination
# (simple interpolation)
# =========================
def move_towards(start, end, fraction=0.5):
    return (
        start[0] + (end[0] - start[0]) * (fraction / 100),
        start[1] + (end[1] - start[1]) * (fraction / 100),
    )


# =========================
# Find cheapest fuel station
# (basic version: global cheapest)
# =========================
def find_cheapest_station_near(point):
    row = FUEL_DATA.loc[FUEL_DATA["price"].idxmin()]

    return {
        "location": row.get("name", "Unknown"),
        "lat": float(row.get("lat", 0)),
        "lon": float(row.get("lon", 0)),
        "price": float(row["price"]),
        "checkpoint": point,
    }


# =========================
# Cost calculation
# =========================
def calculate_total(stops):
    mpg = 25  # assumed vehicle efficiency
    total = 0

    for stop in stops:
        fuel_needed = 450 / mpg
        total += fuel_needed * stop["price"]

    return round(total, 2)


# =========================
# MAIN OPTIMIZATION LOGIC
# =========================
def optimize_route(start, end, max_range=500, safe_range=450):
    """
    start, end format: (lon, lat)
    """

    distance = haversine(start[0], start[1], end[0], end[1])

    # If no fuel needed
    if distance <= max_range:
        return {
            "distance_miles": round(distance, 2),
            "fuel_stops": [],
            "total_cost": 0
        }

    stops = []
    current_point = start
    remaining = distance

    while remaining > max_range:
        checkpoint = move_towards(current_point, end, 50)

        station = find_cheapest_station_near(checkpoint)
        stops.append(station)

        current_point = checkpoint
        remaining -= safe_range

    return {
        "distance_miles": round(distance, 2),
        "fuel_stops": stops,
        "total_cost": calculate_total(stops)
    }