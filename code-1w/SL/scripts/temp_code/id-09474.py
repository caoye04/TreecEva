import itertools

# Simulated industrial turbine sensor data (real and decoy)
turbine_readings = [107, 214, 198, 235, 188, 204, 176, 221]
thermal_flux = [48.2, 52.1, 49.7, 54.3, 47.9, 51.0, 50.2, 53.8]  # irrelevant
efficiency_ratios = []

# Calibration parameters (only some are relevant)
calibration_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
dummy_weights = [0.1, 0.3, 0.05, 0.2, 0.15, 0.08, 0.07, 0.05]  # red herring
scaling_factor = 1.87
offset_correction = -0.93  # unused

# Decoy system state variables
default_thresholds = {"temp": 75, "rpm": 220, "vib": 8.5}
system_flags = [True, False, True, False, True, True, False, True]
status_codes = ['OK', 'WARN', 'OK', 'ERROR', 'OK', 'OK', 'WARN', 'OK']

# Irrelevant transformation chains
def process_thermal_noise(data, factor):
    return [x * factor + 2.1 for x in data if x > 50]  # dead function path
def compute_entropy(seq):
    from math import log
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    total = len(seq)
    for f in freq.values():
        p = f / total
        entropy -= p * log(p)
    return round(entropy, 3)

# Real processing begins here — subtle signal in noise
def extract_significant_pairs(readings, window=2):
    pairs = []
    for i in range(len(readings) - window + 1):
        segment = readings[i:i+window]
        if segment[0] < segment[1]:  # rising trend only
            pairs.append(segment)
    return pairs

def apply_calibration_magnitude(signal, key):
    result = 0
    for a, b in zip(signal, key):
        # Only odd-positioned elements in key affect output
        if (key.index(b) + 1) % 2 == 1:
            result += a * b
    return result

def generate_combinations(values, r=2):
    # Distractor: generates tuples but not used in final logic
    return list(itertools.combinations(values, r))

def detect_anomalies(stream):
    anomalies = []
    for i, val in enumerate(stream):
        if val > 210 and i % 2 == 0:
            anomalies.append((i, val))
    return anomalies  # computed but unused

def aggregate_metrics(sensor_data, calibration):
    # Step 1: Extract rising adjacent pairs
    significant_windows = extract_significant_pairs(sensor_data)
    
    # Step 2: Flatten using itertools.chain
    flattened_diffs = list(itertools.chain.from_iterable(
        [abs(pair[1] - pair[0]) for pair in significant_windows]
    ))  # Note: this creates a flat list of one-element lists; corrected manually below
    
    # Manual correction due to above error (part of logic chain)
    diffs_only = [abs(pair[1] - pair[0]) for pair in significant_windows]
    
    # Step 3: Map calibration weights (only odd indices matter)
    weighted_sum = 0
    for idx, diff in enumerate(diffs_only):
        if idx % 2 == 0:  # even index in diff list
            weighted_sum += diff * calibration[idx % len(calibration)]

    # Step 4: Apply nonlinear boost if over threshold
    if weighted_sum > 300:
        weighted_sum = (weighted_sum * 0.75) + 50
    else:
        weighted_sum = (weighted_sum * 1.1)

    # Step 5: Final adjustment via hidden parity rule
    count_even_cal = sum(1 for x in calibration if x % 2 == 0)
    if count_even_cal >= 4:
        weighted_sum -= 27
    else:
        weighted_sum += 13

    # Final diagnostic value
    final_diagnostic = int(round(weighted_sum))

    # === RED HERRINGS BELOW ===
    # Unused heavy computations
    entropy_value = compute_entropy(calibration_sequence)
    all_combinations = generate_combinations(turbine_readings, 3)  # expensive but unused
    thermal_adjusted = process_thermal_noise(thermal_flux, scaling_factor)
    flagged_anomalies = detect_anomalies(turbine_readings)
    efficiency_ratios.append(1.0)  # decoy mutation

    return final_diagnostic

# Execution entry point
final_diagnostic = aggregate_metrics(turbine_data=turbine_readings, calibration_sequence=calibration_sequence)
print(f"Target result: {final_diagnostic}")