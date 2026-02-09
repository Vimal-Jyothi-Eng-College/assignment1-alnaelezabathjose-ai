numbers = [10, 21, 4, 45, 66, 93, 11]

# Method 1: Using List Comprehension (Recommended)
odd_numbers = [num for num in numbers if num % 2 != 0]

# Method 2: Using a traditional for loop
odd_numbers_loop = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers_loop.append(num)

# Display results
print(f"Original list: {numbers}")
print(f"Odd numbers: {odd_numbers}")
Use code with caution.

