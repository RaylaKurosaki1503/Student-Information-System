"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

File: Assignment.py
"""


class Assignment:
    def __init__(self, grade: str, notes: str):
        self.grade: str = grade
        self.notes: str = notes
        pass

    def get_grade(self) -> str:
        return self.grade

    def set_grade(self, grade: str):
        self.grade = grade
        pass

    def compute_grade(self) -> float:
        num, denom = self.grade.split("/")
        return float(num) / float(denom)

    def get_notes(self) -> str:
        return self.notes

    pass
