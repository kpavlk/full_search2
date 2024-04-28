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
        address_ll = f"{lat},{lon}"
        span = "0.005,0.005"

        organization = get_business(address_ll, span, "аптека")
        point = organization[0]["geometry"]["coordinates"]
        org_lat = float(point[0])
        org_lon = float(point[1])
        point_param = f"pt={org_lat},{org_lon},pm2dgl"
        for i in organization:
            point = i["geometry"]["coordinates"]
            org_lat = float(point[0])
            org_lon = float(point[1])
            time_data = i["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]
            if 'TwentyFourHours' in time_data:
                point_param += f"~{org_lat},{org_lon},pm2dgl"
            elif "Intervals" in time_data:
                point_param += f"~{org_lat},{org_lon},pm2bll"
            else:
                point_param += f"~{org_lat},{org_lon},pm2grl"
        points_param = point_param + f"~{address_ll},pm2pnl"
        show_map(ll_spn=f"ll={address_ll}&spn=0.0109986,0.010998", map_type="map", add_params=points_param)
        for i in organization:
            name = i["properties"]["name"]
            address = i["properties"]["CompanyMetaData"]["address"]
            time = i["properties"]["CompanyMetaData"]["Hours"]["text"]
            distance = round(lonlat_distance((lon, lat), (org_lon, org_lat)))

            snippet = f"Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\n" \
                  f"Расстояние:\t{distance}м."
            print(snippet)
    else:
        print('No data')


if __name__ == "__main__":
    main()