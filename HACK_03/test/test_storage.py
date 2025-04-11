import unittest
import os
import pickle
from employee_mgmt.storage import Storage
from employee_mgmt.employee import Employee

class TestStorage(unittest.TestCase):
    TEST_FILENAME = "test_employees.pkl"

    def setUp(self):
        """Set up the test environment."""
        if os.path.exists(self.TEST_FILENAME):
            os.remove(self.TEST_FILENAME)
        self.store = Storage(fname=self.TEST_FILENAME)
        # Sample employee data for testing
        self.e1 = Employee("Test1", "Dev", "Eng", 50000, 10, 1000)
        self.e2 = Employee("Test2", "QA", "Tester", 45000, 8, 500)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.TEST_FILENAME):
            os.remove(self.TEST_FILENAME)

    def test_save_and_load_employees(self):
        """Test saving and then loading employee data."""
        emp_list = [self.e1, self.e2]
        self.store.save_employees(emp_list)
        self.assertTrue(os.path.exists(self.TEST_FILENAME))
        loaded = self.store.load_employees(Employee)
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].id, self.e1.id)
        self.assertEqual(loaded[0].name, self.e1.name)
        self.assertEqual(loaded[1].id, self.e2.id)
        self.assertEqual(loaded[1].name, self.e2.name)
        self.assertEqual(loaded[0].net_salary, self.e1.net_salary)

    def test_load_non_existent_file(self):
        """Test loading when the file does not exist."""
        loaded = self.store.load_employees(Employee)
        self.assertEqual(loaded, [])

    def test_load_empty_file(self):
        """Test loading from an empty file."""
        open(self.TEST_FILENAME, 'w').close()
        loaded = self.store.load_employees(Employee)
        self.assertEqual(loaded, [])

    def test_save_and_load_empty_list(self):
        """Test saving and loading an empty employee list."""
        self.store.save_employees([])
        self.assertTrue(os.path.exists(self.TEST_FILENAME))
        loaded = self.store.load_employees(Employee)
        self.assertEqual(len(loaded), 0)

if __name__ == '__main__':
    unittest.main()
