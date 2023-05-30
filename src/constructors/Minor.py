"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This class provides basic functionality to store and retrieve
information about a minor, such as the plan code and the name of the minor. It
can be used to create instances of minors with specific plan codes and names,
and retrieve the associated information when needed.
"""


class Minor:
    def __init__(self, plan_code: str, name: str):
        """
        The constructor method initializes a new instance of the `Minor` class.
        :param plan_code: The plan code associated with the minor.
        :param name: The name of the minor.
        """
        self.plan_code: str = plan_code
        self.name: str = name
        pass

    def get_plan_code(self) -> str:
        """
        Returns the plan code associated with the minor.
        :return: The plan code associated with the minor.
        """
        return self.plan_code

    def get_name(self) -> str:
        """
        Returns the name of the minor.
        :return: The name of the minor.
        """
        return self.name

    pass
