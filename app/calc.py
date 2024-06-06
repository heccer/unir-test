import app
import math

#Este import se debe descomentar para poder ejecutar / probar el programa
#import util

class InvalidPermissions(Exception):
    pass

class Calculator:
    def add(self, x, y):
        if not app.util.validate_permissions(f"{x} + {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        if not app.util.validate_permissions(f"{x} - {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        if not app.util.validate_permissions(f"{x} / {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        if not app.util.validate_permissions(f"{x} ^ {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x ** y

    def squareroot(self, x):
        if not app.util.validate_permissions(f"sqrt({x})", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_type(x)
        if x < 0:
            raise TypeError("Square Root of negative numbers results in imaginary numbers")

        return math.sqrt(x)

    def log10(self, x):
        if not app.util.validate_permissions(f"log10({x})", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_type(x)
        if x <= 0:
            raise TypeError("Base 10 Logarithm on zero or negative numbers is not possible")

        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be number")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(3, 2)
    print(result)
    result = calc.substract(3, 2)
    print(result)
    result = calc.multiply(3, 2)
    print(result)
    result = calc.divide(3, 2)
    print(result)
    result = calc.power(3, 2)
    print(result)
    result = calc.squareroot(9)
    print(result)
    result = calc.log10(10)
    print(result)