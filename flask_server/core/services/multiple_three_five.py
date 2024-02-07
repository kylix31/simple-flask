from flask_server.core.abstract.rule import Rule


class MultipleOfThreeAndFiveRule(Rule):
    """
    A rule that checks if a number is a multiple of both 3 and 5.

    This rule extends the abstract Rule class and provides implementations
    for the match and response methods.

    Attributes:
        None

    Methods:
        match(number: int) -> bool:
            Checks if the given number is a multiple of both 3 and 5.

        response() -> str:
            Returns the response message for this rule.

    """

    def match(self, number: int) -> bool:
        """
        Checks if the given number is a multiple of both 3 and 5.

        Parameters:
            number (int): The number to be checked.

        Returns:
            bool: True if the number is a multiple of both 3 and 5, False otherwise.

        """
        return number % 3 == 0 and number % 5 == 0

    def response(self) -> str:
        """
        Returns the response message for this rule.

        Returns:
            str: The response message for this rule.

        """
        return "Type 3"
