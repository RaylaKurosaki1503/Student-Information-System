"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This class represents a student and provides functionality to
store and manage information about the student, such as name, student status,
degrees, minors, terms, courses, and GPAs.
"""

from src.constructors.Course import Course
from src.constructors.Degree import Degree
from src.constructors.Minor import Minor
from src.constructors.Term import Term
from src.lib import pretty_print


class Student:

    def __init__(self):
        """
        The constructor method initializes a new instance of the `Student`
        class.
        """
        self.name: str = ""
        self.student_status: str = ""
        self.degrees: dict[str, Degree] = {}
        self.minors: dict[str, Minor] = {}
        self.terms: dict[int, Term] = {}
        self.courses: dict[str, Course] = {}
        self.gpas: dict[str, float] = {}
        pass

    def get_name(self) -> str:
        """
        Returns the name of the student.
        :return: The name of the student.
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        Sets the name of the student.
        :param name: The name to set.
        :return:
        """
        self.name: str = name
        return None

    def get_student_status(self) -> str:
        """
        Returns the student status.
        :return: The student status.
        """
        return self.student_status

    def set_student_status(self, student_status: str) -> None:
        """
        Sets the student status.
        :param student_status: The student status to set.
        :return: None
        """
        self.student_status: str = student_status
        return None

    def get_degrees(self) -> dict[str, Degree]:
        """
        Returns the dictionary of degrees associated with the student.
        :return: The dictionary of degrees, where the keys are the plan codes
        and the values are instances of the `Degree` class.
        """
        return self.degrees

    def get_degree(self, plan_code: str) -> Degree:
        """
        Returns the degree with the specified plan code.
        :param plan_code: The plan code of the degree.
        :return: The instance of the `Degree` class with the specified plan
        code.
        """
        return self.degrees[plan_code]

    def add_degree(self, plan_code: str, degree: Degree) -> None:
        """
        Adds a new degree to the student.
        :param plan_code: The plan code of the degree.
        :param degree: An instance of the `Degree` class representing the degree to add.
        :return:
        """
        self.degrees[plan_code]: Degree = degree
        return None

    def get_minors(self) -> dict[str, Minor]:
        """
        Returns the dictionary of minors associated with the student.
        :return: The dictionary of minors, where the keys are the plan codes
        and the values are instances of the `Minor` class.
        """
        return self.minors

    def get_minor(self, plan_code: str) -> Minor:
        """
        Returns the minor with the specified plan code.
        :param plan_code: The plan code of the minor.
        :return: The instance of the `Minor` class with the specified plan code.
        """
        return self.minors[plan_code]

    def add_minor(self, plan_code: str, minor: Minor) -> None:
        """
        Adds a new minor to the student.
        :param plan_code: The plan code of the minor.
        :param minor: An instance of the `Minor` class representing the minor
        to add.
        :return: None
        """
        self.minors[plan_code]: Minor = minor
        return None

    def get_terms(self) -> dict[int, Term]:
        """
        Returns the dictionary of terms associated with the student.
        :return: The dictionary of terms, where the keys are the term numbers
        and the values are instances of the `Term` class.
        """
        return self.terms

    def get_term(self, term_num: int) -> Term:
        """
        Returns the term with the specified term number.
        :param term_num: The term number.
        :return: The term with the specified term number.
        """
        return self.terms[term_num]

    def add_term(self, term_num: int, term: Term) -> None:
        """
        Adds a new term to the student.
        :param term_num: The term number.
        :param term: An instance of the `Term` class representing the term to add.
        :return: None
        """
        self.terms[term_num]: Term = term
        return None

    def get_courses(self) -> dict[str, Course]:
        """
        Returns the dictionary of courses associated with the student.
        :return: The dictionary of courses, where the keys are the course IDs
        and the values are instances of the `Course` class.
        """
        return self.courses

    def get_course(self, course_id: str) -> Course:
        """
        Returns the course with the specified course ID.
        :param course_id: The ID of the course.
        :return: The instance of the `Course` class with the specified course ID.
        """
        return self.courses[course_id]

    def add_course(self, term: int, course_id: str, course: Course) -> None:
        """
        Adds a new course to the student for the specified term.
        :param term: The term number.
        :param course_id: The ID of the course.
        :param course: An instance of the `Course` class representing the
        course to add.
        :return: None
        """
        self.courses[course_id]: Course = course
        self.terms[term].add_course(course_id, course)
        return None

    def print_basic_info(self, file):
        """
        Prints basic information about the student to the specified file.
        :param file: The file to write the information to.
        :return: None
        """
        # --------------------------------------------------------------------
        # Student's name
        # --------------------------------------------------------------------
        string_to_print: str = f"Name: {self.get_name()}\n"
        # --------------------------------------------------------------------
        # Student's Degree(s)
        # --------------------------------------------------------------------
        string_to_print += f"Degree(s):\n"
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
        # --------------------------------------------------------------------
        # Student's Minor(s)
        # --------------------------------------------------------------------
        string_to_print += f"Minor(s):\n"
        for minor in self.get_minors().values():
            string_to_print += f"\t{minor.get_name()}\n"
            pass
        # --------------------------------------------------------------------
        # Student's GPA(s)
        # --------------------------------------------------------------------
        string_to_print += f"GPA(s):\n"
        for student_status, gpa in self.get_gpas().items():
            string_to_print += f"\t{student_status}: " \
                               f"{pretty_print.fmt_num_to_str(gpa, 3)}\n"
            pass
        string_to_print += "\n"
        file.write(string_to_print)
        return None

    def get_gpas(self) -> dict[str, float]:
        """
        Returns the dictionary of GPAs associated with the student.
        :return: The dictionary of GPAs, where the keys are the student
        statuses and the values are the corresponding GPAs.
        """
        return self.gpas

    def set_gpa(self, student_status: str, gpa: float) -> None:
        """
        Sets the GPA for the specified student status.
        :param student_status: The student status.
        :param gpa: The GPA to set.
        :return: None
        """
        self.gpas[student_status] = gpa
        return None

    pass
