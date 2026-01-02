import math

# Simulated quantum telemetry processing with diagnostic validation
def generate_quantum_signature(base_sequence, depth):
    signature = []
    temp_val = base_sequence
    for i in range(depth):
        if i % 3 == 0:
            temp_val = (temp_val * 2) ^ 5
        elif i % 5 == 0:
            temp_val = int(math.sqrt(abs(temp_val) + 1)) * 3
        else:
            temp_val = (temp_val + i) | 7
        signature.append(temp_val)
    # Distractor: unused transformation
    reversed_sig = [x ^ 255 for x in signature[::-1]]
    return signature

def validate_calibration_frame(frame_data, threshold=10000):
    calibrated = 0
    checksum = 1
    for val in frame_data:
        if val > threshold:
            calibrated += 1
            checksum *= (val % 17)
    # Dead code path (never executed due to logic)
    if calibrated < 0:
        checksum = -checksum
    return calibrated > 5

def decode_entropy_pattern(raw_data):
    # Real computation branch
    pattern = []
    for x in raw_data:
        if x % 2 == 0:
            pattern.append(int(math.log(x + 1, 2)))
        else:
            pattern.append(x & (x + 1))
    # Irrelevant transformation chain
    temp_dict = {i: (p ** 2) % 100 for i, p in enumerate(pattern)}
    processed = sum(p * (i + 1) for i, p in enumerate(pattern))
    normalization_factor = max(pattern) if pattern else 1
    normalized = processed / normalization_factor if normalization_factor != 0 else 0
    return int(normalized)

def build_system_fingerprint(log_entries):
    fingerprint_map = {}
    total_entries = len(log_entries)
    error_count = 0
    warning_hash = 0
    for idx, entry in enumerate(log_entries):
        severity = entry.get('level', 'INFO')
        code = entry.get('code', 0)
        timestamp = entry.get('ts', 0)
        # Real usage
        if severity == 'ERROR':
            error_count += 1
            warning_hash ^= code
        # Dictionary operation red herring
        fingerprint_map[idx] = {
            'hash': (code * timestamp) % 997,
            'type': severity.lower(),
            'flag': (idx + code) % 4 == 0
        }
    # Another decoy structure
    audit_trail = {f"entry_{i}": {'valid': False} for i in range(0, total_entries, 3)}
    # Actual return signal
    return error_count * 1000 + warning_hash

def analyze_system_state(sequence, log):
    # Core logic step 1: process quantum sequence
    sig = generate_quantum_signature(sequence, 8)
    
    # Core logic step 2: extract entropy metric
    entropy_metric = decode_entropy_pattern(sig)
    
    # Core logic step 3: get system fingerprint
    fp = build_system_fingerprint(log)
    
    # Core logic step 4: calibration check (returns boolean, not used directly)
    calibrated = validate_calibration_frame(sig, threshold=20000)
    
    # Core logic step 5: compute diagnostic level
    diagnostic_level = entropy_metric + (fp // 100)
    
    # Distractor variables and computations
    baseline_ref = 0
    for x in sig[:4]:
        baseline_ref += (x % 10) * 16
    anomaly_buffer = [x for x in sig if x > 1000]
    buffer_score = sum(anomaly_buffer) // len(anomaly_buffer) if anomaly_buffer else 0
    
    # Decoy function call with no side effects
    def simulate_redundant_check(data):
        return sorted(set((d ^ 15) % 100 for d in data))
    
    _ = simulate_redundant_check(sig)
    
    # Final computation - only this matters
    adjustment = len([x for x in sig if x % 4 == 0])
    final_diagnostic = diagnostic_level + adjustment - (fp % 100)
    
    # Critical print statement for observability
    return final_diagnostic

# Input data setup
quantum_sequence = 137
system_log = [
    {'ts': 1623456780, 'code': 5001, 'level': 'ERROR'},
    {'ts': 1623456789, 'code': 5002, 'level': 'WARNING'},
    {'ts': 1623456795, 'code': 5001, 'level': 'ERROR'},
    {'ts': 1623456801, 'code': 4003, 'level': 'ERROR'},
    {'ts': 1623456810, 'code': 4003, 'level': 'ERROR'},
    {'ts': 1623456815, 'code': 5002, 'level': 'ERROR'},
    {'ts': 1623456820, 'code': 6005, 'level': 'INFO'},
    {'ts': 1623456825, 'code': 6005, 'level': 'INFO'}
]

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_sequence, system_log)
print(f"Target result: {final_diagnostic}")