"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This class represents a degree program in a university or
educational institution. It provides basic functionality to store and retrieve
information about a degree, such as the plan code and the name of the degree.
"""


class Degree:
    def __init__(self, plan_code: str, name: str):
        """
        The constructor method initializes a new instance of the `Degree`
        class.
        :param plan_code: The plan code associated with the degree.
        :param name: The name of the degree.
        """
        self.plan_code: str = plan_code
        self.name: str = name
        pass

    def get_plan_code(self) -> str:
        """
        Returns the plan code associated with the degree.
        :return: The plan code of the degree.
        """
        return self.plan_code

    def get_name(self) -> str:
        """
        Returns the name of the degree.
        :return: The name of the degree.
        """
        return self.name

    pass
