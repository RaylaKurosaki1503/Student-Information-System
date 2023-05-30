"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This class represents a specific course in an educational
setting. It provides functionality to store and manage information about the
course, such as student status, term, course code, section, name, credit,
professor, assignment types, grading scale, and grades.
"""

from src.constructors.AssignmentType import AssignmentType


class Course:

    def __init__(self, student_status: str, term: int, course_code: str,
                 section: str, name: str, credit: int, professor: str):
        """
        The constructor method initializes a new instance of the `Course`
        class.
        :param student_status: The student status in relation to the course.
        :param term: The term or semester of the course.
        :param course_code: The code or identifier of the course.
        :param section: The section of the course.
        :param name: The name or title of the course.
        :param credit: The credit value of the course.
        :param professor: The professor or instructor of the course.
        """
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
        """
        Returns the student status in relation to the course.
        :return: The student status.
        """
        return self.student_status

    def get_term(self) -> int:
        """
        Returns the term or semester of the course.
        :return: The term or semester.
        """
        return self.term

    def get_course_code(self) -> str:
        """
        Returns the code or identifier of the course.
        :return: The course code.
        """
        return self.course_code

    def get_section_number(self) -> str:
        """
        Returns the section number of the course.
        :return: The section number.
        """
        return self.section

    def get_course_id(self) -> str:
        """
        Returns the unique identifier of the course.
        :return: The course ID in the format "{term}.{course_code}.{section}".
        """
        return f"{self.term}.{self.course_code}.{self.section}"

    def get_name(self) -> str:
        """
        Returns the name or title of the course.
        :return: The course name.
        """
        return self.name

    def get_credit(self) -> int:
        """
        Returns the credit value of the course.
        :return: The credit value.
        """
        return self.credit

    def get_professor(self) -> str:
        """
        Returns the professor or instructor of the course.
        :return: The professor or instructor.
        """
        return self.professor

    def get_assignment_types(self) -> dict[str, AssignmentType]:
        """
        Returns the dictionary of assignment types associated with the course.
        :return: The dictionary of assignment types, where the keys are the
        assignment type IDs and the values are instances of the
        `AssignmentType` class.
        """
        return self.assignment_types

    def get_assignment_type(self, asgmt_id: str) -> AssignmentType:
        """
        Returns the assignment type with the given assignment type ID.
        :param asgmt_id: The ID of the assignment type.
        :return: An instance of the `AssignmentType` class representing the
        assignment type.
        """
        return self.assignment_types[asgmt_id]

    def add_assignment_type(self, asgmt_id: str,
                            asgmt_type: AssignmentType) -> None:
        """
        Adds a new assignment type to the course.
        :param asgmt_id: The ID of the assignment type.
        :param asgmt_type: An instance of the `AssignmentType` class
        representing the assignment type to add.
        :return: None
        """
        self.assignment_types[asgmt_id] = asgmt_type
        return None

    def get_grading_scale(self) -> dict[float, str]:
        """
        Returns the grading scale associated with the course.
        :return: The grading scale, where the keys are the grade cutoffs and
        the values are the corresponding grade letters.
        """
        return self.grading_scale

    def set_grading_scale(self, grading_scale: dict[float, str]) -> None:
        """
        Sets the grading scale for the course.
        :param grading_scale: The grading scale to set, where the keys are the
        grade cutoffs and the values are the corresponding grade letters.
        :return: None
        """
        self.grading_scale: dict[float, str] = grading_scale
        return None

    def get_extra_credit(self) -> float:
        """
        Returns the amount of extra credit associated with the course.
        :return: The amount of extra credit.
        """
        return self.extra_credit

    def set_extra_credit(self, extra_credit: float) -> None:
        """
        Sets the amount of extra credit for the course.
        :param extra_credit: The amount of extra credit to set.
        :return: None
        """
        self.extra_credit: float = extra_credit
        return None

    def get_raw_grade(self) -> float:
        """
        Returns the raw grade of the course.
        :return: The raw grade.
        """
        return self.raw_grade

    def compute_raw_grade(self) -> None:
        """
        Computes the raw grade of the course based on the grades of the
        associated assignment types.
        :return: None
        """
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
        return None

    def set_raw_grade(self, grade: float) -> None:
        """
        Sets the raw grade of the course.
        :param grade: The raw grade to set.
        :return: None
        """
        self.raw_grade = grade
        return None

    def get_raw_grade_letter(self) -> str:
        """
        Returns the letter grade corresponding to the raw grade of the course.
        :return: The letter grade.
        """
        return self.raw_grade_letter

    def set_raw_grade_letter(self, grade: str) -> None:
        """
        Sets the letter grade corresponding to the raw grade of the course.
        :param grade: The letter grade to set.
        :return: None
        """
        self.raw_grade_letter: str = grade
        return None

    def computing_raw_grade_letter(self) -> None:
        """
        Computes the letter grade corresponding to the raw grade of the course
        based on the grading scale.
        :return: None
        """
        if self.get_raw_grade() >= 0.0:
            self.set_raw_grade_letter("F")
            self.set_final_grade_letter("F")
            for (num, letter) in self.get_grading_scale().items():
                if self.raw_grade >= num:
                    self.set_raw_grade_letter(letter)
                    self.set_final_grade_letter(letter)
                    return None
                pass
            pass
        return None

    def get_final_grade_letter(self) -> str:
        """
        Returns the final letter grade of the course.
        :return: The final letter grade.
        """
        return self.final_grade_letter

    def set_final_grade_letter(self, final_grade_letter: str) -> None:
        """
        Sets the final letter grade of the course.
        :param final_grade_letter: The final letter grade to set.
        :return: None
        """
        self.final_grade_letter: str = final_grade_letter
        return None

    def get_earned_credits(self) -> int:
        """
        Returns the number of earned credits for the course.
        :return: The number of earned credits.
        """
        return self.earned_credits

    def set_earned_credits(self, earned_credits: int) -> None:
        """
        Sets the number of earned credits for the course.
        :param earned_credits: The number of earned credits to set.
        :return: None
        """
        self.earned_credits: int = earned_credits
        return None

    def get_points(self) -> float:
        """
        Returns the number of points for the course.
        :return: The number of points.
        """
        return self.points

    def set_points(self, points: float) -> None:
        """
        Sets the number of points for the course.
        :param points: The number of points to set.
        :return: None
        """
        self.points: float = points
        return None

    pass
