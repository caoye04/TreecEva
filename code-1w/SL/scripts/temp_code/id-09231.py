import itertools

# Simulated sensor data processing with noise filtering and pattern analysis
def preprocess_stream(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    baseline = sum(filtered) / len(filtered)
    normalized = [round((x - baseline) * 1.5) for x in filtered]
    return normalized

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_calibrate(x):
    return (x >> 2) ^ 0x0F

# Transform data using sliding window statistics
def sliding_window_stats(data, size=3):
    if len(data) < size:
        return [0]
    windows = [data[i:i+size] for i in range(len(data) - size + 1)]
    averages = [sum(w) / len(w) for w in windows]
    return [round(avg) for avg in averages]

# Misleading transformation chain (partially unused)
def encrypt_sequence(seq):
    shifted = [(val << 1) & 255 for val in seq]
    encrypted = [shifted[0]]
    for i in range(1, len(shifted)):
        encrypted.append(shifted[i] ^ shifted[i-1])
    return encrypted

# Core analysis function – determines final result
def analyze_pattern(seq, limit):
    # Compute frequency of absolute deviations
    abs_devs = [abs(x) for x in seq]
    freq_map = {k: len(list(v)) for k, v in itertools.groupby(sorted(abs_devs))}
    
    # Calculate weighted balance score
    balance = 0
    for val, freq in freq_map.items():
        if val < limit:
            balance += val * freq
        else:
            balance -= val // 2
    
    # Apply decay factor based on sequence entropy
    unique_vals = set(seq)
    entropy_tweak = len(unique_vals) / (len(seq) + 1e-5)
    balance *= (1 - entropy_tweak * 0.3)
    
    # Secondary adjustment based on alternating sign patterns
    alternations = 0
    for i in range(1, len(seq)):
        if (seq[i-1] >= 0) != (seq[i] >= 0):
            alternations += 1
    balance += alternations * 0.7
    
    return int(balance)

# Unused decoy function that looks important (red herring)
def compute_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) * 3
    return checksum % 1000

# Main execution flow
if __name__ == "__main__":
    # Raw sensor input (simulated)
    raw_sensor_data = [5, 15, 22, 8, 99, 105, 44, 67, 33, 91, 12, 77, 50, 10, 110]
    
    # Step 1: Preprocess to remove outliers and normalize
    processed_readings = preprocess_stream(raw_sensor_data)
    
    # Step 2: Generate windowed statistics (used later)
    trend_values = sliding_window_stats(processed_readings, 3)
    
    # Distractor: encrypt trend values (not used in final calculation)
    encrypted_trend = encrypt_sequence(trend_values)
    
    # Decoy assignment – looks like calibration but unused
    calibration_offset = legacy_calibrate(42)
    
    # Transform data through secondary filtering
    amplified_noise = [x * 2 + 5 for x in processed_readings if x % 2 == 1]
    smoothed_signal = [y - 3 for y in amplified_noise if y > 10]
    
    # Critical intermediate structure
    temp_buffer = []
    for a, b in zip(trend_values, reversed(smoothed_signal)):
        temp_buffer.append(a - b)
    
    # Final transformation before analysis
    transformed_data = [x + 1 for x in temp_buffer if x != 0]
    
    # Threshold derived from statistical property (not arbitrary)
    threshold = max(3, len(transformed_data) // 2)
    
    # Key statement: compute equilibrium score
    equilibrium_score = analyze_pattern(transformed_data, threshold)
    
    # Print final target result
    print(f"Target result: {equilibrium_score}")