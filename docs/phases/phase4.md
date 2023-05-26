# `phase4.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub Username: RaylaKurosaki1503

## File Details
- File: `phase4.py`

## Description
The `phase4.py` file contains functions related to printing various types of data for a student. The functions are used to generate and print transcript data, GPA data, and cumulative GPA data for a given student. The data is printed in formatted tables and saved in separate output files.

## Function Documentation

- `get_transcript_data_to_print(student: Student) -> list[list[str]]`
    - Description: This function takes a `Student` object as input and generates a nested list of transcript data to print. The transcript data includes information such as student status, course ID, course name, credits, final grade, earned credits, and points. The data is returned as a nested list of strings.
    - Parameters:
        - `student` (Student): The `Student` object for which the transcript data is generated.
    - Returns:
        - `data_to_print` (list[list[str]]): A nested list of transcript data to print.

- `print_transcript(student: Student)`
    - Description: This function takes a `Student` object as input and prints the transcript data for the student. The function uses the `get_transcript_data_to_print` function to obtain the transcript data and then formats and prints the data in a table format. The transcript data is saved in a file named "transcript.txt" in the "output" directory.
    - Parameters:
        - `student` (Student): The `Student` object for which the transcript data is printed.

- `get_gpa_data_to_print(student: Student) -> list[list[str]]`
    - Description: This function takes a `Student` object as input and generates a nested list of GPA data to print. The GPA data includes information such as student status, term, GPA, and cumulative GPA. The data is returned as a nested list of strings.
    - Parameters:
        - `student` (Student): The `Student` object for which the GPA data is generated.
    - Returns:
        - `data_to_print` (list[list[str]]): A nested list of GPA data to print.

- `print_gpas(student: Student)`
    - Description: This function takes a `Student` object as input and prints the GPA data for the student. The function uses the `get_gpa_data_to_print` function to obtain the GPA data and then formats and prints the data in a table format. The GPA data is saved in a file named "GPAs.txt" in the "output" directory.
    - Parameters:
        - `student` (Student): The `Student` object for which the GPA data is printed.

- `get_term_gpa_data_to_print(student: Student) -> list[list[str]]`
    - Description: This function takes a `Student` object as input and generates a nested list of term GPA data to print. The term GPA data includes information such as student status, term, GPA, attempted credits, earned credits, GPA units, and points. The data is returned as a nested list of strings.
    - Parameters:
        - `student` (Student): The `Student` object for which the term GPA data is generated.
    - Returns:
        - `data_to_print` (list[list[str]]): A nested list of term GPA data to print.

- `print_term_gpas(student: Student)`
    - Description: This function takes a `Student` object as input and prints the term GPA data for the student. The function uses the `get_term_gpa_data_to_print` function to obtain the term GPA data and then formats and prints the data in a table format. The term GPA data is saved in a file named "Term GPAs.txt" in the "output" directory.
    - Parameters:
        - `student` (Student): The `Student` object for which the term GPA data is printed.

- `get_cumulative_gpa_data_to_print(student: Student) -> list[list[str]]`
    - Description: This function takes a `Student` object as input and generates a nested list of cumulative GPA data to print. The cumulative GPA data includes information such as student status, term, cumulative GPA, cumulative attempted credits, cumulative earned credits, cumulative GPA units, and cumulative points. The data is returned as a nested list of strings.
    - Parameters:
        - `student` (Student): The `Student` object for which the cumulative GPA data is generated.
    - Returns:
        - `data_to_print` (list[list[str]]): A nested list of cumulative GPA data to print.

- `print_cumulative_gpas(student: Student)`
    - Description: This function takes a `Student` object as input and prints the cumulative GPA data for the student. The function uses the `get_cumulative_gpa_data_to_print` function to obtain the cumulative GPA data and then formats and prints the data in a table format. The cumulative GPA data is saved in a file named "Cumulative GPAs.txt" in the "output" directory.
    - Parameters:
        - `student` (Student): The `Student` object for which the cumulative GPA data is printed.

- `get_detailed_gpa_data_to_print(student: Student) -> list[list[str]]`
    - Description: This function takes a `Student` object as input and generates a nested list of detailed GPA data to print. The detailed GPA data includes information such as student status, term, GPA, attempted credits, earned credits, GPA units, points, cumulative GPA, cumulative attempted credits, cumulative earned credits, cumulative GPA units, and cumulative points. The data is returned as a nested list of strings.
    - Parameters:
        - `student` (Student): The `Student` object for which the detailed GPA data is generated.
    - Returns:
        - `data_to_print` (list[list[str]]): A nested list of detailed GPA data to print.

- `print_detailed_gpas(student: Student)`
    - Description: This function takes a `Student` object as input and prints the detailed GPA data for the student. The function uses the `get_detailed_gpa_data_to_print` function to obtain the detailed GPA data and then formats and prints the data in a table format. The detailed GPA data is saved in a file named "Detailed GPAs.txt" in the "output" directory.
    - Parameters:
        - `student` (Student): The `Student` object for which the detailed GPA data is printed.

- `print_data(student: Student)`
    - Description: This function takes a `Student` object as input and calls the other printing functions to print all the available data (transcript data, GPA data, term GPA data, cumulative GPA data, and detailed GPA data) for the student. The function generates separate output files for each type of data.
    - Parameters:
        - `student` (Student): The `Student` object for which the data is printed.