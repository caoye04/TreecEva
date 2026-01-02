def analyze_trend(data, baseline):
    trend = 0
    temp_offset = 0
    for i in range(len(data) // 2):
        if data[i] > baseline:
            trend += 1
        else:
            temp_offset -= 0.5
    return trend


def extract_signals(raw_input):
    signals = raw_input[1::2]  # Take odd indices
    noise_floor = sum(signals) / len(signals)
    adjusted = [s - noise_floor for s in signals]
    return adjusted


def evaluate_performance(metrics, threshold):
    count_valid = 0
    aux_sum = 0
    for val in metrics:
        if val < 0:
            aux_sum += abs(val) * 0.1
        elif val >= threshold:
            count_valid += 1

    stability_check = len(metrics) - count_valid > 2
    penalty = 0
    if stability_check:
        penalty = 5

    # Irrelevant debugging snippet (dead code path)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {aux_sum}, {penalty}')

    result = count_valid * 10 - penalty
    return result

# Main execution
sensor_data = [3, 7, 2, 8, 5, 6, 4, 9]
baseline_ref = 4.5

# Step 1: Analyze trend in first half
initial_trend = analyze_trend(sensor_data, baseline_ref)

# Step 2: Extract signal components
raw_signals = extract_signals(sensor_data)

# Step 3: Normalize and filter
normalized = [round(x * 1.2, 1) for x in raw_signals if x > 0]

# Step 4: Simulate metric transformation
transformed_metrics = []
for v in normalized:
    if v > 6:
        transformed_metrics.append(v * 1.5)
    elif v > 4:
        transformed_metrics.append(v)
    else:
        transformed_metrics.append(v * 0.8)

# Misleading intermediate calculation (not used in final logic)
aggregate_diagnostic = sum(normalized) / len(normalized) if normalized else 0

# Key statement
final_score = evaluate_performance(transformed_metrics, threshold=5.0)

print(f'Result: {final_score}')