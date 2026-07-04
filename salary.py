# Human-Centered Employee Salary Management System

employees = {}

def add_employee():
    print("\n--- Add a New Employee ---")
    emp_id = input("Employee ID: ")

    if emp_id in employees:
        print("This Employee ID already exists.\n")
        return

    name = input("Employee Name: ")
    department = input("Department: ")

    while True:
        try:
            salary = float(input("Monthly Salary (₹): "))
            break
        except ValueError:
            print("Please enter a valid salary.")

    employees[emp_id] = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }

    print(f"\nWelcome {name}! Your record has been created.\n")


def view_employees():
    if not employees:
        print("\nNo employee records found.\n")
        return

    print("\n========== Employee Details ==========")
    for emp_id, details in employees.items():
        print(f"""
Employee ID : {emp_id}
Name        : {details['Name']}
Department  : {details['Department']}
Salary      : ₹{details['Salary']:.2f}
---------------------------------------""")


def update_salary():
    emp_id = input("\nEnter Employee ID: ")

    if emp_id not in employees:
        print("Employee not found.\n")
        return

    employee = employees[emp_id]
    print(f"\nHey {employee['Name']}!")
    print(f"Current Salary: ₹{employee['Salary']:.2f}")

    while True:
        try:
            new_salary = float(input("Enter Updated Salary: ₹"))
            break
        except ValueError:
            print("Please enter a valid amount.")

    employee["Salary"] = new_salary
    print(f"Salary updated for {employee['Name']}.\n")


def search_employee():
    name = input("\nEnter Employee Name: ").strip().lower()
    found = False

    for emp_id, details in employees.items():
        if details["Name"].lower() == name:
            print("\nEmployee Found")
            print(f"ID         : {emp_id}")
            print(f"Department : {details['Department']}")
            print(f"Salary     : ₹{details['Salary']:.2f}")
            found = True

    if not found:
        print("No employee found with that name.")


def salary_summary():
    if not employees:
        print("\nNo salary data available.")
        return

    total = sum(emp["Salary"] for emp in employees.values())
    average = total / len(employees)

    print("\n========== Salary Summary ==========")
    print(f"Total Employees : {len(employees)}")
    print(f"Total Salary    : ₹{total:.2f}")
    print(f"Average Salary  : ₹{average:.2f}")


# Main Program
print("====================================")
print(" Welcome to Employee Salary Manager ")
print("====================================")

while True:
    print("""
1. Add Employee
2. View Employee Details
3. Update Salary
4. Search Employee
5. Salary Summary
6. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_salary()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        salary_summary()
    elif choice == "6":
        print("\nThanks for using Employee Salary Manager.")
        print("Have a great day!")
        break
    else:
        print("Not a valid option, try again.")