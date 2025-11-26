data_stream = [8, 15, 22, 9, 31, 18, 7, 12, 25]
temp_buffer = [x + 5 for x in data_stream]
preliminary_sum = sum(temp_buffer)

# Filter processing
valid_entries = [x for x in data_stream if x > 10]
invalid_entries = [x for x in data_stream if x <= 10]
secondary_check = [x * 2 for x in invalid_entries]

# Main computation with early break condition
filtered_total = sum([x**2 for x in valid_entries if x % 3 != 0])

# Distractor operations
redundant_calc = sum([x // 2 for x in secondary_check])
verification_sum = preliminary_sum + redundant_calc

print(f"Target result: {filtered_total}")