import unittest
import os
from employee_mgmt.employee_manager import EmployeeManager
from employee_mgmt.employee import Employee

class TestEmployeeManager(unittest.TestCase):
    TEST_STORAGE_FILE = "test_manager_employees.pkl"

    def setUp(self):
        """Prepare a clean environment for each test."""
        if os.path.exists(self.TEST_STORAGE_FILE):
            os.remove(self.TEST_STORAGE_FILE)
        self.mgr = EmployeeManager(storage_file=self.TEST_STORAGE_FILE)

    def tearDown(self):
        """Clean up the test storage file."""
        if os.path.exists(self.TEST_STORAGE_FILE):
            os.remove(self.TEST_STORAGE_FILE)

    def test_add_employee(self):
        """Test adding a new employee."""
        init_count = len(self.mgr.employees)
        emp = self.mgr.add_employee("ManagerTest", "Mgmt", "Head", 90000, 20, 10000)
        self.assertEqual(len(self.mgr.employees), init_count + 1)
        self.assertEqual(self.mgr.employees[-1].name, "ManagerTest")
        self.assertEqual(self.mgr.employees[-1].id, emp.id)
        # Verify persistence by reloading using a new manager instance
        new_mgr = EmployeeManager(storage_file=self.TEST_STORAGE_FILE)
        self.assertEqual(len(new_mgr.employees), init_count + 1)

    def test_search_employee_by_id_found(self):
        """Test searching for an existing employee by ID."""
        emp = self.mgr.add_employee("SearchMe", "SearchDept", "Finder", 50000, 10, 100)
        found = self.mgr.search_employee_by_id(emp.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.id, emp.id)
        self.assertEqual(found.name, "SearchMe")

    def test_search_employee_by_id_not_found(self):
        """Test searching for a non-existent employee."""
        found = self.mgr.search_employee_by_id("non-existent-id")
        self.assertIsNone(found)

    def test_delete_employee_found(self):
        """Test deleting an existing employee."""
        emp = self.mgr.add_employee("DeleteMe", "Temp", "Removable", 40000, 5, 0)
        init_count = len(self.mgr.employees)
        result = self.mgr.delete_employee(emp.id)
        self.assertTrue(result)
        self.assertEqual(len(self.mgr.employees), init_count - 1)
        self.assertIsNone(self.mgr.search_employee_by_id(emp.id))
        # Check persistence
        new_mgr = EmployeeManager(storage_file=self.TEST_STORAGE_FILE)
        self.assertEqual(len(new_mgr.employees), init_count - 1)

    def test_delete_employee_not_found(self):
        """Test attempting to delete a non-existent employee."""
        self.mgr.add_employee("KeepMe", "Perm", "Stable", 60000, 10, 1000)
        init_count = len(self.mgr.employees)
        result = self.mgr.delete_employee("non-existent-id")
        self.assertFalse(result)
        self.assertEqual(len(self.mgr.employees), init_count)

if __name__ == '__main__':
    unittest.main()
