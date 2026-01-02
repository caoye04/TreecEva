from collections import defaultdict, Counter

# Simulated sensor data with noise and irrelevant entries
data_stream = [
    ("temp", 23.5), ("temp", 24.1), ("humidity", 45), ("temp", 23.9),
    ("pressure", 1013), ("temp", 24.0), ("co2", 410), ("temp", 23.7),
    ("light", 300), ("temp", 24.2), ("temp", 23.6), ("motion", "active")
]

# Irrelevant auxiliary data (decoy)
aux_metadata = {
    "device_id": "SEN-90210",
    "firmware": "v2.4.1",
    "location": "Server Room B",
    "last_reboot": "2023-10-05T14:22:10Z"
}

# Misleading intermediate calculations (red herring)
baseline_offset = sum([x[1] for x in data_stream if isinstance(x[1], (int, float)) and x[0] == "humidity"]) / 2
dummy_accumulator = 0
for i, item in enumerate(data_stream):
    if i % 3 == 0:
        dummy_accumulator += len(item[0]) * 0.5

# Extract only temperature readings using list comprehension with enumeration (relevant)
temp_readings = [entry[1] for idx, entry in enumerate(data_stream) if entry[0] == "temp"]

# Apply moving average filter to smooth noise (relevant logic step 1)
smoothed_temps = [
    (temp_readings[i-1] + temp_readings[i] + temp_readings[i+1]) / 3
    for i in range(1, len(temp_readings)-1)
]
smoothed_temps = [round(t, 2) for t in smoothed_temps]

# Detect anomalies using lambda (relevant logic step 2)
anomaly_detector = lambda x, mu, sd: abs(x - mu) > 2 * sd
mean_temp = sum(smoothed_temps) / len(smoothed_temps)
std_dev = (sum((x - mean_temp)**2 for x in smoothed_temps) / len(smoothed_temps)) ** 0.5

# Filter out anomalous readings (relevant logic step 3)
cleaned_temps = [t for t in smoothed_temps if not anomaly_detector(t, mean_temp, std_dev)]

# Simulate multiple sensor fusion (distractor with partial relevance)
sensor_fusion_map = defaultdict(float)
for typ, val in data_stream:
    if typ != "temp":
        sensor_fusion_map[typ] += val * 0.1  # Minor contribution, misleading
sensor_fusion_map["temp"] = sum(cleaned_temps) / len(cleaned_temps)

# Calibration chain with decoy transformations (mixed relevance)
calibration_steps = []
def apply_calibration(x):
    steps = [
        x * 1.02,           # gain adjustment
        x + (-0.5),          # offset correction
        abs(x) ** 0.99,      # nonlinearity compensation (decoy)
        round(x, 2)
    ]
    calibration_steps.extend(steps)
    return steps[-1]

calibration_factor = apply_calibration(1.0)

# Data filtering via zip and counter (relevant: uses zip and Counter)
indexed_temps = list(enumerate(cleaned_temps))
pairs = list(zip(cleaned_temps, cleaned_temps[1:]))
drift_estimate = sum(abs(b - a) for a, b in pairs) / len(pairs) if pairs else 0

freq_counter = Counter(cleaned_temps)
dominant_temp = freq_counter.most_common(1)[0][0]

# Secondary processing path (dead code path - never used)
legacy_buffer = []
for val in temp_readings:
    legacy_buffer.append(val * 9/5 + 32)  # Convert to Fahrenheit for unused legacy system

# Main processing function with nested logic (core relevant path)
def process_readings(readings, calib):
    if not readings:
        return -999
    
    # Step 1: Base statistic
    avg = sum(readings) / len(readings)
    
    # Step 2: Weighted contribution from extremes (logic step 4)
    sorted_vals = sorted(readings)
    top_2_avg = sum(sorted_vals[-2:]) / 2
    bot_2_avg = sum(sorted_vals[:2]) / 2
    
    # Step 3: Stability score based on range (logic step 5)
    range_penalty = (sorted_vals[-1] - sorted_vals[0]) * 0.1
    
    # Step 4: Apply calibration factor in non-linear way (logic step 6)
    calibrated_avg = avg * calib
    
    # Step 5: Adjust using stability and edge weighting (logic step 7)
    composite_score = (
        0.6 * calibrated_avg +
        0.2 * top_2_avg +
        0.1 * bot_2_avg +
        0.1 * dominant_temp
    ) - range_penalty
    
    # Step 6: Final nonlinear transformation (logic step 8)
    final_value = (composite_score ** 1.05) * (1 + drift_estimate * 0.05)
    
    # Step 7: Round to meaningful precision (logic step 9)
    return round(final_value, 2)

# Critical execution point
final_diagnostic = process_readings(cleaned_temps, calibration_factor)

# Output result as required
print(f"Result: {final_diagnostic}")