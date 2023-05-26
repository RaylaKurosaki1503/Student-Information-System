# `AssignmentType.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub Username: RaylaKurosaki1503

## File Details
- File: `AssignmentType.py`

## Description
The `AssignmentType` class represents a specific type or category of assignments within an educational setting. It provides functionality to store and manage information about the assignment type, its weight in the overall grading system, the individual assignments associated with it, and the calculated grades based on the assignments.

## Methods Documentation

- `__init__(self, asgmt_type: str, weight: float)`
  - Description: The constructor method initializes a new instance of the `AssignmentType` class.
  - Parameters:
    - `asgmt_type` (str): The type or category of the assignment.
    - `weight` (float): The weight of the assignment type in the overall grading system.

- `get_assignment_type(self) -> str`
  - Description: Returns the type or category of the assignment.
  - Returns:
    - `str`: The assignment type.

- `get_weight(self) -> float`
  - Description: Returns the weight of the assignment type in the overall grading system.
  - Returns:
    - `float`: The weight of the assignment type.

- `get_assignments(self) -> dict[int, Assignment]`
  - Description: Returns the dictionary of assignments associated with the assignment type.
  - Returns:
    - `dict[int, Assignment]`: The dictionary of assignments, where the keys are the indices of the assignments and the values are instances of the `Assignment` class.

- `add_assignment(self, index: int, assignment: Assignment)`
  - Description: Adds a new assignment to the assignment type.
  - Parameters:
    - `index` (int): The index of the assignment.
    - `assignment` (Assignment): An instance of the `Assignment` class representing the assignment to add.

- `get_grade(self) -> float`
  - Description: Returns the calculated grade for the assignment type.
  - Returns:
    - `float`: The calculated grade for the assignment type.

- `set_grade(self, grade: float)`
  - Description: Sets a new grade for the assignment type.
  - Parameters:
    - `grade` (float): The new grade to set for the assignment type.

- `compute_grade(self)`
  - Description: Computes the grade for the assignment type based on the grades of the associated assignments.
  
- `get_weighted_grade(self) -> float`
  - Description: Returns the weighted grade for the assignment type.
  - Returns:
    - `float`: The weighted grade for the assignment type.

- `set_weighted_grade(self, weighted_grade: float)`
  - Description: Sets a new weighted grade for the assignment type.
  - Parameters:
    - `weighted_grade` (float): The new weighted grade to set for the assignment type.

- `get_min_grade(self) -> (int, Assignment)`
  - Description: Returns the index and the assignment with the lowest grade among the associated assignments.
  - Returns:
    - `(int, Assignment)`: A tuple containing the index and an instance of the `Assignment` class with the lowest grade.

- `drop_grades(self, n: int)`
  - Description: Removes the `n` assignments with the lowest grades from the assignment type.
  - Parameters:
    - `n` (int): The number of assignments to remove.
