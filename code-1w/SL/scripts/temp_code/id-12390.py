import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9, 22.6]
humidity_readings = [45, 47, 50, 52, 58, 60, 55, 51, 49, 46]
co2_levels = [400, 410, 415, 430, 450, 470, 460, 440, 435, 425]

# Irrelevant auxiliary variables (distractors)
power_cycles = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
firmware_version = "v2.1.8"
calibration_offset = 0.07
redundant_flag = False
sync_timestamps = [1623456780 + i * 300 for i in range(10)]

# Misleading intermediate processing (dead path)
def legacy_normalization(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) * 1.05 for x in data]  # Not actually used

# Unused transformation function (decoy)
def frequency_filter(signal):
    return [math.sin(x * 0.1) for x in signal]

# Actual relevant signal processing chain
def preprocess_signal(raw_data, factor=1.0, noise_floor=0.5):
    smoothed = []
    for i in range(len(raw_data)):
        window_start = max(0, i - 2)
        window_end = min(len(raw_data), i + 3)
        avg = sum(raw_data[window_start:window_end]) / (window_end - window_start)
        if abs(raw_data[i] - avg) < noise_floor:
            smoothed.append(avg * factor)
        else:
            smoothed.append(raw_data[i] * factor)
    return smoothed

# Composite data structuring using list comprehension
sensor_matrix = [
    {
        't': preprocess_signal(temperature_readings)[i],
        'h': preprocess_signal(humidity_readings, factor=1.02)[i],
        'c': preprocess_signal(co2_levels, factor=0.98)[i],
        'index': i
    }
    for i in range(len(temperature_readings))
]

# Red herring: complex but unused bitwise operation block
checksum = 0
for reading in co2_levels:
    checksum ^= int(reading)
    checksum = (checksum << 1) & 0xFFFF

# Fake anomaly detection with misleading logic
anomaly_flags = []
for entry in sensor_matrix:
    t, h, c = entry['t'], entry['h'], entry['c']
    if t > 25 and h < 50:
        anomaly_flags.append(True)
    elif c > 450 and t < 24:
        anomaly_flags.append(True)
    else:
        anomaly_flags.append(False)  # Mostly false, not impactful

# Unused recursive helper (distractor)
def integrate_recursively(data, index=0):
    if index >= len(data) - 1:
        return data[index]
    return data[index] + 0.5 * integrate_recursively(data, index + 1)

# Real processing: extract and transform relevant features
processed_signals = []
for i, obs in enumerate(sensor_matrix):
    # Apply meaningful transformation
    thermal_humidity_index = obs['t'] * (obs['h'] / 100)
    co2_trend_score = (obs['c'] - 400) / 10
    composite_weight = (thermal_humidity_index * 0.6) + (co2_trend_score * 0.4)
    processed_signals.append(composite_weight)

# Secondary irrelevant aggregation
aggregate_stats = {
    'avg_processed': sum(processed_signals) / len(processed_signals),
    'peak': max(processed_signals),
    'variance': sum((x - sum(processed_signals)/len(processed_signals))**2 for x in processed_signals) / len(processed_signals)
}

# Critical function that computes final result
def analyze_readings(signals):
    base_score = 0
    adjustment = 0
    for i, s in enumerate(signals):
        if i % 2 == 0:
            base_score += math.log(s + 1) * 10
        else:
            base_score -= math.sqrt(s) * 5
        # Complex conditional adjustment
        if s > 15:
            adjustment += 2.5
        elif s > 10:
            adjustment += 1.2
    # Final nonlinear transformation
    final_value = int((base_score + adjustment) * 1.25)  # Deterministic integer result
    return final_value

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")