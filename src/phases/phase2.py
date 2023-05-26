"""
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503

File: phase2.py
"""

import pandas as pd

from src.constructors.Assignment import Assignment as Asgmt
from src.constructors.AssignmentType import AssignmentType as AsgmtType
from src.constructors.Course import Course
from src.constructors.Student import Student
from src.lib import special_cases as sc


def drop_grades(student: Student, path_to_excel_file: str):
    df = pd.read_excel(path_to_excel_file, sheet_name="drop_grades")
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
    pass


def overwrite_final_exam_grade(student: Student, path_to_excel_file: str):
    df = pd.read_excel(path_to_excel_file, sheet_name="overwrite_final_exam")
    for index, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course: Course = student.get_course(f"{term}.{course_code}.{section}")
        asgmt_1: AsgmtType = course.get_assignment_type("Final Exam")
        final_exam: Asgmt = asgmt_1.get_assignments()[0]
        exams: AsgmtType = course.get_assignment_type("Exams")
        min_exam_grade: Asgmt = exams.get_min_grade()[1]
        if final_exam.compute_grade() > min_exam_grade.compute_grade():
            min_exam_grade.set_grade(final_exam.get_grade())
            pass
        pass
    pass


def modify_data(student: Student, path_to_excel_file: str):
    drop_grades(student, path_to_excel_file)
    overwrite_final_exam_grade(student, path_to_excel_file)
    pass
