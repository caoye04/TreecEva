import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 48, 55, 43, 51, 58, 40, 47, 50]
pressure_readings = [1013, 1015, 1010, 1018, 1012, 1009, 1020, 1014, 1011]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 45, 50, 30, 38, 44, 55, 41, 39]  # Decoy sensor data
light_intensity = [800, 950, 1200, 700, 880, 910, 1300, 970, 850]  # Not used in logic

# Calibration profiles (only one is actually used)
calibration_factor = 1.07
legacy_calibration = 0.98
experimental_calibration = 1.12

# Data alignment using zip (real use)
sensor_data = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Misleading transformation chain (partly dead code)
normalized_humidity = [h / 100 for h in humidity_readings if h > 40]  # Partial usage
adjusted_temps = [(t * 1.05) for t in temperature_readings]  # Distractor calculation

# Filtering irrelevant high-pressure readings (red herring)
valid_pressure_range = [p for p in pressure_readings if 1000 < p < 1016]
filtered_indices = [i for i, p in enumerate(pressure_readings) if p in valid_pressure_range]

# Actual relevant filtering: only readings where temp > 22 and humidity < 50
qualified_pairs = [(t, h) for t, h, p in sensor_data if t > 22 and h < 50]
filtered_data = [t for t, h in qualified_pairs]  # Only temperature retained

# Dead function - looks important but unused
def compute_air_quality_index(temp, hum, press):
    return (temp * 2.1) + (hum * 1.3) - (press * 0.01)

# Another decoy function with itertools
def generate_combinations(data):
    return list(itertools.combinations(data, 3))  # Never called

# Real processing function with embedded distractors
def process_readings(readings, calib):
    if not readings:
        return -999.0
    
    # Base statistic (relevant)
    avg_temp = sum(readings) / len(readings)
    
    # Distractor: complex but unused variance calculation
    squared_diffs = [(x - avg_temp) ** 2 for x in readings]
    variance = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
    std_dev = variance ** 0.5
    
    # Red herring: outlier detection (not actually affecting result)
    outliers = [x for x in readings if abs(x - avg_temp) > 1.5 * std_dev]
    clean_readings = [x for x in readings if x not in outliers]  # Not used
    
    # Critical adjustment using calibration (this IS used)
    calibrated_avg = avg_temp * calib
    
    # Additional distraction: entropy-like measure (unused)
    from math import log
    fake_entropy = sum(-p * log(p) for p in [0.1, 0.2, 0.3, 0.4] if p > 0)  # Dummy values
    
    # Final diagnostic computation (this determines answer)
    diagnostic_score = int(round(calibrated_avg * 100))
    
    # Secondary adjustment based on count (also relevant)
    count_factor = len(readings) * 2
    final_index = diagnostic_score + count_factor
    
    return final_index

# Unused advanced grouping (distractor block)
grouped_by_temp = {k: list(g) for k, g in itertools.groupby(sorted(sensor_data), key=lambda x: int(x[0]))}

# Phantom aggregation using itertools (dead path)
possible_triplets = []
if len(filtered_data) >= 3:
    possible_triplets = list(itertools.combinations_with_replacement(filtered_data, 3))

# Key execution point
temp_backup = filtered_data.copy()  # Backup not used later
calibration_factor *= 1.0  # No-op, but looks like adjustment

final_diagnostic = process_readings(filtered_data, calibration_factor)

# Print required result
print(f"Target result: {final_diagnostic}")