import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 23.9, 24.7]
humidity_readings = [45, 47, 50, 52, 48, 55, 53]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016]

# Irrelevant signal processing artifacts (distractor variables)
spectral_components = [complex(1.2, 0.3), complex(0.9, -0.5), complex(1.1, 0.1)]
fft_magnitude = [abs(comp) for comp in spectral_components]
noise_floor = sum(fft_magnitude) / len(fft_magnitude)

# Data preprocessing with red herrings
offset_correction = 0.7
adjusted_temps = [t + offset_correction for t in temperature_readings]
dew_point_estimate = [h * 0.1 + 10 for h in humidity_readings]  # misleading intermediate

# Decoy statistical analysis (dead path)
mean_temp = sum(temperature_readings) / len(temperature_readings)
median_temp = sorted(temperature_readings)[len(temperature_readings)//2]
variance_temp = sum((t - mean_temp) ** 2 for t in temperature_readings) / len(temperature_readings)

# Real processing begins: anomaly detection flags
anomaly_flags = []
for i in range(len(temperature_readings)):
    temp_deviation = abs(temperature_readings[i] - mean_temp)
    if temp_deviation > 1.5:
        anomaly_flags.append(i)

# Unused function - decoy for recursive thinking
def calculate_entropy(data):
    total = sum(data)
    probabilities = [x / total for x in data if x > 0]
    return -sum(p * math.log(p) for p in probabilities)

# Simulated processing chain with bit manipulation red herring
processing_stages = ['raw', 'filtered', 'calibrated']
stage_bits = 0
for i, stage in enumerate(processing_stages):
    stage_bits |= (1 << i)  # irrelevant bit field

# Core logic disguised among distractions
def evaluate_stability(temp_data, hum_data):
    stability_score = 0
    for t, h in zip(temp_data, hum_data):
        if 22 <= t <= 25 and 45 <= h <= 55:
            stability_score += 1
    return stability_score

stability_index = evaluate_stability(temperature_readings, humidity_readings)

# Complex data structure cross-references (distractor)
sensor_matrix = {
    'temp': {'data': temperature_readings, 'unit': 'C'},
    'hum': {'data': humidity_readings, 'unit': '%'},
    'pres': {'data': pressure_readings, 'unit': 'hPa'}
}

# Unused slicing operations (misleading but idiomatic)
window_slice = temperature_readings[2:5]
overlap_region = humidity_readings[1:-1:2]

# Critical algorithm embedded in noise
baseline_ref = math.exp(2.3)  # reference constant
scaling_factor = 1.8

# Diagnostic computation chain
raw_diagnostics = []
for i in range(len(temperature_readings)):
    metric = (temperature_readings[i] * scaling_factor) + (humidity_readings[i] * 0.3)
    if i in anomaly_flags:
        metric *= 0.9
    raw_diagnostics.append(metric)

# Set operations used meaningfully but with distraction
valid_indices = set(range(len(temperature_readings)))
anomaly_set = set(anomaly_flags)
reliable_indices = valid_indices - anomaly_set

# Final transformation using list comprehension and filtering
filtered_diagnostics = [
    raw_diagnostics[i] for i in reliable_indices 
    if pressure_readings[i] > 1010
]

# Aggregation function with red herring parameters
def aggregate_metrics(metrics, config=None):
    if not metrics:
        return -999
    
    # Decoy configuration logic
    threshold = 45.0
    adjustment = 0
    for m in metrics:
        if m > threshold:
            adjustment += 0.5
    
    # Actual final computation
    base_value = sum(metrics) / len(metrics)
    penalty = len([m for m in metrics if m < 40]) * 1.5
    return round(base_value - penalty, 4)

# Execution point of interest
final_diagnostic = aggregate_metrics(filtered_diagnostics, diagnostics="full")

print(f"Result: {final_diagnostic}")