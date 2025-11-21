import requests
import math
import time
import json
import networkx as nx

def nodo_name(n: int) -> str:
    rows = [
        "1a Calle Poniente",
        "2a Calle Poniente",
        "3a Calle Poniente",
        "4a Calle Poniente",
        "5a Calle Poniente",
        "6a Calle Poniente",
        "7a Calle Poniente"
    ]

    columns = [
        ("Alameda Santa Lucia", "Calzada Santa Lucia Sur"),
        "7a Avenida Norte",
        "6a Avenida Norte",
        "5a Avenida Norte",
        "4a Avenida Norte",
        "3a Avenida Norte",
        "2a Avenida Norte",
        "1a Avenida Norte"
    ]

    row_index = math.floor(n / 8)
    col_index = n % 8

    col = columns[col_index]
    if isinstance(col, tuple):
        if row_index < 4:
            col = col[0]
        else:
            col = col[1]
    return rows[row_index], col

def round_math(value, decimals=2):
    if value is None:
        return None
    factor = 10 ** decimals
    if value >= 0:
        return math.floor(value * factor + 0.5) / factor
    else:
        return math.ceil(value * factor - 0.5) / factor

def get_coordinates(query):
    url = "https://photon.komoot.io/api/"
    params = {"q": query, "limit": 1}
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("features"):
        lon, lat = data["features"][0]["geometry"]["coordinates"]
        return round_math(lat), round_math(lon)
    return None, None

def nodo_coordinates(street, avenue):
    query = f"{street}, {avenue}, Antigua Guatemala"
    lat, lon = get_coordinates(query)
    if lat is None:
        lat, lon = get_coordinates(f"{street}, Antigua Guatemala")
    if lat is None:
        lat, lon = get_coordinates(f"{avenue}, Antigua Guatemala")
    return lat, lon

coordinates = []
for nodo in range(8*7):
    street, avenue = nodo_name(nodo)
    coordinates.append(nodo_coordinates(street, avenue))

print(coordinates)
