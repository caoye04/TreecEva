import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [55, 58, 60, 53, 49, 51, 57, 61]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1014, 1016]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_FACTOR_B = 1.014
REFERENCE_VOLTAGE = 3.3
OFFSET_ADJ = -0.05

# Misleading preprocessing: looks important but unused in final logic
def apply_calibration(data, factor):
    return [x * factor + OFFSET_ADJ for x in data]

calibrated_temps = apply_calibration(temperature_readings, CALIBRATION_FACTOR_A)
calibrated_humidity = apply_calibration(humidity_readings, CALIBRATION_FACTOR_B)

# Decoy function that appears relevant but is never called
def analyze_trend_sequence(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 1
    return abs(trend_score) * 1.5

# Dead code path: complex transformation not used
composite_index = []
for t, h, p in zip(temperature_readings, humidity_readings, pressure_readings):
    idx = (t * 2.1) + (h * 0.8) - (p * 0.01)
    composite_index.append(round(idx, 2))

# Unused enumeration with distraction
indexed_pairs = list(enumerate(zip(temperature_readings, humidity_readings)))
status_flags = ['NORMAL' if h < 58 else 'HIGH' for _, h in indexed_pairs]

# Real processing begins here — subtle because buried in noise
valid_range = lambda x: 24.0 <= x <= 26.5
filtered_data = [t for t in temperature_readings if valid_range(t)]

# Bit manipulation red herring
obfuscation_key = 245
scrambled = [int(t * 10) ^ obfuscation_key for t in filtered_data]
descrambled = [float(x ^ obfuscation_key) / 10 for x in scrambled]

# Linear search disguised as validation
def find_first_outlier(data, threshold=26.0):
    for i, val in enumerate(data):
        if val > threshold:
            return i  # This function is defined but not used
    return -1

# Recursive summation — actually used but hidden among decoys
def recursive_sum(seq, index=0):
    if index >= len(seq):
        return 0
    return seq[index] + recursive_sum(seq, index + 1)

# Integer division and rounding play a role in final result
total_temp = recursive_sum(filtered_data)
reading_count = len(filtered_data)
adjusted_avg = total_temp / reading_count

# Key transformation using itertools
shifted_cycle = itertools.cycle([1, -1])
modulated = [val + next(shifted_cycle) for val in filtered_data]
modulated_sum = sum(modulated)

# Final computation chain
baseline = 25.0
variance_score = abs(adjusted_avg - baseline) * 100
normalization_factor = 2.718  # Hint at e, but just a constant

intermediate_result = modulated_sum + variance_score
final_diagnostic = int(intermediate_result * normalization_factor) & 0xFFFF  # Bitwise mask for final step

# Output required for traceability
print(f"Result: {final_diagnostic}")