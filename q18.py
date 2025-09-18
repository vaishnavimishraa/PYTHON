class BankAccount:
  def __init__(self, pin, initial_balance=0):
    self.pin = pin  # Assume a 4-digit PIN for simplicity (replace with stronger authentication in real applications)
    self.balance = initial_balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("Deposit amount must be positive")
    self.balance += amount
    print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Withdrawal amount must be positive")
    if amount > self.balance:
      raise ValueError("Insufficient funds")
    self.balance -= amount
    print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

# Sample usage (replace with secure authentication mechanism)
pin = input("Enter your PIN: ")
if pin != "1234":  # Replace with actual PIN verification logic
  print("Invalid PIN")
  exit()

account = BankAccount(pin, 100)  # Assuming initial balance of $100

while True:
  print("\nMenu:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Exit")
  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    try:
      amount = float(input("Enter amount to deposit: "))
      account.deposit(amount)
    except ValueError as e:
      print(f"Error: {e}")

  elif choice == '2':
    try:
      amount = float(input("Enter amount to withdraw: "))
      account.withdraw(amount)
    except ValueError as e:
      print(f"Error: {e}")

  elif choice == '3':
    print(f"Your current balance: ${account.balance:.2f}")

  elif choice == '4':
    print("Exiting program")
    break

  else:
    print("Invalid choice. Please try again.")
