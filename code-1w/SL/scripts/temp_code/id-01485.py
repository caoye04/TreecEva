import math

# Simulated sensor array data with noise and calibration offsets
temperature_readings = [23.5, 24.1, 19.8, 25.6, 26.7, 22.3, 20.9, 27.1, 28.4, 21.0]
humidity_readings = [45, 48, 55, 60, 52, 47, 58, 62, 50, 49]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1011, 1017, 1019, 1010]

# Calibration constants (some are red herrings)
CALIB_T_OFFSET = 0.5
CALIB_H_FACTOR = 1.02
CALIB_P_ADJUST = -2.1  # Unused in final logic
DUMMY_CONSTANT = 999  # Distractor

# Preprocess: remove outliers using interquartile range logic (simplified)
def remove_outliers(data):
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data) // 4]
    q3 = sorted_data[3 * len(sorted_data) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Misleading function that looks important but is never called
def legacy_calibrate(arr):
    """Old calibration method – not used"""
    return [x * 0.98 + 0.5 for x in arr]

# Another decoy: complex transformation with no downstream use
def spectral_transform(seq):
    transformed = []
    for i in range(len(seq)):
        val = 0
        for j in range(len(seq)):
            val += seq[j] * math.cos(2 * math.pi * i * j / len(seq))
        transformed.append(val)
    return transformed

# Real processing pipeline
filtered_temp = remove_outliers(temperature_readings)
calibrated_temp = [t + CALIB_T_OFFSET for t in filtered_temp]  # Apply offset

# Humidity processing with string-based flag check (use of string method)
mode_flag = 'standard.operation'
if mode_flag.endswith('operation') and 'std' not in mode_flag:
    adjusted_humidity = [h * CALIB_H_FACTOR for h in humidity_readings]
else:
    adjusted_humidity = humidity_readings

# Aggregation step: compute weighted health index (only temperature used in final result)
health_scores = []
for t in calibrated_temp:
    if t < 22.0:
        score = 1
    elif t < 25.0:
        score = 2
    elif t < 27.0:
        score = 3
    else:
        score = 4  # High temp stress level
    health_scores.append(score)

# Dummy list comprehension with side effects (no effect)
_ = [math.log(s + 1) for s in health_scores if s > 2]

# Critical data structure transformation
status_map = {1: 'LOW', 2: 'MOD', 3: 'ELEV', 4: 'HIGH'}
status_codes = [status_map[score] for score in health_scores]

# Another distractor: unused bit manipulation on status length
bit_encoded = 0
for i, code in enumerate(status_codes):
    bit_encoded ^= (len(code) << i) % 256

# Early termination simulation based on false condition
emergency_override = False
if sum(bit_encoded for _ in range(1)) > 1000:  # Always false
    final_diagnostic = -999
    print("Emergency override active")
else:
    # Core logic: count how many high-stress readings after calibration
    stress_count = sum(1 for s in status_codes if s == 'HIGH')
    
    # Additional filtering: only consider systems where pressure variation is low
    pressure_range = max(pressure_readings) - min(pressure_readings)
    if pressure_range > 10:
        adjustment_factor = 0.8
    else:
        adjustment_factor = 1.0  # This will be the case
    
    # Final diagnostic calculation
    base_diagnostic = stress_count * 100
    final_diagnostic = int(base_diagnostic * adjustment_factor)

# Dead code path: unreachable due to above logic
if __name__ == "__fake__":
    backup = spectral_transform([1, 2, 3])
    final_diagnostic = sum(backup)

# Print result as required
print(f"Result: {final_diagnostic}")