# `Assignment.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub: [https://github.com/rkp1503](https://github.com/rkp1503)

## Description
The `Assignment` class represents an assignment in an educational setting. It provides functionality to store and retrieve information about an assignment, such as the grade and any additional notes or comments.

## Methods Documentation

- `__init__(self, grade: str, notes: str)`
  - The constructor method initializes a new instance of the `Assignment` class.
  - Parameters:
    - `grade` (str): The grade received for the assignment.
    - `notes` (str): Additional notes or comments regarding the assignment.

- `get_grade(self) -> str`
  - Returns the grade received for the assignment.
  - Returns:
    - `str`: The grade of the assignment.

- `set_grade(self, grade: str) -> None`
  - Sets a new grade for the assignment.
  - Parameters:
    - `grade` (str): The new grade to set for the assignment.
  - Returns:
    - None

- `compute_grade(self) -> float`
  - Computes and returns the numerical grade as a floating-point value.
  - Returns:
    - `float`: The computed numerical grade.

- `get_notes(self) -> str`
  - Returns any additional notes or comments regarding the assignment.
  - Returns:
    - `str`: The notes or comments for the assignment.
