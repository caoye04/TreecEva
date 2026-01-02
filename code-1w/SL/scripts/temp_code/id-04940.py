def analyze_dataset(raw_values, threshold=10):
    # Preprocess: filter and transform data
    filtered = [x for x in raw_values if x > threshold]
    squared = [x ** 2 for x in filtered]
    shifted = [x >> 2 for x in squared]  # Bitwise shift as transformation

    # Irrelevant intermediate calculation (distractor)
    avg_shifted = sum(shifted) / len(shifted) if shifted else 0
    temp_variance_proxy = sum((x - avg_shifted) ** 2 for x in shifted) / len(shifted) if shifted else 0

    # Slice operation to extract key segment
    relevant_segment = shifted[1:-1] if len(shifted) > 2 else shifted

    # State tracking with cumulative effect
    cumulative_total = 0
    for val in relevant_segment:
        if val % 3 == 0:
            cumulative_total += val // 3
        else:
            cumulative_total += val % 3

    return cumulative_total


def calculate_performance_metric(data_chunk):
    base_accum = sum(data_chunk)
    # Conditional expression based on size
    adjustment_factor = 1.5 if len(data_chunk) >= 5 else 0.8

    # Additional irrelevant computation (dead path)
    outlier_count = sum(1 for x in data_chunk if x > 1000)
    if outlier_count > 10:
        adjustment_factor *= 0.9  # Not triggered in this case

    # Real impact: bitwise AND to modulate signal
    modulation = base_accum & 0xFF  # Use lower 8 bits
    return int(base_accum * adjustment_factor) + modulation

# Main execution flow
raw_input_data = [5, 12, 18, 7, 24, 30, 8, 11, 16]

# Process pipeline
processed_intermediate = analyze_dataset(raw_input_data, threshold=9)

# Convert to list with dummy padding (for slicing relevance)
processed_data = [0, processed_intermediate] + [i * 2 for i in range(3)] + [processed_intermediate]

# Key slicing to extract working portion
processed_data = processed_data[1:4]  # Now contains [result, 0, 2]

# Add a misleading XOR-based checksum (unused)
cs = 0
for x in raw_input_data:
    cs ^= x
checksum_result = cs  # Dead variable

# Final computation point
final_score = calculate_performance_metric(processed_data)

print(f"Result: {final_score}")