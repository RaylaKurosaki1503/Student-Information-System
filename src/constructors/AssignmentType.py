"""
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503

File: AssignmentType.py
"""

from src.constructors.Assignment import Assignment


class AssignmentType:
    def __init__(self, asgmt_type: str, weight: float):
        self.asgmt_type: str = asgmt_type
        self.weight: float = weight

        self.assignments: dict[int, Assignment] = {}
        self.grade: float = -1
        self.weighted_grade: float = -1
        pass

    def get_assignment_type(self) -> str:
        return self.asgmt_type

    def get_weight(self) -> float:
        return self.weight

    def get_assignments(self) -> dict[int, Assignment]:
        return self.assignments

    def add_assignment(self, index: int, assignment: Assignment):
        self.assignments[index] = assignment
        pass

    def get_grade(self) -> float:
        return self.grade

    def set_grade(self, grade: float):
        self.grade: float = grade
        pass

    def compute_grade(self):
        if len(self.assignments) > 0:
            grades: list[float] = []
            for assignment in self.assignments.values():
                grades.append(assignment.compute_grade())
                pass
            self.grade: float = sum(grades) / len(grades)
            self.weighted_grade: float = self.grade * self.weight
            pass
        pass

    def get_weighted_grade(self) -> float:
        return self.weighted_grade

    def set_weighted_grade(self, weighted_grade: float):
        self.weighted_grade: float = weighted_grade
        pass

    def get_min_grade(self) -> (int, Assignment):
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

    def drop_grades(self, n: int):
        for _ in range(n):
            self.assignments.pop(self.get_min_grade()[0])
            pass
        pass

    pass
