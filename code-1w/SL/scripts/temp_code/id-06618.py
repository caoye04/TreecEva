from collections import Counter

# Simulate network packet sizes (in bytes)
packet_sizes = [64, 128, 64, 256, 128, 512, 64, 1024, 256, 128, 64]

# Count frequency of each packet size
counter = Counter(packet_sizes)

# Extract unique sizes that appear more than once
frequent_sizes = {size for size, count in counter.items() if count > 1}

# Filter original data to include only frequent packet sizes
filtered_data = [size for size in packet_sizes if size in frequent_sizes]

# Compute sum of filtered data
filtered_sum = sum(filtered_data)

# Print result
print(f"Result: {filtered_sum}")