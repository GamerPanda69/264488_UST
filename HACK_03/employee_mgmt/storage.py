import pickle
import os

class Storage:
    def __init__(self, fname):
        self.fname = fname

    def save_employees(self, employees):
        """Save employee data to a pickle file."""
        with open(self.fname, 'wb') as f:
            pickle.dump(employees, f)

    def load_employees(self, employee_class):
        """Load employee data from a pickle file."""
        if not os.path.exists(self.fname):
            return []

        with open(self.fname, 'rb') as f:
            try:
                employees = pickle.load(f)
            except EOFError:
                return []  # Return an empty list if the file is empty
            return employees
