import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.7, 25.3, 26.0, 21.2, 18.9, 20.4, 24.6]
humidity_readings = [45, 48, 52, 58, 44, 41, 56, 61, 50, 47]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1014, 1016, 1011, 1017, 1010]

# Irrelevant auxiliary metrics (distractors)
sound_levels = [32, 35, 30, 45, 50, 33, 31, 29, 34, 36]  # Decoy sensor data
light_intensity = [800, 850, 780, 900, 830, 810, 870, 840, 860, 820]  # Unused in logic

# Data alignment via zip (real usage)
sensor_fused = list(zip(temperature_readings, humidity_readings, pressure_readings))

def detect_anomalies(data_seq):
    # Real function: detects temp deviations beyond threshold
    anomalies = []
    base_temp = sum(temp for temp, _, _ in data_seq) / len(data_seq)
    for i, (temp, hum, pres) in enumerate(data_seq):
        if abs(temp - base_temp) > 2.0:
            anomalies.append(i)
    return set(anomalies)

# Distractor function: looks useful but unused
def analyze_acoustic_patterns(levels):
    peak_events = 0
    for level in levels:
        if level > 40:
            peak_events += 1
    return peak_events // 2

# Another red herring: complex but irrelevant transformation
def generate_spectral_signature(data):
    transformed = []
    for x in data:
        val = x
        for _ in range(3):
            val = (val * 7 + 13) % 100
        transformed.append(round(val, 2))
    return transformed[:len(data)//2]

# Real filtering logic based on anomaly detection
anomaly_indices = detect_anomalies(sensor_fused)
filtered_data = [row for i, row in enumerate(sensor_fused) if i not in anomaly_indices]

# Calibration factor derived from pressure median (relevant)
pressure_vals = sorted([pres for _, _, pres in filtered_data])
calibration_factor = pressure_vals[len(pressure_vals)//2] - 1000  # Offset from standard

# Distractor: unused statistical summary
drift_analysis = {
    'temp_trend': sum(temperature_readings[i+1] - temperature_readings[i] 
                       for i in range(len(temperature_readings)-1)),
    'humidity_variance': sum((h - 47)**2 for h in humidity_readings) / len(humidity_readings),
    'pressure_stability': len([p for p in pressure_readings if 1010 <= p <= 1015])
}

# Real processing pipeline
state_registry = []
for temp, hum, pres in filtered_data:
    # Compute derived indices
    heat_index = temp + 0.33*hum - 0.7*pres/100 - 4.0
    state_code = int(heat_index * 10) % 25
    state_registry.append(state_code)

# Use of itertools: grouping consecutive repeated states (real logic)
grouped_states = [list(g) for k, g in itertools.groupby(sorted(state_registry))]
state_frequency = {i: len(group) for i, group in enumerate(grouped_states)}

# Secondary filter using set operations (relevant)
common_states = {k for k, v in state_frequency.items() if v >= 2}
active_codes = set(state_registry)
overlap_set = common_states & active_codes

# Final processing with slicing and arithmetic
def process_readings(data_chunk, calib):
    raw_scores = []
    for t, h, p in data_chunk:
        score = (t * 2.1 + h * 0.8) / (calib + 1) - (p - 1000) / 50
        raw_scores.append(score)
    
    # Use of slicing: take every second element after sorting
    sorted_scores = sorted(raw_scores)
    selected_scores = sorted_scores[::2]  # Every second lowest
    
    # Final diagnostic computed from truncated mean
    trimmed_mean = sum(selected_scores) / len(selected_scores)
    diagnostic_value = int(trimmed_mean * 100) / 100  # Round to 2 decimals
    return diagnostic_value

# Critical execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output requirement
print(f"Result: {final_diagnostic}")