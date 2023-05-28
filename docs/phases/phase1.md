# `phase1.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub: https://github.com/rkp1503

## File Details
- File: `phase1.py`

## Description
The `phase1.py` file contains functions to parse and add student data from an Excel file. It utilizes the pandas library to read data from specific sheets in the Excel file and updates a `Student` object with the extracted information. This file provides functions for adding basic student information, courses, assignment types, assignments, grading scales, and extra credit.

## Function Documentation

- `add_basic_info(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "basic_info" sheet from the Excel file and updates the `student` object with the student's name, degrees, and minors.
    - Parameters:
        - `student` (Student): The student object to update with basic information.
        - `path_to_excel_file` (str): The path to the Excel file containing the basic info.

- `add_courses(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "courses" sheet from the Excel file and adds course information to the `student` object. It creates `Course` and `Term` objects and associates them with the student.
    - Parameters:
        - `student` (Student): The student object to update with course information.
        - `path_to_excel_file` (str): The path to the Excel file containing the course data.

- `add_assignment_types(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "assignments" sheet from the Excel file and adds assignment types to each course. It creates `AssignmentType` objects and associates them with the corresponding `Course` objects.
    - Parameters:
        - `student` (Student): The student object to update with assignment types.
        - `path_to_excel_file` (str): The path to the Excel file containing the assignment type data.

- `add_assignments(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "grades" sheet from the Excel file and adds assignments to the assignment types in each course. It creates `Assignment` objects and associates them with the corresponding `AssignmentType` objects.
    - Parameters:
        - `student` (Student): The student object to update with assignments.
        - `path_to_excel_file` (str): The path to the Excel file containing the assignment data.

- `add_grading_scales(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "grading_scales" sheet from the Excel file and adds grading scales to each course. It creates grading scale dictionaries and associates them with the corresponding `Course` objects.
    - Parameters:
        - `student` (Student): The student object to update with grading scales.
        - `path_to_excel_file` (str): The path to the Excel file containing the grading scale data.

- `add_extra_credit(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "extra_credit" sheet from the Excel file and adds extra credit information to each course. It updates the extra credit values of the corresponding `Course` objects.
    - Parameters:
        - `student` (Student): The student object to update with extra credit.
        - `path_to_excel_file` (str): The path to the Excel file containing the extra credit data.

- `add_data(student: Student, path_to_excel_file: str)`
    - Description: This function calls all the above functions in the appropriate order to add all the data for the student from the Excel file.
    - Parameters:
        - `student` (Student): The student object to update with data.
        - `path_to_excel_file` (str): The path to the Excel file containing the student data.

## Requirements

- pandas library: This file requires the pandas library to read data from the Excel file.

## Limitations

- This file assumes a specific structure and format for the Excel file. Any deviations may lead to errors or incorrect results.
- This file does not handle complex data validations or error handling. It assumes the data in the Excel file is correct and consistent.
