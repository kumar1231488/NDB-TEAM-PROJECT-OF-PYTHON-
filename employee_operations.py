employees = {}


def add_employee():
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.
    """
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))

    employees[emp_id] = {'name': name, 'department': department, 'salary': salary}
    print("Employee added successfully.")


def delete_employee():
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.
    """
    emp_id = input("Enter employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


def update_employee():
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.
    """
    emp_id = input("Enter employee ID to update: ")
    if emp_id in employees:
        print("Enter new details (leave blank to keep current):")
        name = input(f"Current Name: {employees[emp_id]['name']}. New Name: ") or employees[emp_id]['name']
        department = input(f"Current Department: {employees[emp_id]['department']}. New Department: ") or \
                     employees[emp_id]['department']
        salary = input(f"Current Salary: {employees[emp_id]['salary']}. New Salary: ") or employees[emp_id]['salary']
        employees[emp_id] = {'name': name, 'department': department, 'salary': float(salary)}
        print("Employee updated successfully.")
    else:
        print("Employee not found.")

