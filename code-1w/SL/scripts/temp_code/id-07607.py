def analyze_sensor_readings(readings):
    filtered = [x for x in readings if x > 0]
    squared = list(map(lambda y: y ** 2, filtered))
    avg = sum(squared) / len(squared) if squared else 0
    threshold = 150
    high_vals = [v for v in squared if v > threshold]
    count_above = len(high_vals)
    return avg, count_above

readings_input = [3, -1, 4, 1, -5, 9, 2, 6, -5, 3, 5]

# Irrelevant transformation chain
transformed = []
for val in readings_input:
    if val % 2 == 0:
        transformed.append(val * 3 + 1)
    else:
        transformed.append(val * 2 - 1)

# Semi-relevant preprocessing with distractor variables
offset = 2
shifted_readings = [r + offset for r in readings_input]
decayed = [round(s * 0.95, 2) for s in shifted_readings]

# Core processing branch
base_avg, spike_count = analyze_sensor_readings(readings_input)

# Distractor: unused statistical computation
variance_proxy = sum((x - base_avg) ** 2 for x in [r**2 for r in readings_input if r > 0]) / len([r for r in readings_input if r > 0])

# Simulated calibration factor (misleading but not used)
calibration_sequence = [abs(hash(str(i))) % 10 for i in range(5)]
adjustment_factor = sum(calibration_sequence) / 10.0

# Actual relevant data pipeline
raw_magnitude = sum(abs(r) for r in readings_input)
normalized_score = raw_magnitude / len(readings_input)
processed_data = {
    'magnitude': raw_magnitude,
    'spikes': spike_count,
    'norm_score': normalized_score,
    'base_trend': base_avg
}

# Secondary irrelevant calculation
entropy_approx = 0
for p in processed_data.values():
    if p > 0:
        entropy_approx += p * (-p).log()

# Main yield logic with conditional expression
intermediate_yield = processed_data['magnitude'] * 0.8 + processed_data['base_trend'] * 0.3
penalty = 10 if processed_data['spikes'] < 3 else 5
final_yield = intermediate_yield - penalty

# Red herring output
debug_info = f"Yield components: {intermediate_yield=}, {penalty=}, adj={adjustment_factor:.2f}"

# Target result output
print(f"Result: {final_yield}")