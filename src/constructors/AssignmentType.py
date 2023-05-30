"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This class represents a specific type or category of assignments
within an educational setting. It provides functionality to store and manage
information about the assignment type, its weight in the overall grading
system, the individual assignments associated with it, and the calculated
grades based on the assignments.
"""

from src.constructors.Assignment import Assignment


class AssignmentType:
    def __init__(self, asgmt_type: str, weight: float):
        """
        The constructor method initializes a new instance of the
        `AssignmentType` class.
        :param asgmt_type: The type or category of the assignment.
        :param weight: The weight of the assignment type in the overall
        grading system.
        """
        self.asgmt_type: str = asgmt_type
        self.weight: float = weight

        self.assignments: dict[int, Assignment] = {}
        self.grade: float = -1
        self.weighted_grade: float = -1
        pass

    def get_assignment_type(self) -> str:
        """
        Returns the type or category of the assignment.
        :return: The assignment type.
        """
        return self.asgmt_type

    def get_weight(self) -> float:
        """
        Returns the weight of the assignment type in the overall grading
        system.
        :return: The weight of the assignment type.
        """
        return self.weight

    def get_assignments(self) -> dict[int, Assignment]:
        """
        Returns the dictionary of assignments associated with the assignment
        type.
        :return: The dictionary of assignments, where the keys are the indices
        of the assignments and the values are instances of the `Assignment`
        class.
        """
        return self.assignments

    def add_assignment(self, index: int, assignment: Assignment) -> None:
        """
        Adds a new assignment to the assignment type.
        :param index: The index of the assignment.
        :param assignment: An instance of the `Assignment` class representing
        the assignment to add.
        :return: None
        """
        self.assignments[index] = assignment
        return None

    def get_grade(self) -> float:
        """
        Returns the calculated grade for the assignment type.
        :return: The calculated grade for the assignment type.
        """
        return self.grade

    def set_grade(self, grade: float) -> None:
        """
        Sets a new grade for the assignment type.
        :param grade: The new grade to set for the assignment type.
        :return: None
        """
        self.grade: float = grade
        return None

    def compute_grade(self) -> None:
        """
        Computes the grade for the assignment type based on the grades of the
        associated assignments.
        :return: None
        """
        if len(self.assignments) > 0:
            grades: list[float] = []
            for assignment in self.assignments.values():
                grades.append(assignment.compute_grade())
                pass
            self.grade: float = sum(grades) / len(grades)
            self.weighted_grade: float = self.grade * self.weight
            pass
        return None

    def get_weighted_grade(self) -> float:
        """
        Returns the weighted grade for the assignment type.
        :return: The weighted grade for the assignment type.
        """
        return self.weighted_grade

    def set_weighted_grade(self, weighted_grade: float) -> None:
        """
        Sets a new weighted grade for the assignment type.
        :param weighted_grade: The new weighted grade to set for the
        assignment type.
        :return: None
        """
        self.weighted_grade: float = weighted_grade
        return None

    def get_min_grade(self) -> tuple[int, Assignment]:
        """
        Returns the index and the assignment with the lowest grade among the
        associated assignments.
        :return: A tuple containing the index and an instance of the
        `Assignment` class with the lowest grade.
        """
        low_index: int = next(iter(self.assignments))
        min_grade: float = self.assignments[low_index].compute_grade()
        for index, assignment in self.assignments.items():
            grade: float = assignment.compute_grade()
            if grade < min_grade:
                low_index: int = index
                min_grade: float = self.assignments[low_index].compute_grade()
                pass
            pass
        return low_index, self.assignments[low_index]

    def drop_grades(self, n: int) -> None:
        """
        Removes `n` assignments with the lowest grades from the assignment
        type.
        :param n: The number of assignments to remove.
        :return: None
        """
        for _ in range(n):
            self.assignments.pop(self.get_min_grade()[0])
            pass
        return None

    pass
