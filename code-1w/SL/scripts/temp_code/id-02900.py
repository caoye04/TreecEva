from collections import defaultdict, Counter

# Simulated quantum state telemetry data
def generate_quantum_sequence(length):
    seq = []
    for i in range(length):
        if i % 5 == 0:
            seq.append((i * 2) ^ 3)
        elif i % 3 == 0:
            seq.append((i + 1) ** 2)
        else:
            seq.append(i - (i % 7))
    return seq

# Irrelevant helper: computes harmonic mean (not used in final result)
def harmonic_mean(arr):
    total = 0.0
    for x in arr:
        if x != 0:
            total += 1 / x
    return len(arr) / total if total != 0 else 0

# Decoy function: appears important but unused
def calculate_entropy(data):
    freq = Counter(data)
    entropy = 0.0
    n = len(data)
    for count in freq.values():
        p = count / n
        entropy -= p * (p ** 0.5)  # Not actual entropy
    return round(entropy, 6)

# Misleading diagnostic chain
def false_diagnostic(signal, flags):
    temp_state = 0
    for i, val in enumerate(signal):
        if i % 4 == 0 and val > 5:
            temp_state += (val & 7) * flags.get('mode', 1)
        elif val < 0:
            temp_state -= (val ^ 2) // 3
    return temp_state * 2  # Red herring result

# Core analysis with distractors embedded
def analyze_system_state(sequence, config):
    # Distractor variables
    shadow_buffer = [x ^ 5 for x in sequence if x % 4 != 2]
    audit_trail = defaultdict(int)
    
    # Real computation begins
    filtered = [x for x in sequence if x > 0 and (x | 3) % 5 < 4]
    
    # Multiple layers of transformation
    transformed = []
    for idx, val in enumerate(filtered):
        if idx % 2 == 0:
            transformed.append(val * 3 + 2)
        else:
            transformed.append(val + (idx & 3))
    
    # Accumulation with conditional logic
    accumulator = 0
    for i, v in enumerate(transformed):
        if config['active'] and v % 2 == 1:
            accumulator += v * (i % 4 + 1)
        elif v % 7 == 0:
            accumulator -= v // 7
    
    # Dead code path - never executed due to config
    if config.get('legacy_mode'):
        backup = sum(shadow_buffer) // 10
        accumulator = max(accumulator, backup)
    
    # Secondary processing on distractor structure (misleading)
    decoy_sum = 0
    for a, b in zip(shadow_buffer, reversed(shadow_buffer)):
        decoy_sum += (a & b) ^ 1
        if decoy_sum > 1000:  # Threshold never reached
            break
    
    # Final adjustment based on bit patterns
    bit_analysis = 0
    for num in transformed:
        ones = bin(num).count('1')
        zeros = bin(num).count('0')
        if ones >= zeros:
            bit_analysis += ones * 2
        else:
            bit_analysis -= zeros // 2
    
    # Key result formation (combines real path only)
    base_result = accumulator + bit_analysis
    calibration = config.get('calibration_offset', -4)
    final_score = base_result + calibration
    
    # Critical red herring: looks like final output but isn't
    temp_diagnostic = (final_score ^ 256) - len(shadow_buffer)
    
    # Actual target variable
    final_diagnostic = abs(final_score) + config['version']
    
    # Unused trace
    log_entry = f"Diag:{final_diagnostic}, Temp:{temp_diagnostic}, Size:{len(transformed)}"
    
    return final_diagnostic

# Main execution with distractions
if __name__ == '__main__':
    # Initialize system telemetry
    quantum_sequence = generate_quantum_sequence(64)
    
    # Configuration with misleading fields
    system_flags = {
        'active': True,
        'version': 7,
        'calibration_offset': -4,
        'mode': 3,
        'debug_trace': True,
        'timeout_ms': 500,
        'buffer_limit': 1024,
        # Legacy key included to tempt usage
        'legacy_mode': False
    }
    
    # Compute irrelevant metrics (distractors)
    mean_val = sum(quantum_sequence) / len(quantum_sequence)
    peak = max(quantum_sequence)
    variance_proxy = sum((x - mean_val) ** 2 for x in quantum_sequence) / len(quantum_sequence)
    
    # Call decoy function to increase interference
    _ = calculate_entropy(quantum_sequence[:10])
    
    # Real critical computation
    intermediate = false_diagnostic(quantum_sequence, system_flags)
    final_diagnostic = analyze_system_state(quantum_sequence, system_flags)
    
    # Print only the required result
    print(f"Target result: {final_diagnostic}")