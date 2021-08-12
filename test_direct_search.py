import requests
import pytest
import allure
from direct_param_list import direct_param_list_value
from reverse_param_list import reverse_param_list_value

# объявляем класс и его параметры
class Coordinates:

    # конструктор с параметрами
    def __init__(self, display_name, lat, lon):
        self.display_name = display_name
        self.lat = lat
        self.lon = lon

    # функция "печати" содержимого класса
    def print(self):
        print("display_name: ", self.display_name)
        print("lat: ", self.lat)
        print("lon: ", self.lon)
        print("")


# объявляем функцию, добавляем параметр в словарь, отправляем запрос, ответ в формате джейсон
def direct_search(req_params):
    req_params["format"] = "json"
    response = requests.get("https://nominatim.openstreetmap.org/search?", params=req_params)
    json_response = response.json()
    result = []
    for json_item in json_response:
        display_name = json_item["display_name"]
        lat = json_item["lat"]
        lon = json_item["lon"]
        coords = Coordinates(display_name, lat, lon)
        result.append(coords)

    return result

#
# # объявляем тест с параметрами (два набора входных данных)
# @pytest.mark.parametrize("param_list", direct_param_list_value)
# def test_direct_any_params(param_list):
#     req_params = param_list["req_params"]
#     coordinates_list = direct_search(req_params)
#
#     expected_lat = param_list["expected_lat"]
#     expected_lon = param_list["expected_lon"]
#
#     find_coordinates = False
#     for coordinates in coordinates_list:
#         if coordinates.lat == expected_lat and coordinates.lon == expected_lon:
#             find_coordinates = True
#             print("FOUND!!")
#             coordinates.print()
#
#     assert find_coordinates, "not find expected coordinates"


@pytest.mark.parametrize("reverse_param", reverse_param_list_value)
def test_revers_param(reverse_param):
    lat = reverse_param["coordinats"]["lat"]
    lon = reverse_param["coordinats"]["lon"]
    dict_requests = {"lat": lat, "lon": lon, "format": "json", "accept-language": "ru"}
    response = requests.get("https://nominatim.openstreetmap.org/reverse?", params=dict_requests)
    json_response = response.json()
    expected_object = reverse_param["expected_address"]
    if expected_object["city"] == json_response["address"]["city"] and expected_object["country"] == json_response["address"]["country"]:
        print("Good job:", json_response["address"]["city"], json_response["address"]["country"])




