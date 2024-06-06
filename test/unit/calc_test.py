import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(6, 2))
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(0, self.calc.substract(-2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(2, 0))
        self.assertEqual(0, self.calc.multiply(-2, 0))
        self.assertEqual(4, self.calc.multiply(-2, -2))
        self.assertEqual(3, self.calc.multiply(2, 1.5))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.power(1, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(-8, self.calc.power(-2, 3))
        self.assertEqual(16, self.calc.power(-2, 4))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(1.4142135623730951, self.calc.power(2, 0.5))

    def test_squareroot_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.squareroot(4))
        self.assertEqual(3, self.calc.squareroot(9))
        self.assertEqual(2.449489742783178, self.calc.squareroot(6))

    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(0.6989700043360189, self.calc.log10(5))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_subtract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, "2", None)
        self.assertRaises(TypeError, self.calc.power, 2, object())
        self.assertRaises(TypeError, self.calc.power, "2", object())

    def test_squareroot_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.squareroot, "2")
        self.assertRaises(TypeError, self.calc.squareroot, "")
        self.assertRaises(TypeError, self.calc.squareroot, None)
        self.assertRaises(TypeError, self.calc.squareroot, object())

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "2")
        self.assertRaises(TypeError, self.calc.log10, "")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_squareroot_method_fails_with_negative_numbers(self):
        self.assertRaises(TypeError, self.calc.squareroot, -2)
        self.assertRaises(TypeError, self.calc.squareroot, -0.1)
        self.assertRaises(TypeError, self.calc.squareroot, "-1")

    def test_log10_method_fails_with_negative_or_zero(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -1)
        self.assertRaises(TypeError, self.calc.log10, -0)
        self.assertRaises(TypeError, self.calc.log10, "-1")

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_add_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_subtract_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.substract(6, 2))
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(0, self.calc.substract(-2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(2, 0))
        self.assertEqual(0, self.calc.multiply(-2, 0))
        self.assertEqual(4, self.calc.multiply(-2, -2))
        self.assertEqual(3, self.calc.multiply(2, 1.5))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_divide_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_power_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(1, self.calc.power(1, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(-8, self.calc.power(-2, 3))
        self.assertEqual(16, self.calc.power(-2, 4))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(1.4142135623730951, self.calc.power(2, 0.5))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_squareroot_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(2, self.calc.squareroot(4))
        self.assertEqual(3, self.calc.squareroot(9))
        self.assertEqual(2.449489742783178, self.calc.squareroot(6))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_log10_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(0.6989700043360189, self.calc.log10(5))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
