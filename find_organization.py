import requests


def find_business(ll, spn, request, locale="ru_RU"):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    apikey = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    params = {
        "apikey": apikey,
        "text": request,
        "lang": locale,
        "ll": ll,
        "spn": spn,
        "type": "biz"
    }
    response = requests.get(search_api_server, params=params)
    if not response:
        raise RuntimeError()
    response_json = response.json()
    organizations = response_json["features"]
    return organizations


def get_business(ll, spn, request, locale="ru_RU"):
    organizations = find_business(ll, spn, request)
    if len(organizations):
        return organizations[0]
