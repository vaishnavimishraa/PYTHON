class Student:
  def __init__(self, name, sap_id, marks):
    self.name = name
    self.sap_id = sap_id
    self.marks = marks

  def display_details(self):
    """Displays the student's information."""
    print(f"Name: {self.name}")
    print(f"SAP ID: {self.sap_id}")
    print(f"Marks:")
    print(f"\tPhysics: {self.marks['phy']}")
    print(f"\tChemistry: {self.marks['che']}")
    print(f"\tMaths: {self.marks['maths']}")
    print("-" * 20)  # Optional separator for better readability

# Create a list to store student objects
students = []

# Create 3 student objects with user input
for i in range(3):
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
  student.display_details()
