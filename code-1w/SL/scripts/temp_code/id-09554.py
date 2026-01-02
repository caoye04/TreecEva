sequence = list(range(1, 21))

# Apply transformation: square even numbers, cube odd numbers
tmapped = []
for num in sequence:
    if num % 2 == 0:
        tmapped.append(num ** 2)
    else:
        tmapped.append(num ** 3)

# Slice to take only middle segment (elements from index 4 to 11)
sliced_part = tmapped[4:12]

# Filter: keep only values greater than 100
filtered_sequence = [x for x in sliced_part if x > 100]

# Final computation
filtered_sum = sum(filtered_sequence)

# Additional irrelevant variable (minor distraction)
dummy_label = "post-process"

print(f"Result: {filtered_sum}")