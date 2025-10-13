#PRACTICAL 5
#Q1

def count_capital_letters(input_string):
    count = 0

    for char in input_string:
        if char.isupper():
            count += 1

    return count

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to count capital letters
capital_count = count_capital_letters(user_input)

# Display the result
print(f"Number of capital letters: {capital_count}")

