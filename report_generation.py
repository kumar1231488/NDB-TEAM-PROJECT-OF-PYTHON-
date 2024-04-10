def generate_reports(employees_data):
    departments = set(employee["department"] for employee in employees_data)
    department_salaries = {}
    department_employees = {}

    for department in departments:
        department_salaries[department] = sum(
            employee["salary"] for employee in employees_data if employee["department"] == department)
        department_employees[department] = [
            employee for employee in employees_data if employee["department"] == department
        ]

    report_1 = list(departments)

    report_2 = [
        {"id": employee["id"], "full_name": f"{employee['firstname']} {employee['secondname']}",
         "department": employee["department"]}
        for employee in employees_data
    ]

    report_3 = [
        {
            "department": department,
            "average_age": sum(
                (2024 - int(employee["birth"].split("/")[2])) for employee in employees_data if
                employee["department"] == department) / len(
                department_employees[department]),
            "average_salary": department_salaries[department] / len(department_employees[department]),
        }
        for department in departments
    ]

    report_4 = []
    for department in departments:
        for employee in department_employees[department]:
            report_4.append(
                {
                    "id": employee["id"],
                    "full_name": f"{employee['firstname']} {employee['secondname']}",
                    "date_of_birth": employee["birth"],
                    "salary": employee["salary"],
                    "total_salary_for_department": department_salaries[department],
                }
            )

    return {
        "report_1": report_1,
        "report_2": report_2,
        "report_3": report_3,
        "report_4": report_4,
    }
