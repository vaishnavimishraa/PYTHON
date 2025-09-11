class Fraction:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
    self.simplify()

  def simplify(self):
    """Calculates the greatest common divisor (GCD) and simplifies the fraction."""
    gcd = self._gcd(self.numerator, self.denominator)
    self.numerator //= gcd
    self.denominator //= gcd

  def _gcd(self, a, b):
    """Calculates the greatest common divisor (GCD) of two numbers."""
    while b != 0:
      a, b = b, a % b
    return a

  def __str__(self):
    """Returns a string representation of the fraction in its simplified form."""
    return f"{self.numerator}/{self.denominator}"

# Get numerator and denominator input from the user
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator (must not be zero): "))

# Create a Fraction object and print the simplified form
fraction = Fraction(numerator, denominator)
print(f"Simplified fraction: {fraction}")
