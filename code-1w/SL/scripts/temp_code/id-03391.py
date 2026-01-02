def analyze_sensor_readings(readings):
    valid_ranges = [(15, 30), (40, 55), (70, 85)]
    outliers = []
    normalized = []
    adjustment_factor = 0.95
    temp_sum = 0
    count = 0

    for i, val in enumerate(readings):
        if any(low <= val <= high for low, high in valid_ranges):
            adjusted = val * adjustment_factor
            normalized.append(adjusted)
            temp_sum += adjusted
            count += 1
        else:
            outliers.append((i, val))

    avg_normalized = temp_sum / count if count > 0 else 0

    # Irrelevant computation: tracking outlier trends (not used later)
    trend_flags = [1 if i > 0 and prev < curr else 0 for i, (curr_idx, curr) in enumerate(outliers) for prev_idx, prev in [outliers[i-1] if i > 0 else (0,0)]]
    
    return normalized, avg_normalized, outliers


def filter_noise(data, threshold=25.0):
    filtered = [x for x in data if x > threshold]
    noise_floor = sum(1 for x in data if x <= threshold)
    return filtered


def calculate_compression_ratio(seq):
    if len(seq) == 0:
        return 1.0
    unique_vals = list(set(seq))
    return len(seq) / len(unique_vals)


def calculate_final_score(data_chunk):
    base_score = 0
    compression = calculate_compression_ratio(data_chunk)
    
    for val in data_chunk:
        if val > 40:
            base_score += val * 0.3
        elif val > 25:
            base_score += val * 0.1
    
    penalty = 0
    sorted_vals = sorted(data_chunk)
    if len(sorted_vals) > 2:
        spread = sorted_vals[-1] - sorted_vals[0]
        if spread > 50:
            penalty += 15

    # Distractor: unused intermediate calculation
    hypothetical_max = sum(x * 0.5 for x in data_chunk if x > 30)
    efficiency_bonus = compression * 5
    
    final_score = int(base_score - penalty + efficiency_bonus)
    return final_score

# Main execution
raw_readings = [10, 18, 22, 27, 35, 44, 48, 60, 77, 81, 95, 103]

processed_data, avg_norm, detected_outliers = analyze_sensor_readings(raw_readings)
cleaned_data = filter_noise(processed_data, threshold=28)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")