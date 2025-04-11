import uuid

class Employee:
    """Represents an employee with their details."""
    
    def __init__(self, nm, dpt, des, grs, tx, bs):
        """
        Initializes an Employee object.

        Args:
            nm (str): Employee's name.
            dpt (str): Employee's department.
            des (str): Employee's designation.
            grs (float): Employee's gross salary.
            tx (float): Tax percentage applicable.
            bs (float): Bonus amount.
        """
        # Auto-generate unique identifier
        self.id = str(uuid.uuid4())
        self.name = nm
        self.department = dpt
        self.designation = des
        self.gross_salary = float(grs)
        self.tax = float(tx)  # Tax is a percentage
        self.bonus = float(bs)
        # Calculate net salary
        self.net_salary = self._calculate_net_salary()

    def _calculate_net_salary(self):
        """Calculates the net salary."""
        tax_amt = self.gross_salary * (self.tax / 100)
        return self.gross_salary - tax_amt + self.bonus

    def __str__(self):
        """Returns a string representation of the employee."""
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Designation: {self.designation}\n"
            f"Gross Salary: {self.gross_salary:.2f}\n"
            f"Tax (%): {self.tax:.2f}\n"
            f"Bonus: {self.bonus:.2f}\n"
            f"Net Salary: {self.net_salary:.2f}\n" + "-"*20
        )

    def to_dict(self):
        """Converts employee object to a dictionary for storage."""
        return {
            'id': self.id,
            'name': self.name,
            'department': self.department,
            'designation': self.designation,
            'gross_salary': self.gross_salary,
            'tax': self.tax,
            'bonus': self.bonus,
            'net_salary': self.net_salary
        }

    @classmethod
    def from_dict(cls, data):
        """Creates an Employee object from a dictionary."""
        emp = cls(
            nm=data['name'],
            dpt=data['department'],
            des=data['designation'],
            grs=data['gross_salary'],
            tx=data['tax'],
            bs=data['bonus']
        )
        # Restore the original ID and net salary
        emp.id = data['id']
        emp.net_salary = data['net_salary']
        return emp
