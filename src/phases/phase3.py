"""
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503

File: phase3.py
"""

import pandas as pd

from src.constructors import Assignment as Asgmt
from src.constructors.AssignmentType import AssignmentType as AsgmtType
from src.constructors.Course import Course
from src.constructors import Student
from src.lib import special_cases as sc


def compute_course_grades(student: Student):
    special_calc_lst = [
        "2175.CSCI-141.02", "2181.CSCI-142.01", "2185.ENGL-314.01",
        "2185.MATH-399.01", "2185.PHYS-212.06", "2188.CSCI-243.01",
        "2195.PHYS-283.01"
    ]
    for course in student.get_courses().values():
        if len(course.get_assignment_types()) == 1:
            asgmt: AsgmtType = course.get_assignment_type("Final Grade")
            if len(asgmt.get_assignments()) == 1:
                final_grade: Asgmt = asgmt.get_assignments()[0]
                if "/" in final_grade.get_grade():
                    final_grade_num: float = asgmt.compute_grade()
                    course.set_raw_grade(final_grade_num)
                    pass
                else:
                    final_grade_letter: str = final_grade.get_grade()
                    course.set_raw_grade_letter(final_grade_letter)
                    course.set_final_grade_letter(final_grade_letter)
                    pass
                pass
            pass
        elif course.get_course_id() in special_calc_lst:
            sc.compute_course_grade_helper(course)
            pass
        else:
            course.compute_raw_grade()
            pass
        pass
    pass


def setting_raw_letter_grades(student: Student):
    lst: list[str] = ["2185.MATH-399.01"]
    for course in student.get_courses().values():
        if course.get_course_id() in lst:
            sc.computing_raw_letter_grade_2185_math_399_01(course)
            pass
        else:
            course.computing_raw_grade_letter()
            pass
        pass
    pass


def overwrite_final_grade(student: Student, path_to_excel_file: str):
    df = pd.read_excel(path_to_excel_file, sheet_name="overwrite_final_grade")
    for i, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        final_grade: str = str(row["Final Grade"])
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course: Course = student.get_course(f"{term}.{course_code}.{section}")
        course.set_final_grade_letter(final_grade)
        pass
    pass


def compute_course_credit_and_points(student: Student):
    for course in student.get_courses().values():
        credit: int = course.get_credit()
        letter: str = course.get_final_grade_letter()
        no_credit_lst: list[str] = ["F", "NE"]
        if letter != "n/a":
            if (credit == 0) or (letter in no_credit_lst):
                course.set_earned_credits(0)
                course.set_points(0)
                pass
            else:
                course.set_earned_credits(credit)
                no_points_lst: list[str] = ["SE", "PE", "UE", "R"]
                if letter in no_points_lst:
                    course.set_points(0)
                    pass
                else:
                    gpa_points: dict[str, float] = {
                        "A": 4.000, "A-": 3.667, "B+": 3.333, "B": 3.000,
                        "B-": 2.667, "C+": 2.333, "C": 2.000, "C-": 1.667,
                        "D": 1.000
                    }
                    earned_credit: int = course.get_earned_credits()
                    course.set_points(earned_credit * gpa_points[letter])
                    pass
                pass
            pass
        pass
    pass


def compute_term_gpas(student: Student):
    for term in student.get_terms().values():
        term.compute_gpa()
        pass
    pass


def compute_cumulative_gpas(student: Student):
    student_status: str = "Undergraduate"
    cumulative_attempted_credits: int = 0
    cumulative_earned_credits: int = 0
    cumulative_gpa_units: int = 0
    cumulative_points: float = 0
    for term in student.get_terms().values():
        curr_student_status: str = term.get_student_status()
        if curr_student_status != student_status:
            gpa: float = cumulative_points / cumulative_gpa_units
            student.set_gpa(student_status, gpa)
            student_status: str = curr_student_status
            cumulative_attempted_credits: int = 0
            cumulative_earned_credits: int = 0
            cumulative_gpa_units: int = 0
            cumulative_points: float = 0
            pass
        cumulative_attempted_credits += term.get_attempted_credits()
        term.set_cumulative_attempted_credits(cumulative_attempted_credits)
        cumulative_earned_credits += term.get_earned_credits()
        term.set_cumulative_earned_credits(cumulative_earned_credits)
        cumulative_gpa_units += term.get_gpa_units()
        term.set_cumulative_gpa_units(cumulative_gpa_units)
        cumulative_points += term.get_points()
        term.set_cumulative_points(cumulative_points)
        if cumulative_gpa_units > 0:
            term.set_cumulative_gpa(cumulative_points / cumulative_gpa_units)
            pass
        pass
    gpa: float = cumulative_points / cumulative_gpa_units
    student.set_gpa(student_status, gpa)
    pass


def perform_computations(student: Student, path_to_excel_file: str):
    compute_course_grades(student)
    setting_raw_letter_grades(student)
    overwrite_final_grade(student, path_to_excel_file)
    compute_course_credit_and_points(student)
    compute_term_gpas(student)
    compute_cumulative_gpas(student)
    pass
