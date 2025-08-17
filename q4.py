class MyClass:
  def __init__(self, data):
    # Instance variable with a mutable type (list)
    self.data = data

  def modify_data(self):
    # Modify the list (mutable attribute)
    self.data.append("New element")
    print(f"Modified data: {self.data}")

# Create an object with a list
obj = MyClass(["Element 1", "Element 2"])

# Call the method to modify the list
obj.modify_data()
