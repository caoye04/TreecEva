from itertools import zip_longest

def analyze_readings(readings):
    baseline = sum(readings) / len(readings)
    deviations = [abs(r - baseline) for r in readings]
    high_deviation_count = sum(1 for d in deviations if d > baseline * 0.1)
    normalized = [r / (baseline + 1e-5) for r in readings]
    return normalized, high_deviation_count

def compute_segments(data):
    segments = []
    temp_sum = 0
    for i, val in enumerate(data):
        temp_sum += val
        if (i + 1) % 3 == 0:
            segments.append(temp_sum)
            temp_sum = 0
    if temp_sum != 0:
        segments.append(temp_sum)
    
    # Distractor: unused transformation
    squared_segments = [s**2 for s in segments]
    smoothed = [s * 0.9 for s in segments]
    
    return segments

def aggregate_results(totals, weights):
    weighted_total = 0
    weight_sum = 0
    for t, w in zip_longest(totals, weights, fillvalue=1):
        adjusted_weight = w if w else 0.5
        weighted_total += t * adjusted_weight
        weight_sum += adjusted_weight
    
    # Misleading intermediate computation
    pseudo_average = sum(totals) / (len(totals) + 1)
    penalty = 0
    if len(totals) > len(weights):
        penalty = 0.1 * (len(totals) - len(weights))
    
    final_value = weighted_total / weight_sum - penalty
    return int(final_value)

# Main execution
sensor_data = [12.5, 14.0, 13.7, 15.2, 16.1, 14.8, 13.0]
normalized_data, flagged_errors = analyze_readings(sensor_data)
segment_sums = compute_segments(normalized_data)

# Irrelevant auxiliary list
aux_logs = [(i, round(v, 2)) for i, v in enumerate(normalized_data)]

weights = [0.8, 1.2, 0.9, 1.1]
totals = segment_sums

intermediate_metric = sum(segment_sums) / (flagged_errors + 1) if flagged_errors else 0

final_score = aggregate_results(totals, weights)
print(f"Result: {final_score}")