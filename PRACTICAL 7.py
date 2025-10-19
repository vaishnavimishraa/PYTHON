#Q1

def find_max_min(numbers):
    if not numbers:
        return None, None

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num
sequence = [10, 5, 7, 13, 2, 20, 8]
maximum, minimum = find_max_min(sequence)
print("Maximum number:", maximum)
print("Minimum number:", minimum)

#Q2

def sum_of_cubes(n):
    if n <= 0:
        return 0

    sum_cubes = 0
    for i in range(1, n):
        sum_cubes += i**3

    return sum_cubes

positive_integer = int(input("Enter a positive integer: "))
result = sum_of_cubes(positive_integer)
print("Sum of cubes of positive integers smaller than", positive_integer, "is:", result)

#Q3

def print_numbers(n):
    if n < 1:
        return
    else:
        print_numbers(n - 1)
        print(n)

n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, "using recursion:")
print_numbers(n)

#Q4

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

n = int(input("Enter the number of terms for Fibonacci series: "))
fib_series = fibonacci(n)
print("Fibonacci series up to", n, "terms:")
print(fib_series)

#Q5

cone_volume = lambda r, h: (1/3) * 3.14159 * r**2 * h
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))
volume = cone_volume(radius, height)
print("Volume of the cone:", volume)

#Q6

max_min_tuple = lambda lst: (max(lst), min(lst))

input_list = [10, 6, 8, 90, 12, 56]

result = max_min_tuple(input_list)

print("Tuple of max and min:", result)

#Q7

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet(name="vaishnavi")
greet(name="anjali", message="Hi there")
