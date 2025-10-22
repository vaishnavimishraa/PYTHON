#q1
# Open the file
with open("names.txt", "r") as file:
    # Read all lines
    names = file.readlines
total_names = len(names)

vowel_start_count = 0
longest_name = ""

for name in names:
    name = name.strip().lower()
    
    if name[0] in "aeiou":
        vowel_start_count += 1
    
    if len(name) > len(longest_name):
        longest_name = name

# Print the results
print("Total number of names:", total_names)
print("Number of names starting with a vowel:", vowel_start_count)
print("Longest name:", longest_name)

#q2
# Read integers from the file
with open("numbers.txt", "r") as file:
    numbers = [int(num) for num in file.readlines()]

# Find the maximum number
max_number = max(numbers)

# Calculate the average of all numbers
average = sum(numbers) / len(numbers)

# Count the number of numbers greater than 100
greater_than_100 = sum(1 for num in numbers if num > 100)

# Print the results
print("Max number:", max_number)
print("Average of all numbers:", average)
print("Number of numbers greater than 100:", greater_than_100)




#q3
# Open the file
with open("city.txt", "r") as file:
    city_data = file.readlines()
cities = []
population_more_than_10lakh = []
total_area = 0
for data in city_data:
    # Split the line into city name, population, and area
    city_name, population, area = data.split()
    # Convert population and area to appropriate data types
    population = float(population)
    area = float(area)
    
    # Append city details to the list of cities
    cities.append((city_name, population, area))
    
    # Check if population is more than 10 lakhs
    if population > 10:
        population_more_than_10lakh.append(city_name)
    
    # Add area to the total area
    total_area += area

# Display details of all cities
print("Details of all cities:")
for city in cities:
    print("City:", city[0])
    print("Population (in lakhs):", city[1])
    print("Area (in sq KM):", city[2])
    print()

# Display city names with population more than 10 lakhs
print("City names with population more than 10 lakhs:", population_more_than_10lakh)

# Display sum of areas of all cities
print("Sum of areas of all cities:", total_area)






#q4
try:
    N = int(input("Enter the number of test cases: "))
    for _ in range(N):
        a, b = input("Enter two values of a and b separated by space: ").split()
        a = int(a)
        b = int(b)
        result = a // b
        
        # Print the result
        print(result)

except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")
except ValueError as e:
    print(f"Error Code: {e}")




#q5
try:
    # Try to open a file that doesn't exist
    with open("nonexistent.txt", "r") as file:
        contents = file.read()

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied to access the file.")

except IOError:
    print("An I/O error occurred.")

except EOFError:
    print("End of file reached unexpectedly.")

except IsADirectoryError:
    print("The specified path is a directory, not a file.")

except FileExistsError:
    print("The file or directory already exists.")

except UnicodeDecodeError:
    print("Error decoding file contents as Unicode.")

else:
    print("File read successfully.")

finally:
    print("File handling operation complete.")
