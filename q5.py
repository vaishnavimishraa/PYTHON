class MyClass:
  # Public variable (accessible from anywhere)
  public_var = "This is a public variable"

  # Private variable (conventionally not accessed from outside the class)
  _private_var = "This is a private variable"

  def get_private_var(self):
    # Access private variable within a class method (allowed)
    return self._private_var

# Create an object
obj = MyClass()

# Accessing public variable (works)
print(f"Public variable: {obj.public_var}")


# Accessing private variable using a class method (recommended)
print(f"Private variable (using method): {obj.get_private_var()}")
