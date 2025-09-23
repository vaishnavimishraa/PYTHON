class Vehicle:
  """Base class for vehicles."""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def display_info(self):
    """Displays basic vehicle information."""
    print(f"Make: {self.make}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")

class Car(Vehicle):
  """Derived class representing a car."""

  def __init__(self, make, model, year, num_doors):
    super().__init__(make, model, year)  # Call base class constructor
    self.num_doors = num_doors

  def display_info(self):
    """Overrides the base class display_info to include number of doors."""
    super().display_info()  # Call base class display_info method
    print(f"Number of doors: {self.num_doors}")

class ElectricVehicle(Vehicle):
  """Derived class representing an electric vehicle."""

  def __init__(self, make, model, year, battery_range):
    super().__init__(make, model, year)
    self.battery_range = battery_range

  def display_info(self):
    """Overrides the base class display_info to include battery range."""
    super().display_info()
    print(f"Battery range: {self.battery_range} km")

class HybridCar(Car, ElectricVehicle):
  """Derived class representing a hybrid car (multiple inheritance)."""

  def __init__(self, make, model, year, num_doors, battery_range, engine_type):
    super().__init__(make, model, year, num_doors)  # Call first base class (Car)
    ElectricVehicle.__init__(self, make, model, year, battery_range)  # Call second base class (ElectricVehicle)
    self.engine_type = engine_type  # Additional attribute specific to HybridCar

  def display_info(self):
    """Overrides methods from both base classes to display combined information."""
    print(f"\nHybrid Car Details:")
    super(Car, self).display_info()  # Call display_info from Car class (skips ElectricVehicle)
    print(f"Battery range: {self.battery_range} km")
    print(f"Engine type: {self.engine_type}")


# Create objects and demonstrate inheritance

# Regular car
car = Car("Toyota", "Camry", 2023, 4)
car.display_info()
print("\n")

# Electric vehicle
ev = ElectricVehicle("Tesla", "Model S", 2024, 628)
ev.display_info()
print("\n")

# Hybrid car (demonstrating method resolution order with multiple inheritance)
hybrid = HybridCar("Toyota", "Prius", 2022, 4, 51, "Hybrid Electric")
hybrid.display_info()
