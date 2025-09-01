class Circle:
  PI = 3.14159  # Class variable for pi

  def __init__(self, radius):
    self.radius = radius

  def calculate_area(self):
    """Calculates the area of the circle."""
    return Circle.PI * self.radius**2

  def calculate_circumference(self):
    """Calculates the circumference of the circle."""
    return 2 * Circle.PI * self.radius

# Create a circle object
circle = Circle(5)

# Print the area and circumference of the circle
print(f"Area: {circle.calculate_area()}")
print(f"Circumference: {circle.calculate_circumference()}")
