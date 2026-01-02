import math

# Simulated sensor array data processing with diagnostic validation
def collect_sensor_data(baseline, threshold, mode):
    raw_signals = []
    for i in range(5):
        value = (baseline * (i + 1)) % 17
        if mode == 'calibrate':
            value = int(math.sqrt(value)) if value > 0 else 0
        elif mode == 'diagnose':
            value = value ** 2 % 13
        raw_signals.append(value)
    return raw_signals

def filter_noise(signal_list, cutoff):
    filtered = [x for x in signal_list if x >= cutoff]
    padding = [0] * (5 - len(filtered))
    return filtered[:5] + padding  # Ensure fixed length

def generate_checksum(sequence):
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum ^= (val + idx) & 0xF  # Simple bitwise checksum
    return checksum

def decode_frequency(signal_set, key):
    if len(signal_set) < 4:
        return 0
    product = 1
    for s in signal_set[:4]:
        product *= (s + 1)
    return (product // 4) % 1000

def analyze_pattern(input_signals, auth_key):
    # Core analysis logic
    normalized = [x % 10 for x in input_signals]
    
    # Irrelevant transformation branch (dead path due to fixed mode)
    transform_mode = 'none'
    temp_buffer = []
    if transform_mode == 'fft':  # Never executed
        temp_buffer = [complex(x, -x) for x in normalized]
    elif transform_mode == 'wavelet':
        temp_buffer = [x * 2 for x in normalized]

    # Distractor: unused statistical computation
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in normalized) / len(normalized)

    # Key set operation: detect recurring magnitude patterns
    magnitude_set = set(normalized)
    pattern_pool = {x for x in magnitude_set if x in {2, 4, 6, 8}}  # Even magnitudes

    # Conditional expression chain with red herring variables
    adjustment = 10 if len(pattern_pool) >= 3 else (5 if len(pattern_pool) == 2 else 2)
    scaling_factor = adjustment if auth_key & 0x1 else adjustment * 2
    
    # Decoy cryptographic simulation (no effect on output)
    encrypted_flag = ''
    if auth_key > 0:
        masked = auth_key ^ 0xDEADBEEF
        encrypted_flag = ''.join([hex(masked >> (i*8) & 0xFF) for i in range(3)])

    # Actual computation path
    base_score = sum(normalized) * scaling_factor
    bonus = 0
    
    # Conditional bonus based on set characteristics
    if 7 in magnitude_set and len(magnitude_set.intersection({1, 3, 5})) >= 2:
        bonus += 25
    elif len(magnitude_set) == len(normalized):  # All unique
        bonus += 15
    
    # Final result influenced by checksum side-channel
    integrity_check = generate_checksum(normalized)
    frequency_marker = decode_frequency(normalized, auth_key)
    
    # Critical red herring: irrelevant loop modifying unused variable
    accumulator = 0
    for _ in range(100):
        accumulator += (integrity_check * frequency_marker) % 19
        accumulator %= 1000

    # True result formation
    final_value = base_score + bonus
    final_value -= (integrity_check % 7) * 3  # Minor correction

    # Answer-carrying variable
    final_diagnostic = int(final_value)
    return final_diagnostic

# Main execution sequence
if __name__ == '__main__':
    # Initial parameters
    system_baseline = 11
    activity_threshold = 3
    operation_mode = 'diagnose'

    # Step 1: Collect raw signals
    collected_signals = collect_sensor_data(system_baseline, activity_threshold, operation_mode)
    
    # Step 2: Apply noise filtering
    filtered_signals = filter_noise(collected_signals, activity_threshold)
    
    # Step 3: Prepare security context (used in analysis)
    system_key = (system_baseline ^ 0xABC) & 0xFFFF
    
    # Step 4: Run diagnostic analysis
    final_diagnostic = analyze_pattern(filtered_signals, system_key)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")