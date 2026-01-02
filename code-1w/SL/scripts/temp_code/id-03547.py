data_sequence = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]
start_index = 2
end_index = 8
divisor = 3

# Extract a subsequence using slicing	sliced_data = data_sequence[start_index:end_index]

# Compute sum of elements divisible by divisor using lambda and filter
filtered_sum = sum(filter(lambda x: x % divisor == 0, sliced_data))

# Irrelevant distraction: unused variable (minimal interference)
temp_result = [x ** 0.5 for x in sliced_data if x % 6 == 0]

print(f"Result: {filtered_sum}")