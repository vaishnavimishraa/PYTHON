class Employee:
  """Class to represent an employee with name, designation, salary, and a class variable for employee count."""

  # Class variable to keep track of the number of employees
  emp_count = 0

  def __init__(self, name, designation, salary):
    """Constructor to initialize employee details and increment employee count."""
    self.name = name
    self.designation = designation
    self.salary = salary
    Employee.emp_count += 1  # Increment employee count

  def get_details(self):
    """Method to return employee details as a dictionary."""
    return {
      "Name": self.name,
      "Designation": self.designation,
      "Salary": self.salary,
    }

  @classmethod
  def get_employee_count(cls):
    """Class method to access the current number of employees."""
    return cls.emp_count

# Create employee objects
employee1 = Employee("Alice", "Software Engineer", 80000)
employee2 = Employee("Bob", "Manager", 100000)

# Print employee details
print(employee1.get_details())
print(employee2.get_details())

# Print total number of employees
print(f"Total Employees: {Employee.get_employee_count()}")
