import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_values = [127, 255, 64, 192, 32]
    timestamps = [1623456780, 1623456781, 1623456782]
    metadata = {'version': '2.1', 'calibrated': True}
    return raw_values

# Irrelevant helper - dead code path
def legacy_compatibility_mode(data):
    transformed = []
    for x in data:
        transformed.append((x << 2) ^ 0xFF)
    return transformed

# Unused signal smoothing (distractor)
def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        avg = (signal[i-1] + signal[i] + signal[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(signal[-1])
    return smoothed

# Core transformation: normalize and detect peaks
def preprocess_signal(raw):
    normalized = []
    peak_flags = []
    base_ref = sum(raw) / len(raw)
    
    for val in raw:
        norm_val = (val - base_ref) / base_ref
        normalized.append(round(norm_val * 1000))
        peak_flags.append(abs(norm_val) > 0.5)
    
    # Decoy computation
    checksum = 0
    for i, v in enumerate(normalized):
        checksum ^= (v + i) & 0xFFFF
    
    result_bundle = {
        'data': normalized,
        'peaks': peak_flags,
        'stats': {
            'mean_offset': sum(normalized) // len(normalized),
            'variance_proxy': sum([x*x for x in normalized[:3]]) // 3
        },
        'debug_checksum': checksum  # Red herring
    }
    
    return result_bundle

# Signal classification (not used in final path)
def classify_environment(signal_data):
    energy = sum([x**2 for x in signal_data['data']])
    if energy > 500000:
        return 'high_activity'
    elif energy > 200000:
        return 'moderate'
    else:
        return 'low'

# Main processing with dictionary unpacking and conditional logic
def process_diagnostics(diag_map):
    readings = diag_map['data']
    stats = diag_map['stats']
    accumulator = 0
    
    # Complex interdependent calculations
    for i in range(len(readings)):
        if i % 2 == 0:
            temp = abs(readings[i])
            temp = (temp >> 1) + (temp & 1)
            if temp > 200:
                temp = temp ^ 150
            accumulator += temp
        else:
            temp = readings[i] // 3
            accumulator -= temp
    
    # Dead branch - never taken due to data constraints
    if len(readings) < 2:
        accumulator *= 2
    
    # Secondary manipulation
    modifier = stats['mean_offset']
    if modifier < 0:
        accumulator -= modifier
    else:
        accumulator += modifier // 2
    
    # Bitwise obfuscation layer (partially relevant)
    accumulator = ((accumulator ^ 0x5A5A) + 321) & 0xFFFF
    
    return accumulator

# Final analysis combining multiple concepts
def analyze_readings(signal_packet):
    interim_value = process_diagnostics(signal_packet)
    
    # Spurious string-based calculation (distraction)
    status_code = "SNSR_OK_200"
    error_mask = 0
    for c in status_code:
        error_mask += ord(c) ^ 0x55
    
    # Critical path: combinatorics + modular arithmetic
    selection_count = 0
    values = signal_packet['data']
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if (values[i] + values[j]) % 7 == 0:
                selection_count += 1
    
    # Integration with prior result
    intermediate = interim_value + (selection_count * 1000)
    
    # Final adjustment using dictionary default lookup (red herring)
    flags = signal_packet.get('flags', [])
    override = flags.count(True) if flags else 0
    final_score = intermediate - (override * 500)  # override is 0
    
    # Additional decoy: unused recursive function
    def explore_combinations(n, r):
        if r == 0 or r == n:
            return 1
        return explore_combinations(n-1, r-1) + explore_combinations(n-1, r)
    
    return final_score

# Orchestration with irrelevant setup
if __name__ == '__main__':
    # Unused configuration map
    sys_config = {
        'mode': 'diagnostic',
        'verbosity': 3,
        'buffer_size': 1024,
        'timeout_ms': 5000
    }
    
    # Primary data flow
    raw_sensor_data = collect_sensor_data()
    processed_signals = preprocess_signal(raw_sensor_data)
    
    # Debug probe (irrelevant)
    if 'debug_checksum' in processed_signals:
        hex_dump = hex(processed_signals['debug_checksum'])[2:]
        chunks = [hex_dump[i:i+4] for i in range(0, len(hex_dump), 4)]
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output requirement
    print(f"Target result: {final_diagnostic}")