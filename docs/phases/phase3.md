# `phase3.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub Username: RaylaKurosaki1503

## File Details
- File: `phase3.py`

## Description
The `phase3.py` script provides functions to perform various computations and modifications on a `Student` object based on information from an Excel file.

## Function Documentation

- `compute_course_grades(student: Student)`
    - Description: This function computes the course grades for each course in the `Student` object. It handles special cases where the course has only one assignment type, and the final grade is either a numerical value or a letter grade.
    - Parameters:
        - `student`: A `Student` object representing the student's data.

- `setting_raw_letter_grades(student: Student)`
    - Description: This function sets the raw letter grades for each course in the `Student` object. It handles special cases where specific courses require custom calculations for raw letter grades.
    - Parameters:
        - `student`: A `Student` object representing the student's data.

- `overwrite_final_grade(student: Student, path_to_excel_file: str)`
    - Description: This function overwrites the final grade for each course in the `Student` object based on the information from the "overwrite_final_grade" sheet in the specified Excel file.
    - Parameters:
        - `student`: A `Student` object representing the student's data.
        - `path_to_excel_file`: The path to the Excel file containing the data.

- `compute_course_credit_and_points(student: Student)`
    - Description: This function computes the course credits and points for each course in the `Student` object. It calculates the earned credits and points based on the final grade letter.
    - Parameters:
        - `student`: A `Student` object representing the student's data.

- `compute_term_gpas(student: Student)`
    - Description: This function computes the term GPAs for each term in the `Student` object. It calculates the GPA based on the earned credits and points for each term.
    - Parameters:
        - `student`: A `Student` object representing the student's data.

- `compute_cumulative_gpas(student: Student)`
    - Description: This function computes the cumulative GPAs for each student status in the `Student` object. It calculates the cumulative GPA based on the cumulative earned credits and points for each student status.
    - Parameters:
        - `student`: A `Student` object representing the student's data.

- `perform_computations(student: Student, path_to_excel_file: str)`
    - Description: This function performs all the necessary computations and modifications on the `Student` object based on the information from the Excel file. It calls the above functions in the appropriate order.
    - Parameters:
        - `student`: A `Student` object representing the student's data.
        - `path_to_excel_file`: The path to the Excel file containing the data.

## Limitations

- This file assumes a specific structure and format for the Excel file. Any deviations may lead to errors or incorrect results.
- This file does not handle complex data validations or error handling. It assumes the data in the Excel file is correct and consistent.
