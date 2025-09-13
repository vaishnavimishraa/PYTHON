class NumberList:
  def __init__(self, numbers):
    self.numbers = numbers

  @classmethod
  def find_largest(cls, numbers):
    """Finds the largest value in a list of numbers."""
    if not numbers:
      raise ValueError("List cannot be empty")
    return max(numbers)

# Create a NumberList object
number_list = NumberList([3, 7, 1, 9])

# Find and print the largest value using the class method
largest_number = NumberList.find_largest(number_list.numbers)
print(f"Largest number: {largest_number}")

# Example of handling empty list 
try:
  empty_list = NumberList([])
  largest_number = empty_list.find_largest([])
except ValueError as e:
  print(f"Error: {e}")
