"""
Author: Rayla Kurosaki

GitHub Username: RaylaKurosaki1503

File: phase4.py
"""

from src.constructors.Student import Student
from src.lib import pretty_print


def get_transcript_data_to_print(student: Student) -> list[list[str]]:
    data_to_print: list[list[str]] = []
    for course in student.get_courses().values():
        data_to_print.append([
            course.get_student_status(),
            course.get_course_id(),
            course.get_name(),
            str(course.get_credit()),
            # str(course.get_raw_grade()),
            # course.get_raw_grade_letter(),
            course.get_final_grade_letter(),
            str(course.get_earned_credits()),
            pretty_print.fmt_num_to_str(course.get_points(), 3)
        ])
        pass
    return data_to_print


def print_transcript(student: Student):
    header: list[str] = [
        "Status", "Course ID", "Description", "Credits",
        # "Raw Grade", "Raw Grade Letter",
        "Final Grade", "Earned Credits", "Points"
    ]
    data: list[list[str]] = get_transcript_data_to_print(student)
    column_widths: list[int] = pretty_print.get_column_widths(header, data)
    with open("output/transcript.txt", "w") as file:
        student.print_basic_info(file)
        term: int = -1
        pretty_print.print_boundary(file, column_widths)
        pretty_print.print_row(file, header, column_widths)
        for row in data:
            curr_term: int = int(row[1][0:4])
            if curr_term != term:
                pretty_print.print_separator(file, column_widths)
                term = curr_term
                pass
            pretty_print.print_row(file, row, column_widths)
            pass
        pretty_print.print_boundary(file, column_widths)
        pass
    pass


def get_gpa_data_to_print(student: Student) -> list[list[str]]:
    data_to_print: list[list[str]] = []
    for term in student.get_terms().values():
        term_num: str = str(term.get_term_num())[1:]
        if term_num.endswith("1"):
            season: str = "Fall"
            pass
        elif term_num.endswith("5"):
            season: str = "Spring"
            pass
        else:
            season: str = "Summer"
            pass
        year: int = int(term_num[:-1])
        data_to_print.append([
            term.get_student_status(),
            f"20{year}-20{year + 1} {season}",
            pretty_print.fmt_num_to_str(term.get_gpa(), 3),
            pretty_print.fmt_num_to_str(term.get_cumulative_gpa(), 3),
        ])
        pass
    return data_to_print


def print_gpas(student: Student):
    header: list[str] = ["Status", "Term", "GPA", "Cumulative GPA"]
    data: list[list[str]] = get_gpa_data_to_print(student)
    student_status = ""
    column_widths: list[int] = pretty_print.get_column_widths(header, data)
    with open("output/GPAs.txt", "w") as file:
        student.print_basic_info(file)
        pretty_print.print_boundary(file, column_widths)
        pretty_print.print_row(file, header, column_widths)
        for row in data:
            curr_student_status: str = row[0]
            if curr_student_status != student_status:
                student_status = curr_student_status
                pretty_print.print_separator(file, column_widths)
                pass
            pretty_print.print_row(file, row, column_widths)
            pass
        pretty_print.print_boundary(file, column_widths)
        pass
    pass


def get_term_gpa_data_to_print(student: Student) -> list[list[str]]:
    data_to_print: list[list[str]] = []
    for term in student.get_terms().values():
        term_num: str = str(term.get_term_num())[1:]
        if term_num.endswith("1"):
            season: str = "Fall"
            pass
        elif term_num.endswith("5"):
            season: str = "Spring"
            pass
        else:
            season: str = "Summer"
            pass
        year: int = int(term_num[:-1])
        data_to_print.append([
            term.get_student_status(),
            f"20{year}-20{year + 1} {season}",
            pretty_print.fmt_num_to_str(term.get_gpa(), 3),
            str(term.get_attempted_credits()),
            str(term.get_earned_credits()),
            str(term.get_gpa_units()),
            pretty_print.fmt_num_to_str(term.get_points(), 3),
        ])
        pass
    return data_to_print


def print_term_gpas(student: Student):
    header: list[str] = [
        "Status", "Term", "GPA", "Attempted", "Earned", "GPA Units", "Points",
    ]
    data: list[list[str]] = get_term_gpa_data_to_print(student)
    student_status = ""
    column_widths: list[int] = pretty_print.get_column_widths(header, data)
    with open("output/Term GPAs.txt", "w") as file:
        student.print_basic_info(file)
        pretty_print.print_boundary(file, column_widths)
        pretty_print.print_row(file, header, column_widths)
        for row in data:
            curr_student_status: str = row[0]
            if curr_student_status != student_status:
                student_status = curr_student_status
                pretty_print.print_separator(file, column_widths)
                pass
            pretty_print.print_row(file, row, column_widths)
            pass
        pretty_print.print_boundary(file, column_widths)
        pass
    pass


