import itertools

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 19.0, 27.3, 22.1, 30.2, 25.8, 18.9, 24.4]
humidity_readings = [45, 60, 52, 48, 70, 55, 63, 50]
pressure_readings = [1013, 1009, 1015, 1012, 1008, 1014, 1010, 1011]

# Irrelevant calibration coefficients (distractor)
calibration_map = {t: t * 1.002 for t in temperature_readings}
offset_matrix = [[i + j * 0.1 for j in range(4)] for i in range(4)]

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    mean = sum(data) / len(data)
    return [(x - mean) / mean for x in data]

# Unused transformation chain
smoothed_temps = [round((a + b + c) / 3, 2) for a, b, c in zip(
    temperature_readings,
    [x + 0.1 for x in temperature_readings][1:],
    [x - 0.1 for x in temperature_readings][2:]
)] + [0, 0]

# Decoy statistical function that is never called
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    from math import log
    return -sum(p * log(p) for p in probs)

# Real processing begins here
valid_indices = [
    i for i in range(len(temperature_readings))
    if humidity_readings[i] > 47 and pressure_readings[i] < 1013
]

filtered_data = [
    (temperature_readings[i], humidity_readings[i])
    for i in valid_indices
    if temperature_readings[i] > 20.0
]

# Bit manipulation red herring
obfuscation_key = 0b110101
encoded_flags = [hash(str(hr)) ^ obfuscation_key for hr in humidity_readings]

# Conditional expression with distractor logic
diagnostic_flags = [
    'ELEVATED' if temp > 25 else 'NORMAL' if humid < 60 else 'MONITORED'
    for temp, humid in filtered_data
]

# Unused itertools permutation (misleading complexity)
all_pairs = list(itertools.combinations_with_replacement(filtered_data, 2))
pair_distances = [
    abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    for p1, p2 in all_pairs
]

# Real computation path
baseline_ref = sum(temperature_readings) / len(temperature_readings)
adjustment_factor = len([df for df in diagnostic_flags if df == 'ELEVATED']) * 0.3

# Core recursive reduction (actual logic)
def reduce_readings(data, acc=0.0):
    if not data:
        return acc
    temp, humid = data[0]
    # Weighted contribution
    contribution = (temp * 0.7) + (humid * 0.01)
    return reduce_readings(data[1:], acc + contribution)

interim_score = reduce_readings(filtered_data)

# Final processing step with conditional logic
threshold_met = len(filtered_data) >= 3
boost = 1.25 if threshold_met else 1.0

scaling_constant = 2.0 if __name__ == "__main__" else 1.0  # Always true

intermediate_result = interim_score * boost * scaling_constant

# Actual answer computation
final_diagnostic = int(intermediate_result + adjustment_factor * 100)

# Output result
print(f"Result: {final_diagnostic}")