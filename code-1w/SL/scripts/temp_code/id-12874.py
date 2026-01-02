import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [127, 255, 192, 64, 224, 32, 160, 96]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

# Irrelevant transformation: color space mockup
def rgb_to_hsv(r, g, b):
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val
    if max_val == min_val:
        h = 0
    elif max_val == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    else:
        h = (60 * ((r - g) / diff) + 240) % 360
    return h, 1.0, max_val

# Unused helper: checksum decoy
def compute_legacy_checksum(data_str):
    checksum = 0
    for char in data_str:
        checksum += ord(char) * 3
    return checksum % 256

# Distractor: network simulation (never called)
def simulate_handshake(packet_size):
    retries = 0
    while packet_size > 1024 and retries < 3:
        packet_size //= 2
        retries += 1
    return retries

# Core data transformation chain
def preprocess(signal_list):
    filtered = [x for x in signal_list if x > 50.0]
    normalized = [round(x / max(filtered), 4) for x in filtered]
    inverted = [1.0 - val for val in normalized]
    return inverted

# Bit manipulation red herring
def encode_flags(mode, active, priority):
    flag = 0
    flag |= (mode & 0b111)
    flag |= (active << 3)
    flag |= (priority << 5)
    # Additional unused encoding
    if priority > 3:
        flag ^= 0b101010
    return flag

# String processing distraction
def parse_metadata(meta_string):
    segments = meta_string.split('|')
    info_map = {}
    for seg in segments:
        if ':' in seg:
            k, v = seg.split(':', 1)
            info_map[k.strip()] = v.strip()
    # Decoy computation
    hash_val = sum(ord(c) for c in meta_string if c.isalpha()) % 17
    return info_map.get('id', 'unknown'), hash_val

# Recursive combinatorics decoy (not used in main flow)
def count_subsequences(arr, target=3):
    if len(arr) == 0 or target == 0:
        return 1 if target == 0 else 0
    return count_subsequences(arr[1:], target) + count_subsequences(arr[1:], target - arr[0])

# Real processing path begins here
def transform_sequence(values):
    sequence_state = {i: val for i, val in enumerate(values)}
    temp_log = []
    for idx in sorted(sequence_state.keys()):
        if idx % 2 == 0:
            sequence_state[idx] = math.sqrt(sequence_state[idx])
        else:
            sequence_state[idx] = math.log(sequence_state[idx]) if sequence_state[idx] > 0 else 0
        temp_log.append(f"Step{idx}:{sequence_state[idx]:.3f}")
    
    # Extract values in order
    transformed = [sequence_state[i] for i in range(len(sequence_state))]
    return transformed, temp_log

# Conditional expression mix
def evaluate_threshold(value, baseline=0.85):
    return 'stable' if value >= baseline else ('fluctuating' if value >= 0.6 else 'critical')

# Main analysis function with distractors
def analyze_signal(data_stream):
    stats = {
        'count': len(data_stream),
        'sum': sum(data_stream),
        'max': max(data_stream),
        'min': min(data_stream)
    }
    
    # Meaningful intermediate
    avg = stats['sum'] / stats['count']
    deviation = [abs(x - avg) for x in data_stream]
    mean_dev = sum(deviation) / len(deviation)
    
    # Conditional logic with nested expressions
    category = 'high' if avg > 0.7 else 'medium' if avg > 0.4 else 'low'
    
    # Red herring: string-based state tracking
    state_code = "DGN-" + ("H" if stats['max'] > 0.9 else "M" if stats['max'] > 0.6 else "L")
    status_msg = f"Signal {state_code}: {'Optimal' if 'high' in category else 'Suboptimal'}"
    
    # Critical branching - only this affects final result
    if category == 'high':
        base_score = 850
    elif category == 'medium':
        base_score = 420
    else:
        base_score = 110
    
    # Additional adjustment based on variance pattern
    peak_ratio = stats['max'] / (stats['min'] + 1e-8)
    if peak_ratio > 3.0:
        adjustment = -75
    elif peak_ratio > 1.5:
        adjustment = 30
    else:
        adjustment = 10
    
    # Final computation
    final_score = base_score + int(mean_dev * 200) + adjustment
    
    # Dead code: object-oriented wrapper never used
    class DiagnosticReport:
        def __init__(self, score):
            self.score = score
            self.timestamp = '2023-11-05'
        def export(self):
            return f"[REP]{self.score}/{self.timestamp}"
    
    return final_score

# Orchestration with hidden key path
if __name__ == "__main__":
    # Collect and process real data
    raw_data = collect_readings()
    processed_data = preprocess(raw_data)
    refined_values, logs = transform_sequence(processed_data)
    
    # Spurious operations
    encoded_flag = encode_flags(5, True, 2)
    parsed_id, magic_hash = parse_metadata("type:scan|id:S4X9|version:2.1")
    
    # Actual answer derivation
    final_diagnostic = analyze_signal(refined_values)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")