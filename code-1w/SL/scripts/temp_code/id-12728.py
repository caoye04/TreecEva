data = [15, 8, 23, 12, 7, 30, 14]
threshold = 10
index_offset = 1  # Irrelevant distractor variable
temp_result = [x * 2 for x in data]  # Distractor: unused computation

# Key computation with list comprehension and enumerate
filtered_sum = sum([x for i, x in enumerate(data) if x > threshold and (i % 2 == 0)])

# Additional irrelevant operation
dummy_counter = 0
for val in data:
    if val < 15:
        dummy_counter += 1

print(f"Result: {filtered_sum}")