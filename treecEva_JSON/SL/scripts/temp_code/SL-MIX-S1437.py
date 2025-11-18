from collections import defaultdict

# Packet size-frequency data
packet_log = [
    (128, 3),
    (256, 2),
    (64, 5),
    (512, 1),
    (32, 4)
]

# Initialize aggregated packet statistics
aggregated_stats = defaultdict(int)
for size, freq in packet_log:
    aggregated_stats[size] += freq

# Compute base metric using dictionary comprehension
base_metrics = {size: size * freq for size, freq in aggregated_stats.items()}

# Calculate weighted sum
weighted_sum = sum(base_metrics.values())

# Apply modular transformation
modulus_base = 1000
verification_score = (weighted_sum * 7 + 256) % modulus_base

print(f"Result: {verification_score}")