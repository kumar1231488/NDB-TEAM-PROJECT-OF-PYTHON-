def read_employees():
    """
    Read Employees Function

    This function reads employee data from the text file and returns it.

    Returns:
        list: A list containing employee data read from the text file.
    """
    employees_list = []
    with open("employees.txt", "r") as employees_file:
        for line in employees_file:
            fields = line.strip().split(",")
            employee_data = {
                "id": int(fields[0]),
                "firstname": fields[1],
                "secondname": fields[2],
                "birth": fields[3],
                "startingdate": fields[4],
                "position": fields[5],
                "salary": float(fields[6]),
            }
            employees_list.append(employee_data)
    return employees_list

def write_employees(employees_data):
    """
    Write Employees Function

    This function writes employee data to the text file.

    Parameters:
        employees_data (list): A list containing employee data to be written to the text file.
    """
    with open("employees.txt", "a") as employees_file:
        for employee in employees_data:
            line = f"{employee['id']},{employee['firstname']},{employee['secondname']},{employee['birth']},{employee['startingdate']},{employee['position']},{employee['salary']}\n"
            employees_file.write(line)
