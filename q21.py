class Shape:
  """Base class for shapes."""

  def __init__(self, name):
    self.name = name

  def calculate_area(self):
    """Calculates and returns the area of the shape (base implementation)."""
    raise NotImplementedError("Area calculation not implemented for base Shape class")

class Square(Shape):
  """Derived class representing a square."""

  def __init__(self, side_length):
    super().__init__("Square")  # Call base class constructor
    self.side_length = side_length

  def calculate_area(self):
    """Overrides the base class calculate_area to compute the area of a square."""
    return self.side_length * self.side_length

# Create objects

square = Square(5)

# Attempting to call calculate_area on the base class will raise an error
# shape = Shape("Circle")  # Uncomment to see the error
# shape.calculate_area()

# Call the overridden method on the Square object
area = square.calculate_area()
print(f"Area of the square: {area}")
