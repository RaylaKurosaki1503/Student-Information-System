# `pretty_print.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub Username: RaylaKurosaki1503

## File Details
- File: `pretty_print.py`

## Description
The `pretty_print.py` file contains a set of formatting and printing functions that can be used to generate visually appealing tables with aligned columns. These functions are designed to work together to create formatted output in a text-based table format.

## Function Documentation

- `format_string_header(string: str) -> str`
  - Description: Formats a string as a centered header with surrounding decorative characters.
  - Parameters:
    - `string` (str): The input string to be formatted as a header.
  - Returns:
    - (str): The formatted header string.

- `fmt_num_to_str(number: float, n: int) -> str`
  - Description: Formats a number as a string with a specified number of decimal places.
  - Parameters:
    - `number` (float): The input number to be formatted.
    - `n` (int): The number of decimal places to include in the formatted string.
  - Returns:
    - (str): The formatted number as a string.

- `get_column_widths(header: list[str], data: list[list[str]]) -> list[int]`
  - Description: Determines the maximum width for each column in a table based on the header and data rows.
  - Parameters:
    - `header` (list[str]): The list of strings representing the header row.
    - `data` (list[list[str]]): The list of lists representing the data rows.
  - Returns:
    - (list[int]): The list of maximum column widths.

- `print_boundary(file, column_widths: list[int])`
  - Description: Prints a horizontal boundary line in the table.
  - Parameters:
    - `file`: The file object to write the output to.
    - `column_widths` (list[int]): The list of column widths.
  - Returns:
    - None

- `print_separator(file, column_widths: list[int])`
  - Description: Prints a horizontal separator line in the table.
  - Parameters:
    - `file`: The file object to write the output to.
    - `column_widths` (list[int]): The list of column widths.
  - Returns:
    - None

- `print_row(file, data: list[str], column_widths: list[int])`
  - Description: Prints a single row of data in the table.
  - Parameters:
    - `file`: The file object to write the output to.
    - `data` (list[str]): The list of strings representing the row data.
    - `column_widths` (list[int]): The list of column widths.
  - Returns:
    - None

## Constants

- `MAX`
  - Description: A constant representing the preferred maximum character length per line.
  - Value: 78
