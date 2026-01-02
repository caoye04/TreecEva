def analyze_signal(data, config):
    baseline = sum(data[:5]) / 5
    adjusted = [x - baseline for x in data]
    squared_errors = [(x ** 2) for x in adjusted if x > 0.3]
    return sum(squared_errors) ** 0.5 if squared_errors else 0.0

# Irrelevant auxiliary function (dead code path)
def legacy_calibrate(x):
    return (x * 0.87) + 2.1 if x > 0 else x

# Unused transformation map
decoys = {k: (k*3 + 1)//2 for k in range(10, 20)}

# Simulated sensor readings
sensor_log = [127, 134, 129, 131, 128, 136, 140, 133, 129, 137]

# Distractor: unused signal analysis
noise_floor = analyze_signal([x % 10 for x in sensor_log], {'mode': 'low'})

# Core system: health diagnostics engine
health_trace = [18, 22, 25, 24, 27, 30, 33, 31, 29, 35, 38, 36]

# Threshold configuration with red herring entries
threshold_map = {
    'normal': 20,
    'elevated': 26,
    'critical': 32,
    'unused_mode_a': 40,
    'deprecated_b': 15
}

# Auxiliary state tracker (partially used)
counter_states = [0] * 5
for i in range(len(health_trace)):
    idx = min(i // 3, 4)
    counter_states[idx] += 1

# Conditional expression based escalation logic
current_level = 'critical' if any(h > threshold_map['critical'] for h in health_trace[-3:]) else 'elevated'

# Bit manipulation decoy
obfuscated_key = 0
for h in health_trace[:4]:
    obfuscated_key ^= (h << 2) | (h >> 1)
obfuscated_key = obfuscated_key & 0xFFFF  # Mask to 16 bits

# Real processing pipeline
filtered_readings = [h for h in health_trace if h > threshold_map['normal']]
rolling_avg = [sum(filtered_readings[i:i+3]) / 3 for i in range(0, len(filtered_readings)-2)]
peaks = [v for v in rolling_avg if v > threshold_map['elevated']]

# Secondary validation using conditional expression
validation_score = sum(peaks) if len(peaks) > 2 else (sum(filtered_readings) * 0.1)

# Final diagnostic calculation (depends on multiple prior chains)
def process_metrics(trace, thresholds):
    a = sum(1 for x in trace if x > thresholds['elevated'])
    b = sum(1 for x in trace if x > thresholds['critical'])
    c = len([x for x in trace if x in range(thresholds['normal']+1, thresholds['elevated'])])
    # Complex formula with distractor terms
    temp_bias = (a * 2.1) + (b * 3.8) - (c * 0.9)
    adjustment = 0.0
    if temp_bias > 10:
        adjustment = 5.5
    elif temp_bias > 5:
        adjustment = 2.2
    # Final result influenced by control flow
    return int(temp_bias + adjustment)

final_diagnostic = process_metrics(health_trace, threshold_map)

# Output target variable
print(f"Target result: {final_diagnostic}")