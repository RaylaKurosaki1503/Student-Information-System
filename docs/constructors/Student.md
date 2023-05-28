# `Student.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub: https://github.com/rkp1503

## File Details
- File: `Student.py`

## Description
The `Student` class represents a student and provides functionality to store and manage information about the student, such as name, student status, degrees, minors, terms, courses, and GPAs.

## Methods Documentation

- `__init__(self)`
  - Description: The constructor method initializes a new instance of the `Student` class.

- `get_name(self) -> str`
  - Description: Returns the name of the student.
  - Returns:
    - `str`: The name of the student.

- `set_name(self, name: str)`
  - Description: Sets the name of the student.
  - Parameters:
    - `name` (str): The name to set.

- `get_student_status(self) -> str`
  - Description: Returns the student status.
  - Returns:
    - `str`: The student status.

- `set_student_status(self, student_status: str)`
  - Description: Sets the student status.
  - Parameters:
    - `student_status` (str): The student status to set.

- `get_degrees(self) -> dict[str, Degree]`
  - Description: Returns the dictionary of degrees associated with the student.
  - Returns:
    - `dict[str, Degree]`: The dictionary of degrees, where the keys are the plan codes and the values are instances of the `Degree` class.

- `get_degree(self, plan_code: str) -> Degree`
  - Description: Returns the degree with the specified plan code.
  - Parameters:
    - `plan_code` (str): The plan code of the degree.
  - Returns:
    - `Degree`: The instance of the `Degree` class with the specified plan code.

- `add_degree(self, plan_code: str, degree: Degree)`
  - Description: Adds a new degree to the student.
  - Parameters:
    - `plan_code` (str): The plan code of the degree.
    - `degree` (Degree): An instance of the `Degree` class representing the degree to add.

- `get_minors(self) -> dict[str, Minor]`
  - Description: Returns the dictionary of minors associated with the student.
  - Returns:
    - `dict[str, Minor]`: The dictionary of minors, where the keys are the plan codes and the values are instances of the `Minor` class.

- `get_minor(self, plan_code: str) -> Minor`
  - Description: Returns the minor with the specified plan code.
  - Parameters:
    - `plan_code` (str): The plan code of the minor.
  - Returns:
    - `Minor`: The instance of the `Minor` class with the specified plan code.

- `add_minor(self, plan_code: str, minor: Minor)`
  - Description: Adds a new minor to the student.
  - Parameters:
    - `plan_code` (str): The plan code of the minor.
    - `minor` (Minor): An instance of the `Minor` class representing the minor to add.

- `get_terms(self) -> dict[int, Term]`
  - Description: Returns the dictionary of terms associated with the student.
  - Returns:
    - `dict[int, Term]`: The dictionary of terms, where the keys are the term numbers and the values are instances of the `Term` class.

- `get_term(self, term_num: int) -> Term`
  - Description: Returns the term with the specified term number.
  - Parameters:
    - `term_num` (int): The term number.
  - Returns:
   

 - `Term`: The instance of the `Term` class with the specified term number.

- `add_term(self, term_num: int, term: Term)`
  - Description: Adds a new term to the student.
  - Parameters:
    - `term_num` (int): The term number.
    - `term` (Term): An instance of the `Term` class representing the term to add.

- `get_courses(self) -> dict[str, Course]`
  - Description: Returns the dictionary of courses associated with the student.
  - Returns:
    - `dict[str, Course]`: The dictionary of courses, where the keys are the course IDs and the values are instances of the `Course` class.

- `get_course(self, course_id: str) -> Course`
  - Description: Returns the course with the specified course ID.
  - Parameters:
    - `course_id` (str): The ID of the course.
  - Returns:
    - `Course`: The instance of the `Course` class with the specified course ID.

- `add_course(self, term: int, course_id: str, course: Course)`
  - Description: Adds a new course to the student for the specified term.
  - Parameters:
    - `term` (int): The term number.
    - `course_id` (str): The ID of the course.
    - `course` (Course): An instance of the `Course` class representing the course to add.

- `print_basic_info(self, file)`
  - Description: Prints basic information about the student to the specified file.
  - Parameters:
    - `file`: The file to write the information to.

- `get_gpas(self) -> dict[str, float]`
  - Description: Returns the dictionary of GPAs associated with the student.
  - Returns:
    - `dict[str, float]`: The dictionary of GPAs, where the keys are the student statuses and the values are the corresponding GPAs.

- `set_gpa(self, student_status: str, gpa: float)`
  - Description: Sets the GPA for the specified student status.
  - Parameters:
    - `student_status` (str): The student status.
    - `gpa` (float): The GPA to set.
