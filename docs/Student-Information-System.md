## Student-Information-System.py Documentation

### Author's Details
- Name: Rayla Kurosaki
- GitHub Username: RaylaKurosaki1503

### File Details
- File: Student-Information-System.py

### Description
The `Student-Information-System.py` file is a Python script that processes an Excel file containing student data and performs various operations on the data. The script imports modules from the `constructors` and `phases` directories to construct a `Student` object and execute different phases of data processing.

### Function Documentation

- `get_path_to_excel_file(path: str) -> str`
    - Description: This function takes a file path as input and verifies if the path exists and if the file has an ".xlsx" extension. If the path does not exist or the file is not an Excel file, an exception is raised. If the path is valid, the function returns the path.
    - Parameters:
        - `path` (str): The file path to be validated.
    - Returns:
        - `path` (str): The validated file path.

- `__main__()`
    - Description: The main function of the script. It constructs a `Student` object and performs the following phases of data processing:
        1. Phase 1: Adding data to the `Student` object using the `add_data` function from the `phase1` module.
        2. Phase 2: Modifying data in the `Student` object using the `modify_data` function from the `phase2` module.
        3. Phase 3: Performing computations on the data in the `Student` object using the `perform_computations` function from the `phase3` module.
        4. Phase 4: Printing the data of the `Student` object using the `print_data` function from the `phase4` module.
    - The path to the Excel file is obtained from the command-line arguments passed when executing the script. The `get_path_to_excel_file` function is used to validate the file path. If the file path is invalid, an exception is raised.
