"""
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503

File: phase1.py
"""

import pandas as pd

from src.constructors.Assignment import Assignment as Asgmt
from src.constructors.AssignmentType import AssignmentType as AsgmtType
from src.constructors.Course import Course
from src.constructors.Degree import Degree
from src.constructors.Minor import Minor
from src.constructors.Student import Student
from src.constructors.Term import Term


def add_basic_info(student: Student, path_to_excel_file: str):
    df = pd.read_excel(path_to_excel_file, sheet_name="basic_info")
    for index, row in df.iterrows():
        data_type: str = str(row["Type"])
        data: str = str(row["Data"])
        if data_type == "Name":
            student.set_name(data)
            pass
        elif data_type == "Degree":
            plan_code, name = data.split(": ")
            if plan_code in student.get_degrees():
                raise Exception(f"Duplicate degree: {plan_code}: {name}")
            new_degree: Degree = Degree(plan_code, name)
            student.add_degree(plan_code, new_degree)
            pass
        elif data_type == "Minor":
            plan_code, name = data.split(": ")
            if plan_code in student.get_minors():
                raise Exception(f"Duplicate minor: {plan_code}: {name}")
            new_minor: Minor = Minor(plan_code, name)
            student.add_minor(plan_code, new_minor)
            pass
        else:
            raise Exception(f"Fix the entry in Cell {row[0].coordinate}")
        pass
    pass


def add_courses(student: Student, path_to_excel_file: str):
    prev_term: int = -1
    df = pd.read_excel(path_to_excel_file, sheet_name="courses")
    for index, row in df.iterrows():
        student_status: str = row["Status"]
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        name: str = str(row["Name"])
        credit: int = int(row["Credit"])
        professor: str = str(row["Professor"])
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course_id: str = f"{term}.{course_code}.{section}"
        if term != prev_term:
            if term in student.get_terms():
                raise Exception(f"Duplicate term: {term}")
            student.add_term(term, Term(student_status, term))
            student.set_student_status(student_status)
            prev_term = term
            pass
        if course_id in student.get_courses():
            raise Exception(f"Duplicate course: {course_id}")
        new_course: Course = Course(student_status, term, course_code, section,
                                    name, credit, professor)
        student.add_course(term, course_id, new_course)
        pass
    pass


def add_assignment_types(student: Student, path_to_excel_file: str):
    df = pd.read_excel(path_to_excel_file, sheet_name="assignments")
    for index, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        asgmt_type = str(row["Type"])
        weight: float = float(row["Weight"])
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course_id: str = f"{term}.{course_code}.{section}"
        course: Course = student.get_course(course_id)
        if asgmt_type in course.get_assignment_types():
            raise Exception(f"Duplicate Assignment Type {asgmt_type} for "
                            f"{course_id}")
        new_asgmt_type: AsgmtType = AsgmtType(asgmt_type, weight)
        course.add_assignment_type(asgmt_type, new_asgmt_type)
        pass
    pass


def add_assignments(student: Student, path_to_excel_file: str):
    df = pd.read_excel(path_to_excel_file, sheet_name="grades")
    for index, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        assignment_type = str(row["Type"])
        notes: str = str(row["Notes"])
        grade: str = str(row["Raw Grade"])
        if not pd.isna(row["Raw Grade"]):
            if not pd.isna(row["Curved Grade"]):
                grade: str = str(row["Curved Grade"])
                pass
            if len(section) == 1:
                section: str = f"0{section}"
                pass
            course_id: str = f"{term}.{course_code}.{section}"
            course: Course = student.get_course(course_id)
            asgmt_type: AsgmtType = course.get_assignment_type(assignment_type)
            new_assignment: Asgmt = Asgmt(grade, notes)
            new_assignment_id: int = len(asgmt_type.get_assignments())
            asgmt_type.add_assignment(new_assignment_id, new_assignment)
            pass
        pass
    pass


def add_grading_scales(student: Student, path_to_excel_file: str):
    lst = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
    df = pd.read_excel(path_to_excel_file, sheet_name="grading_scales")
    for i, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        values = row[4:]
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course: Course = student.get_course(f"{term}.{course_code}.{section}")
        new_grading_scale: dict[float, str] = {
            float(k / 100): v
            for (k, v) in zip(values, lst) if not pd.isnull(k)
        }
        course.set_grading_scale(new_grading_scale)
        pass
    pass


def add_extra_credit(student: Student, path_to_excel_file: str):
    df = pd.read_excel(path_to_excel_file, sheet_name="extra_credit")
    for i, row in df.iterrows():
        term: int = int(row["Term"])
        course_code: str = str(row["Course"])
        section: str = str(row["Section"])
        extra_credit: int = int(row["Amount"])
        if len(section) == 1:
            section: str = f"0{section}"
            pass
        course: Course = student.get_course(f"{term}.{course_code}.{section}")
        course.set_extra_credit(extra_credit)
        pass
    pass


def add_data(student: Student, path_to_excel_file: str):
    add_basic_info(student, path_to_excel_file)
    add_courses(student, path_to_excel_file)
    add_assignment_types(student, path_to_excel_file)
    add_assignments(student, path_to_excel_file)
    add_grading_scales(student, path_to_excel_file)
    add_extra_credit(student, path_to_excel_file)
    pass
