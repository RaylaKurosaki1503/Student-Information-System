# `phase2.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub Username: RaylaKurosaki1503

## File Details
- File: `phase2.py`

## Description
The `phase2.py` script provides functions to modify and update data in a `Student` object based on information from an Excel file.

## Function Documentation

- `drop_grades(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "drop_grades" sheet from the specified Excel file and drops a certain number of grades for each assignment type in each course. The number of grades to be dropped is specified in the Excel sheet.
    - Parameters:
        - `student`: A `Student` object representing the student's data.
        - `path_to_excel_file`: The path to the Excel file containing the data.

- `overwrite_final_exam_grade(student: Student, path_to_excel_file: str)`
    - Description: This function reads the "overwrite_final_exam" sheet from the specified Excel file and overwrites the final exam grade with the minimum exam grade if the final exam grade is higher. This is done for each course.
    - Parameters:
        - `student`: A `Student` object representing the student's data.
        - `path_to_excel_file`: The path to the Excel file containing the data.

- `modify_data(student: Student, path_to_excel_file: str)`
    - Description: This function calls the `drop_grades()` and `overwrite_final_exam_grade()` functions to modify and update the student's data based on the information from the Excel file.
    - Parameters:
        - `student`: A `Student` object representing the student's data.
        - `path_to_excel_file`: The path to the Excel file containing the data.

## Limitations

- This file assumes a specific structure and format for the Excel file. Any deviations may lead to errors or incorrect results.
- This file does not handle complex data validations or error handling. It assumes the data in the Excel file is correct and consistent.
