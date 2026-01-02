import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9, 22.6]
humidity_readings = [45, 47, 50, 52, 58, 60, 55, 53, 51, 49]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014, 1013]

# Irrelevant auxiliary arrays (distractors)
power_levels = [98, 95, 92, 88, 85, 80, 75, 70, 65, 60]  # Battery diagnostics (unused)
signal_strength = [-67, -70, -65, -72, -68, -75, -71, -69, -73, -74]  # Network metrics (unused)

def normalize(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) for x in data]

def detect_outliers(values, threshold=1.5):
    normalized = normalize(values)
    std_dev = (sum([x**2 for x in normalized]) / len(normalized)) ** 0.5
    if std_dev == 0:
        return []
    return [i for i, x in enumerate(normalized) if abs(x) > threshold * std_dev]

def apply_calibration(readings, factor=1.02, offset=0.5):
    # This function is defined but not used in the main logic
    return [r * factor + offset for r in readings]

def rolling_average(data, window=3):
    if len(data) < window:
        return data
    avgs = []
    for i in range(len(data) - window + 1):
        avgs.append(sum(data[i:i+window]) / window)
    return avgs

def filter_stable_ranges(temps, humids, stability_threshold=1.0):
    indices = []
    for i in range(len(temps) - 1):
        temp_change = abs(temps[i+1] - temps[i])
        humid_change = abs(humids[i+1] - humids[i])
        if temp_change < stability_threshold and humid_change < stability_threshold:
            indices.append(i)
    return indices

def compute_entropy(data):
    # Unused advanced metric (red herring)
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [x / total for x in data]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

def extract_key_metrics(temp_src, humid_src, pres_src):
    # Identify outlier points in temperature
    bad_indices = detect_outliers(temp_src, threshold=1.2)
    
    # Filter out unstable periods
    stable_windows = filter_stable_ranges(temp_src, humid_src, stability_threshold=1.5)
    
    # Combine filters: only keep readings that are both stable and not outliers
    valid_indices = [i for i in stable_windows if i not in bad_indices and i < len(temp_src)-1]
    
    # Extract corresponding data slices
    temp_filtered = [temp_src[i] for i in valid_indices]
    humid_filtered = [humid_src[i] for i in valid_indices]
    pres_filtered = [pres_src[i] for i in valid_indices]
    
    # Compute derived features
    temp_deltas = [abs(temp_filtered[i+1] - temp_filtered[i]) for i in range(len(temp_filtered)-1)]
    avg_temp_delta = sum(temp_deltas) / len(temp_deltas) if temp_deltas else 0
    
    # Secondary derived index (partially used)
    composite_index = []
    for t, h, p in zip(temp_filtered, humid_filtered, pres_filtered):
        score = (t * 0.4) + (h * 0.3) + ((p - 1000) * 0.3)  # Normalize pressure
        composite_index.append(score)
    
    return {
        'temperatures': temp_filtered,
        'humidity': humid_filtered,
        'pressure': pres_filtered,
        'composite': composite_index,
        'delta_metric': avg_temp_delta
    }

def process_readings(data_packet):
    raw_composite = data_packet['composite']
    
    # Apply smoothing via list comprehension (key relevant operation)
    smoothed = [val * 0.85 + 1.5 for val in raw_composite]
    
    # Additional transformation
    adjusted = [math.sin(x / 10) * x for x in smoothed]
    
    # Final aggregation
    if len(adjusted) == 0:
        return 0
    
    # Final diagnostic is the floored sum
    return int(sum(adjusted))

# --- Execution Flow ---

# Step 1: Preprocess to extract valid data segments
diagnostic_bundle = extract_key_metrics(
    temperature_readings, 
    humidity_readings, 
    pressure_readings
)

# Step 2: Simulate unused transformations (dead code paths)
rolling_temps = rolling_average(temperature_readings, 3)
rolling_humid = rolling_average(humidity_readings, 3)

# Step 3: Calibrate (function defined but not applied)
# Note: apply_calibration is never called — misleading because it looks important
calibration_warning = False  # Flag never set to True

# Step 4: Main filtering result used here
filtered_data = diagnostic_bundle  # Critical assignment

# Step 5: Compute entropy (irrelevant computation - distractor)
entropy_pressure = compute_entropy(pressure_readings)
entropy_temp = compute_entropy([int(x) for x in temperature_readings])  # Lossy conversion

# Step 6: Key statement
final_diagnostic = process_readings(filtered_data)

# Output result
print(f"Result: {final_diagnostic}")