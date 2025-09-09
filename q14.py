class Student:
  def __init__(self, roll_number, name, marks):
    self.roll_number = roll_number
    self.name = name
    self.marks = marks

  def display_info(self):
    """Displays the student information."""
    print(f"Roll Number: {self.roll_number}")
    print(f"Name: {self.name}")
    print(f"Marks: {self.marks}")

# Create student objects
student1 = Student(123, "Alice", 85)
student2 = Student(456, "Bob", 92)

# Display information for each student
student1.display_info()
print("\n")
student2.display_info()
