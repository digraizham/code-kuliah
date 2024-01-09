# Taking input from the user with space as a divider
input_numbers = input("Enter numbers separated by space: ")

# Splitting the input string into a list of strings
number_strings = input_numbers.split()

# Converting each string to an integer
numbers = [int(num) for num in number_strings]

# Calculating the sum of the numbers
result_sum = sum(numbers)

# Displaying the result
print("Sum of the entered numbers:", result_sum)