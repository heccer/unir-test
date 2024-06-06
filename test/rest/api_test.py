import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add_response_ok(self):
        self.checkConnectionAndResponse("calc/add/2/2", b'4')
        self.checkConnectionAndResponse("calc/add/0/2", b'2')

    def test_api_add_incorrect_parameters(self):
        self.checkErrorResponse("calc/add/2/none")
        self.checkErrorResponse("calc/add/X/5")
        self.checkErrorResponse("calc/add/1/ocho")

    def test_api_substract_response_ok(self):
        self.checkConnectionAndResponse("calc/substract/2/2", b'0')
        self.checkConnectionAndResponse("calc/substract/0/2", b'-2')
        self.checkConnectionAndResponse("calc/substract/1/-2", b'3')

    def test_api_substract_incorrect_parameters(self):
        self.checkErrorResponse("calc/substract/2/cuatro")
        self.checkErrorResponse("calc/substract/X/0")
        self.checkErrorResponse("calc/substract/0/Y")

    def test_api_multiply_response_ok(self):
        self.checkConnectionAndResponse("calc/multiply/3/2", b'6')
        self.checkConnectionAndResponse("calc/multiply/0/2", b'0')
        self.checkConnectionAndResponse("calc/multiply/-2/-4", b'8')

    def test_api_multiply_incorrect_parameters(self):
        self.checkErrorResponse("calc/multiply/tres/2")
        self.checkErrorResponse("calc/multiply/2/object()")

    def test_api_divide_response_ok(self):
        self.checkConnectionAndResponse("calc/divide/6/2", b'3.0')
        self.checkConnectionAndResponse("calc/divide/0/2", b'0.0')
        self.checkConnectionAndResponse("calc/divide/-8/4", b'-2.0')

    def test_api_divide_incorrect_parameters(self):
        self.checkErrorResponse("calc/divide/4/_")
        self.checkErrorResponse("calc/divide/T/3")

    def test_api_divide_by_zero(self):
        self.checkErrorResponse("calc/divide/4/0")
        self.checkErrorResponse("calc/divide/2/-0")

    def test_api_power_response_ok(self):
        self.checkConnectionAndResponse("calc/power/2/4", b'16')
        self.checkConnectionAndResponse("calc/power/2/1", b'2')
        self.checkConnectionAndResponse("calc/power/2/-1", b'0.5')

    def test_api_power_incorrect_parameters(self):
        self.checkErrorResponse("calc/power/tres/2")
        self.checkErrorResponse("calc/power/9/_")

    def test_api_squareroot_response_ok(self):
        self.checkConnectionAndResponse("calc/squareroot/9", b'3.0')
        self.checkConnectionAndResponse("calc/squareroot/4", b'2.0')
        self.checkConnectionAndResponse("calc/squareroot/6", b'2.449489742783178')

    def test_api_squareroot_incorrect_parameters(self):
        self.checkErrorResponse("calc/squareroot/X")
        self.checkErrorResponse("calc/squareroot/nueve")

    def test_api_squareroot_negative_number_fail(self):
        self.checkErrorResponse("calc/squareroot/-4")
        self.checkErrorResponse("calc/squareroot/-0.01")

    def test_api_log10_response_ok(self):
        self.checkConnectionAndResponse("calc/log10/1", b'0.0')
        self.checkConnectionAndResponse("calc/log10/10", b'1.0')
        self.checkConnectionAndResponse("calc/log10/5", b'0.6989700043360189')

    def test_api_log10_incorrect_parameters(self):
        self.checkErrorResponse("calc/log10/siete")
        self.checkErrorResponse("calc/log10/L")

    def test_api_log10_negative_number_or_zero_fail(self):
        self.checkErrorResponse("calc/log10/-4")
        self.checkErrorResponse("calc/log10/0")
        self.checkErrorResponse("calc/log10/-0")

    #Funcion para llamar centralizadamente al API
    def callApi(self, uri):
        url = f"{BASE_URL}/{uri}"
        return urlopen(url, timeout=DEFAULT_TIMEOUT)

    #Funcion para probar conexion al API y enviar una prueba OK
    def checkConnectionAndResponse(self, uri, value):
        response = self.callApi(uri)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {uri}"
        )
        self.assertEqual(
            response.read(), value, f"Resultado incorrecto en {uri}"
        )

    #Funcion para comprar un error en la llamada al API
    def checkErrorResponse(self, uri):
        try:
            response = self.callApi(uri)
            self.assertEqual(
                response.status, http.client.BAD_REQUEST, f"Parámetros incorrectos en la URL {uri}"
            )
        except Exception as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Parámetros incorrectos en la URL {uri}"
            )