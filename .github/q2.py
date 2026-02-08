def find_odd_numbers(arr):
    odd_numbers = []
    for num in arr:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

# Example usage:
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = find_odd_numbers(my_array)
print(f"The array is: {my_array}")
print(f"The odd numbers are: {result}")

# Another example:
another_array = [10, 20, 30, 40, 55, 66]
result_2 = find_odd_numbers(another_array)
print(f"The array is: {another_array}")
print(f"The odd numbers are: {result_2}")
