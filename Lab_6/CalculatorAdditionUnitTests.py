import random
import string
import unittest
from Lab_2.calculator import Calculator


class CalculatorAdditionUnitTests(unittest.TestCase):
    def test_addition_of_two_positive_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = 10
        number2 = 20
        expected_result = 30

        # Act
        actual_result = calculator.addition(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_addition_of_two_negative_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = -10
        number2 = -20
        expected_result = -30

        # Act
        actual_result = calculator.addition(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_addition_of_positive_and_negative_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = 10
        number2 = -20
        expected_result = -10

        # Act
        actual_result = calculator.addition(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_addition_of_two_random_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        expected_result = number1 + number2

        # Act
        actual_result = calculator.addition(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_addition_of_two_random_float_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = random.uniform(1, 100)
        number2 = random.uniform(1, 100)
        expected_result = number1 + number2

        # Act
        actual_result = calculator.addition(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_addition_of_two_random_string_numbers(self):
        # Arrange
        calculator = Calculator()
        number1 = ''.join(random.choices(string.digits, k=5))
        number2 = ''.join(random.choices(string.digits, k=5))
        expected_result = int(number1) + int(number2)

        # Act
        actual_result = calculator.addition(number1, number2)

        # Assert
        self.assertEqual(expected_result, actual_result)