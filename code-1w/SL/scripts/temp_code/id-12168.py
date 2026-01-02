def process_sensor_stream(raw_readings, calibration_factor):
    temporal_slices = [raw_readings[i:i+4] for i in range(0, len(raw_readings), 4)]
    filtered_blocks = []
    cumulative_shift = 0
    adjustment_log = []

    for block in temporal_slices:
        if len(block) < 4:
            continue
        
        # Irrelevant transformation (distractor)
        inverted = [round((1.0 / x) * 100, 2) for x in block if x != 0]
        adjustment_log.append(sum(inverted))
        
        # Real processing path
        shifted = [x + calibration_factor for x in block]
        normalized = [x / (calibration_factor + 1) for x in shifted]
        filtered_blocks.append(normalized)

    # Dead code path - never accessed under current logic
    def deprecated_correction(data):
        return [x * 0.95 for x in data]

    # Misleading intermediate
    transient_score = sum([sum(block[:2]) for block in filtered_blocks])
    stability_index = transient_score * 0.73

    # Actual aggregation preparation
    flattened = [item for sublist in filtered_blocks for item in sublist]
    windowed_averages = [sum(flattened[i:i+3]) / 3 for i in range(0, len(flattened)-2, 3)]
    
    return windowed_averages


def evaluate_anomaly_peaks(measures):
    threshold = sum(measures) / len(measures)
    anomalies = []
    for i, val in enumerate(measures):
        if val > threshold * 1.1:
            anomalies.append((i, val))
    # This function is called but its return is unused (red herring)
    return anomalies

def aggregate_measures(trend_series, offset):
    base = offset ** 2
    total = 0
    for i, val in enumerate(trend_series):
        if i % 2 == 0:
            total += val * (i + 1)
        else:
            total -= val * 0.5
    final = int(base + total)
    return final

# Simulated sensor input (realistic domain context: IoT diagnostic system)
initial_readings = [12.0, 15.3, 18.7, 20.1, 14.2, 16.8, 19.5, 22.3, 13.9, 17.1, 20.4, 23.6]
calibration_constant = 3
baseline_offset = 7

# Key processing steps
processed_trends = process_sensor_stream(initial_readings, calibration_constant)

# Irrelevant secondary analysis (distractor)
diagnostic_map = {}
for idx, (a, b) in enumerate(zip(processed_trends, processed_trends[1:])):
    diagnostic_map[idx] = abs(a - b) * 100

# Another decoy operation
sliced_view = processed_trends[::2]
slice_correlation = sum(sliced_view) / len(sliced_view) if sliced_view else 0

# Critical statement - answer depends on this
final_diagnostic = aggregate_measures(processed_trends, baseline_offset)

# Additional misleading calculation (looks important but isn't)
rolling_metrics = []
for i in range(len(processed_trends)):
    segment = processed_trends[max(0, i-2):i+1]
    rolling_metrics.append(sum(segment) / len(segment))

# Output the true answer
print(f"Result: {final_diagnostic}")