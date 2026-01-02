def process_metrics(entries, limits):
    # Irrelevant transformation: counts characters in limit keys (distractor)
    key_length_sum = sum(len(k) for k in limits.keys())

    # Relevant: extract numeric data and apply filtering
    valid_values = []
    for entry in entries:
        parts = entry.split(':')
        if len(parts) != 2:
            continue
        try:
            sensor_id = parts[0].strip()
            reading_str = parts[1].strip()
            # Extract numeric value using string methods
            clean_value = float(reading_str.rstrip('x%'))

            # Only include readings within any of the defined threshold ranges
            is_within_threshold = any(
                clean_value >= limits[zone][0] and clean_value <= limits[zone][1]
                for zone in limits
            )
            if is_within_threshold:
                valid_values.append(clean_value)

            # Dead code path: never used in final computation
            if sensor_id.startswith('X'):
                temp_flag = True
                unused_buffer = [temp_flag, key_length_sum]

        except ValueError:
            pass  # Skip malformed entries

    # Semi-relevant: compute smoothed average using lambda
    if not valid_values:
        return 0.0

    # Apply moving window average of size 2 as preprocessing (only affects order)
    smooth_func = lambda arr: [(arr[i] + arr[i+1]) / 2 for i in range(len(arr)-1)] if len(arr) > 1 else arr
    smoothed = smooth_func(sorted(valid_values))

    # Another distraction: build a dictionary of index-to-value that isn't used
    index_map = {i: val for i, val in enumerate(smoothed)}
    total_entries_processed = len(entries)

    # Final computation: use only the maximum of smoothed values
    final_output = max(smoothed) if smoothed else 0.0
    return final_output

# Main execution context
sensor_data = [
    "A1: 45.2x", "B2: 78.9%", "C3: 23.1", "D4: 91.5x",
    "E5: 67.3%", "F6: 44.8", "G7: 88.0", "H8: 12.5"
]

threshold_ranges = {
    "critical": (85.0, 100.0),
    "optimal": (40.0, 70.0),
    "low": (20.0, 30.0)
}

# Unused auxiliary variables (distractors)
baseline_offset = 3.1415
debug_mode = False
log_buffer = []

result_cache = {}

# Key execution point
final_output = process_metrics(sensor_data, threshold_ranges)
print(f"Target result: {final_output}")