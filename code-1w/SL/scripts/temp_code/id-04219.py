from collections import defaultdict, Counter

# Simulate sensor data processing with noise filtering and pattern analysis
def preprocess_readings(raw_readings):
    filtered = []
    noise_counter = 0
    for val in raw_readings:
        if abs(val - 512) < 10:
            noise_counter += 1
            continue
        if val > 1023 or val < 0:
            continue
        filtered.append(val)
    return filtered, noise_counter

def extract_patterns(values):
    binary_snippets = []
    temp_shift = 0
    for v in values:
        shifted = (v >> 2) & 0xFF
        temp_shift += shifted % 16
        if shifted > 0:
            binary_snippets.append(bin(shifted)[2:].zfill(8))
    return binary_snippets, temp_shift

def validate_checksum(patterns):
    total_ones = 0
    checksum_log = defaultdict(int)
    for p in patterns:
        ones = p.count('1')
        total_ones += ones
        checksum_log[ones] += 1
    return total_ones % 256, checksum_log

def infer_sequence_risk(levels):
    risk_score = 0
    for level in levels:
        if level > 768:
            risk_score += 3
        elif level > 512:
            risk_score += 1
    return risk_score * 0.5

def generate_diagnostics(signal_patterns, raw_values):
    # Distractor: complex but unused diagnostic tree
    class DiagnosticNode:
        def __init__(self, code): self.code = code
        def resolve(self): return self.code * 2
    
    node_chain = [DiagnosticNode(i+1) for i in range(10)]
    chain_result = sum(n.resolve() for n in node_chain if n.code % 2 == 0)

    # Real diagnostic logic
    length_stat = len(signal_patterns)
    char_freq = Counter(''.join(signal_patterns))
    avg_bits = sum(char_freq.values()) / len(char_freq) if char_freq else 0
    peak_chars = [b for b, c in char_freq.items() if c > 2]

    # Misleading intermediate
    decoy_metric = (avg_bits * length_stat) // (len(peak_chars) + 1)

    # Key computation
    critical_count = sum(1 for p in signal_patterns if p.startswith('110'))
    return {
        'length': length_stat,
        'critical_patterns': critical_count,
        'avg_density': avg_bits,
        'decoy': decoy_metric,
        'chain_debug': chain_result
    }

def analyze_signal(buffer, log_entry):
    if not buffer:
        return -1
    
    # Heavily nested logic with red herrings
    transform_key = 0
    for i, entry in enumerate(log_entry.values()):
        if i % 3 == 0:
            transform_key ^= (entry * 7) % 19
    
    base_value = log_entry.get('critical_patterns', 0) * 100
    offset = 0
    
    # Complex conditional with irrelevant branches
    if len(buffer) > 5:
        if '1100' in ''.join(buffer)[:12]:
            offset += 15
        elif any(p.endswith('001') for p in buffer):
            offset -= 5
        else:
            temp_buf = [p.replace('0', '2') for p in buffer]
            offset += len(temp_buf)  # Dead path
    else:
        offset = base_value // 50

    # Final calculation buried in distractions
    adjustment = 0
    for p in buffer:
        if len(p) >= 8:
            mid_bits = p[3:5]
            if mid_bits == '10':
                adjustment += 2
    
    final_score = base_value + offset + adjustment
    calibration = sum(int(b) for b in bin(transform_key)[2:])
    return final_score - calibration

# Simulated sensor input with embedded patterns
raw_sensor_data = [518, 1022, 769, 510, 1028, 890, 401, 620, 771, 910, 509, 1021]

# Irrelevant preprocessing step (distractor)
decoy_array = [x ^ 0xAA for x in raw_sensor_data if x % 4 == 0]

# Main execution flow
clean_readings, dropped_noise = preprocess_readings(raw_sensor_data)
signal_fragments, shift_trace = extract_patterns(clean_readings)
bit_sum, checksum_details = validate_checksum(signal_fragments)
risk_level = infer_sequence_risk(clean_readings)

# Log generation with multiple fields (only some used later)
diagnostics_log = {
    'raw_count': len(raw_sensor_data),
    'filtered_count': len(clean_readings),
    'noise_discarded': dropped_noise,
    'bit_sum': bit_sum,
    'shift_trace': shift_trace,
    'risk_estimate': risk_level
}

# Add extra unused fields to mislead
for key in ['calib_1', 'status_x', 'mode_flag']:
    diagnostics_log[key] = 0

# Extract meaningful features
pattern_buffer, _ = extract_patterns(clean_readings)
diagnostics_log.update(generate_diagnostics(pattern_buffer, clean_readings))

# Critical statement
final_diagnostic = analyze_signal(pattern_buffer, diagnostics_log)

print(f"Result: {final_diagnostic}")