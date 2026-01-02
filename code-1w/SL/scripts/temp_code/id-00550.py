import math

# Simulated signal processing system for deep-space probe diagnostics
def generate_harmonics(base_freq, depth):
    return [base_freq * (i + 1) for i in range(depth)]

def evaluate_stability(signal_sequence, threshold=0.85):
    variance = sum((x - sum(signal_sequence)/len(signal_sequence))**2 for x in signal_sequence) / len(signal_sequence)
    max_val = max(signal_sequence)
    stability_score = (max_val - variance) / max_val
    return stability_score > threshold

# Irrelevant helper: computes theoretical bandwidth (not used in final result)
def calculate_bandwidth(frequency, modulation_index):
    return 2 * modulation_index * frequency + 10  # Unused red herring

# Signal transformation with conditional logic and distractors
def transform_signal(raw_data, mode='adaptive'):
    processed = []
    temp_offset = 0
    for idx, val in enumerate(raw_data):
        if idx % 3 == 0:
            temp_offset += idx * 0.1
        transformed = val * math.sin(idx) + temp_offset
        if mode == 'adaptive':
            transformed *= 1.1
        processed.append(abs(transformed))
    return processed

# Decoy function: looks important but unused
def encrypt_sequence(seq, key):
    return [x ^ (key % 256) for x in seq]

# Core diagnostic analyzer with combinatorial filtering
def filter_anomalies(data_stream):
    normal_range = (0.5, 95.0)
    filtered = []
    anomaly_count = 0
    for reading in data_stream:
        if not (normal_range[0] <= reading <= normal_range[1]):
            anomaly_count += 1
        else:
            filtered.append(reading * 1.05)
    # Distractor variable
    correction_factor = 1.0 if anomaly_count < 3 else 0.9
    return filtered

# Main analysis chain with nested logic and conditional expressions
def analyze_pattern(signals, key):
    # Step 1: Initial validation
    if not signals or len(signals) < 5:
        return -1
    
    # Step 2: Apply non-linear transformation
    adjusted = [x ** 0.5 * (1.1 if x > 10 else 0.9) for x in signals]
    
    # Step 3: Conditional filtering based on dynamic criteria
    limit = sum(adjusted) / len(adjusted) if len(adjusted) > 0 else 0
    narrowed = [x for x in adjusted if x >= limit * 0.7]
    
    # Step 4: Count valid phases using logical conditions
    phase_counter = 0
    for val in narrowed:
        is_coherent = val % 7 < 5
        meets_threshold = val > 4.2
        phase_counter += 1 if (is_coherent and meets_threshold) else 0
    
    # Step 5: Compute entropy-like metric (intermediate distractor)
    entropy_approx = 0.0
    if narrowed:
        avg = sum(narrowed) / len(narrowed)
        entropy_approx = sum(math.log(x / avg) for x in narrowed if x > 0) / len(narrowed)
    
    # Step 6: Final combinatorial decision using bit manipulation
    # Key-based control flow with masking
    control_mask = (key & 7) | 0x01
    raw_contribution = phase_counter * 25
    masked_result = raw_contribution & ~(control_mask << 2)
    
    # Step 7: Final adjustment with conditional expression
    base_value = masked_result if masked_result > 100 else 100
    final_score = base_value if entropy_approx > -1.5 else base_value - 20
    
    # Critical result variable
    final_diagnostic = int(final_score + (key % 10) * 2)
    
    # Dead code path - never executed due to above assignment
    if final_diagnostic < 0:
        final_diagnostic = 0
        
    return final_diagnostic

# === Execution Body ===

# Generate initial signal harmonics (real input)
system_harmonics = generate_harmonics(base_freq=17, depth=6)

# Apply real transformation
processed_signal = transform_signal(system_harmonics, mode='adaptive')

# Filter anomalies from processed data
collected_signals = filter_anomalies(processed_signal)

# System identifier key (used in analysis)
system_key = 0x5A3  # 1443 in decimal

# Irrelevant encryption attempt (dead end)
tampered = encrypt_sequence([int(x) for x in system_harmonics], system_key)

# UNUSED bandwidth calculations - red herrings
dummy_bandwidth_1 = calculate_bandwidth(1443, 2.5)
dummy_bandwidth_2 = calculate_bandwidth(867, 3.1)

# Central computation - answer derived here
final_diagnostic = analyze_pattern(collected_signals, system_key)

# Output result as required
print(f"Result: {final_diagnostic}")