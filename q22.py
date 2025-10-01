class Point:
  """Represents a point in 2D space."""

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    """Overloads the + operator to add two Point objects."""
    if not isinstance(other, Point):
      raise TypeError("Can only add Point objects")
    return Point(self.x + other.x, self.y + other.y)

  def __str__(self):
    """Returns a string representation of the point."""
    return f"Point(X={self.x}, Y={self.y})"

# Create Point objects
p1 = Point(10, 20)
p2 = Point(12, 15)

# Add points using the + operator
p3 = p1 + p2

# Print the result
print(f"P1: {p1}")
print(f"P2: {p2}")
print(f"P3 (P1 + P2): {p3}")
