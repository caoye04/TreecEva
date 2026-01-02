from collections import defaultdict, Counter
import math

# Simulated sensor array data (temperature, pressure, vibration)
sensor_logs = [
    (23.4, 101.3, 12), (22.9, 102.1, 15), (24.1, 100.8, 11),
    (23.7, 101.5, 14), (25.0, 99.9, 20), (23.2, 101.0, 10),
    (24.3, 100.5, 25), (23.8, 101.7, 13), (26.1, 98.7, 30),
    (23.5, 101.2, 11)
]

# Irrelevant auxiliary function (decoy)
def analyze_trends(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i][0] > data[i-1][0]:
            trend_score += 1
    return trend_score * 0.5

# Unused transformation (dead code path)
transform_log = lambda x: [(t, math.log(p), v) for t, p, v in x]

# Misleading preprocessing step with decoy variables
decoys = [math.sin(i) * 0.1 for i in range(len(sensor_logs))]
shadow_weights = [0.1, 0.2, 0.7]
weighted_sum = sum([w * d for w, d in zip(shadow_weights, decoys[:3])])

# Actual filtering: isolate readings where vibration > 12
critical_indices = []
for idx, entry in enumerate(sensor_logs):
    if entry[2] > 12:  # high vibration threshold
        critical_indices.append(idx)

filtered_data = [sensor_logs[i] for i in critical_indices]

# Red herring: frequency analysis on pressure (not used later)
pressure_freq = defaultdict(int)
for _, p, _ in filtered_data:
    rounded_p = round(p, 1)
    pressure_freq[rounded_p] += 1
mode_pressure = max(pressure_freq, key=lambda x: pressure_freq[x])

# Decoy statistical calculation
mean_vibration = sum([v for _, _, v in filtered_data]) / len(filtered_data) if filtered_data else 0
median_temp = sorted([t for t, _, _ in filtered_data])[len(filtered_data)//2]

# Core processing pipeline
scaling_factor = 1.8
offset_correction = 0.3

def normalize_reading(temp, pressure):
    return (temp * scaling_factor) + offset_correction - (pressure / 100)

# Bit manipulation decoy (irrelevant)
def hash_code(temp, vib):
    raw = int(temp * 10) ^ int(vib * 100)
    return (raw << 2) | (raw >> 15)

# Real processing function
def process_readings(readings):
    results = []
    for temp, pressure, vibration in readings:
        # Apply normalization
        norm_val = normalize_reading(temp, pressure)
        
        # Secondary adjustment based on vibration level
        if vibration > 20:
            adjustment = 1.25
        else:
            adjustment = 0.85
        
        adjusted = norm_val * adjustment
        results.append(adjusted)
    
    # Aggregate using a Counter (actual use)
    result_counter = Counter(results)
    primary_peak = max(result_counter, key=result_counter.get)
    
    # Final diagnostic computed from dominant normalized reading
    final_score = int(round(primary_peak * 100))
    return final_score

# Execution point of interest
final_diagnostic = process_readings(filtered_data)

# Print target result
print(f"Target result: {final_diagnostic}")