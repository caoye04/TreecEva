def process_telemetry_stream(raw_data):
    # Irrelevant signal filtering (distractor)
    filtered_signals = [x * 0.98 + 2.1 for x in raw_data if x > 5]
    noise_floor = sum(filtered_signals) / len(filtered_signals) if filtered_signals else 0

    # Core diagnostic hash computation (relevant)
    cumulative_hash = 0
    for val in raw_data:
        cumulative_hash ^= (val << 2)
        cumulative_hash &= 0xFFFF  # Keep within 16-bit range

    return cumulative_hash


def validate_checksum(sequence):
    # Complex but ultimately unused validation routine (dead path)
    if not sequence:
        return False
    weighted_sum = sum((i + 1) * v for i, v in enumerate(sequence))
    checksum = weighted_sum % 257
    return checksum == 131


def decode_priority_flag(encoded_flag):
    # Misleading flag decoding (partially relevant)
    flags = {
        'CRITICAL': (encoded_flag & 0b1000) >> 3,
        'WARNING': (encoded_flag & 0b0100) >> 2,
        'INFO': (encoded_flag & 0b0010) >> 1,
        'DEBUG': (encoded_flag & 0b0001)
    }
    # Only 'CRITICAL' bit is actually used later
    return flags['CRITICAL']


def compute_entropy(values):
    # Unused statistical analysis (red herring)
    from math import log2
    if not values:
        return 0.0
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 6)


def analyze_fault_sequence(log_data, flags_dict):
    # Key function with critical logic steps
    base_signature = process_telemetry_stream(log_data)
    
    # Bit manipulation chain
    temp_sig = base_signature
    temp_sig ^= 0xABCD
    temp_sig = ((temp_sig << 3) | (temp_sig >> 13)) & 0xFFFF
    temp_sig ^= temp_sig >> 5
    temp_sig &= 0x7FFF  # Clear highest bit

    # Conditional data transformation
    if flags_dict.get('override_mode', False):
        temp_sig += 1000
    elif decode_priority_flag(flags_dict.get('priority_code', 0)):
        temp_sig += 250
    else:
        temp_sig -= 75

    # Dictionary-based state resolution
    state_map = {
        0: 100, 1: 200, 2: 300, 3: 400, 4: 500
    }
    state_key = (temp_sig // 250) % 5
    adjustment = state_map.get(state_key, 0)

    # Final composite calculation
    intermediate = (temp_sig ^ adjustment) + (adjustment & 0xFF)
    final_value = (intermediate * 3) // 4

    # Unused alternate path (decoy)
    if validate_checksum(log_data):
        alt = compute_entropy(log_data)
        final_value = int(alt * 1000)

    return final_value

# Simulated telemetry input (real data)
telemetry_log = [12, 45, 67, 23, 89, 34, 78]
system_flags = {
    'priority_code': 8,  # Triggers CRITICAL (bit 3 set)
    'override_mode': False,
    'debug_enabled': True,
    'timeout_count': 3,
    'last_reset': '2023-08-01'
}

# Execution point of interest
final_diagnostic = analyze_fault_sequence(telemetry_log, system_flags)
print(f"Result: {final_diagnostic}")