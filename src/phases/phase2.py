"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This file provides functions to modify and update data in a
`Student` object based on information from an Excel file.
"""

import pandas as pd

from src.constructors.Assignment import Assignment as Asgmt
from src.constructors.AssignmentType import AssignmentType as AsgmtType
from src.constructors.Course import Course
from src.constructors.Student import Student
from src.lib import special_cases as sc


def drop_grades(student: Student, path: str) -> None:
    """
    This function reads the "drop_grades" sheet from the specified Excel file
    and drops a certain number of grades for each assignment type in each
    course. The number of grades to be dropped is specified in the Excel sheet.
    :param student: A `Student` object representing the student's data.
    :param path: The path to the Excel file containing the data.
    :return: None
    """
    df = pd.read_excel(path, sheet_name="drop_grades")
    for i, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        assignment_type: str = str(row["Type"])
        n: int = int(row["Amount"])
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course_id: str = f"{term}.{course_code}.{section}"
        course: Course = student.get_course(course_id)
        assignments: AsgmtType = course.get_assignment_type(assignment_type)
        if len(assignments.get_assignments()) > n:
            if course_id == "2191.PHYS-320.01":
                sc.drop_grades_2191_phys_320_01(assignments, n)
                pass
            else:
                assignments.drop_grades(n)
                pass
            pass
        pass
    return None


def overwrite_final_exam_grade(student: Student, path: str) -> None:
    """
    This function reads the "overwrite_final_exam" sheet from the specified
    Excel file and overwrites the final exam grade with the minimum exam grade
    if the final exam grade is higher. This is done for each course.
    :param student: A `Student` object representing the student's data.
    :param path: The path to the Excel file containing the data.
    :return: None
    """
    df = pd.read_excel(path, sheet_name="overwrite_final_exam")
    for index, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course: Course = student.get_course(f"{term}.{course_code}.{section}")
        asgmt_1: AsgmtType = course.get_assignment_type("Final Exam")
        if len(asgmt_1.get_assignments()) > 0:
            final_exam: Asgmt = asgmt_1.get_assignments()[0]
            exams: AsgmtType = course.get_assignment_type("Exams")
            min_exam_grade: Asgmt = exams.get_min_grade()[1]
            if final_exam.compute_grade() > min_exam_grade.compute_grade():
                min_exam_grade.set_grade(final_exam.get_grade())
                pass
            pass
        pass
    return None


def modify_data(student: Student, path: str) -> None:
    """
    This function calls the above functions to modify and update the student's
    data based on the information from the Excel file.
    :param student: A `Student` object representing the student's data.
    :param path: The path to the Excel file containing the data.
    :return: None
    """
    drop_grades(student, path)
    overwrite_final_exam_grade(student, path)
    return None
