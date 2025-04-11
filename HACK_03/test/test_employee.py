import unittest
import uuid
from employee_mgmt.employee import Employee

class TestEmployee(unittest.TestCase):

    def test_employee_creation_and_net_salary(self):
        """Test basic employee creation and net salary calculation."""
        emp = Employee("Alice", "IT", "Developer", 60000, 10, 5000)
        self.assertEqual(emp.name, "Alice")
        self.assertEqual(emp.department, "IT")
        self.assertEqual(emp.designation, "Developer")
        self.assertEqual(emp.gross_salary, 60000.0)
        self.assertEqual(emp.tax, 10.0)
        self.assertEqual(emp.bonus, 5000.0)
        # Expected net salary: 60000 - (60000 * 0.10) + 5000 = 59000
        self.assertEqual(emp.net_salary, 59000.0)
        # Validate the auto-generated ID is a valid UUID4
        self.assertTrue(isinstance(uuid.UUID(emp.id, version=4), uuid.UUID))

    def test_employee_string_representation(self):
        """Test the string representation of the employee."""
        emp = Employee("Bob", "HR", "Manager", 75000, 15, 7000)
        emp.id = "test-id-123"  # Override auto-generated ID for testing
        emp.net_salary = emp._calculate_net_salary()  # Recalculate if needed
        expected_str = (
            "ID: test-id-123\n"
            "Name: Bob\n"
            "Department: HR\n"
            "Designation: Manager\n"
            "Gross Salary: 75000.00\n"
            "Tax (%): 15.00\n"
            "Bonus: 7000.00\n"
            "Net Salary: 70750.00\n"
            "--------------------"
        )
        self.assertEqual(str(emp), expected_str)

    def test_employee_to_dict(self):
        """Test converting employee object to dictionary."""
        emp = Employee("Charlie", "Finance", "Analyst", 55000, 12, 3000)
        emp_d = emp.to_dict()
        self.assertEqual(emp_d['name'], "Charlie")
        self.assertEqual(emp_d['id'], emp.id)
        self.assertEqual(emp_d['gross_salary'], 55000.0)
        self.assertEqual(emp_d['net_salary'], emp.net_salary)

    def test_employee_from_dict(self):
        """Test creating an employee object from a dictionary."""
        data = {
            'id': 'fixed-id-for-test',
            'name': 'Diana',
            'department': 'Marketing',
            'designation': 'Specialist',
            'gross_salary': 62000.0,
            'tax': 11.0,
            'bonus': 4500.0,
            'net_salary': 59680.0  # Pre-calculated for consistency
        }
        emp = Employee.from_dict(data)
        self.assertEqual(emp.id, 'fixed-id-for-test')
        self.assertEqual(emp.name, 'Diana')
        self.assertEqual(emp.department, 'Marketing')
        self.assertEqual(emp.gross_salary, 62000.0)
        self.assertEqual(emp.net_salary, 59680.0)
        self.assertAlmostEqual(emp._calculate_net_salary(), 59680.0, places=2)

if __name__ == '__main__':
    unittest.main()
