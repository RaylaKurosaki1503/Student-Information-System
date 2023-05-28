"""
Author: Rayla Kurosaki

GitHub: https://github.com/RaylaKurosaki1503

File: special_cases.py
"""

from src.constructors.Assignment import Assignment as Asgmt
from src.constructors.AssignmentType import AssignmentType as AsgmtType
from src.constructors.Course import Course


def drop_grades_2191_phys_320_01(asgmt_type: AsgmtType, n: int):
    for _ in range(n):
        low_index: int = next(iter(asgmt_type.get_assignments()))
        asgmt: Asgmt = asgmt_type.get_assignments()[low_index]
        low_grade: float = asgmt.compute_grade()
        for index, assignment in asgmt_type.get_assignments().items():
            if "Homework" in assignment.get_notes():
                grade: float = assignment.compute_grade()
                if grade < low_grade:
                    low_index: int = index
                    asgmt: Asgmt = asgmt_type.get_assignments()[low_index]
                    low_grade: float = asgmt.compute_grade()
                    pass
                pass
            pass
        asgmt_type.get_assignments().pop(low_index)
        pass
    pass


def compute_course_grade_helper(course: Course):
    lst_cs: list[str] = ["2175.CSCI-141.02", "2181.CSCI-142.01",
                         "2188.CSCI-243.01"]
    lst_basic: list[str] = ["2185.ENGL-314.01", "2185.MATH-399.01"]
    course_id: str = course.get_course_id()
    if course_id in lst_cs:
        compute_course_grade_a(course)
        pass
    elif course_id in lst_basic:
        compute_course_grade_b(course)
        pass
    elif course_id == "2185.PHYS-212.06":
        compute_course_grade_c(course)
        pass
    elif course_id == "2195.PHYS-283.01":
        compute_course_grade_d(course)
        pass
    pass


def compute_course_grade_a(course: Course):
    """
    For some courses, they have a course grade limit rule. This rule comes
    into play when the difference between your Assignments and Tests averages
    is more than about 20%. Also, the raw grade may only be at most 10% more
    than the average grade of the elements of your worse Assignments
    Component or Tests Component. Courses that would use this rule include
    but are not limited to:
        - Computer Science I
        - Computer Science II
        - The Mechanics of Programming
    """
    course.compute_raw_grade()
    raw_grade: float = course.get_raw_grade()
    total_asgmt_weighted_grade: float = 0
    total_asgmt_weight: float = 0
    total_exam_weighted_grade: float = 0
    total_exam_weight: float = 0
    for assignment in course.get_assignment_types().values():
        weighted_grade: float = assignment.get_weighted_grade()
        if weighted_grade > -1:
            if "Exam" in assignment.get_assignment_type():
                total_exam_weighted_grade += weighted_grade
                total_exam_weight += assignment.get_weight()
                pass
            else:
                total_asgmt_weighted_grade += weighted_grade
                total_asgmt_weight += assignment.get_weight()
                pass
            pass
        pass
    assignment_grade: float = total_asgmt_weighted_grade / total_asgmt_weight
    exam_grade: float = total_exam_weighted_grade / total_exam_weight
    if abs(assignment_grade - exam_grade) > 0.2:
        if assignment_grade < exam_grade:
            if raw_grade > assignment_grade + 0.1:
                course.set_raw_grade(assignment_grade + 0.1)
                pass
            pass
        else:
            if raw_grade > exam_grade + 0.1:
                course.set_raw_grade(exam_grade + 0.1)
                pass
            pass
        pass
    pass


def compute_course_grade_b(course: Course):
    """
    For some courses, the raw grade is calculated simply by computing the
    sum of the numerators of the grades and the sum of the numerators of
    the grades. Then dividing the two values.
    """
    numerator: float = 0.0
    denominator: float = 0.0
    for asgmt_type in course.get_assignment_types().values():
        for grade in asgmt_type.get_assignments().values():
            grade_lst: list[str] = grade.get_grade().split("/")
            numerator += float(grade_lst[0])
            denominator += float(grade_lst[1])
            pass
        pass
    if denominator != 0:
        course.set_raw_grade(numerator / denominator)
        pass
    pass


def compute_course_grade_c(course: Course):
    """
    Special calculations to compute the raw grade for University Physics II.
    For this class, all quiz grades have their grades raised by a set amount.
    """
    quizzes: AsgmtType = course.get_assignment_type("Quizzes")
    for quiz in quizzes.get_assignments().values():
        grade_lst = quiz.get_grade().split("/")
        numerator: float = float(grade_lst[0])
        denominator: float = float(grade_lst[1])
        quiz.set_grade(f"{numerator + 10 - denominator}/10")
        pass
    course.compute_raw_grade()
    pass


def compute_course_grade_d(course: Course):
    """
    Special calculations to compute the raw grade for Vibrations and Waves.
    For this class, the average homework grade is calculated differently.
    """
    total_asgmt_grade: float = 0.0
    total_weight: float = 0.0
    for asgmt_type in course.get_assignment_types().values():
        if asgmt_type.get_assignment_type() == "Homework":
            numerator: float = 0.0
            denominator: float = 0.0
            homeworks: dict[int, Asgmt] = asgmt_type.get_assignments()
            if len(homeworks) > 0:
                for homework in homeworks.values():
                    grade_lst = homework.get_grade().split("/")
                    numerator += float(grade_lst[0])
                    denominator += float(grade_lst[1])
                    pass
                grade: float = numerator / denominator
                asgmt_type.set_grade(grade)
                asgmt_type.set_weighted_grade(asgmt_type.get_weight() * grade)
                pass
            pass
        else:
            asgmt_type.compute_grade()
            pass
        if asgmt_type.get_grade() > -1:
            total_asgmt_grade += asgmt_type.get_weighted_grade()
            total_weight += asgmt_type.get_weight()
            pass
        pass
    if total_weight > 0.0:
        grade: float = total_asgmt_grade / total_weight
        course.set_raw_grade((course.get_extra_credit() / 100) + grade)
        pass
    pass


def computing_raw_letter_grade_2185_math_399_01(course: Course):
    """
    For the course 2185.MATH-399.01, a student passes this class with an 'A'
    if their raw grade is at least 70%. Otherwise, then the student fails with
    an 'F'.
    """
    grade: str = "F"
    if course.get_raw_grade() >= 0.70:
        grade: str = "A"
        pass
    course.set_raw_grade_letter(grade)
    course.set_final_grade_letter(grade)
    pass
