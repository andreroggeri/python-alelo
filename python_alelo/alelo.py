import datetime
import os
from enum import Enum
from typing import Dict
from typing import Optional

import requests
from requests import Response

import jwt

HOST = "https://www.meualelo.com.br"


class TransactionsTime(Enum):
    LAST_FIVE = "LAST_FIVE"
    LAST_FIFTY_DAYS = "LAST_FIFTY_DAYS"
    LAST_MONTH = "LAST_MONTH"
    LAST_THREE_MONTHS = "LAST_THREE_MONTHS"
    LAST_FOUR_MONTHS = "LAST_FOUR_MONTHS"


class Alelo:
    def __init__(self, cpf: Optional[str] = None, pwd: Optional[str] = None):
        self.cpf = cpf if cpf else os.getenv("ALELO_CPF")
        self.pwd = pwd if pwd else os.getenv("ALELO_PWD")

        self.token = None

    def login(self):

        if not self.token:

            json_data = {"cpf": self.cpf, "password": self.pwd, "captcha": ""}
            response = requests.post(
                f"{HOST}/api/meualelo-web-api/s/p/authentication/login",
                json=json_data,
                headers={"x-api-key": self._get_api_key()},
            )

            self.token = self._handle_response(response)["token"]

    def _get_token(self) -> str:
        if not self.token:
            raise Exception("Token not found. You need login first")

        return self.token

    def _get_headers(self) -> Dict:

        return {"x-api-key": self._get_api_key(), "authorization": self._get_token()}

    def get_cards(self) -> Dict:

        response = requests.get(f"{HOST}/api/meualelo-web-api/s/card", headers=self._get_headers())

        return self._handle_response(response)

    def get_statement(self, card_id: str) -> Dict:

        response = requests.get(f"{HOST}/api/meualelo-web-api/s/card/{card_id}/statement", headers=self._get_headers())

        return self._handle_response(response)

    def get_transactions(self, card_id: str, period: TransactionsTime = TransactionsTime.LAST_FIVE) -> Dict:

        response = requests.get(
            f"{HOST}/api/meualelo-web-api/s/card/{card_id}/statement/transactions?period={period.name}&cardType=REFEICAO",
            headers=self._get_headers(),
        )

        return self._handle_response(response)

    def _handle_response(self, response: Response) -> Dict:

        if response.status_code == 401:
            self.token = None
            raise Exception("Status 401. You need login again")

        if response.status_code != 200:
            print(response.json())
            raise Exception(f"The request made failed with HTTP status code {response.status_code}")

        return response.json()

    @staticmethod
    def _get_api_key():
        payload = {
            "iss": "meualelo.alelo.com.br",
            "sub": "meualelo",
            "fnp": "91a646d8f05e17d9d92ab32f711d3579",
            "src": "WEB",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        }

        token = jwt.encode(payload, "<hb(yk%YK8s{tw6T", algorithm="HS256")
        return token
