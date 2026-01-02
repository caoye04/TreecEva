import itertools

# Simulate sensor readings with noise
data_stream = [3, 5, 8, 13, 21, 34, 55, 67, 89, 100]

# Remove outliers using simple statistical threshold (mean ± 2σ)
mean_val = sum(data_stream) / len(data_stream)
variance = sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)
std_dev = variance ** 0.5

# Define valid range and filter
tolerance = 2 * std_dev
filtered_data = [x for x in data_stream if abs(x - mean_val) <= tolerance]

# Apply transformation: get every second element after filtering
processed_data = filtered_data[::2]

# Use itertools to generate pairwise sums and take first three pairs
pairwise_sums = [a + b for a, b in itertools.pairwise(processed_data)][:3]

# Final computation step
result = sum(filtered_data)
print(f"Result: {result}")