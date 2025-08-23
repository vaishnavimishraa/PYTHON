class MyClass:
  def __init__(self):
    self.class_variables = {}  # Empty dictionary to store dynamic variables

  def add_variable(self, name, value):
    """Method to add a variable to the class at runtime."""
    self.class_variables[name] = value

  def get_variable(self, name):
    """Method to retrieve a variable added at runtime."""
    return self.class_variables.get(name)

# Create an instance of the class
obj = MyClass()

# Add a variable at runtime
obj.add_variable("school", "Hogwarts")

# Access the added variable
school_name = obj.get_variable("school")
print(f"School name: {school_name}")
