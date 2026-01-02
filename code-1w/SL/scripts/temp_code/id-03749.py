import math

def preprocess_sensor_data(raw_data):
    # Irrelevant preprocessing (dead path)
    normalized = [x / max(raw_data) for x in raw_data]
    filtered = [x for x in normalized if x > 0.1]
    return [round(x * 100) for x in filtered]

def compute_entropy(sequence):
    # Distractor function: looks important but unused in final result
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def shift_cipher(text, shift):
    # Red herring: string manipulation with no impact
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def validate_checksum(data_chunk):
    # Looks critical but only used in decoy branch
    checksum = 0
    for i, val in enumerate(data_chunk):
        checksum ^= (val + i) * 3
    return checksum % 256

def decode_quantum_signature(signature):
    # Unused complex transformation (misleading)
    decoded = 0
    for i, bit in enumerate(signature):
        decoded += bit << (i % 8)
    return decoded ^ 0xFF

def analyze_phase_shift(readings):
    # Relevant but indirect: contributes to control flow
    squared_sum = sum([x ** 2 for x in readings])
    magnitude = math.sqrt(squared_sum)
    return int(magnitude // 10)

def evaluate_coherence(state_vector):
    # Contributes one input to final logic
    if not state_vector:
        return 0
    avg = sum(state_vector) / len(state_vector)
    deviance = sum([abs(x - avg) for x in state_vector])
    return int(deviance // 5)

def analyze_system_state(readings, flags):
    # Core logic with embedded distractors
    
    # Irrelevant block: dead computation
    temp_analysis = []
    for r in readings:
        if r % 7 == 0:
            temp_analysis.append(r * 2)
    temp_checksum = sum(temp_analysis) % 1000
    
    # Meaningful intermediate: actual dependency
    phase_index = analyze_phase_shift(readings)
    coherence_score = evaluate_coherence(readings)
    
    # Distractor: complex-looking but unused dict
    diagnostic_map = {
        'levels': [readings[i] - readings[i-1] for i in range(1, len(readings))],
        'peaks': [x for x in readings if x > 50],
        'bins': {i: 0 for i in range(10)},
        'meta': {'version': '2.1', 'calibrated': False}
    }
    
    # Another red herring variable
    security_token = shift_cipher("system_ready", coherence_score % 13)
    
    # Key branching logic with conditional expression
    base_diagnostic = phase_index * 17 if flags['stabilized'] else phase_index * 3
    
    # Final computation chain
    adjustment_factor = 0
    if flags['overclocked']:
        adjustment_factor += 29
    if len(readings) > 6:
        adjustment_factor += 11
    
    # Critical statement
    final_diagnostic = base_diagnostic + coherence_score * adjustment_factor
    
    # Dead assignment (distractor)
    final_diagnostic = final_diagnostic ^ 0x55 if temp_checksum < 500 else final_diagnostic
    
    return final_diagnostic

# Simulated sensor inputs (real data)
quantum_readings = [12, 18, 24, 36, 48, 54, 72]
system_flags = {
    'stabilized': True,
    'overclocked': False,
    'encrypted': True,
    'legacy_mode': False
}

# Unused variables to increase interference
baseline_profile = preprocess_sensor_data([5, 10, 15, 20, 25])
entropy_value = compute_entropy([1, 1, 0, 0, 1, 1, 1])
auth_code = validate_checksum([255, 128, 64, 32])
quantum_sig = decode_quantum_signature([1, 0, 1, 1, 0, 0, 1])

cipher_test = shift_cipher("debug_mode", 7)

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_readings, system_flags)

print(f"Result: {final_diagnostic}")