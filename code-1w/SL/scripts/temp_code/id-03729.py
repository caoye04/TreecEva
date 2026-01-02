def analyze_metrics(data, threshold=10):
    count_valid = 0
    temp_sum = 0
    outlier_count = 0

    for val in data:
        if val < 0:
            continue  # Ignore negative values
        if val > threshold * 2:
            outlier_count += 1
            continue
        count_valid += 1
        temp_sum += val

    average = temp_sum / count_valid if count_valid else 0
    return average, outlier_count


def adjust_for_skew(value, factor=1.5):
    # Simulate correction for measurement skew
    adjusted = value * factor if value < 5 else value
    padding = 0.001  # Irrelevant constant
    return adjusted + padding


def calculate_final_score(raw_data):
    # Preprocess: filter and compute base metrics
    filtered_data = [x for x in raw_data if x % 2 == 1]  # Keep only odd numbers
    
    # Distraction block: irrelevant transformation
    mirrored = [abs(x - 10) for x in raw_data]
    total_mirrored = sum(mirrored)
    avg_mirror = total_mirrored / len(mirrored) if mirrored else 0

    # Core analysis on filtered data
    base_avg, outliers = analyze_metrics(filtered_data, threshold=8)

    # Apply conditional adjustment using ternary-like logic
    adjusted_avg = adjust_for_skew(base_avg) if base_avg < 7 else (base_avg + 0.5)

    # Secondary metric: entropy approximation via XOR dispersion
    xor_accum = 0
    for i in range(len(filtered_data)):
        if i > 0:
            xor_accum ^= (filtered_data[i] ^ filtered_data[i-1])

    # Combine metrics with weighted contribution
    stability_factor = 1 + (outliers / len(filtered_data) if filtered_data else 0)
    final_score = int(
        adjusted_avg * 10 
        + (xor_accum % 7) 
        - int(stability_factor * 2)
    )

    # Dead code path - never executed under normal input
    debug_mode = False
    if debug_mode:
        print(f'Debug: {final_score}')

    return final_score

# Main execution
sensor_readings = [3, 12, 5, 9, 14, 7, 6, 11, 13, 4, 8]
data_snapshot = sensor_readings.copy()

# Execute calculation
final_score = calculate_final_score(data_snapshot)
print(f'Target result: {final_score}')