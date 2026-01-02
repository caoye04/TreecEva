import math

# Simulated sensor calibration and diagnostic analysis
# Mix of relevant signal processing, red herrings, and complex data transformations

def generate_noise_profile(size):
    return [math.sin(i * 0.1) + 0.5 for i in range(size)]

# Irrelevant function: simulates temperature drift (not used in final result)
def compute_thermal_drift(samples):
    base = [1.0 + 0.01 * i for i in range(len(samples))]
    return [samples[i] * base[i] for i in range(len(samples))]

# Decoy transformation: looks important but unused
def apply_frequency_shift(signal, shift=0.3):
    return [val * math.cos(shift) for val in signal]

# Core metric processor: actually used
def extract_amplitude_envelope(signal):
    envelope = []
    for x in signal:
        if x >= 0:
            envelope.append(math.sqrt(x))
        else:
            envelope.append(-math.sqrt(abs(x)))
    return envelope

def calculate_entropy(values):
    norm = sum(abs(v) for v in values)
    if norm == 0:
        return 0.0
    probs = [abs(v) / norm for v in values]
    entropy = 0.0
    for p in probs:
        if p > 0:
            entropy -= p * math.log(p)
    return entropy

# Unused recursive decoy
def binary_partition_sum(data, depth=0):
    if depth >= 3 or len(data) <= 1:
        return sum(data)
    mid = len(data) // 2
    left = binary_partition_sum(data[:mid], depth + 1)
    right = binary_partition_sum(data[mid:], depth + 1)
    return left * 0.7 + right * 1.3

# Key processing function
def process_metrics(sequence, config_map):
    # Step 1: Extract critical bands
    band_a = [x for i, x in enumerate(sequence) if i % 3 == 0]
    band_b = [x for i, x in enumerate(sequence) if i % 3 == 1]
    
    # Step 2: Apply envelope detection
    env_a = extract_amplitude_envelope(band_a)
    env_b = extract_amplitude_envelope(band_b)
    
    # Step 3: Compute cross-correlation at lag 1
    min_len = min(len(env_a), len(env_b)) - 1
    correlation = 0.0
    for i in range(min_len):
        correlation += env_a[i] * env_b[i + 1]
    correlation /= min_len if min_len > 0 else 1
    
    # Step 4: Use config_map to weight metrics
    weight_x = config_map['alpha'] * 0.8
    weight_y = config_map['beta'] * 1.25
    
    # Step 5: Calculate entropy of transformed bands
    entropy_x = calculate_entropy(env_a)
    entropy_y = calculate_entropy(env_b)
    
    # Step 6: Combine with non-linear interaction
    interaction = abs(correlation) ** 1.5
    
    # Step 7: Apply weighted fusion (this determines final_diagnostic)
    result = weight_x * entropy_x + weight_y * entropy_y * interaction
    
    # Red herring: unused derived values
    spurious_index = sum(math.tanh(x) for x in env_a[:5]) * math.pi
    auxiliary_score = binary_partition_sum([int(100*x) for x in env_b[:8]])
    
    # Final computation
    result *= 1.75  # Final scaling factor
    return round(result, 6)

# --- Main execution ---
if __name__ == "__main__":
    # Generate realistic input sequence
    raw_input = [0.1 * i * math.cos(0.2 * i) for i in range(1, 26)]
    
    # Add noise profile (actually used)
    noise = generate_noise_profile(25)
    calibration_sequence = [raw_input[i] + 0.05 * noise[i] for i in range(25)]
    
    # Threshold configuration (used in process_metrics)
    thresholds = {
        'alpha': 2.3,
        'beta': 1.7,
        'gamma': 0.9  # unused parameter (decoy)
    }
    
    # Dead code path - never executed
    if False:
        dummy = [math.asin(x) for x in calibration_sequence if abs(x) <= 1]
        temp_result = compute_thermal_drift(dummy)
    
    # Key statement
    final_diagnostic = process_metrics(calibration_sequence, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")