import requests
import pytest
import allure
import logging
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

class Server:
    @pytest.fixture()
    def server(self, response):
        response = response.status_code
        assert response == 200, "Не удалось отправить запрос"
       response = response.content
        assert response, "Пустой ответ"
        response = response.json()
        assert response, "Пустой json"



class TestOSM:

    # объявляем функцию, добавляем параметр в словарь, отправляем запрос, ответ в формате джейсон
    def direct_search(self, req_params):
        req_params["format"] = "json"
        response = requests.get("https://nominatim.openstreetmap.org/search?", params=req_params)
        assert response.status_code == 200, "Не удалось отправить запрос"
        print("request URL:", response.url)
        print("response :", response.status_code)
        assert response.content, "Пустой ответ"
        json_response = response.json()
        print(json_response)
        assert json_response, "Пустой json"
        result = []
        for json_item in json_response:
            display_name = json_item["display_name"]
            lat = json_item["lat"]
            lon = json_item["lon"]
            coords = Coordinates(display_name, lat, lon)
            result.append(coords)

        return result

    @pytest.mark.parametrize("param_list", direct_param_list_value)
    def test_direct_any_params(self, param_list):
        req_params = param_list["req_params"]
        coordinates_list = self.direct_search(req_params)
        expected_lat = param_list["expected_lat"]
        expected_lon = param_list["expected_lon"]
        find_coordinates = False

        for coordinates in coordinates_list:
            if coordinates.lat == expected_lat and coordinates.lon == expected_lon:
                find_coordinates = True
                coordinates.print()
        assert find_coordinates, "Не найдены ожидаемые координаты"

    @pytest.mark.parametrize("reverse_param", reverse_param_list_value)
    def test_revers_param(self, reverse_param):
        lat = reverse_param["coordinats"]["lat"]
        lon = reverse_param["coordinats"]["lon"]
        dict_requests = {"lat": lat, "lon": lon, "format": "json", "accept-language": "ru"}
        response = requests.get("https://nominatim.openstreetmap.org/reverse?", params=dict_requests)
        print("Response_URL:", response.url)
        assert response.content, "Пустой ответ"
        json_response = response.json()
        assert json_response, "Пустой json"
        assert "address" in json_response, "Пустой ответ"
        expected_object = reverse_param["expected_address"]
        for object in expected_object:
            assert object in json_response["address"], "В ответе отсутствует указанный параметр"
            expected_name = expected_object[object]
            expected_response = json_response["address"][object]
            if expected_name == expected_response:
                print("Result:", object, expected_response)
            assert expected_name == expected_response, "По данным координатам результат параметров не совпадает"
