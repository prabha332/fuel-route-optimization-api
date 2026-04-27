import math
from typing import List, Tuple


# ----------------------------
# Distance Calculation (Haversine)
# ----------------------------
def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate distance between two lat/lon points in miles using Haversine formula.
    """
    R = 3958.8  # Earth radius in miles

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.asin(math.sqrt(a))

    return R * c


# ----------------------------
# Route Interpolation
# ----------------------------
def interpolate_route(
    route_points: List[Tuple[float, float]],
    step_miles: float = 20
) -> List[Tuple[float, float]]:
    """
    Densify route points by interpolating between coordinates.
    Helps in finding fuel stops along long routes.
    """

    if not route_points or len(route_points) < 2:
        return route_points

    interpolated = []

    for i in range(len(route_points) - 1):
        lat1, lon1 = route_points[i]
        lat2, lon2 = route_points[i + 1]

        segment_distance = calculate_distance(lat1, lon1, lat2, lon2)

        steps = max(int(segment_distance // step_miles), 1)

        for s in range(steps):
            t = s / steps

            lat = lat1 + (lat2 - lat1) * t
            lon = lon1 + (lon2 - lon1) * t

            interpolated.append((lat, lon))

    # include final point
    interpolated.append(route_points[-1])

    return interpolated


# ----------------------------
# Total Route Distance
# ----------------------------
def total_route_distance(route_points: List[Tuple[float, float]]) -> float:
    """
    Calculate full route distance.
    """
    total = 0.0

    for i in range(len(route_points) - 1):
        lat1, lon1 = route_points[i]
        lat2, lon2 = route_points[i + 1]

        total += calculate_distance(lat1, lon1, lat2, lon2)

    return round(total, 2)