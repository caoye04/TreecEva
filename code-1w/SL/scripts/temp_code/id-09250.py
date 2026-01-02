def analyze_trends(data, mode='advanced'):
    baseline = sum(data) / len(data)
    deviations = [abs(x - baseline) for x in data]
    high_deviation_count = len([d for d in deviations if d > baseline * 0.5])
    
    # Irrelevant trend analysis (distraction)
    growth_trend = 'stable'
    if all(data[i] <= data[i+1] for i in range(len(data)-1)):
        growth_trend = 'increasing'
    elif all(data[i] >= data[i+1] for i in range(len(data)-1)):
        growth_trend = 'decreasing'
    
    outlier_flags = set()
    for i, d in enumerate(deviations):
        if d > 2 * baseline:
            outlier_flags.add(i)
    
    # Distractor computation: unused transformation
    transformed_data = [x * 1.1 for x in data if x > baseline]
    smoothed = list(map(lambda x: round(x, 1), transformed_data))

    return baseline, len(outlier_flags)


def evaluate_stability(reading_sequence):
    rolling_max = max(reading_sequence[:3])
    for i in range(3, len(reading_sequence)):
        window = reading_sequence[i-3:i]
        if reading_sequence[i] > 2 * sum(window) / len(window):
            rolling_max = reading_sequence[i]
    return rolling_max

# Main execution context
sensor_readings = [12, 15, 10, 8, 23, 16, 7, 11, 19, 25]
threshold_set = {5, 10, 15, 20, 25}

# Secondary metric calculations (some irrelevant)
raw_magnitude = sum(abs(x) for x in sensor_readings)
corrected_readings = [x - 1 for x in sensor_readings if x > 10]
adjusted_total = sum(corrected_readings)

# Dummy string processing to incorporate string methods (required feature)
status_log = "ERROR: Reading unstable | WARNING: Offset detected | INFO: Normal"
log_entries = status_log.split('|')
severity_flags = {entry.strip().split(':')[0].lower() for entry in log_entries}
info_present = 'info' in severity_flags

# Real signal extraction
peak_response = evaluate_stability(sensor_readings)
signal_strength = peak_response * 0.8

# Core logic with set operations (required feature)
valid_peaks = {x for x in sensor_readings if x in threshold_set}
peak_count_score = len(valid_peaks) * 2

# Conditional expression and multiple concepts integration
metrics = {
    'amplitude': signal_strength,
    'peaks': len(valid_peaks),
    'stability': 1 if abs(signal_strength - adjusted_total) < 50 else 0
}

# Key computational step — target of the question
def process_performance(perf_metrics, thresholds):
    base = perf_metrics['amplitude']
    extra_weight = 1.5 if perf_metrics['stability'] else 0.5
    
    # Nested conditionals and intermediate distractions
    temp_debug = base * 0.1  # Unused debugging artifact
    if base > 15:
        cap_limit = 20
        if perf_metrics['peaks'] > 2:
            base += 5
        else:
            base += 2
    
    # More misleading code
    dummy_sequence = ['a', 'b', 'c']
    ''.join(dummy_sequence).upper()  # No effect

    # Final score calculation (depends on prior logic)
    final_component = base + (perf_metrics['peaks'] * extra_weight)
    return int(round(final_component))

final_score = process_performance(metrics, threshold_set)
print(f"Target result: {final_score}")