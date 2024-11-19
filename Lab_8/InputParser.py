import re


class InputParser:
    """A class to parse date and phone numbers."""

    @staticmethod
    def parse_date(input_str):
        """
        Parses the input string and checks if it matches the date format YYYY-MM-DD.

        Args:
            input_str (str): The input string to be parsed.

        Returns:
            str: A message indicating whether the date format is valid or invalid.
        """
        if re.match(r'^\d{4}-\d{2}-\d{2}$', input_str):
            return "Дата розпізнана!"
        return "Невірний формат дати"

    @staticmethod
    def parse_phone(input_str):
        """
        Parses the input string and checks if it matches a valid phone number format.

        Args:
            input_str (str): The input string to be parsed.

        Returns:
            str: A message indicating whether the phone number format is valid or invalid.
        """
        if re.match(r'^\+?\d[\d -]{7,12}\d$', input_str):
            return "Телефонний номер розпізнано!"
        return "Невірний формат телефону"
