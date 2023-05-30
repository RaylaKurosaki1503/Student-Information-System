# `Student-Information-System.py` Documentation

## Author's Details
- Name: Rayla Kurosaki
- GitHub: [https://github.com/rkp1503](https://github.com/rkp1503)

## Terminal Command
`python src/Student-Information-System.py "C:/.../excel_file.xlsx"`

## Description
The `Student-Information-System.py` script is designed to process an Excel file containing student data and perform various operations on the data. The script utilizes modules from the `constructors` and `phases` directories to create a `Student` object and execute different phases of data processing.

## Function Documentation
- `get_path_to_excel_file(path: str) -> str`
  - This function verifies the validity of a file path and ensures that the specified path exists and points to an Excel file (.xlsx). If the path does not exist or the file is not in the correct format, an exception is raised. If the path is valid, it is returned.
  - Parameters:
    - `path` (str): The file path to be validated.
  - Returns:
    - `path` (str): The validated file path.
    
- `check_for_output_dir() -> None`
  - This function checks if an output directory exists in the current working directory. If the directory does not exist, it creates a new directory named "output" to store the output files.
  - Parameters:
    - None
  - Returns:
    - None

- `__main__()`
  - The main function of the script. It performs the following steps:
    1. Creates an instance of the `Student` class.
    2. Retrieves the file path from the command-line arguments provided when executing the script.
    3. Calls the `get_path_to_excel_file` function to validate the file path.
    4. Calls the `check_for_output_dir` function to ensure the existence of the output directory.
    5. Executes the data processing phases in the following order:
        - Phase 1: Adds data to the `Student` object using the `add_data` function from the `phase1` module.
        - Phase 2: Modifies data in the `Student` object using the `modify_data` function from the `phase2` module.
        - Phase 3: Performs computations on the data in the `Student` object using the `perform_computations` function from the `phase3` module.
        - Phase 4: Prints the data of the `Student` object using the `print_data` function from the `phase4` module.
  - Parameters:
    - None
  - Returns:
    - None
