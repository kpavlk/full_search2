import requests

apikey = "40d1649f-0493-4b70-98ba-98533de7710b"


def geocode(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": apikey,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocoder_api_server, params=params)
    json_response = response.json()
    toponyms = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return toponyms[0]["GeoObject"] if toponyms else None


def get_coordinates(address):
    toponym = geocode(address)
    toponym_coord = toponym["Point"]["pos"]
    long, lat = toponym_coord.split()
    return float(long), float(lat)


def get_ll_span(address):
    toponym = geocode(address)
    if not toponym:
        return [None, None]
    toponym_coord = toponym["Point"]["pos"]
    long, lat = toponym_coord.split()
    ll = ",".join([long, lat])
    env = toponym["boundedBy"]["Envelope"]
    l, b = env["lowerCorner"].split(" ")
    r, t = env["upperCorner"].split(" ")
    dx = abs(float(l) - float(r)) / 2
    dy = abs(float(t) - float(b)) / 2
    span = f"{dx},{dy}"
    return ll, span