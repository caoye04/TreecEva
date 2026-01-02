from collections import defaultdict

# Simulate fragmented disk blocks across multiple drives
disk_fragments = [45, 30, 15, 60, 20, 10, 25]
threshold = 25

# Track blocks above threshold by category
block_map = defaultdict(list)
for size in disk_fragments:
    category = 'large' if size >= threshold else 'small'
    block_map[category].append(size)

# Calculate optimized storage using only large blocks
total_utilized = sum(block_map['large'])

# Adjust based on compression efficiency
compression_ratio = 0.8 if len(block_map['large']) > 3 else 1.0
compressed_capacity = total_utilized * compression_ratio

# Secondary calculation (irrelevant but present for mild distraction)
avg_small_block = sum(block_map['small']) / len(block_map['small']) if block_map['small'] else 0

# Final optimization step
final_capacity = int(compressed_capacity + avg_small_block * 0.1)

Result: final_capacity