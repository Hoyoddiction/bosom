def is_beautiful(number):
    return all(digit == str(number)[0] for digit in str(number))

def smallest_beautiful_number(x):
    current_number = x

    # Iterate through prime factors starting from 2
    for factor in range(2, int(x**0.5) + 1):
        while current_number % factor == 0:
            current_number //= factor
            if is_beautiful(current_number):
                return current_number

    if current_number > 1:
        return current_number

# Get user input for x
x = int(input("Enter a number: "))

# Find the smallest beautiful number divisible by x
result = smallest_beautiful_number(x)

print(f"The smallest beautiful number divisible by {x} is: {result}")
