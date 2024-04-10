"""
Employee Management System Module

This module provides various functionalities for managing employee data.
"""
# Define the list of modules to be imported when the package is imported
'''employee_operations: This module contains functions for performing various employee-related operations, such as adding, updating, or deleting employee data.
file_operations: This module contains functions for handling file operations, such as reading and writing employee data to or from text files.
menu: This module contains functions for displaying and handling user interactions with the system's menu to add,delete and update employee data.
report_generation: This module contains functions for generating various reports based on employee data.'''

__all__ = ['employee_operations', 'file_operations', 'menu', 'report_generation']

# Import modules to make them available when the package is imported
from . import employee_operations
from . import file_operations
from . import menu
from . import report_generation
