class Rectangle:
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def calculate_area(self):
    """Calculates and returns the area of the rectangle."""
    return self.length * self.breadth

# Create a rectangle object
rectangle = Rectangle(5, 3)

# Calculate and print the area of the rectangle
area = rectangle.calculate_area()
print(f"Area of the rectangle: {area}")
