class Student:
  """Represents a student with name, SAP ID, and marks."""

  def __init__(self, name, sap_id, marks):
    self.name = name
    self.sap_id = sap_id
    self.marks = marks

  def display(self):
    """Displays the student's details."""
    print(f"\nName: {self.name}")
    print(f"SAP ID: {self.sap_id}")
    print(f"Marks:")
    print(f"\tPhysics: {self.marks['phy']}")
    print(f"\tChemistry: {self.marks['che']}")
    print(f"\tMaths: {self.marks['maths']}")
    print("-" * 20)  # Separator for readability

  def display_result(self):
    """Displays pass/fail status for each subject and overall."""
    passed_subjects = 0
    total_subjects = len(self.marks)

    print("\nResults:")
    for subject, mark in self.marks.items():
      result = "Pass" if mark >= 40 else "Fail"
      passed_subjects += 1 if result == "Pass" else 0
      print(f"\t{subject.capitalize()}: {mark} ({result})")

    overall_result = "Pass" if passed_subjects == total_subjects else "Fail"
    print(f"\nOverall Result: {overall_result}")

  def calculate_average(self):
    """Calculates and returns the student's average marks."""
    total_marks = sum(self.marks.values())
    average = total_marks / len(self.marks)
    return average


def calculate_class_average(students):
  """Calculates and returns the average marks for the entire class."""
  total_marks = 0
  for student in students:
    total_marks += student.calculate_average()
  class_average = total_marks / len(students)
  return class_average


# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Create a list to store student objects
students = []

# Create student objects with user input
for i in range(num_students):
  name = input(f"Enter student {i+1}'s name: ")
  sap_id = input(f"Enter student {i+1}'s SAP ID: ")
  phy_marks = float(input(f"Enter Physics marks for student {i+1}: "))
  che_marks = float(input(f"Enter Chemistry marks for student {i+1}: "))
  maths_marks = float(input(f"Enter Maths marks for student {i+1}: "))
  marks = {"phy": phy_marks, "che": che_marks, "maths": maths_marks}
  student = Student(name, sap_id, marks)
  students.append(student)

# Display details for all students
print("\nDetails of all students:")
for student in students:
  student.display()
  student.display_result()

# Calculate and display class average
class_average = calculate_class_average(students)
print(f"\nClass Average: {class_average:.2f}")
