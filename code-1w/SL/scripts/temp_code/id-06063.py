sequence = [12, 3, 8, 17, 4, 23, 9, 11, 6]
threshold = 10

# Extract every second element starting from index 0
even_indexed_elements = sequence[::2]

# Compute the sum of elements greater than threshold from these
temp_result = [x for x in even_indexed_elements if x > threshold]

filtered_sum = sum(temp_result)

# Irrelevant distraction: unused variable
dummy = len(sequence) + max(even_indexed_elements)

print(f"Result: {filtered_sum}")