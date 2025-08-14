class MyClass:
  # Class variable (shared by all instances)
  class_var = "This is a class variable"

  def __init__(self, value):
    # Instance variable (unique to each object)
    self.instance_var = value

  def show_variables(self):
    print(f"Class variable: {MyClass.class_var}")
    print(f"Instance variable: {self.instance_var}")

    # Modify class variable (affects all instances)
    MyClass.class_var = "Modified class variable"

    # Modify instance variable (only affects this object)
    self.instance_var = "Modified instance variable"

    print(f"Modified class variable: {MyClass.class_var}")
    print(f"Modified instance variable: {self.instance_var}")

# Create objects
obj1 = MyClass("Object 1 value")
obj2 = MyClass("Object 2 value")

# Call the method to show variables
obj1.show_variables()
obj2.show_variables()
