# `Term.py` Documentation

## Author's Details

- Name: Rayla Kurosaki
- GitHub: [https://github.com/rkp1503](https://github.com/rkp1503)

## Description

The `Term` class represents an academic term or semester. It provides functionality to store and
manage information about the term, such as student status, term number, courses, attempted credits,
earned credits, GPA units, points, GPA, cumulative attempted credits, cumulative earned credits,
cumulative GPA units, cumulative points, and cumulative GPA.

## Methods Documentation
- `__init__(self, student_status: str, term_num: int)`
  - The constructor method initializes a new instance of the `Term` class.
  - Parameters:
    - `student_status` (str): The student status in relation to the term.
    - `term_num` (int): The term or semester number.

- `get_student_status(self) -> str`
  - Returns the student status in relation to the term.
  - Returns:
    - `str`: The student status.

- `get_term_num(self) -> int`
  - Returns the term or semester number.
  - Returns:
    - `int`: The term or semester number.

- `get_courses(self) -> dict[str, Course]`
  - Returns the dictionary of courses associated with the term.
  - Returns:
    - `dict[str, Course]`: The dictionary of courses, where the keys are the course IDs and the values are instances of the `Course` class.

- `add_course(self, course_id: str, course: Course) -> None`
  - Adds a new course to the term.
  - Parameters:
    - `course_id` (str): The ID of the course.
    - `course` (Course): An instance of the `Course` class representing the course to add.
  - Returns:
    - None

- `get_attempted_credits(self) -> int`
  - Returns the number of attempted credits for the term.
  - Returns:
    - `int`: The number of attempted credits.

- `set_attempted_credits(self, attempted_credits: int) -> None`
  - Sets the number of attempted credits for the term.
  - Parameters:
    - `attempted_credits` (int): The number of attempted credits to set.
  - Returns:
    - None

- `get_earned_credits(self) -> int`
  - Returns the number of earned credits for the term.
  - Returns:
    - `int`: The number of earned credits.

- `set_earned_credits(self, earned_credits: int) -> None`
  - Sets the number of earned credits for the term.
  - Parameters:
    - `earned_credits` (int): The number of earned credits to set.
  - Returns:
    - None

- `get_gpa_units(self) -> int`
  - Returns the GPA units for the term.
  - Returns:
    - `int`: The GPA units.

- `set_gpa_units(self, gpa_units: int) -> None`
  - Sets the GPA units for the term.
  - Parameters:
    - `gpa_units` (int): The GPA units to set.
  - Returns:
    - None

- `get_points(self) -> float`
  - Returns the number of points for the term.
  - Returns:
    - `float`: The number of points.

- `set_points(self, points: float) -> None`
  - Sets the number of points for the term.
  - Parameters:
    - `points` (float): The number of points to set.
  - Returns:
    - None

- `get_cumulative_attempted_credits(self) -> int`
  - Returns the cumulative number of attempted credits.
  - Returns:
    - `int`: The cumulative number of attempted credits.

- `set_cumulative_attempted_credits(self, cum_attempted_credits: int)`
  - Sets the cumulative number of attempted credits.
  - Parameters:
    - `cum_attempted_credits` (int): The cumulative number of attempted credits to set.

- `get_cumulative_earned_credits(self) -> int`
  - Returns the cumulative number of earned credits.
  - Returns:
    - `int`: The cumulative number of earned credits.

- `set_cumulative_earned_credits(self, cumulative_earned_credits: int)`
  - Sets the cumulative number of earned credits.
  - Parameters:
    - `cumulative_earned_credits` (int): The cumulative number of earned credits to set.
  - Returns:
    - None

- `get_cumulative_gpa_units(self) -> int`
  - Returns the cumulative GPA units.
  - Returns:
    - `int`: The cumulative GPA units.

- `set_cumulative_gpa_units(self, cumulative_gpa_units: int) -> None`
  - Sets the cumulative GPA units.
  - Parameters:
    - `cumulative_gpa_units` (int): The cumulative GPA units to set.
  - Returns:
    - None

- `get_cumulative_points(self) -> float`
  - Returns the cumulative number of points.
  - Returns:
    - `float`: The cumulative number of points.

- `set_cumulative_points(self, cumulative_points: float) -> None`
  - Sets the cumulative number of points.
  - Parameters:
    - `cumulative_points` (float): The cumulative number of points to set.
  - Returns:
  -   None

- `get_gpa(self) -> float`
  - Returns the GPA (Grade Point Average) for the term.
  - Returns:
    - `float`: The GPA.

- `set_gpa(self, gpa: float) -> None`
  - Sets the GPA (Grade Point Average) for the term.
  - Parameters:
    - `gpa` (float): The GPA to set.
  - Returns:
    - None

- `compute_gpa(self) -> None`
  - Computes the GPA (Grade Point Average) for the term based on the grades of the associated courses.
  - Returns:
    - None

- `get_cumulative_gpa(self) -> float`
  - Returns the cumulative GPA (Grade Point Average).
  - Returns:
    - `float`: The cumulative GPA.

- `set_cumulative_gpa(self, gpa: float)`
  - Sets the cumulative GPA (Grade Point Average).
  - Parameters:
    - `gpa` (float): The cumulative GPA to set.
  - Returns:
    - None
