"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This class represents an assignment in an educational setting. It
provides functionality to store and retrieve information about an assignment,
such as the grade and any additional notes or comments.
"""


class Assignment:
    def __init__(self, grade: str, notes: str):
        """
        The constructor method initializes a new instance of the `Assignment`
        class.
        :param grade: The grade received for the assignment
        :param notes: Additional notes or comments regarding the assignment.
        """
        self.grade: str = grade
        self.notes: str = notes
        pass

    def get_grade(self) -> str:
        """
        Returns the grade received for the assignment.
        :return: The grade of the assignment.
        """
        return self.grade

    def set_grade(self, grade: str) -> None:
        """
        Sets a new grade for the assignment.
        :param grade: The new grade to set for the assignment.
        :return: None
        """
        self.grade = grade
        return None

    def compute_grade(self) -> float:
        """
        Computes and returns the numerical grade as a floating-point value.
        :return: The computed numerical grade.
        """
        num, denom = self.grade.split("/")
        return float(num) / float(denom)

    def get_notes(self) -> str:
        """
        Returns any additional notes or comments regarding the assignment.
        :return: The notes or comments for the assignment.
        """
        return self.notes

    pass
