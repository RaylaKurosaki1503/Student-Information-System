"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: This file contains a set of formatting and printing functions
that can be used to generate visually appealing tables with aligned columns.
These functions are designed to work together to create formatted output in a
text-based table format.
"""

MAX = 78


def format_string_header(string: str) -> str:
    """
    Formats a string as a centered header with surrounding decorative
    characters.
    :param string: The input string to be formatted as a header.
    :return: The formatted header string.
    """
    n: int = ((MAX - len(string)) // 2) - 1
    return f"{'':~>{n}} {string} {'':~<{n}}"


def fmt_num_to_str(number: float, n: int) -> str:
    """
    Formats a number as a string with a specified number of decimal places.
    :param number: The input number to be formatted.
    :param n: The number of decimal places to include in the formatted string.
    :return: The formatted number as a string.
    """
    string: str = "{:0." + str(n) + "f}"
    return string.format(number)


def get_column_widths(header: list[str], data: list[list[str]]) -> list[int]:
    """
    Determines the maximum width for each column in a table based on the
    header and data rows.
    :param header: The list of strings representing the header row.
    :param data: The list of lists representing the data rows.
    :return: The list of maximum column widths.
    """
    column_widths: list[int] = [len(e) for e in header]
    for lst in data:
        for index, element in enumerate(lst):
            if len(element) > column_widths[index]:
                column_widths[index] = len(element)
                pass
            pass
        pass
    return column_widths


def print_boundary(file, column_widths: list[int]) -> None:
    """
    Prints a horizontal boundary line in the table.
    :param file: The file object to write the output to.
    :param column_widths: The list of column widths.
    :return: None
    """
    string = f"|"
    for index, width in enumerate(column_widths):
        string += f"{'-' * (2 + width)}"
        if index + 1 == len(column_widths):
            string += f"|"
            pass
        else:
            string += f"-"
            pass
        pass
    file.write(f"{string}\n")
    return None


def print_separator(file, column_widths: list[int]) -> None:
    """
    Prints a horizontal separator line in the table.
    :param file: The file object to write the output to.
    :param column_widths: The list of column widths.
    :return: None
    """
    string = f"|"
    for index, width in enumerate(column_widths):
        string += f"{'-' * (2 + width)}"
        if index + 1 == len(column_widths):
            string += f"|"
            pass
        else:
            string += f"+"
            pass
        pass
    file.write(f"{string}\n")
    return None


def print_row(file, data: list[str], column_widths: list[int]) -> None:
    """
    Prints a single row of data in the table.
    :param file: The file object to write the output to.
    :param data: The list of strings representing the row data.
    :param column_widths: The list of column widths.
    :return: None
    """
    string = f"|"
    for e1, e2 in zip(data, column_widths):
        string += f" {e1}{' ' * (e2 - len(e1))} |"
        pass
    file.write(f"{string}\n")
    return None
