def analyze_sensor_pattern(readings):
    threshold = 25
    duration = len(readings)
    peak_count = 0
    cumulative_energy = 0
    transient_spikes = []

    for i in range(duration):
        sample = readings[i]
        if sample > threshold:
            peak_count += 1
            cumulative_energy += sample ** 0.8

        # Detect transient spike: high value followed by rapid drop
        if i > 0 and readings[i-1] > 30 and sample < 10:
            transient_spikes.append(i)

    # Secondary processing: ignore spikes in first/last 2 positions
    valid_transients = [t for t in transient_spikes if 2 <= t <= duration - 3]
    instability_score = len(valid_transients) * 1.5

    # Irrelevant transformation (distractor)
    normalized_curve = [round((x - min(readings)) / (max(readings) - min(readings)) * 100) for x in readings]
    average_normalized = sum(normalized_curve) / len(normalized_curve)

    return peak_count, cumulative_energy, instability_score


def filter_outliers(raw_data, limit=50):
    # Remove values beyond hard limit (simulated sensor cap)
    cleaned = [x for x in raw_data if 0 <= x <= limit]
    
    # Dead code path - never executed due to fixed limit
    if limit > 100:
        smoothing_factor = 0.9
        cleaned = [int(x * smoothing_factor) for x in cleaned]

    return cleaned


def process_readings(data_chunk):
    size = len(data_chunk)
    base_metric = 0
    adjustment = 0

    # Simulate multi-stage diagnostic
    for idx, val in enumerate(data_chunk):
        if idx % 4 == 0:
            base_metric += (val % 7) * 2
        elif idx % 3 == 0:
            base_metric -= val // 10

        # Bitwise anomaly check (light usage)
        if (val ^ 15) & 8:
            adjustment += 1

    # Combine with dummy weight
    dummy_weight = len([x for x in data_chunk if x > 10])  # unused metric
    
    # Final heuristic
    result = (base_metric + adjustment) * (size % 5)
    
    # Key assignment point
    final_diagnostic = result + 5
    return final_diagnostic

# Main execution sequence
sensor_log = [12, 34, 56, 8, 23, 45, 9, 11, 67, 4, 33, 28, 15, 71, 6]
filtered_data = filter_outliers(sensor_log)
peak_info = analyze_sensor_pattern(filtered_data)
final_diagnostic = process_readings(filtered_data)
print(f"Result: {final_diagnostic}")