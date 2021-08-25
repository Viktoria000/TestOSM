import requests
import pytest
import allure
from direct_param_list import direct_param_list_value
from server import ServerConnection

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

# class Server:
#     def __init__(self, url, params):
#         self.url = url
#         self.params = params
#         response = requests.get(url, params)
#         print(response.url)
#


class TestOSM:

    def object_request(self):
        result = []
        for json_item in json_response:
            display_name = json_item["display_name"]
            lat = json_item["lat"]
            lon = json_item["lon"]
            coords = Coordinates(display_name, lat, lon)
            result.append(coords)

        return result

    @allure.feature('Прямой запрос')
    @pytest.mark.usefixtures("object_class_server")
    @pytest.mark.parametrize("param_list", direct_param_list_value)
    def test_direct_any_params(self, param_list, object_class_server):
        req_params = param_list["req_params"]
        coordinates_list = object_class_server.search(req_params)
        expected_lat = param_list["expected_lat"]
        expected_lon = param_list["expected_lon"]
        find_coordinates = False
        with allure.step("Сравниваем полученные результаты"):
            for coordinates in coordinates_list:
                if coordinates.lat == expected_lat and coordinates.lon == expected_lon:
                    find_coordinates = True
                    coordinates.print()
        assert find_coordinates, "Не найдены ожидаемые координаты"

    # @allure.feature("Обратный запрос")
    # @pytest.mark.parametrize("reverse_param", reverse_param_list_value)
    # def test_revers_param(self, reverse_param):
    #     lat = reverse_param["coordinats"]["lat"]
    #     lon = reverse_param["coordinats"]["lon"]
    #     dict_requests = {"lat": lat, "lon": lon, "format": "json", "accept-language": "ru"}
    #     with allure.step("Отправляем запрос и получаем ответ"):
    #         response = requests.get("https://nominatim.openstreetmap.org/reverse?", params=dict_requests)
    #     print("Response_URL:", response.url)
    #     assert response.content, "Пустой ответ"
    #     with allure.step("Формируем ответ в формат json"):
    #         json_response = response.json()
    #     assert json_response, "Пустой json"
    #     assert "address" in json_response, "Пустой ответ"
    #     expected_object = reverse_param["expected_address"]
    #     with allure.step("Проверяем есть ли нужный параметр в ответе"):
    #         for object in expected_object:
    #             assert object in json_response["address"], "В ответе отсутствует указанный параметр"
    #         expected_name = expected_object[object]
    #         expected_response = json_response["address"][object]
    #         with allure.step("Сравниваем результаты"):
    #             if expected_name == expected_response:
    #                 print("Result:", object, expected_response)
    #         assert expected_name == expected_response, "По данным координатам результат параметров не совпадает"
