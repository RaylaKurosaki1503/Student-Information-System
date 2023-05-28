"""
Author: Rayla Kurosaki

GitHub: https://github.com/RaylaKurosaki1503

File: Term.py
"""

from src.constructors.Course import Course


class Term:

    def __init__(self, student_status: str, term_num: int):
        self.student_status: str = student_status
        self.term_num: int = term_num

        self.courses: dict[str, Course] = {}
        self.attempted_credits: int = 0
        self.earned_credits: int = 0
        self.gpa_units: int = 0
        self.points: float = 0
        self.gpa: float = 0.0
        self.cumulative_attempted_credits: int = 0
        self.cumulative_earned_credits: int = 0
        self.cumulative_gpa_units: int = 0
        self.cumulative_points: float = 0
        self.cumulative_gpa: float = 0.0
        pass

    def get_student_status(self) -> str:
        return self.student_status

    def get_term_num(self) -> int:
        return self.term_num

    def get_courses(self) -> dict[str, Course]:
        return self.courses

    def add_course(self, course_id: str, course: Course):
        self.courses[course_id]: Course = course
        pass

    def get_attempted_credits(self) -> int:
        return self.attempted_credits

    def set_attempted_credits(self, attempted_credits: int):
        self.attempted_credits: int = attempted_credits
        pass

    def get_earned_credits(self) -> int:
        return self.earned_credits

    def set_earned_credits(self, earned_credits: int):
        self.earned_credits: int = earned_credits
        pass

    def get_gpa_units(self) -> int:
        return self.gpa_units

    def set_gpa_units(self, gpa_units: int):
        self.gpa_units: int = gpa_units
        pass

    def get_points(self) -> float:
        return self.points

    def set_points(self, points: float):
        self.points: float = points
        pass

    def get_cumulative_attempted_credits(self) -> int:
        return self.cumulative_attempted_credits

    def set_cumulative_attempted_credits(self,
                                         cumulative_attempted_credits: int):
        self.cumulative_attempted_credits: int = cumulative_attempted_credits
        pass

    def get_cumulative_earned_credits(self) -> int:
        return self.cumulative_earned_credits

    def set_cumulative_earned_credits(self, cumulative_earned_credits: int):
        self.cumulative_earned_credits: int = cumulative_earned_credits
        pass

    def get_cumulative_gpa_units(self) -> int:
        return self.cumulative_gpa_units

    def set_cumulative_gpa_units(self, cumulative_gpa_units: int):
        self.cumulative_gpa_units: int = cumulative_gpa_units
        pass

    def get_cumulative_points(self) -> float:
        return self.cumulative_points

    def set_cumulative_points(self, cumulative_points: float):
        self.cumulative_points: float = cumulative_points
        pass

    def get_gpa(self) -> float:
        return self.gpa

    def set_gpa(self, gpa: float):
        self.gpa: float = gpa
        pass

    def compute_gpa(self):
        attempted_credits: int = 0
        earned_credits: int = 0
        gpa_units: int = 0
        points: float = 0
        for course in self.courses.values():
            attempted_credits += course.get_credit()
            earned_credits += course.get_earned_credits()
            final_grade: str = course.get_final_grade_letter()
            no_gpa_lst: list[str] = ["SE", "NE", "R"]
            if final_grade not in no_gpa_lst:
                gpa_units += course.get_earned_credits()
                pass
            points += course.get_points()
            pass
        self.set_attempted_credits(attempted_credits)
        self.set_earned_credits(earned_credits)
        self.set_gpa_units(gpa_units)
        self.set_points(points)
        if gpa_units > 0:
            self.set_gpa(points / gpa_units)
            pass
        pass

    def get_cumulative_gpa(self) -> float:
        return self.cumulative_gpa

    def set_cumulative_gpa(self, gpa: float):
        self.cumulative_gpa: float = gpa
        pass

    pass
