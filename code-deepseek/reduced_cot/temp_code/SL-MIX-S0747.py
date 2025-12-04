# Calculate transformations on a sequence of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Apply conditional transformations: double even numbers, halve odd numbers
transformed = [x * 2 if x % 2 == 0 else x // 2 for x in numbers]

# Sum the transformed values
final_result = sum(transformed)

# Display the final computation result
print(f"Result: {final_result}")