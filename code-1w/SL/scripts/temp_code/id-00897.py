data_sequence = [17, 23, 47, 53, 61, 73, 83, 97]

# Extract every second element starting from index 1
sampled_data = data_sequence[1::2]

# Reverse the sampled data and drop the first and last elements
processed_data = sampled_data[::-1][1:-1]

# Define index mapping and divisor
indices = [0, len(processed_data) // 2, len(processed_data) - 1]
divisor = 10

# Final computation step
temporary_sum = sum(processed_data)
result = processed_data[indices[-1]] % divisor

print(f"Target result: {result}")