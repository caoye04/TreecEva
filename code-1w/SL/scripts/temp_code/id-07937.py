from collections import defaultdict, Counter
import math

def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    normalized = [round(math.log(x), 3) for x in filtered]
    return normalized

def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def dummy_analysis(data):
    stats = defaultdict(float)
    total = sum(data)
    stats['mean'] = total / len(data)
    stats['peak'] = max(data)
    stats['entropy'] = 0.0
    for x in data:
        if x > 0:
            stats['entropy'] -= x * math.log(x)
    return stats

def transform_readings(signal):
    shifted = [(int(x * 10) ^ 7) & 15 for x in signal]
    reversed_bytes = [((val << 4) | (val >> 4)) & 255 for val in shifted]
    return [reversed_bytes[i] ^ (i % 25) for i in range(len(reversed_bytes))]

def detect_anomaly(pattern):
    count = 0
    for i in range(1, len(pattern)):
        if pattern[i] != pattern[i-1]:
            count += 1
    return count > len(pattern) // 2

def compute_checksum(arr):
    chk = 0
    for i, v in enumerate(arr):
        chk ^= (v + i) * 3
    return chk % 1000

def analyze_pattern(data):
    freq = Counter(data)
    modes = [k for k, v in freq.items() if v == max(freq.values())]
    if len(modes) == 1:
        mode_val = modes[0]
    else:
        mode_val = min(modes)
    
    # Irrelevant transformation branch
    temp_buffer = []
    for x in data:
        temp_buffer.append(x ** 0.5)
    temp_buffer = [t for t in temp_buffer if t > 1]
    
    # Decoy statistical calculation
    fake_moment = 0
    for idx, val in enumerate(data):
        fake_moment += (val - mode_val) ** 3
    fake_moment /= len(data)
    
    # Real logic: count rising edges in bit-reversed sequence
    binary_rep = ''.join([bin(x)[2:].zfill(4)[-4:] for x in data])
    edge_count = 0
    for j in range(1, len(binary_rep)):
        if binary_rep[j-1] == '0' and binary_rep[j] == '1':
            edge_count += 1
    
    # Secondary check based on combinatorics
    n = len(data)
    k = len(set(data))
    combinations = math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) if n >= k else 1
    
    # Final decision logic (this is the actual answer path)
    if edge_count > 10 and combinations % 2 == 0:
        result_code = mode_val * 2 + 5
    elif edge_count == 0:
        result_code = -999
    else:
        result_code = (mode_val + edge_count) % 7 * 3
    
    # Dead code - never used
    debug_snapshot = {}
    for item in data:
        debug_snapshot[item] = bin(item).count('1')
    
    return result_code

# Main execution flow
raw_sensor_data = [18, 24, 18, 30, 18, 24, 24, 18, 30, 30]
signal_clean = preprocess_signal(raw_sensor_data)
transformed_data = transform_readings(signal_clean)

# Dummy calls with misleading outputs
baseline_stats = dummy_analysis(transformed_data)
seq_for_timing = generate_sequence(8)
anomaly_flag = detect_anomaly(seq_for_timing)
useless_checksum = compute_checksum(transformed_data)

# Key statement
final_diagnostic = analyze_pattern(transformed_data)

print(f"Result: {final_diagnostic}")