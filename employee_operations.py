# Employee Operations Module

employee = []  # Define the employee list globally

def add_employee():
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.
    """
    how = int(input("Enter how many employees to add: "))
    for _ in range(how):
        id = int(input("Enter id of employee: "))
        first = input("Enter first name of employee: ")
        last = input("Enter last name of employee: ")
        birth = input("Enter birth date: ")
        start = int(input("Enter starting year: "))
        position = input("Enter position: ")
        salary = int(input("Enter salary: "))
        employee.append([id, first, last, birth, start, position, salary])
    return employee

def delete_employee():
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.
    """
    who = int(input("Enter Employee id to delete: "))
    for i in employee:
        if who == i[0]:
            employee.remove(i)
    return employee

def update_employee():
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.
    """
    who = int(input("Enter Employee id to update: "))
    for i in employee:
        if who == i[0]:
            id = int(input("Enter id of employee: "))
            first = input("Enter first name of employee: ")
            last = input("Enter last name of employee: ")
            birth = input("Enter birth date: ")
            start = int(input("Enter starting year: "))
            position = input("Enter position: ")
            salary = int(input("Enter salary: "))
            i[1:] = [first, last, birth, start, position, salary]  # Update the employee's details
    return employee
