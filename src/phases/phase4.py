"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This file contains functions related to printing various types of
data for a student. The functions are used to generate and print transcript
data, GPA data, and cumulative GPA data for a given student. The data is
printed in formatted tables and saved in separate output files.
"""

from src.constructors.Student import Student
from src.lib import pretty_print


def get_transcript_data_to_print(student: Student) -> list[list[str]]:
    """
    This function takes a `Student` object as input and generates a nested
    list of transcript data to print. The transcript data includes information
    such as student status, course ID, course name, credits, final grade,
    earned credits, and points. The data is returned as a nested list of
    strings.
    :param student: The `Student` object for which the transcript data is
    generated.
    :return: A nested list of transcript data to print.
    """
    data_to_print: list[list[str]] = []
    for course in student.get_courses().values():
        credit: str = ""
        if course.get_credit() >= 0:
            credit: str = str(course.get_credit())
            pass
        final_grade: str = ""
        if course.get_final_grade_letter() != "n/a":
            final_grade: str = str(course.get_final_grade_letter())
            pass
        earned_credits: str = ""
        if course.get_earned_credits() >= 0:
            earned_credits: str = str(course.get_earned_credits())
            pass
        points: str = ""
        if course.get_points() >= 0:
            points: str = pretty_print.fmt_num_to_str(course.get_points(), 3)
            pass
        data_to_print.append([
            course.get_student_status(),
            course.get_course_id(),
            course.get_name(),
            credit,
            # str(course.get_raw_grade()),
            # course.get_raw_grade_letter(),
            final_grade,
            earned_credits,
            points
        ])
        pass
    return data_to_print


def print_transcript(student: Student) -> None:
    """
    This function takes a `Student` object as input and prints the transcript
    data for the student. The function uses the `get_transcript_data_to_print`
    function to obtain the transcript data and then formats and prints the
    data in a table format. The transcript data is saved in a file named
    "transcript.txt" in the "output" directory.
    :param student: The `Student` object for which the transcript data is
    printed.
    :return: None
    """
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
    return None


def get_gpa_data_to_print(student: Student) -> list[list[str]]:
    """
    This function takes a `Student` object as input and generates a nested
    list of GPA data to print. The GPA data includes information such as
    student status, term, GPA, and cumulative GPA. The data is returned as a
    nested list of strings.
    :param student: The `Student` object for which the GPA data is generated.
    :return: A nested list of GPA data to print.
    """
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


def print_gpas(student: Student) -> None:
    """
    This function takes a `Student` object as input and prints the GPA data
    for the student. The function uses the `get_gpa_data_to_print` function to
    obtain the GPA data and then formats and prints the data in a table
    format. The GPA data is saved in a file named "GPAs.txt" in the "output"
    directory.
    :param student: The `Student` object for which the GPA data is printed.
    :return: None
    """
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
    return None


def get_term_gpa_data_to_print(student: Student) -> list[list[str]]:
    """
    This function takes a `Student` object as input and generates a nested
    list of term GPA data to print. The term GPA data includes information
    such as student status, term, GPA, attempted credits, earned credits, GPA
    units, and points. The data is returned as a nested list of strings.
    :param student: The `Student` object for which the term GPA data is
    generated.
    :return: A nested list of term GPA data to print.
    """
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


def print_term_gpas(student: Student) -> None:
    """
    This function takes a `Student` object as input and prints the term GPA
    data for the student. The function uses the `get_term_gpa_data_to_print`
    function to obtain the term GPA data and then formats and prints the data
    in a table format. The term GPA data is saved in a file named
    "Term GPAs.txt" in the "output" directory.
    :param student: The `Student` object for which the term GPA data is
    printed.
    :return: None
    """
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
    return None


def get_cumulative_gpa_data_to_print(student: Student) -> list[list[str]]:
    """
    This function takes a `Student` object as input and generates a nested
    list of cumulative GPA data to print. The cumulative GPA data includes
    information such as student status, term, cumulative GPA, cumulative
    attempted credits, cumulative earned credits, cumulative GPA units, and
    cumulative points. The data is returned as a nested list of strings.
    :param student: The `Student` object for which the cumulative GPA data is
    generated.
    :return: A nested list of cumulative GPA data to print.
    """
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


def print_cumulative_gpas(student: Student) -> None:
    """
    This function takes a `Student` object as input and prints the cumulative
    GPA data for the student. The function uses the
    `get_cumulative_gpa_data_to_print` function to obtain the cumulative GPA
    data and then formats and prints the data in a table format.
    The cumulative GPA data is saved in a file named "Cumulative GPAs.txt" in
    the "output" directory.
    :param student: The `Student` object for which the cumulative GPA data is
    printed.
    :return: None
    """
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
    return None


def get_detailed_gpa_data_to_print(student: Student) -> list[list[str]]:
    """
    This function takes a `Student` object as input and generates a nested
    list of detailed GPA data to print. The detailed GPA data includes
    information such as student status, term, GPA, attempted credits, earned
    credits, GPA units, points, cumulative GPA, cumulative attempted credits,
    cumulative earned credits, cumulative GPA units, and cumulative points.
    The data is returned as a nested list of strings.
    :param student: The `Student` object for which the detailed GPA data is
    generated.
    :return: A nested list of detailed GPA data to print.
    """
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


def print_detailed_gpas(student: Student) -> None:
    """
    This function takes a `Student` object as input and prints the detailed
    GPA data for the student. The function uses the
    `get_detailed_gpa_data_to_print` function to obtain the detailed GPA data
    and then formats and prints the data in a table format. The detailed GPA
    data is saved in a file named "Detailed GPAs.txt" in the "output"
    directory.
    :param student: The `Student` object for which the detailed GPA data is
    printed.
    :return: None
    """
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
    return None


def print_data(student: Student) -> None:
    """
    This function takes a `Student` object as input and calls the other
    printing functions to print all the available data (transcript data, GPA
    data, term GPA data, cumulative GPA data, and detailed GPA data) for the
    student. The function generates separate output files for each type of
    data.
    :param student: The `Student` object for which the data is printed.
    :return: None
    """
    print_transcript(student)
    print_gpas(student)
    print_term_gpas(student)
    print_cumulative_gpas(student)
    print_detailed_gpas(student)
    return None
