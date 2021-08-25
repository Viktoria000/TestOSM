import requests
import allure


class ServerConnection:

    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, full_url, params):
        params["format"] = "json"
        response = requests.get(full_url, params=params)
        assert response.status_code == 200, "Не удалось отправить запрос"
        print("request URL:", response.url)
        print("response :", response.status_code)
        assert response.content, "Пустой ответ"
        with allure.step("Формируем ответ в формат json"):
            json_response = response.json()
        print(json_response)
        assert json_response, "Пустой json"
        return json_response

    def search(self, params):
        full_url = self.base_url + "search"
        self.send_request(full_url, params)
        return self.send_request()
     #
     # def Reverse(self, params):
     #     full_url = self.base_url + "reverse"
