from core.number_printer import NumberPrinter
from core.services import MultipleOfFiveRule, MultipleOfThreeRule, MultipleOfThreeAndFiveRule


class NumberModel:
    """
    A class that represents a collection of numbers and provides methods to add
    numbers, retrieve their values, and get all numbers.

    Attributes:
        numbers_collection (dict): A dictionary that stores the numbers and
        their corresponding values.
        printer (NumberPrinter): An instance of the NumberPrinter class that
        handles the printing of numbers based on certain rules.
    """

    def __init__(self):
        """
        Initializes a new instance of the NumberModel class.

        The numbers_collection attribute is initialized as an empty dictionary.
        The printer attribute is initialized with an instance of the
        NumberPrinter class, which is configured with three rules:
        - MultipleOfThreeAndFiveRule: Prints "Type 3" for numbers that are
        multiples of both 3 and 5.
        - MultipleOfThreeRule: Prints "Type 1" for numbers that are multiples
        of 3.
        - MultipleOfFiveRule: Prints "Type 2" for numbers that are multiples
        of 5.
        """
        self.numbers_collection = {}
        self.printer = NumberPrinter([
            MultipleOfThreeAndFiveRule(),
            MultipleOfThreeRule(),
            MultipleOfFiveRule()
        ])

    def add_number(self, number):
        """
        Adds a number to the numbers_collection dictionary and returns its
        corresponding value.

        Args:
            number (int): The number to be added to the collection.

        Returns:
            str: The value associated with the added number, based on the rules
            defined in the printer attribute.

        Raises:
            None
        """
        value = self.printer.print_number_or_type(number)
        self.numbers_collection[number] = value
        return value

    def get_value(self, number):
        """
        Retrieves the value associated with a given number from the
        numbers_collection
        dictionary.

        Args:
            number (int): The number for which the value needs to be retrieved.

        Returns:
            str: The value associated with the given number, or None if the
            number is not present in the collection.

        Raises:
            None
        """
        return self.numbers_collection.get(number)

    def get_all(self):
        """
        Retrieves the entire numbers_collection dictionary.

        Args:
            None

        Returns:
            dict: The dictionary containing all the numbers and their
            corresponding values.

        Raises:
            None
        """
        return self.numbers_collection
