"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Description: The code snippet imports the `os` and `sys` modules and appends
the current working directory to the `sys.path`. This allows the program to
access modules and packages located in the current working directory.
"""

import os
import sys

sys.path.append(os.getcwd())
