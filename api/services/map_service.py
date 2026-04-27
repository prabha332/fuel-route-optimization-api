import folium
from typing import List, Dict, Tuple


def generate_map(
    route_coords: List[Tuple[float, float]],
    stops: List[Dict]
) -> str:
    """
    Generate HTML map with route + fuel stops
    """

    if not route_coords:
        raise ValueError("route_coords cannot be empty")

    # start map
    m = folium.Map(location=list(route_coords[0]), zoom_start=5)

    # =============================
    # ROUTE LINE
    # =============================
    folium.PolyLine(
        locations=[(lat, lon) for lat, lon in route_coords],
        color="blue",
        weight=4,
        opacity=0.8
    ).add_to(m)

    # =============================
    # FUEL STOPS
    # =============================
    for stop in stops:
        try:
            # ✅ FIX: match your optimizer output format
            lat = stop.get("lat")
            lon = stop.get("lon")

            if lat is None or lon is None:
                continue

            name = stop.get("city", "Fuel Stop")
            price = stop.get("price", "N/A")

            folium.Marker(
                location=[lat, lon],
                popup=f"{name} - ${price}",
                icon=folium.Icon(color="green")
            ).add_to(m)

        except Exception:
            continue

    # =============================
    # SAVE MAP
    # =============================
    file_path = "route_map.html"
    m.save(file_path)

    return file_path