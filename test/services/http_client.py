import requests
from requests import Response

from helpers.allure_helpers import AllureHelpers


class HTTPClient:

    def __init__(self) -> None:
        self.token = None
        self.headers = None
        self.response = None

    def get(self, url: str, **kwargs: dict) -> Response:
        self.response = requests.get(url, headers=self.headers, **kwargs)
        AllureHelpers.attach_response_body(self.response)
        return self.response

    def post(self, url: str, **kwargs: dict) -> Response:
        self.response = requests.post(url, headers=self.headers, **kwargs)
        AllureHelpers.attach_response_body(self.response)
        return self.response

    def patch(self, url: str, **kwargs: dict) -> Response:
        self.response = requests.patch(url, headers=self.headers, **kwargs)
        AllureHelpers.attach_response_headers(self.response)
        return self.response

    def delete(self, url: str, **kwargs: dict) -> Response:
        self.response = requests.delete(url, headers=self.headers, **kwargs)
        AllureHelpers.attach_response_headers(self.response)
        return self.response
