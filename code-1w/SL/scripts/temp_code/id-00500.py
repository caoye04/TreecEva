import itertools

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if x > -50 and x < 300]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]
    return normalized

# Irrelevant transformation: frequency domain red herring
def fft_approx(data):
    result = []
    for i in range(len(data)):
        temp = 0
        for j in range(len(data)):
            temp += data[j] * (i + 1)  # Not a real FFT, just distraction
        result.append(temp % 100)
    return result

# Core pattern detection logic
def detect_cycles(signal):
    cycles = 0
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            cycles += 1
    return cycles

# Matrix-based weighting (used later)
def generate_key_matrix(seeds):
    matrix = [[(i * seeds[0] + j * seeds[1]) % 7 for j in range(3)] for i in range(3)]
    return matrix

# Data transformation chain
def transform_sequence(seq, factor):
    shifted = [(x * factor) % 89 for x in seq]
    reversed_chunks = [shifted[i:i+3][::-1] for i in range(0, len(shifted), 3)]
    flattened = list(itertools.chain.from_iterable(reversed_chunks))
    return [flattened[i] + i%5 for i in range(len(flattened))]

# Main analysis function
def analyze_pattern(data, weights):
    weighted_sum = 0
    for i, val in enumerate(data):
        contribution = val * weights[i % 3][i % 3]
        weighted_sum += contribution
    base_score = int(weighted_sum / len(data))
    
    # Secondary metric: entropy-like measure (distraction)
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0
    for count in freq_map.values():
        p = count / len(data)
        entropy -= p * p  # Simplified, not used in final result
    
    # Tertiary check: palindrome structure (unused)
    mid = len(data) // 2
    is_palindrome = data[:mid] == data[:-mid-1:-1]  # Dead code path
    
    # Actual decision logic
    cycle_count = detect_cycles(data)
    if cycle_count > 5:
        adjustment = 17
    else:
        adjustment = -23
    
    # Final computation
    intermediate = base_score * (cycle_count + 1)
    final_value = intermediate + adjustment
    return final_value

# --- Execution Block ---
if __name__ == "__main__":
    # Real input data
    sensor_log = [127, 89, 201, 45, 153, 77, 188, 65, 142, 98, 131, 117, 104]
    
    # Irrelevant variables and decoy operations
    calibration_offsets = [-3.2, 1.8, 4.5, -2.1, 0.9]
    baseline_checksum = sum(calibration_offsets) * 1000  # Unused
    temporal_flags = {f"t{i}": False for i in range(5)}  # Dead data structure
    
    # Processing pipeline
    cleaned = preprocess_readings(sensor_log)
    transformed_data = transform_sequence([int(x) for x in cleaned], 1.7)
    
    # Unused alternative processing branch
    spectral_analysis = fft_approx(transformed_data)  # Distractor
    peak_magnitude = max(spectral_analysis) if spectral_analysis else 0  # Misleading
    
    # Key parameters
    seed_group = [13, 19]
    key_matrix = generate_key_matrix(seed_group)
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, key_matrix)
    
    # Output target
    print(f"Result: {final_diagnostic}")