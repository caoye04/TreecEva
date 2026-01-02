import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val for val in x if val > 0.5]

# Decoy transformation with misleading intermediate result
def decoy_transform(data):
    shifted = [(x * 1.5) % 1 for x in data]
    return [round(s, 3) for s in shifted]

# Real processing begins here
raw_readings = [0.1, 0.4, 0.7, 0.9, 1.2, 1.5, 1.8, 2.0]

# Distractor: complex-looking but unused signal smoothing
smoothed = list(map(lambda x: math.sin(x) ** 2 + 0.1 * x, raw_readings))

# Relevant transformation chain
filtered = [x for x in raw_readings if x >= 0.7]  # Only values >= 0.7 matter
scaled = [int(x * 10) for x in filtered]  # Scale to integer amplitudes

# Bit manipulation red herring (looks important, not used in final logic)
bit_encoded = 0
for val in scaled:
    bit_encoded ^= (val << 2) | (val >> 1)

# Irrelevant set operations (set distraction)
unique_scaled = set(scaled)
overlap_check = unique_scaled & {7, 9, 12, 15, 17}
disjoint_flag = unique_scaled.isdisjoint({25, 30, 35})

# Dummy threshold structure (misleading)
temp_thresholds = {
    'low': 5,
    'high': 20,
    'critical': 25
}

# Actual threshold map used in analysis (nested dict, 3-level deep)
threshold_map = {
    'amplitude': {
        'bounds': {
            'min': 6,
            'max': 19
        }
    },
    'tolerance': 1.5
}

# Simulated processed data with noise floor removal
noise_floor = 0.2
processed_data = []
for reading in raw_readings:
    if reading > noise_floor:
        adjusted = math.log(reading + 1) * 10
        if adjusted.is_integer():
            processed_data.append(int(adjusted))
        else:
            processed_data.append(round(adjusted))

# Another decoy: unused recursive function
def recursive_denoise(arr, depth=0):
    if depth > 2 or len(arr) == 0:
        return []
    return recursive_denoise([x//2 for x in arr if x > 5], depth + 1)

# Core analysis function with conditional branching and lambda
analyze_signal = lambda data, thresholds: (
    sum(
        (x - thresholds['amplitude']['bounds']['min']) ** 2 
        for x in data 
        if thresholds['amplitude']['bounds']['min'] <= x <= thresholds['amplitude']['bounds']['max']
    ) + int(math.sqrt(len(data)))
)

# Misleading post-processing (never called)
final_calibration = lambda x: x * 0.98 + 2.1

# Key statement: actual computation of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")