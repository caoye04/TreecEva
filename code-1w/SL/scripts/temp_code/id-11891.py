def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]


def decode_quantum_signature(registers):
    accumulator = 0
    for i, reg in enumerate(registers):
        accumulator ^= (reg * (i + 1)) & 255
    return accumulator + 17


def calculate_entropy(sequence):
    from math import log2
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = sum(-freq / total * log2(freq / total) for freq in freq_map.values())
    return round(entropy, 4)


def validate_checksum(data_block):
    checksum = 0
    for val in data_block:
        checksum = (checksum + val) % 257
    return checksum == 98


def analyze_system_state(registers, calib):
    # Core logic path
    base_metric = sum(registers) % 1000
    
    # Irrelevant transformation chain
    temp_buffer = [r ^ 42 for r in registers]
    encoded_str = ''.join([chr(r % 90 + 33) for r in temp_buffer[:5]])
    str_analysis = {"length": len(encoded_str), "special": encoded_str.count('@')}
    
    # Distractor: complex but unused calculation
    phantom_score = 0
    for k, v in calib.items():
        if len(k) % 2 == 0:
            phantom_score += v ** 2
    phantom_score = int(phantom_score / (len(calib) or 1))
    
    # Meaningful intermediate
    trigger_threshold = calib.get('threshold', 50) * calib.get('gain', 1.2)
    
    # Another decoy branch
    if len(registers) > 10:
        aggregation = 0
        for r in registers:
            aggregation += r << 2
        aggregation >>= 3

    # Key signal processing
    processed_registers = [r & 0xFF for r in registers]
    signature = decode_quantum_signature(processed_registers)
    
    # Conditional mutation based on hidden rule
    if signature % 3 == 0 and base_metric > trigger_threshold:
        base_metric *= 2
    elif signature % 3 == 1:
        base_metric += 113
    else:
        base_metric -= 47
    
    # Final red herring
    audit_log = {
        "timestamp": "2024-01-01T00:00:00Z",
        "source": "QPU-A7",
        "valid": validate_checksum(registers),
        "debug_info": preprocess_signal([0.12, 0.33, 0.05, 0.81])
    }
    
    # Actual result computation
    entropy_value = calculate_entropy(processed_registers)
    final_diagnostic = (base_metric + signature) - int(entropy_value * 100)
    
    # Dead code - never reached
    if final_diagnostic < 0:
        raise RuntimeError("Negative diagnostic")
    
    return final_diagnostic

# Initialization data
quantum_registers = [123, 45, 67, 89, 101, 112, 13, 57, 211, 7]

# Calibration dictionary with mixed relevant/irrelevant keys
calibration_data = {
    "threshold": 7,
    "gain": 9.0,
    "offset_x": 0.001,
    "damping_factor": 2.3,
    "mode_flag": True,
    "legacy_id": 888
}

# Trigger execution
final_diagnostic = analyze_system_state(quantum_registers, calibration_data)
print(f"Result: {final_diagnostic}")