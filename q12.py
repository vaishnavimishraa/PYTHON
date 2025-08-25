from datetime import date

class Person:
  """Class to represent a person with name and date of birth."""

  def __init__(self, name, dob):
    """Constructor to initialize name and date of birth."""
    self.name = name
    self.dob = dob

  def calculate_age(self):
    """Method to calculate age based on date of birth."""
    today = date.today()
    age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    return age

  def is_eligible_to_vote(self):
    """Method to check if the person is eligible to vote based on age (18 years)."""
    return self.calculate_age() >= 18

# Create person objects with different birth dates
person1 = Person("Alice", date(2005, 1, 1))  # Not eligible (born in 2005)
person2 = Person("Bob", date(1980, 12, 31))  # Eligible (born in 1980)

# Check and print voting eligibility
print(f"{person1.name} is eligible to vote: {person1.is_eligible_to_vote()}")
print(f"{person2.name} is eligible to vote: {person2.is_eligible_to_vote()}")
