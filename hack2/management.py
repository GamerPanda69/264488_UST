import json

class Person:
    def __init__(self, name, age, gender):
        self.name, self.age, self.gender = name, age, gender 
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"  # Tinder bio, but HR-safe.

class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)  
        self.emp_id, self.department, self.salary = emp_id, department, salary  # You’re officially a barcode with a paycheck.

    def get_details(self):
        return f"{super().get_details()}, Emp ID: {self.emp_id}, Department: {self.department}, Salary: {self.salary}"  # Resume flex, but we all know you’re still a mess.

    def is_eligible_for_bonus(self):
        return self.salary < 50000  # Under 50K? Here’s a participation trophy, champ.

    def from_string(cls, data_string):
        name, age_str, gender, emp_id, dept, salary_str = data_string.split(',') 
        return cls(name, int(age_str), gender, emp_id, dept, int(salary_str))  # Congrats, you’re reborn as a corporate drone.
    from_string = classmethod(from_string)  

    def bonus_policy():
        print("Bonus Policy: Salary < 50,000 is eligible.")  # Policy so basic it’s basically communism.
    bonus_policy = staticmethod(bonus_policy) 

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Starts empty ‘cause no one’s dumb enough to join yet.

    def add_employee(self, employee):
        self.employees.append(employee)  # Welcome y'all

    def get_average_salary(self):
        return sum(emp.salary for emp in self.employees) / len(self.employees) if self.employees else 0  # Average pay so low it’s basically charity.

    def get_all_employees(self):
        return self.employees  # Here’s your list of wage slaves, boss.

    def save_to_json(self, filename):
        data_to_save = [
            {"name": emp.name, "age": emp.age, "gender": emp.gender,
             "emp_id": emp.emp_id, "department": emp.department, "salary": emp.salary}
            for emp in self.employees
        ]  # Turning people into JSON.
        try:
            with open(filename, 'w') as f_out:
                json.dump(data_to_save, f_out, indent=4) 
        except IOError as e:
            print(f"Error writing to {filename}: {e}")  # Oops, your disk hates you.

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as f_in:
                data_loaded = json.load(f_in)  # Reviving employees from digital purgatory.
            self.employees = [
                Employee(emp_data['name'], emp_data['age'], emp_data['gender'],
                         emp_data['emp_id'], emp_data['department'], emp_data['salary'])
                for emp_data in data_loaded
            ]  
        except FileNotFoundError:
            print(f"Error: {filename} not found.")  # File’s missing just like my bank balance
            self.employees = []
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading or parsing {filename}: {e}")  # broke it worse than spines of men in IT
            self.employees = []

def save_to_json(employee_list, filename="employees.json"):
    data = [
        {"name": emp.name, "age": emp.age, "gender": emp.gender,
         "emp_id": emp.emp_id, "department": emp.department, "salary": emp.salary}
        for emp in employee_list
    ]  # Packing souls into JSON 
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=3)  # Dumping it prettier than my ex's breakup text
    except IOError as e:
        print(f"Global save error writing to {filename}: {e}")  # Save failed, just like my life

def load_from_json(filename="employees.json"):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)  
        return [
            Employee(emp_data['name'], emp_data['age'], emp_data['gender'],
                     emp_data['emp_id'], emp_data['department'], emp_data['salary'])
            for emp_data in data
        ] 
    except FileNotFoundError:
        print(f"Global load error: {filename} not found.")  # file gone