import unittest

import requests_mock

from python_alelo.alelo import Alelo


class AleloTest(unittest.TestCase):
    @requests_mock.mock()
    def test_login_should_update_token(self, mock_request):
        alelo = Alelo("04387645698", "my-pass")

        mock_request.post(
            "https://www.meualelo.com.br/api/meualelo-web-api/s/p/authentication/login",
            status_code=200,
            json={"token": "mock_token"},
        )
        alelo.login()

        self.assertEqual(alelo.token, "mock_token")
