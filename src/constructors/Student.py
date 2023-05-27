"""
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503

File: Student.py
"""

from src.constructors.Course import Course
from src.constructors.Degree import Degree
from src.constructors.Minor import Minor
from src.constructors.Term import Term
from src.lib import pretty_print


class Student:

    def __init__(self):
        self.name: str = ""
        self.student_status: str = ""
        self.degrees: dict[str, Degree] = {}
        self.minors: dict[str, Minor] = {}
        self.terms: dict[int, Term] = {}
        self.courses: dict[str, Course] = {}
        self.gpas: dict[str, float] = {}
        pass

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name: str = name
        pass

    def get_student_status(self) -> str:
        return self.student_status

    def set_student_status(self, student_status: str):
        self.student_status: str = student_status
        pass

    def get_degrees(self) -> dict[str, Degree]:
        return self.degrees

    def get_degree(self, plan_code: str) -> Degree:
        return self.degrees[plan_code]

    def add_degree(self, plan_code: str, degree: Degree):
        self.degrees[plan_code]: Degree = degree
        pass

    def get_minors(self) -> dict[str, Minor]:
        return self.minors

    def get_minor(self, plan_code: str) -> Minor:
        return self.minors[plan_code]

    def add_minor(self, plan_code: str, minor: Minor):
        self.minors[plan_code]: Minor = minor
        pass

    def get_terms(self) -> dict[int, Term]:
        return self.terms

    def get_term(self, term_num: int) -> Term:
        return self.terms[term_num]

    def add_term(self, term_num: int, term: Term):
        self.terms[term_num]: Term = term
        pass

    def get_courses(self) -> dict[str, Course]:
        return self.courses

    def get_course(self, course_id: str) -> Course:
        return self.courses[course_id]

    def add_course(self, term: int, course_id: str, course: Course):
        self.courses[course_id]: Course = course
        self.terms[term].add_course(course_id, course)
        pass

    def print_basic_info(self, file):
        string_to_print: str = f"Name: {self.get_name()}\nDegree(s):\n"
        for degree in self.get_degrees().values():
            degree_plans: dict[str, str] = {
                "PHD": "Doctor of Philosophy",
                "MS": "Master of Science",
                "MST": "Master of Science for Teachers",
                "ME": "Master of Engineering",
                "MBA": "Master of Business Administration",
                "MFA": "Master of Fine Arts",
                "MARCH": "Master of Architecture",
                "ACT": "Advanced Certificate",
                "BS": "Bachelor of Science",
                "BFA": "Bachelor of Fine Arts",
                "AAS": "Associate in Applied Science",
                "AOS": "Associate in Occupational Studies",
            }
            string: str = degree_plans[degree.get_plan_code().split("-")[1]]
            string_to_print += f"\t{string} in {degree.get_name()}\n"
            pass
        string_to_print += f"Minor(s):\n"
        for minor in self.get_minors().values():
            string_to_print += f"\t{minor.get_name()}\n"
            pass
        string_to_print += f"GPA(s):\n"
        for student_status, gpa in self.get_gpas().items():
            string_to_print += f"\t{student_status}: " \
                               f"{pretty_print.fmt_num_to_str(gpa, 3)}\n"
            pass
        string_to_print += "\n"
        file.write(string_to_print)
        pass

    def get_gpas(self) -> dict[str, float]:
        return self.gpas

    def set_gpa(self, student_status: str, gpa: float):
        self.gpas[student_status] = gpa
        pass

    pass
