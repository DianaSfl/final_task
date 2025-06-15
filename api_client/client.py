
import requests
from requests import Response

from utils.logger_api import log_response


class FormClient:
    def __init__(self, url: str):
        self.url = url
        self.requests = requests

    _REGISTER = "/api/register"

    def register_admin(self, body: dict) -> Response:
        res = self.requests.post(url=f'{self.url}{self._REGISTER}', json=body)
        log_response(response=res, request_body=body)
        return res

