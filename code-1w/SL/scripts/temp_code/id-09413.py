def analyze_telemetry_data(raw_readings):
    adjusted_values = []
    outlier_count = 0
    cumulative_shift = 0.0

    for i, reading in enumerate(raw_readings):
        if abs(reading - sum(raw_readings) / len(raw_readings)) > 2 * (max(raw_readings) - min(raw_readings)) / 2:
            outlier_count += 1
            continue
        
        shifted = reading + (i % 3) - 1
        adjusted_values.append(shifted)
        cumulative_shift += shifted * 0.1

    normalized = [val / max(adjusted_values) for val in adjusted_values] if adjusted_values else [0]
    return adjusted_values, normalized, outlier_count


def filter_and_enhance(signal_data, threshold=0.15):
    filtered = [s for s in signal_data if abs(s) >= threshold]
    enhancement_factor = len(filtered) / len(signal_data) if signal_data else 0
    enhanced = [s * (1 + enhancement_factor) for s in filtered]
    return enhanced


def calculate_performance_metric(metrics):
    base = sum(metrics)
    penalty = 0
    
    for i, val in enumerate(metrics):
        if i % 2 == 0 and val < 0.5:
            penalty += 0.1
        elif i % 3 == 0:
            penalty -= 0.05  # reward for alignment
    
    adjustment = max(0.8, min(1.2, 1 - penalty))
    return int(base * adjustment)

# Main execution block
readings = [0.7, 0.3, 1.2, 0.1, 0.9, 0.4, 1.1, 0.25, 0.65]

# Step 1: Analyze raw telemetry
raw_analysis, normalized_signals, anomalies = analyze_telemetry_data(readings)

# Step 2: Filter and enhance signals
enhanced_signals = filter_and_enhance(normalized_signals, threshold=0.15)

# Step 3: Process data through multiple transformations
processed_data = []
noise_floor = 0.05
for idx, (raw, norm) in enumerate(zip(raw_analysis, normalized_signals)):
    contribution = norm * (raw // 0.5 + 1)  # integer division simulation
    temp_weight = (idx + 1) * 0.1
    processed_data.append(min(contribution, temp_weight + noise_floor))

# Irrelevant tracking variables (distractors)
total_iterations = idx + 1
average_contribution = sum(processed_data) / len(processed_data) if processed_data else 0
dummy_aggregate = sum([x * x for x in processed_data])

# Key statement
final_score = calculate_performance_metric(processed_data)

print(f"Result: {final_score}")