def get_cumulative_gpa_data_to_print(student: Student) -> list[list[str]]:
    data_to_print: list[list[str]] = []
    for term in student.get_terms().values():
        term_num: str = str(term.get_term_num())[1:]
        if term_num.endswith("1"):
            season: str = "Fall"
            pass
        elif term_num.endswith("5"):
            season: str = "Spring"
            pass
        else:
            season: str = "Summer"
            pass
        year: int = int(term_num[:-1])
        data_to_print.append([
            term.get_student_status(),
            f"20{year}-20{year + 1} {season}",
            pretty_print.fmt_num_to_str(term.get_cumulative_gpa(), 3),
            str(term.get_cumulative_attempted_credits()),
            str(term.get_cumulative_earned_credits()),
            str(term.get_cumulative_gpa_units()),
            pretty_print.fmt_num_to_str(term.get_cumulative_points(), 3),
        ])
        pass
    return data_to_print


def print_cumulative_gpas(student: Student):
    header: list[str] = [
        "Status", "Term", "Cumulative GPA", "Cumulative Attempted",
        "Cumulative Earned", "Cumulative GPA Units", "Cumulative Points"
    ]
    data: list[list[str]] = get_cumulative_gpa_data_to_print(student)
    student_status = ""
    column_widths: list[int] = pretty_print.get_column_widths(header, data)
    with open("output/Cumulative GPAs.txt", "w") as file:
        student.print_basic_info(file)
        pretty_print.print_boundary(file, column_widths)
        pretty_print.print_row(file, header, column_widths)
        for row in data:
            curr_student_status: str = row[0]
            if curr_student_status != student_status:
                student_status = curr_student_status
                pretty_print.print_separator(file, column_widths)
                pass
            pretty_print.print_row(file, row, column_widths)
            pass
        pretty_print.print_boundary(file, column_widths)
        pass
    pass


def get_detailed_gpa_data_to_print(student: Student) -> list[list[str]]:
    data_to_print: list[list[str]] = []
    for term in student.get_terms().values():
        term_num: str = str(term.get_term_num())[1:]
        if term_num.endswith("1"):
            season: str = "Fall"
            pass
        elif term_num.endswith("5"):
            season: str = "Spring"
            pass
        else:
            season: str = "Summer"
            pass
        year: int = int(term_num[:-1])
        data_to_print.append([
            term.get_student_status(),
            f"20{year}-20{year + 1} {season}",
            pretty_print.fmt_num_to_str(term.get_gpa(), 3),
            str(term.get_attempted_credits()),
            str(term.get_earned_credits()),
            str(term.get_gpa_units()),
            pretty_print.fmt_num_to_str(term.get_points(), 3),
            pretty_print.fmt_num_to_str(term.get_cumulative_gpa(), 3),
            str(term.get_cumulative_attempted_credits()),
            str(term.get_cumulative_earned_credits()),
            str(term.get_cumulative_gpa_units()),
            pretty_print.fmt_num_to_str(term.get_cumulative_points(), 3),
        ])
        pass
    return data_to_print


def print_detailed_gpas(student: Student):
    header: list[str] = [
        "Status", "Term", "GPA", "Attempted", "Earned", "GPA Units", "Points",
        "Cumulative GPA", "Cumulative Attempted", "Cumulative Earned",
        "Cumulative GPA Units", "Cumulative Points"
    ]
    data: list[list[str]] = get_detailed_gpa_data_to_print(student)
    student_status = ""
    column_widths: list[int] = pretty_print.get_column_widths(header, data)
    with open("output/Detailed GPAs.txt", "w") as file:
        student.print_basic_info(file)
        pretty_print.print_boundary(file, column_widths)
        pretty_print.print_row(file, header, column_widths)
        for row in data:
            curr_student_status: str = row[0]
            if curr_student_status != student_status:
                student_status = curr_student_status
                pretty_print.print_separator(file, column_widths)
                pass
            pretty_print.print_row(file, row, column_widths)
            pass
        pretty_print.print_boundary(file, column_widths)
        pass
    pass


def print_data(student: Student):
    print_transcript(student)
    print_gpas(student)
    print_term_gpas(student)
    print_cumulative_gpas(student)
    print_detailed_gpas(student)
    pass
