"""
Author: Rayla Kurosaki

GitHub: https://github.com/RaylaKurosaki1503

File: pretty_print.py
"""

MAX = 78


def format_string_header(string: str) -> str:
    n: int = ((MAX - len(string)) // 2) - 1
    return f"{'':~>{n}} {string} {'':~<{n}}"


def fmt_num_to_str(number: float, n: int) -> str:
    string: str = "{:0." + str(n) + "f}"
    return string.format(number)


def get_column_widths(header: list[str], data: list[list[str]]) -> list[int]:
    column_widths: list[int] = [len(e) for e in header]
    for lst in data:
        for index, element in enumerate(lst):
            if len(element) > column_widths[index]:
                column_widths[index] = len(element)
                pass
            pass
        pass
    return column_widths


def print_boundary(file, column_widths: list[int]):
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
    pass


def print_separator(file, column_widths: list[int]):
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
    pass


def print_row(file, data: list[str], column_widths: list[int]):
    string = f"|"
    for e1, e2 in zip(data, column_widths):
        string += f" {e1}{' ' * (e2 - len(e1))} |"
        pass
    file.write(f"{string}\n")
    pass
