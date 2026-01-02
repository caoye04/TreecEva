from collections import defaultdict, Counter
import math

# Simulated sensor data processing system with diagnostic routines
def collect_sensor_data():
    raw_readings = [127, 64, 255, 32, 192, 16, 8, 4, 2, 1]
    timestamped = [(i, val) for i, val in enumerate(raw_readings)]
    return timestamped

def extract_patterns(data):
    pattern_buffer = []
    for ts, val in data:
        if val & (val - 1) == 0:  # power of two check
            pattern_buffer.append(val)
    
    # Irrelevant transformation chain (distractor)
    temp_analysis = [x ^ 255 for x in pattern_buffer]
    shifted = [x >> 2 for x in temp_analysis if x > 100]
    masked = [x & 0b1111 for x in shifted]
    decoy_aggregate = sum(masked) * 3 - 17
    
    # Real but hidden logic: count frequency of bit positions set
    bit_freq = defaultdict(int)
    for val in pattern_buffer:
        for bit_pos in range(8):
            if val & (1 << bit_pos):
                bit_freq[bit_pos] += 1
    
    return pattern_buffer, bit_freq

def compute_entropy(values):
    # Fake entropy used in dead path
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def generate_metrics(patterns):
    metrics_log = {}
    
    # Actual relevant metric: sum of squared indices
    index_power_sum = 0
    for i, p in enumerate(patterns):
        index_power_sum += i * i * (p % 7)
    
    # Distractor metrics (unused in final result)
    length_coded = len(patterns) * 19
    reversed_vals = patterns[::-1]
    xor_chain = 0
    for v in reversed_vals:
        xor_chain ^= (v + 5) % 100
    checksum_fake = (xor_chain + length_coded) % 997
    
    # Dead function definition (red herring)
    def validate_integrity(data):
        return sum(data) % 256 == 0
    
    # Another decoy structure
    audit_trail = []
    for p in patterns:
        audit_trail.append(f"CHK-{p%13}-V2")
    
    # Only this part matters
    metrics_log['index_power_sum'] = index_power_sum
    metrics_log['base_count'] = len([x for x in patterns if x < 100])
    
    return metrics_log

def analyze_signal(patterns, log):
    # Core logic hidden among distractions
    
    # Irrelevant pre-processing
    filtered = [p for p in patterns if p != 255]
    transformed = [((x | 3) ^ 17) % 50 for x in filtered]
    dummy_map = {i: transformed[i] for i in range(len(transformed))}
    
    # Critical calculation (non-obvious dependency)
    base_score = 0
    for i, p in enumerate(patterns):
        if i % 2 == 0 and p > 100:
            base_score += int(math.sqrt(p))

    # Decoy recursive function (never called)
    def trace_path(value, depth):
        if depth == 0 or value < 10:
            return value
        return trace_path((value // 2) ^ 3, depth - 1)
    
    # Key signal extraction
    multiplier = log.get('base_count', 0) + 3
    signal_strength = log.get('index_power_sum', 0) // 5
    
    # Hidden adjustment based on bit pattern from earlier
    bit_offset = sum(1 for b in [1, 2, 4, 8, 16, 32, 64, 128] if b in patterns) - 2
    
    # Final computation (only one that matters)
    final_diagnostic = base_score * multiplier + signal_strength - bit_offset
    
    # Unused complex structure (distractor)
    report_summary = {
        'status': 'OK' if final_diagnostic > 10 else 'FAIL',
        'details': [{'ref': i, 'val': v*2} for i, v in enumerate(transformed[:3])]
    }
    
    return final_diagnostic

# Main execution flow
sensor_data = collect_sensor_data()
data_patterns, bit_frequency = extract_patterns(sensor_data)
performance_metrics = generate_metrics(data_patterns)
final_diagnostic = analyze_signal(data_patterns, performance_metrics)
print(f"Target result: {final_diagnostic}")