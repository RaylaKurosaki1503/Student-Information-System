"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This class represents an academic term or semester. It provides
functionality to store and manage information about the term, such as student
status, term number, courses, attempted credits, earned credits, GPA units,
points, GPA, cumulative attempted credits, cumulative earned credits,
cumulative GPA units, cumulative points, and cumulative GPA.
"""

from src.constructors.Course import Course


class Term:

    def __init__(self, student_status: str, term_num: int):
        """
        The constructor method initializes a new instance of the `Term` class.
        :param student_status: The student status in relation to the term.
        :param term_num: The term or semester number.
        """
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
        """
        Returns the student status in relation to the term.
        :return: The student status.
        """
        return self.student_status

    def get_term_num(self) -> int:
        """
        Returns the term or semester number.
        :return: The term or semester number.
        """
        return self.term_num

    def get_courses(self) -> dict[str, Course]:
        """
        Returns the dictionary of courses associated with the term.
        :return: The dictionary of courses, where the keys are the course IDs
        and the values are instances of the `Course` class.
        """
        return self.courses

    def add_course(self, course_id: str, course: Course) -> None:
        """
        Adds a new course to the term.
        :param course_id: The ID of the course.
        :param course: An instance of the `Course` class representing the
        course to add.
        :return: None
        """
        self.courses[course_id]: Course = course
        return None

    def get_attempted_credits(self) -> int:
        """
        Returns the number of attempted credits for the term.
        :return: The number of attempted credits.
        """
        return self.attempted_credits

    def set_attempted_credits(self, attempted_credits: int) -> None:
        """
        Sets the number of attempted credits for the term.
        :param attempted_credits: The number of attempted credits to set.
        :return: None
        """
        self.attempted_credits: int = attempted_credits
        return None

    def get_earned_credits(self) -> int:
        """
        Returns the number of earned credits for the term.
        :return: The number of earned credits.
        """
        return self.earned_credits

    def set_earned_credits(self, earned_credits: int):
        """
        Sets the number of earned credits for the term.
        :param earned_credits: The number of earned credits to set.
        :return: None
        """
        self.earned_credits: int = earned_credits
        return None

    def get_gpa_units(self) -> int:
        """
        Returns the GPA units for the term.
        :return: The GPA units.
        """
        return self.gpa_units

    def set_gpa_units(self, gpa_units: int):
        """
        Sets the GPA units for the term.
        :param gpa_units: The GPA units to set.
        :return: None
        """
        self.gpa_units: int = gpa_units
        return None

    def get_points(self) -> float:
        """
        Returns the number of points for the term.
        :return: The number of points.
        """
        return self.points

    def set_points(self, points: float) -> None:
        """
        Sets the number of points for the term.
        :param points: The number of points to set.
        :return: None
        """
        self.points: float = points
        return None

    def get_cumulative_attempted_credits(self) -> int:
        """
        Returns the cumulative number of attempted credits.
        :return: The cumulative number of attempted credits.
        """
        return self.cumulative_attempted_credits

    def set_cumulative_attempted_credits(self,
                                         cum_attempted_credits: int) -> None:
        """
        Sets the cumulative number of attempted credits.
        :param cum_attempted_credits: The cumulative number of
        attempted credits to set.
        :return: None
        """
        self.cumulative_attempted_credits: int = cum_attempted_credits
        return None

    def get_cumulative_earned_credits(self) -> int:
        """
        Returns the cumulative number of earned credits.
        :return: The cumulative number of earned credits.
        """
        return self.cumulative_earned_credits

    def set_cumulative_earned_credits(self,
                                      cumulative_earned_credits: int) -> None:
        """
        Sets the cumulative number of earned credits.
        :param cumulative_earned_credits: The cumulative number of earned
        credits to set.
        :return: None
        """
        self.cumulative_earned_credits: int = cumulative_earned_credits
        return None

    def get_cumulative_gpa_units(self) -> int:
        """
        Returns the cumulative GPA units.
        :return: The cumulative GPA units.
        """
        return self.cumulative_gpa_units

    def set_cumulative_gpa_units(self, cumulative_gpa_units: int) -> None:
        """
        Sets the cumulative GPA units.
        :param cumulative_gpa_units: The cumulative GPA units to set.
        :return: None
        """
        self.cumulative_gpa_units: int = cumulative_gpa_units
        return None

    def get_cumulative_points(self) -> float:
        """
        Returns the cumulative number of points.
        :return: The cumulative number of points.
        """
        return self.cumulative_points

    def set_cumulative_points(self, cumulative_points: float):
        """
        Sets the cumulative number of points.
        :param cumulative_points: The cumulative number of points to set.
        :return: None
        """
        self.cumulative_points: float = cumulative_points
        return None

    def get_gpa(self) -> float:
        """
        Returns the GPA (Grade Point Average) for the term.
        :return: The GPA.
        """
        return self.gpa

    def set_gpa(self, gpa: float) -> None:
        """
        Sets the GPA (Grade Point Average) for the term.
        :param gpa: The GPA to set.
        :return:
        """
        self.gpa: float = gpa
        return None

    def compute_gpa(self) -> None:
        """
        Computes the GPA (Grade Point Average) for the term based on the
        grades of the associated courses.
        :return: None
        """
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
        return None

    def get_cumulative_gpa(self) -> float:
        """
        Returns the cumulative GPA (Grade Point Average).
        :return: The cumulative GPA.
        """
        return self.cumulative_gpa

    def set_cumulative_gpa(self, gpa: float):
        """
        Sets the cumulative GPA (Grade Point Average).
        :param gpa: The cumulative GPA to set.
        :return: None
        """
        self.cumulative_gpa: float = gpa
        return None

    pass
