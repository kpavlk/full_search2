import math


def lonlat_distance(a, b):
    degree_to_meter_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_lat = math.radians(a_lat + b_lat / 2.0)
    lan_lon_factor = math.cos(radians_lat)
    dx = abs(a_lon - b_lon) * degree_to_meter_factor * lan_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meter_factor * lan_lon_factor
    return math.sqrt(dx ** 2 + dy ** 2)


