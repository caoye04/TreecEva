def process_signal_chain(raw_samples, threshold=0.75):
    filtered = [x for x in raw_samples if abs(x) > threshold]
    energy = sum(x**2 for x in filtered)
    return energy / len(filtered) if filtered else 0

# Irrelevant signal processing functions (distractors)
def apply_noise_gate(signal, level=0.1):
    return [s for s in signal if abs(s) > level]  # Unused

def compute_coherence(a, b):
    return sum(i * j for i, j in zip(a, b))  # Dead code path

def detect_harmonic_distortion(waveform):
    harmonics = []
    for i in range(2, 6):
        harmonics.append(sum(w ** i for w in waveform[:10]) % 4)
    return harmonics  # Never called

# Core diagnostic system
status_codes = {
    'OK': 0,
    'WARNING': 1,
    'FAULT': 2,
    'CRITICAL': 3
}

def log_event(timestamp, code, priority=1):
    return {'ts': timestamp, 'code': code, 'priority': priority, 'meta': False}

def validate_sequence(integrity_check):
    base_score = 0
    for c in integrity_check:
        base_score += ord(c) % 7
    return base_score % 5 == 0

def generate_audit_trace(entries):
    trace = {}
    for i, e in enumerate(entries):
        trace[i] = {'raw': e['code'], 'flag': e['priority'] > 2}
    return trace  # Distractor structure

def analyze_fault_sequence(log):
    # Key logic hidden among noise
    critical_count = 0
    total_priority = 0
    sequence_valid = validate_sequence(''.join(str(e['ts']) for e in log))
    
    temp_accum = 0
    for entry in log:
        if entry['code'] == status_codes['CRITICAL']:
            critical_count += 1
            total_priority += entry['priority']
        temp_accum ^= entry['ts'] % 8  # Red herring operation
    
    # Decoy block: looks important but unused
    audit = generate_audit_trace(log)
    fake_diagnostic = len(audit) * 17
    
    # Real answer computation buried here
    if sequence_valid and critical_count > 0:
        result = (total_priority * 1000) + (critical_count * 100) + temp_accum
    else:
        result = -1
    
    return result

# Simulated sensor data (distorted with irrelevant fields)
sensor_readings = [-0.2, 0.81, -1.05, 0.3, 1.22, 0.67, -0.95]
noise_floor = [0.01 * i for i in range(len(sensor_readings))]  # Unused

# Signal energy calculation - irrelevant to final result
effective_energy = process_signal_chain(sensor_readings)
distorted_metric = effective_energy * 128  # Misleading intermediate

# Main diagnostic log - core data structure
diagnostic_log = [
    log_event(1001, status_codes['OK'], 1),
    log_event(1003, status_codes['WARNING'], 1),
    log_event(1007, status_codes['CRITICAL'], 3),
    log_event(1011, status_codes['CRITICAL'], 4),
    log_event(1013, status_codes['WARNING'], 2),
    log_event(1017, status_codes['CRITICAL'], 5)
]

# Phantom operations to distract
redundant_map = {idx: val['ts'] * val['priority'] for idx, val in enumerate(diagnostic_log)}
bitwise_fingerprint = 0
for k in redundant_map:
    bitwise_fingerprint ^= k ^ int(redundant_map[k])

# Character counting decoy
text_signature = "error_log_2024"
char_count = sum(1 for c in text_signature if c in 'aeiou')

# Critical execution point
final_diagnostic = analyze_fault_sequence(diagnostic_log)

# Output the target result
print(f"Target result: {final_diagnostic}")