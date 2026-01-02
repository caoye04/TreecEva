import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.3, 25.0, 26.7, 18.9, 20.4, 24.8]
humidity_readings = [45, 50, 52, 60, 58, 49, 55, 62, 51]
pressure_readings = [1013, 1015, 1012, 1018, 1020, 1016, 1010, 1014, 1019]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 45, 50, 60, 55, 40, 38, 42, 48]  # Unused in final calculation
light_intensity = list(range(100, 190, 10))  # Dead code path material

# Preprocessing: Normalize readings to baseline range [0,1]
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Misleading transformation chain (partially unused)
norm_temp = normalize(temperature_readings)
norm_humid = normalize(humidity_readings)
norm_press = normalize(pressure_readings)

# Composite index creation (red herring)
composite_index = [
    0.4 * t + 0.3 * h + 0.3 * p
    for t, h, p in zip(norm_temp, norm_humid, norm_press)
]

# Critical threshold filter based on anomaly detection logic
def detect_anomalies(data, threshold=0.15):
    moving_avg = [
        sum(data[i-2:i+3]) / 5 if i >= 2 and i <= len(data)-3 else 0
        for i in range(len(data))
    ]
    # Only use non-zero windows
    valid_avgs = [avg for avg in moving_avg if avg != 0]
    deviations = [abs(data[i+2] - valid_avgs[i]) for i in range(len(valid_avgs))]
    return [i for i, dev in enumerate(deviations) if dev > threshold]

# Apply filtering (this result is actually unused - misleading)
anomaly_positions = detect_anomalies(norm_temp)

# Real processing path begins: extract significant fluctuations
def get_fluctuations(series):
    return [abs(series[i] - series[i-1]) for i in range(1, len(series))]

# Key transformations with distractors
temp_changes = get_fluctuations(temperature_readings)  # Relevant
humid_changes = get_fluctuations(humidity_readings)  # Partially relevant

# Combine changes using weighted sensitivity model (core logic)
sensitivity_map = list(map(lambda x: x * 1.8 if x > 0.5 else x * 1.2, temp_changes))

# Filter data based on dynamic thresholds (key step)
dynamic_threshold = sum(sensitivity_map) / len(sensitivity_map) * 0.75
filtered_indices = [i for i, val in enumerate(sensitivity_map) if val >= dynamic_threshold]
filtered_data = [temperature_readings[i+1] for i in filtered_indices]  # Shift due to fluctuation indexing

# Decoy function with unused side effects
def calculate_entropy(data):
    prob_dist = normalize([x * x for x in data])
    return -sum(p * math.log(p) for p in prob_dist if p > 0)

# Another red herring: complex string-based log generation
log_template = "ENV_RECORD_{}"
logs = [
    log_template.format(str(i).zfill(3)) + f"_T{temperature_readings[i]:.1f}".replace('.', 'p')
    for i in range(len(temperature_readings))
]

# Extract numeric parts from logs (distraction)
extracted_temps = [
    float(entry.split('_T')[1].replace('p', '.')) for entry in logs
]

# Validate extraction (unnecessary verification)
assert extracted_temps == temperature_readings

# Core diagnostic processor (uses filtered_data only)
def process_readings(readings):
    if not readings:
        return 0.0
    # Multi-stage processing
    squared = [x * x for x in readings]
    avg_square = sum(squared) / len(squared)
    root_mean = math.sqrt(avg_square)
    # Apply correction factor based on count
    correction = len(readings) % 4 or 1
    adjusted = root_mean * (1 + 0.05 * correction)
    # Final transformation
    return round(adjusted * 100) / 100

# Execute main computation
final_diagnostic = process_readings(filtered_data)

# Print result as required
print(f"Target result: {final_diagnostic}")