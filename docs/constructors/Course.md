# `Course.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub: https://github.com/rkp1503

## File Details
- File: `Course.py`

## Description
The `Course` class represents a specific course in an educational setting. It provides functionality to store and manage information about the course, such as student status, term, course code, section, name, credit, professor, assignment types, grading scale, and grades.

## Methods Documentation

- `__init__(self, student_status: str, term: int, course_code: str, section: str, name: str, credit: int, professor: str)`
  - Description: The constructor method initializes a new instance of the `Course` class.
  - Parameters:
    - `student_status` (str): The student status in relation to the course.
    - `term` (int): The term or semester of the course.
    - `course_code` (str): The code or identifier of the course.
    - `section` (str): The section of the course.
    - `name` (str): The name or title of the course.
    - `credit` (int): The credit value of the course.
    - `professor` (str): The professor or instructor of the course.

- `get_student_status(self) -> str`
  - Description: Returns the student status in relation to the course.
  - Returns:
    - `str`: The student status.

- `get_term(self) -> int`
  - Description: Returns the term or semester of the course.
  - Returns:
    - `int`: The term or semester.

- `get_course_code(self) -> str`
  - Description: Returns the code or identifier of the course.
  - Returns:
    - `str`: The course code.

- `get_section(self) -> str`
  - Description: Returns the section of the course.
  - Returns:
    - `str`: The section.

- `get_course_id(self) -> str`
  - Description: Returns the unique identifier of the course.
  - Returns:
    - `str`: The course ID in the format "{term}.{course_code}.{section}".

- `get_name(self) -> str`
  - Description: Returns the name or title of the course.
  - Returns:
    - `str`: The course name.

- `get_credit(self) -> int`
  - Description: Returns the credit value of the course.
  - Returns:
    - `int`: The credit value.

- `get_professor(self) -> str`
  - Description: Returns the professor or instructor of the course.
  - Returns:
    - `str`: The professor or instructor.

- `get_assignment_types(self) -> dict[str, AssignmentType]`
  - Description: Returns the dictionary of assignment types associated with the course.
  - Returns:
    - `dict[str, AssignmentType]`: The dictionary of assignment types, where the keys are the assignment type IDs and the values are instances of the `AssignmentType` class.

- `get_assignment_type(self, asgmt_id: str) -> AssignmentType`
  - Description: Returns the assignment type with the given assignment type ID.
  - Parameters:
    - `asgmt_id` (str): The ID of the assignment type.
  - Returns:
    - `AssignmentType`: An instance of the `AssignmentType` class representing the assignment type.

- `add_assignment_type(self, asgmt_id: str, asgmt_type: AssignmentType)`
  - Description: Adds a new assignment type to the course.
  - Parameters:
    - `asgmt_id` (str): The ID of the assignment type.
    - `asgmt_type` (AssignmentType): An instance of the `AssignmentType` class representing the assignment type to add.

- `get_grading_scale(self) -> dict[float, str]`
  - Description: Returns the grading scale associated with the course.
  - Returns:
    - `dict[float, str]`: The grading scale, where the keys are the grade cutoffs and the values are the corresponding grade letters.

- `set_grading_scale(self, grading_scale: dict[float, str])`
  - Description: Sets the grading scale for the course.
  - Parameters:
    - `grading_scale` (dict[float, str]): The grading scale to set, where the keys are the grade cutoffs and the values are the corresponding grade letters.

- `get_extra_credit(self) -> float`
  - Description: Returns the amount of extra credit associated with the course.
  - Returns:
    - `float`: The amount of extra credit.

- `set_extra_credit(self, extra_credit: float)`
  - Description: Sets the amount of extra credit for the course.
  - Parameters:
    - `extra_credit` (float): The amount of extra credit to set.

- `get_raw_grade(self)`
  - Description: Returns the raw grade of the course.
  - Returns:
    - `float`: The raw grade.

- `compute_raw_grade(self)`
  - Description: Computes the raw grade of the course based on the grades of the associated assignment types.

- `set_raw_grade(self, grade: float)`
  - Description: Sets the raw grade of the course.
  - Parameters:
    - `grade` (float): The raw grade to set.

- `get_raw_grade_letter(self)`
  - Description: Returns the letter grade corresponding to the raw grade of the course.
  - Returns:
    - `str`: The letter grade.

- `set_raw_grade_letter(self, grade: str)`
  - Description: Sets the letter grade corresponding to the raw grade of the course.
  - Parameters:
    - `grade` (str): The letter grade to set.

- `computing_raw_grade_letter(self)`
  - Description: Computes the letter grade corresponding to the raw grade of the course based on the grading scale.

- `get_final_grade_letter(self)`
  - Description: Returns the final letter grade of the course.
  - Returns:
    - `str`: The final letter grade.

- `set_final_grade_letter(self, final_grade_letter: str)`
  - Description: Sets the final letter grade of the course.
  - Parameters:
    - `final_grade_letter` (str): The final letter grade to set.

- `get_earned_credits(self) -> int`
  - Description: Returns the number of earned credits for the course.
  - Returns:
    - `int`: The number of earned credits.

- `set_earned_credits(self, earned_credits: int)`
  - Description: Sets the number of earned credits for the course.
  - Parameters:
    - `earned_credits` (int): The number of earned credits to set.

- `get_points(self) -> float`
  - Description: Returns the number of points for the course.
  - Returns:
    - `float`: The number of points.

- `set_points(self, points: float)`
  - Description: Sets the number of points for the course.
  - Parameters:
    - `points` (float): The number of points to set.
