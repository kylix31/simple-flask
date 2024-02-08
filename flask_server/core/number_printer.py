from typing import List

from flask_server.core.contracts.rule_protocol import RuleProtocol


class NumberPrinter:

    def __init__(self, rules: List[RuleProtocol]) -> None:
        """
        Initialize a NumberPrinter object.

        Parameters:
        - rules (List[RuleProtocol]): A list of RuleProtocol objects
        representing the rules to be applied.

        Returns:
        - None

        Raises:
        - None
        """
        self.rules = rules

    def print_number_or_type(self, number: int) -> str:
        """
        Print the number or its corresponding type based on the provided rules.

        Parameters:
        - number (int): The number to be printed.

        Returns:
        - str: The printed number or its corresponding type.

        Raises:
        - None
        """
        for rule in self.rules:
            if rule.match(number):
                return rule.response()
        return str(number)
