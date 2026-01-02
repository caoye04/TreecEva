from collections import defaultdict, Counter

# Simulated sensor grid readings (row, col) -> temperature
raw_sensor_data = [
    (0, 0, 23.1), (0, 1, 24.5), (0, 2, 19.8),
    (1, 0, 25.3), (1, 1, 102.5), (1, 2, 20.9),
    (2, 0, 22.7), (2, 1, 26.8), (2, 2, 24.1)
]

# Misleading diagnostic flag (unused in final logic)
diagnostic_mode = True
debug_iterations = 0
max_iterations = 1000

# Data aggregation structures
temperature_grid = defaultdict(float)
reading_count = defaultdict(int)
spike_log = []

# Populate grid with raw data (with potential duplicates)
for row, col, temp in raw_sensor_data:
    key = (row, col)
    temperature_grid[key] += temp
    reading_count[key] += 1

# Calculate average per cell
for key in temperature_grid:
    temperature_grid[key] /= reading_count[key]

# Irrelevant noise: historical baseline (not used)
historical_avg = 22.5
baseline_drift = (temperature_grid[(0,0)] - historical_avg) * 1.5

# Filter out anomalous readings (>100 considered faulty)
filtered_readings = []
for row, col, temp in raw_sensor_data:
    if temp < 100.0:
        filtered_readings.append(temp)
    else:
        spike_log.append((row, col, temp))  # logged but not used

# Dead function - looks important but unused
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Another red herring: system calibration offset (never applied)
calibration_map = defaultdict(lambda: 0.0)
for r in range(3):
    for c in range(3):
        calibration_map[(r,c)] = (r - c) * 0.1

# Core processing function
def process_thermal_data(readings):
    if not readings:
        return 0.0
    
    # Sort and find quartiles (some intermediate values)
    sorted_vals = sorted(readings)
    n = len(sorted_vals)
    q1_idx = n // 4
    q3_idx = 3 * n // 4
    
    q1 = sorted_vals[q1_idx]
    q3 = sorted_vals[q3_idx]
    iqr = q3 - q1
    
    # Identify outliers (not actually removed - just analyzed)
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outlier_count = 0
    for val in sorted_vals:
        if val < lower_bound or val > upper_bound:
            outlier_count += 1
    
    # Decoy statistic
    mode_count = Counter(readings).most_common(1)
    mode_val, mode_freq = mode_count[0] if mode_count else (0, 0)
    
    # Actual computation path: weighted sum based on position in sorted array
    weighted_sum = 0.0
    total_weight = 0.0
    for i, val in enumerate(sorted_vals):
        weight = 1.0 + (i / len(sorted_vals))  # increasing weight
        weighted_sum += weight * val
        total_weight += weight
    
    final_mean = weighted_sum / total_weight
    
    # Transform through non-linear response curve (simulates sensor fusion)
    adjusted = final_mean * 1.1 + 0.5
    
    # Final clipping (not needed here but part of pattern)
    if adjusted < 0:
        adjusted = 0
    
    return adjusted

# Unused alternative processing path
def legacy_processing(data):
    return sum(x ** 0.5 for x in data) / len(data)

# Critical execution point
thermal_output = process_thermal_data(filtered_readings)

# Print result as required
print(f"Target result: {thermal_output}")