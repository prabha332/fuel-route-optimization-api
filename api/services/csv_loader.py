import pandas as pd
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="fuel_route_app")


# ==============================
# GEOCODER WITH SAFETY
# ==============================
def get_lat_lon(address):
    try:
        location = geolocator.geocode(address, timeout=10)

        if location:
            return location.latitude, location.longitude

    except Exception as e:
        print(f"Geocode error for {address}: {e}")

    return None, None


# ==============================
# LOAD FUEL DATA
# ==============================
def load_fuel_data():

    df = pd.read_csv("fuel_data/fuel_prices.csv")

    # clean NaN early
    df = df.dropna(subset=["address", "city", "state"])

    df["full_address"] = (
        df["address"].astype(str) + ", " +
        df["city"].astype(str) + ", " +
        df["state"].astype(str)
    )

    # ==============================
    # CACHE (IMPORTANT FIX)
    # ==============================
    cache = {}

    latitudes = []
    longitudes = []

    for addr in df["full_address"]:

        if addr in cache:
            lat, lon = cache[addr]
        else:
            lat, lon = get_lat_lon(addr)
            cache[addr] = (lat, lon)

            # rate limiting (still required)
            time.sleep(0.5)

        latitudes.append(lat)
        longitudes.append(lon)

    df["latitude"] = latitudes
    df["longitude"] = longitudes

    # remove failed geocodes
    df = df.dropna(subset=["latitude", "longitude"])

    return df