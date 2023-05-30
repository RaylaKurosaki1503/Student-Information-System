"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Terminal cmd: python src/Student-Information-System.py "C:/.../excel_file.xlsx"

Description: The `Student-Information-System.py` script is designed to process
an Excel file containing student data and perform various operations on the
data. The script utilizes modules from the `constructors` and `phases`
directories to create a `Student` object and execute different phases of data
processing.
"""

import os
import sys

# 3rd party libraries to import
# pip install openpyxl, pandas

from constructors.Student import Student
from phases import phase1
from phases import phase2
from phases import phase3
from phases import phase4


def get_path_to_excel_file(path: str) -> str:
    """
    This function verifies the validity of a file path and ensures that the
    specified path exists and points to an Excel file (.xlsx). If the path
    does not exist or the file is not in the correct format, an exception is
    raised. If the path is valid, it is returned.
    :param path: The file path to be validated.
    :return: The validated file path.
    """
    if not (os.path.exists(path)):
        raise Exception(f"The path '{path}' does not exist.")
    if not path.endswith(".xlsx"):
        file: str = path.split('\\')[-1]
        raise Exception(f"The file '{file}' is not an Excel file.")
    return path


def check_for_output_dir() -> None:
    """
    This function checks if an output directory exists in the current working
    directory. If the directory does not exist, it creates a new directory
    named "output" to store the output files.
    :return: None
    """
    path_to_output: str = os.path.join(os.getcwd(), "output")
    if not os.path.exists(path_to_output):
        os.makedirs(path_to_output)
        pass
    return None


if __name__ == '__main__':
    # -------------------------------------------------------------------------
    # Creates an instance of the `Student` class.
    # -------------------------------------------------------------------------
    student: Student = Student()
    # -------------------------------------------------------------------------
    # Retrieves the file path from the command-line arguments provided when
    # executing the script and validate the file path.
    # -------------------------------------------------------------------------
    path_to_excel_file: str = get_path_to_excel_file(sys.argv[1])
    # -------------------------------------------------------------------------
    # Ensure the existence of the output directory.
    # -------------------------------------------------------------------------
    check_for_output_dir()
    # -------------------------------------------------------------------------
    # Adds data to the `Student` object.
    # -------------------------------------------------------------------------
    phase1.add_data(student, path_to_excel_file)
    # -------------------------------------------------------------------------
    # Modifies data in the `Student` object.
    # -------------------------------------------------------------------------
    phase2.modify_data(student, path_to_excel_file)
    # -------------------------------------------------------------------------
    # Performs computations on the data in the `Student` object.
    # -------------------------------------------------------------------------
    phase3.perform_computations(student, path_to_excel_file)
    # -------------------------------------------------------------------------
    # Prints the data of the `Student` object.
    # -------------------------------------------------------------------------
    phase4.print_data(student)
    pass
