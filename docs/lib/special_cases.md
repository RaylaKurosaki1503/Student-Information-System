# `special_cases.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub: [https://github.com/rkp1503](https://github.com/rkp1503)

## Description
The `special_cases.py` file contains functions that handle specific cases or special calculations for computing grades in different courses. These functions are designed to be used within a larger grading system and provide additional logic or adjustments based on the requirements of the specific courses.

## Function Documentation

- `drop_grades_2191_phys_320_01(asgmt_type: AsgmtType, n: int) -> None`
  - Drops the lowest grades for a specific assignment type in a Physics course.
  - Parameters:
    - `asgmt_type` (AsgmtType): The assignment type object representing a specific type of assignment.
    - `n` (int): The number of lowest grades to drop.
  - Returns:
    - None

- `compute_course_grade_helper(course: Course) -> None`
  - Helper function to compute the course grade based on the course ID.
  - Parameters:
    - `course` (Course): The course object representing a specific course.
  - Returns:
    - None

- `compute_course_grade_a(course: Course) -> None`
  - Computes the raw grade for courses with a specific grade limit rule.
  - Parameters:
    - `course` (Course): The course object representing a specific course.
  - Returns:
    - None

- `compute_course_grade_b(course: Course) -> None`
  - Computes the raw grade for courses using a simple sum of grades calculation.
  - Parameters:
    - `course` (Course): The course object representing a specific course.
  - Returns:
    - None

- `compute_course_grade_c(course: Course) -> None`
  - Computes the raw grade for a specific Physics course with raised quiz grades.
  - Parameters:
    - `course` (Course): The course object representing a specific course.
  - Returns:
    - None

- `compute_course_grade_d(course: Course) -> None`
  - Computes the raw grade for a specific course with a different calculation for homework grades.
  - Parameters:
    - `course` (Course): The course object representing a specific course.
  - Returns:
    - None

- `computing_raw_letter_grade_2185_math_399_01(course: Course) -> None`
  - Determines the raw letter grade for a specific course based on a pass/fail threshold.
  - Parameters:
    - `course` (Course): The course object representing a specific course.
  - Returns:
    - None
