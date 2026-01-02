import math

# Simulated sensor array data processing with diagnostic logic
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if x > -50 and x < 150]
    baseline = sum(filtered) / len(filtered)
    normalized = [val - baseline for val in filtered]
    return normalized

# Irrelevant helper - decoy function (dead path)
def deprecated_calibrate(x):
    return (x * 0.98) + 1.2

# Core transformation function
def apply_fourier_shift(data, phase):
    transformed = []
    for i, val in enumerate(data):
        shifted = val * math.sin(i + phase)
        transformed.append(round(shifted, 6))
    return transformed

# Misleading auxiliary computation (unused final result)
def compute_entropy(arr):
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(arr)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Data fusion from multiple channels (red herring variables included)
def fuse_signals(primary, secondary):
    fused = []
    weights = [0.7, 0.3]
    for i in range(min(len(primary), len(secondary))):
        fused.append(weights[0] * primary[i] + weights[1] * secondary[i])
    padding = [0] * abs(len(primary) - len(secondary))
    return fused + padding

# Real pattern analyzer (used in final step)
def analyze_pattern(seq, limit):
    if not seq:
        return 0
    
    # Extract peaks above threshold
    peaks = [x for x in seq if abs(x) > limit]
    
    # Compute alternating sum with index-based sign
    alt_sum = 0
    for idx, val in enumerate(peaks):
        alt_sum += val if idx % 2 == 0 else -val
    
    # Apply decay factor based on peak density
    density = len(peaks) / len(seq) if seq else 0
    decay_factor = math.exp(-2 * density)
    
    intermediate_result = alt_sum * decay_factor
    
    # Secondary validation via bit metric (bit manipulation red herring)
    bit_score = 0
    int_rep = int(abs(intermediate_result) * 1000) % 1024
    for _ in range(8):
        bit_score += int_rep & 1
        int_rep >>= 1
    
    # Final adjustment using conditional expression
    final_value = intermediate_result if bit_score > 3 else intermediate_result / 2
    return round(final_value, 6)

# Unused signal generation (distractor)
def generate_test_tone(freq, duration):
    import random
    random.seed(42)
    return [math.sin(freq * t) + random.uniform(-0.1, 0.1) for t in range(duration)]

# Main execution flow
if __name__ == '__main__':
    raw_sensor_data = [120, -30, 45, 88, -22, 91, 134, -48, 67, 73, 141, -15, 58, 82]
    
    # Step 1: Preprocess the sensor readings
    cleaned_data = preprocess_readings(raw_sensor_data)
    
    # Step 2: Apply Fourier-like transformation
    transformed_data = apply_fourier_shift(cleaned_data, phase=1.57)
    
    # Step 3: Fictitious secondary channel (never actually fused)
    dummy_auxiliary = [-0.3, 0.4, -0.1, 0.8, -0.6, 0.2, 0.7, -0.5]
    
    # Step 4: Compute meaningless entropy (distraction)
    _ = compute_entropy([int(x*100) for x in transformed_data if x != 0])
    
    # Step 5: Determine dynamic threshold
    base_threshold = 1.8
    adjustment_factor = 0.15 if len(transformed_data) > 6 else 0.05
    threshold = base_threshold + adjustment_factor
    
    # Step 6: Analyze final diagnostic pattern
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")