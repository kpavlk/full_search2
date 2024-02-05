# python3 main.py Москва, ул. Шолохова, 20

import sys
from module import get_coordinates
from find_organization import get_business, find_business
from count_distance import lonlat_distance
from show_module import show_map


def main():
    toponym_to_find = " ".join(sys.argv[1:])

    if toponym_to_find:
        lat, lon = get_coordinates(toponym_to_find)
        address_ll = f"{lat}{lon}"
        span = "0.005,0.005"

        organization = get_business(address_ll, span, "аптека")
        point = organization["geometry"]["coordinates"]
        org_lat = float(point[0])
        org_lon = float(point[1])
        point_param = f"pt={org_lat},{org_lon},pm2dgl"
        points_param = point_param + f"{address_ll},pm2dgl"
        show_map(map_type="map", add_params=points_param)
        name = organization["properties"]["CompanyMetadata"]["name"]
        address = organization["properties"]["CompanyMetadata"]["address"]
        time = organization["properties"]["CompanyMetadata"]["Hours"]["text"]
        distance = round(lonlat_distance((lon, lat), (org_lon, org_lat)))

        snippet = f"Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\n" \
                  f"Расстояние:\t{distance}м."
        print(snippet)
    else:
        print('No data')


if __name__ == "__main__":
    main()