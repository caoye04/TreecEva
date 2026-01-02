import itertools

# Simulated sensor array data from a distributed monitoring system
def acquire_sensor_data():
    raw_values = [18, 22, 19, 25, 30, 28, 21, 17]
    timestamps = list(range(1000, 1008))
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'OK', 'OK', 'WARNING', 'OK']
    return list(zip(raw_values, timestamps, statuses))

# Legacy function – only used for backward compatibility checks (distractor)
def legacy_normalization(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

# Signal conditioning with noise filtering and thresholding
def filter_noisy_readings(data, threshold=20):
    filtered = []
    noise_floor = 15
    for val, ts, status in data:
        if status == 'ERROR':
            continue  # Drop erroneous readings
        if val > noise_floor:
            corrected = val - 2 if val % 3 == 0 else val + 1  # arbitrary correction
            filtered.append(corrected)
    return filtered

# Advanced transformation using sliding window analysis
def sliding_window_transform(signal, window_size=3):
    if len(signal) < window_size:
        return [sum(signal)]
    transformed = []
    for i in range(len(signal) - window_size + 1):
        window = signal[i:i+window_size]
        avg = sum(window) / len(window)
        transformed.append(avg)
    return transformed

# Secondary analysis path – never called in main flow (dead code path)
def deprecated_analysis(sequence):
    result = 0
    for x in sequence:
        result ^= int(x * 10)  # bit manipulation red herring
    return result

# Frequency domain approximation using basic trigonometric sums (distractor)
def estimate_dominant_frequency(signal):
    import math
    N = len(signal)
    if N == 0:
        return 0.0
    frequencies = []
    for k in range(N // 2):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = math.sqrt(real**2 + imag**2)
        frequencies.append((k, magnitude))
    return max(frequencies, key=lambda x: x[1])[0] if frequencies else 0

# Core diagnostic logic chain
def compute_stability_index(values):
    if not values:
        return 0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5
    stability = 100 * (1 - (std_dev / (mean_val + 1)))  # normalize stability
    return round(stability, 4)

# Data fusion using itertools to generate combinations (relevant use)
def generate_consensus_groups(readings):
    groups = []    
    for r in range(2, min(5, len(readings)+1)):
        for combo in itertools.combinations(readings, r):
            groups.append(combo)
    # Only return some consensus groups based on criteria
    valid_groups = [g for g in groups if sum(g) % 2 == 1]  # odd-sum filtering
    return valid_groups[:10]  # limit output

# Final analysis pipeline
def analyze_readings(signal_chunk):
    if len(signal_chunk) == 0:
        return -999

    # Step 1: Apply window transform
    processed = sliding_window_transform(signal_chunk, window_size=3)
    
    # Step 2: Compute base metrics
    base_metric = sum(processed) / len(processed)
    
    # Step 3: Generate auxiliary data (partially irrelevant)
    dummy_pairs = [(a, b) for a in processed for b in processed if a > b]
    pair_xor_sum = 0
    for p in dummy_pairs:
        pair_xor_sum ^= (int(p[0]) & int(p[1]))  # bitwise distraction

    # Step 4: Use itertools-generated groups for redundancy check
    consensus = generate_consensus_groups([int(x) for x in processed])
    redundancy_score = len(consensus) * 0.75

    # Step 5: Calculate stability (this feeds into final result)
    stability = compute_stability_index(processed)
    
    # Step 6: Apply corrective weighting (key computation)
    adjustment_factor = 0.85 if len(processed) > 3 else 1.15
    adjusted_stability = stability * adjustment_factor
n    # Step 7: Final diagnostic calculation
    final_score = adjusted_stability + redundancy_score - (pair_xor_sum % 100)
    
    # Critical assignment point
    final_diagnostic = int(round(final_score))
    return final_diagnostic

# Irrelevant utility – simulates calibration but unused (decoy function)
def recalibrate_sensors(sensor_list, force=False):
    calibration_log = []
    for i, s in enumerate(sensor_list):
        if s[0] < 20:
            calibration_log.append(f"Sensor_{i}_recalibrated")
    return calibration_log

# Unused global constants (red herrings)
CALIBRATION_THRESHOLD = 0.97
MAX_ERROR_TOLERANCE = 5e-3
DEFAULT_SAMPLE_RATE = 44100

# Main execution flow
data_stream = acquire_sensor_data()
processed_signals = filter_noisy_readings(data_stream, threshold=20)
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")