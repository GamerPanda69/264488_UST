from .employee_manager import EmployeeManager
def print_menu():
    """Prints the main menu options."""
    print("\n--- Employee Management Menu ---")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. Delete Employee")
    print("5. Exit")
    print("-----------------------------")

def get_employee_details():
    """Gets employee details from user input."""
    while True:
        try:
            name = input("Enter Name: ")
            if not name: 
                raise ValueError("Name cannot be empty.")
            department = input("Enter Department: ")
            if not department: 
                raise ValueError("Department cannot be empty.")
            designation = input("Enter Designation: ")
            if not designation: 
                raise ValueError("Designation cannot be empty.")
            gross_salary = float(input("Enter Gross Salary: "))
            if gross_salary < 0: 
                raise ValueError("Gross salary cannot be negative.")
            tax = float(input("Enter Tax Percentage (e.g., 10 for 10%): "))
            if not (0 <= tax <= 100): 
                raise ValueError("Tax must be between 0 and 100.")
            bonus = float(input("Enter Bonus Amount: "))
            if bonus < 0: 
                raise ValueError("Bonus cannot be negative.")
            return name, department, designation, gross_salary, tax, bonus
        except ValueError as err:
            print(f"Invalid input: {err}. Please try again.")

def main():
    """Runs the CLI application."""
    # Initialize the EmployeeManager (this also loads any existing employee data)
    manager = EmployeeManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':  # Add Employee
            print("\n--- Add New Employee ---")
            details = get_employee_details()
            if details:
                manager.add_employee(*details)

        elif choice == '2':  # View All Employees
            manager.view_all_employees()

        elif choice == '3':  # Search Employee by ID
            print("\n--- Search Employee ---")
            emp_id = input("Enter Employee ID to search: ")
            emp = manager.search_employee_by_id(emp_id)
            if emp:
                print("\n--- Employee Found ---")
                print(emp)
                print("--------------------")
            else:
                print(f"\nEmployee with ID '{emp_id}' not found.")

        elif choice == '4':  # Delete Employee
            print("\n--- Delete Employee ---")
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)

        elif choice == '5':  # Exit
            print("\nExiting Employee Management Application. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
