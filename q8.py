def my_global_function(message):
  """A simple function defined in the global namespace."""
  print(message)

class MyClass:
  @classmethod
  def call_global_function(cls, message):
    """A class method that calls the global function."""
    my_global_function(message)

# Create an instance of the class
obj = MyClass()

# Call the class method to utilize the global function
obj.call_global_function("This message is from the global function!")
