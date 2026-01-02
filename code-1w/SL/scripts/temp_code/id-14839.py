import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [45, 47, 50, 52, 55, 58, 60, 54, 51]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1007, 1009, 1011, 1014]

# Irrelevant auxiliary measurements (distractor)
sound_levels = [32, 35, 40, 38, 36, 34, 33, 37, 39]  # dB, not used in final calculation
light_intensity = [500, 600, 700, 800, 900, 850, 750, 650, 550]  # lux, decoy

# Calibration profiles (only one is active)
legacy_calibration = lambda x: x * 1.02 + 0.5
active_calibration = lambda x: x * 0.98 - 0.3
emergency_offset = 1.2  # Unused under normal conditions

def analyze_trend(data):
    """Compute moving average trend (red herring function)"""
    trends = []
    for i in range(1, len(data)):
        trends.append(data[i] - data[i-1])
    return sum(trends) / len(trends) if trends else 0

def filter_outliers(values, threshold=2.0):
    """Remove values beyond threshold standard deviations (used indirectly)"""
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

# Misleading pre-processing chain (some steps are irrelevant)
temp_trend = analyze_trend(temperature_readings)  # Computed but unused
humidity_trend = analyze_trend(humidity_readings)  # Dead code path

# Simulate corrupted data point injection (but filtered out)
corrupted_temps = temperature_readings + [99.9]  # Invalid reading
filtered_temps = filter_outliers(corrupted_temps, threshold=2.0)

# Data fusion using Cartesian product (itertools usage)
raw_pairs = list(itertools.product(filtered_temps[:3], humidity_readings[:3]))
combined_index = sum(abs(t - h/20) for t, h in raw_pairs)  # Complex distractor metric

# Actual processing begins here — subtle shift in logic
primary_dataset = {
    'temps': filtered_temps,
    'humidity': humidity_readings,
    'pressure': pressure_readings
}

# Conditional data selection based on diagnostic mode
DIAGNOSTIC_MODE = True
if DIAGNOSTIC_MODE:
    working_keys = ['temps', 'humidity']
    backup_correction = False
else:
    working_keys = ['pressure']
    backup_correction = True  # Never reached

# Extract relevant data (core path)
working_data = []
for key in working_keys:
    working_data.extend(primary_dataset[key])

# Filtering operation with set de-duplication (set operations)
unique_scaled = list(set([round(x * 10) for x in working_data]))  # Remove duplicates after scaling
normalized_data = [x / 10.0 for x in unique_scaled]  # Back to original scale

# Redundant transformation pipeline
shifted_data = [x + 0.5 for x in normalized_data]
double_shifted = [x - 0.5 for x in shifted_data]  # Cancels previous shift

# Correct calibration applied here
filtered_data = double_shifted  # Final input dataset

calibration_factor = active_calibration(1.0)  # Only this calibration is used

# Decoy statistical computations
mean_noise = sum(sound_levels) / len(sound_levels)  # Irrelevant
median_light = sorted(light_intensity)[len(light_intensity)//2]  # Unused median

# Core processing function
def process_readings(readings, calib):
    base_score = 0
    adjustment = 0
    
    # Multi-phase integration
    for i, val in enumerate(readings):
        if i % 3 == 0:
            base_score += val * calib
        elif i % 3 == 1:
            base_score -= val * 0.1
        else:
            adjustment += (val % 2) * 0.05
    
    # Final aggregation with hidden offset
    result = base_score + adjustment
    
    # Additional decoy logic
    if result < 0:
        result *= 1.1  # Not triggered
    elif result > 1000:
        result = 999.999  # Safety cap (not needed)
        
    return round(result, 6)

# Critical execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Extraneous post-processing (dead code)
if final_diagnostic > 50:
    final_diagnostic *= 0.99
    secondary_diagnostics = [final_diagnostic * 0.1, final_diagnostic * 0.01]  # Unused

# Output the target result
print(f"Target result: {final_diagnostic}")