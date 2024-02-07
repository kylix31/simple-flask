from typing import Protocol, runtime_checkable


@runtime_checkable
class RuleProtocol(Protocol):
    """
    A protocol for defining rules.

    This protocol defines the methods that a rule class should implement.

    Attributes:
        None

    Methods:
        match(number: int) -> bool:
            Check if the rule matches the given number.

        response() -> str:
            Get the response associated with the rule.

    Raises:
        None

    Returns:
        None
    """

    def match(self, number: int) -> bool:
        """
        Check if the rule matches the given number.

        Args:
            number (int): The number to check.

        Returns:
            bool: True if the rule matches the number, False otherwise.
        """

    def response(self) -> str:
        """
        Get the response associated with the rule.

        Returns:
            str: The response associated with the rule.
        """
