from .employee import Employee
from .storage import Storage

class EmployeeManager:
    """Manages employee records."""

    def __init__(self, storage_file="employees.pkl"):
        """Initializes the EmployeeManager."""
        self.storage = Storage(storage_file)
        # Load existing employees when manager is initialized
        self.employees = self.storage.load_employees(Employee)

    def add_employee(self, nm, dpt, des, grs, tx, bs):
        """
        Creates and adds a new employee to the list.

        Args:
            nm (str): Employee's name.
            dpt (str): Employee's department.
            des (str): Employee's designation.
            grs (float): Employee's gross salary.
            tx (float): Tax percentage.
            bs (float): Bonus amount.

        Returns:
            Employee: The newly created Employee object.
        """
        new_emp = Employee(nm, dpt, des, grs, tx, bs)
        self.employees.append(new_emp)
        self.save_data()  # Save after adding the new employee
        print(f"\nEmployee '{nm}' added successfully with ID: {new_emp.id}")
        return new_emp

    def view_all_employees(self):
        """Prints details of all employees."""
        if not self.employees:
            print("\nNo employees found.")
            return

        print("\n--- All Employees ---")
        for emp in self.employees:
            print(emp)
        print("---------------------")

    def search_employee_by_id(self, emp_id):
        """
        Searches for an employee by their ID.

        Args:
            emp_id (str): The ID to search for.

        Returns:
            Employee or None: The found Employee object or None if not found.
        """
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def delete_employee(self, emp_id):
        """
        Deletes an employee by their ID.

        Args:
            emp_id (str): The ID of the employee to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        targ = self.search_employee_by_id(emp_id)
        if targ:
            self.employees.remove(targ)
            self.save_data()  # Save after deletion
            print(f"\nEmployee with ID '{emp_id}' deleted successfully.")
            return True
        else:
            print(f"\nEmployee with ID '{emp_id}' not found.")
            return False

    def save_data(self):
        """Saves the current list of employees to storage."""
        self.storage.save_employees(self.employees)
