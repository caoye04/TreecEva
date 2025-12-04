import itertools

data_streams = [120, 85, 200, 150, 90]
compression_ratios = [0.8, 1.2, 0.95, 1.1, 0.75]

# Distractor variables that don't affect final calculation
buffer_capacity = 1000
network_latency = 45
protocol_overhead = 0.12

# Process data in batches of 2
batch_processor = itertools.combinations(data_streams, 2)
processed_sizes = []

for batch in batch_processor:
    batch_sum = sum(batch)
    # Apply compression ratio from middle element (distractor)
    middle_idx = len(data_streams) // 2
    temp_compression = compression_ratios[middle_idx]
    processed_size = batch_sum * temp_compression
    processed_sizes.append(processed_size)

# Only use first 3 processed batches
processed_batches = len(processed_sizes[:3])

# Calculate data multiplier based on compression ratios
data_multiplier = sum(compression_ratios[:3]) / 3

# The actual final throughput calculation
final_throughput = processed_batches * data_multiplier

print(f"Result: {final_throughput}")