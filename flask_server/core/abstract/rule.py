from abc import ABC, abstractmethod

from flask_server.core.contracts.rule_protocol import RuleProtocol


class Rule(ABC, RuleProtocol):
    """
    Abstract base class for defining rules.

    This class provides a common interface for defining rules. Subclasses must
    implement the `match` and `response` methods.

    Attributes:
        None

    Methods:
        match(number: int) -> bool:
            Determines if the given number matches the rule.

        response() -> str:
            Returns the response associated with the rule.

    Raises:
        None

    Returns:
        None
    """

    @abstractmethod
    def match(self, number: int) -> bool:
        """
        Determines if the given number matches the rule.

        Args:
            number (int): The number to be checked.

        Returns:
            bool: True if the number matches the rule, False otherwise.
        """

        pass

    @abstractmethod
    def response(self) -> str:
        """
        Returns the response associated with the rule.

        Returns:
            str: The response associated with the rule.
        """

        pass
