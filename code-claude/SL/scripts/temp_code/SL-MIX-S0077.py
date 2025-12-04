# Network traffic analysis
# Analyzing packet data for suspicious patterns

packet_data = {
    'source_1': [45, 67, 23, 89],
    'source_2': [12, 78, 34, 56],
    'source_3': [90, 34, 12, 45]
}

# Configuration parameters
base_threshold = 30
adjustment_factor = 1.5
scaling_modifier = 0.8

# Initialize counters
total_packets = 0
high_volume_sources = 0

# Process packet sources
processed_data = {}
source_metrics = set()

for idx, (source, packets) in enumerate(packet_data.items()):
    # Track source packet count
    total_packets += sum(packets)
    
    # Calculate average packet size
    avg_size = sum(packets) / len(packets)
    source_metrics.add(int(avg_size))
    
    # Apply scaling based on source index
    scaling = scaling_modifier * (idx + 1)
    
    # Calculate weighted value
    weighted_value = avg_size * scaling
    processed_data[source] = weighted_value
    
    # Check for high volume sources
    if avg_size > base_threshold * adjustment_factor:
        high_volume_sources += 1

# Calculate adjusted threshold based on metrics
metrics_avg = sum(source_metrics) / len(source_metrics)
threshold = base_threshold * (metrics_avg / 50)

# Find sources exceeding the threshold
exceeding_sources = [s for s, v in processed_data.items() if v > threshold]

# Calculate supplementary statistics (not used in final calculation)
supplementary_data = {}
for source, value in processed_data.items():
    deviation = abs(value - metrics_avg)
    supplementary_data[source] = deviation

# Extract filtered sum of values exceeding threshold
filtered_sum = sum(value for value in processed_data.values() if value > threshold)

# Apply normalization (not used in final result)
normalized_sum = filtered_sum / (len(processed_data) if processed_data else 1)

print(f"Result: {filtered_sum}")