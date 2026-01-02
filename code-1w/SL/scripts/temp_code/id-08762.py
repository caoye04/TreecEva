def analyze_phase_shift(voltages, thresholds):
    adjusted = []
    for i, v in enumerate(voltages):
        if v > thresholds[i % len(thresholds)]:
            adjusted.append(v * 0.9)
        else:
            adjusted.append(v * 1.1)
    return adjusted

voltages = [120, 240, 180, 300, 210]
thresholds = [150, 200, 250]

# Misleading preprocessing step (distractor)
baseline_correction = sum(voltages) / len(voltages)
scaled_readings = [v - baseline_correction for v in voltages]

# Simulate sensor drift compensation (semi-relevant but not used)
drift_adjusted = [v * (0.98 + i * 0.01) for i, v in enumerate(scaled_readings)]

# Actual relevant data path
filtered_readings = analyze_phase_shift(voltages, thresholds)

# Introduce auxiliary transformation with zip (required feature)
weights = [0.1, 0.2, 0.4, 0.2, 0.1]
weighted_values = [v * w for v, w in zip(filtered_readings, weights)]

# Secondary distraction: simulate noise estimation
noise_floor = sum(abs(a - b) for a, b in zip(voltages, filtered_readings)) / len(voltages)
peak_noise = max(abs(a - b) for a, b in zip(voltages, filtered_readings))

# Core logic hidden among distractions
def calculate_net_flow(data):
    flow = 0
    for idx, reading in enumerate(data):
        if idx % 2 == 0:
            flow += reading * 1.5
        else:
            flow -= reading * 0.5
    # Additional interference inside function
    temp_debug = [x * 2 for x in data]  # unused
    return int(flow)

# Key statement
readings = filtered_readings

# Dead code path (distractor)
if len(readings) > 10:
    total_flux = -1
else:
    total_flux = calculate_net_flow(readings)

print(f"Result: {total_flux}")