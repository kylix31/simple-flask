from flask_server.core.abstract.rule import Rule


class MultipleOfFiveRule(Rule):
    """
    A rule that checks if a number is a multiple of five.

    Attributes:
        None

    Methods:
        match(number: int) -> bool:
            Checks if the given number is a multiple of five.

        response() -> str:
            Returns the response message for a number that is a multiple of five.

    """

    def match(self, number: int) -> bool:
        """
        Checks if the given number is a multiple of five.

        Parameters:
            number (int): The number to be checked.

        Returns:
            bool: True if the number is a multiple of five, False otherwise.

        """
        return number % 5 == 0

    def response(self) -> str:
        """
        Returns the response message for a number that is a multiple of five.

        Parameters:
            None

        Returns:
            str: The response message for a number that is a multiple of five.

        """
        return "Type 2"
