import requests
import allure
import logging
log_server = logging.getLogger("server")


class ServerConnection:

    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, full_url, params):
        params["format"] = "json"
        response = requests.get(full_url, params=params)
        assert response.status_code == 200, "Не удалось отправить запрос"
        log_server.debug(f"request URL: {response.url}")
        log_server.debug(f"response : {response.status_code}")
        assert response.content, "Пустой ответ"
        with allure.step("Формируем ответ в формат json"):
            json_response = response.json()
        log_server.debug(f"response data: {json_response}")
        assert json_response, "Пустой json"
        return json_response

    def search(self, params):
        full_url = self.base_url + "search"
        server_response_json = self.send_request(full_url, params)
        return server_response_json

    def reverse(self, params):
        full_url = self.base_url + "reverse"
        server_response_json = self.send_request(full_url, params)
        return server_response_json
