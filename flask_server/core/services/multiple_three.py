from abstract.rule import Rule


class MultipleOfThreeRule(Rule):
    """
    A rule that checks if a number is a multiple of three.

    Attributes:
        None

    Methods:
        match(number: int) -> bool:
            Checks if the given number is a multiple of three.

        response() -> str:
            Returns the response message for a number that is a multiple of
            three.

    """

    def match(self, number: int) -> bool:
        """
        Checks if the given number is a multiple of three.

        Parameters:
            number (int): The number to be checked.

        Returns:
            bool: True if the number is a multiple of three, False otherwise.

        """
        return number % 3 == 0

    def response(self) -> str:
        """
        Returns the response message for a number that is a multiple of three.

        Parameters:
            None

        Returns:
            str: The response message for a number that is a multiple of three.

        """
        return "Type 1"
