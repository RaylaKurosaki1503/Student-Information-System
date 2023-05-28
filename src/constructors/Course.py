"""
Author: Rayla Kurosaki

GitHub: https://github.com/RaylaKurosaki1503

File: Course.py
"""

from src.constructors.AssignmentType import AssignmentType


class Course:

    def __init__(self, student_status: str, term: int, course_code: str,
                 section: str, name: str, credit: int, professor: str):
        self.student_status: str = student_status
        self.term: int = term
        self.course_code: str = course_code
        self.section: str = section
        self.name: str = name
        self.credit: int = credit
        self.professor: str = professor

        self.assignment_types: dict[str, AssignmentType] = {}
        self.grading_scale: dict[float, str] = {}
        self.extra_credit: float = 0
        self.raw_grade: float = -1
        self.raw_grade_letter: str = "n/a"
        self.final_grade_letter: str = "n/a"
        self.earned_credits: int = -1
        self.points: float = -1
        pass

    def get_student_status(self) -> str:
        return self.student_status

    def get_term(self) -> int:
        return self.term

    def get_course_code(self) -> str:
        return self.course_code

    def get_section(self) -> str:
        return self.section

    def get_course_id(self) -> str:
        return f"{self.term}.{self.course_code}.{self.section}"

    def get_name(self) -> str:
        return self.name

    def get_credit(self) -> int:
        return self.credit

    def get_professor(self) -> str:
        return self.professor

    def get_assignment_types(self) -> dict[str, AssignmentType]:
        return self.assignment_types

    def get_assignment_type(self, asgmt_id: str) -> AssignmentType:
        return self.assignment_types[asgmt_id]

    def add_assignment_type(self, asgmt_id: str, asgmt_type: AssignmentType):
        self.assignment_types[asgmt_id] = asgmt_type
        pass

    def get_grading_scale(self) -> dict[float, str]:
        return self.grading_scale

    def set_grading_scale(self, grading_scale: dict[float, str]):
        self.grading_scale: dict[float, str] = grading_scale
        pass

    def get_extra_credit(self) -> float:
        return self.extra_credit

    def set_extra_credit(self, extra_credit: float):
        self.extra_credit: float = extra_credit
        pass

    def get_raw_grade(self):
        return self.raw_grade

    def compute_raw_grade(self):
        total_asgmt_grade: float = 0.0
        total_weight: float = 0.0
        for assignment in self.get_assignment_types().values():
            assignment.compute_grade()
            if assignment.get_grade() > -1:
                total_asgmt_grade += assignment.get_weighted_grade()
                total_weight += assignment.get_weight()
                pass
            pass
        if total_weight > 0.0:
            raw_grade: float = total_asgmt_grade / total_weight
            self.set_raw_grade((self.get_extra_credit() / 100) + raw_grade)
            pass
        pass

    def set_raw_grade(self, grade: float):
        self.raw_grade = grade
        pass

    def get_raw_grade_letter(self):
        return self.raw_grade_letter

    def set_raw_grade_letter(self, grade: str):
        self.raw_grade_letter: str = grade
        pass

    def computing_raw_grade_letter(self):
        if self.get_raw_grade() >= 0.0:
            self.set_raw_grade_letter("F")
            self.set_final_grade_letter("F")
            for (num, letter) in self.get_grading_scale().items():
                if self.raw_grade >= num:
                    self.set_raw_grade_letter(letter)
                    self.set_final_grade_letter(letter)
                    break
                    pass
                pass
            pass
        pass

    def get_final_grade_letter(self):
        return self.final_grade_letter

    def set_final_grade_letter(self, final_grade_letter: str):
        self.final_grade_letter: str = final_grade_letter
        pass

    def get_earned_credits(self) -> int:
        return self.earned_credits

    def set_earned_credits(self, earned_credits: int):
        self.earned_credits: int = earned_credits
        pass

    def get_points(self) -> float:
        return self.points

    def set_points(self, points: float):
        self.points: float = points
        pass

    pass
