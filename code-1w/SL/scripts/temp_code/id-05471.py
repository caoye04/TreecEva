import itertools

# Simulated sensor data processing with diagnostic logic
def preprocess_signal(raw_samples, threshold=100):
    filtered = []
    accumulator = 0
    for sample in raw_samples:
        if abs(sample) > threshold:
            accumulator += sample // 4
        else:
            accumulator += sample % 7
    return accumulator + len(raw_samples)

# Irrelevant helper - dead code path (distractor)
def deprecated_filter(sequence):
    return [x for x in sequence if x & 1]  # Only odd numbers

# Misleading transformation chain
def transform_sequence(seq, mode='legacy'):
    temp_result = 0
    for i, val in enumerate(seq):
        if mode == 'legacy':
            temp_result ^= (val * i) % 15
        elif mode == 'modern':
            temp_result += (val + i) ** 2
    return temp_result

# Core analysis function (used)
def compute_entropy(signal):
    counts = {}
    for x in signal:
        key = x % 5
        counts[key] = counts.get(key, 0) + 1
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 6)

# Secondary computation - appears important but only partially used
def generate_calibration_profile(base_factor):
    profile = []
    for i in range(3):
        profile.append((base_factor + i) ** 2 % 23)
    return profile  # Only last element is actually used

# Main diagnostic engine
def analyze_signal(buffer, factor):
    # Step 1: Preprocess input
    prep_value = preprocess_signal(buffer)
    
    # Step 2: Compute entropy (relevant)
    entropy_metric = compute_entropy(buffer)
    
    # Step 3: Generate calibration (partial use)
    profile = generate_calibration_profile(factor)
    adjusted_factor = profile[-1]  # Only last element matters
    
    # Step 4: Transform with decoy logic
    transformed = transform_sequence(buffer, mode='legacy')  # Used in final calc
    
    # Step 5: Simulate hardware response (mixed relevance)
    response_curve = []
    for i in range(5):
        point = (prep_value + i * adjusted_factor) % 17
        response_curve.append(point)
    
    # Step 6: Aggregate multiple signals
    aggregate = prep_value
    for cycle in range(2):
        aggregate = (aggregate * 31) % 10007
        if cycle == 0:
            aggregate += int(entropy_metric * 100)
    
    # Step 7: Apply bitwise conditioning
    masked = aggregate & 0xFFFF
    shifted = (masked >> 4) | (masked << 12)
    masked = shifted & 0xFFFF
    
    # Step 8: Final integration with distractors
    decoy_sum = sum(itertools.accumulate([adjusted_factor, transformed % 100, len(response_curve)]))
    # But only 'transformed' is truly needed here
    final_score = (masked ^ transformed) % 5000
    
    # Final adjustment using entropy (subtle but critical)
    adjustment = int(entropy_metric * 10) % 7
    final_diagnostic = final_score + adjustment
    
    return final_diagnostic

# --- Execution Context ---
if __name__ == '__main__':
    # Sensor input data
    pattern_buffer = [12, -45, 67, 89, -23, 44, 13, 5, 91, 77]
    calibration_factor = 17
    
    # Dead variable assignments - red herrings
    baseline_ref = deprecated_filter(pattern_buffer)
    legacy_mode_checksum = transform_sequence(pattern_buffer, mode='modern')
    debug_trace = generate_calibration_profile(calibration_factor)  # Unused
    
    # Key execution point
    final_diagnostic = analyze_signal(pattern_buffer, calibration_factor)
    
    # Output result
    print(f"Target result: {final_diagnostic}")