def analyze_signal(pattern):
    if not pattern:
        return 0
    return sum(p * (i + 1) for i, p in enumerate(pattern)) % 7

def decode_sequence(seq):
    base = 1
    result = 0
    for char in reversed(seq):
        result += (ord(char.lower()) - ord('a') + 1) * base
        base *= 26
    return result % 100

def validate_checksum(data):
    total = 0
    for i, val in enumerate(data):
        total += val * (i % 5 + 1)
    return total % 13 == 0

def transform_coordinates(coords):
    x, y = coords
    transformed = (x ^ y) + ((x + y) // 2)
    return transformed % 1000

def filter_anomalies(records):
    clean = []
    for r in records:
        if r.get('status') == 'active' and r.get('flag', 0) != 1:
            clean.append(r['value'])
    return clean

def compute_entropy(values):
    from math import log2
    if not values or sum(values) == 0:
        return 0.0
    total = sum(values)
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 6)

def merge_strings(str_list):
    # Irrelevant distractor function
    return ''.join(s.title() for s in str_list[::-1])

def dummy_analysis(x):
    # Dead code path, never used
    return (x ** 2 + 3 * x + 1) % 17

def evaluate_thresholds(vals):
    # Unused helper with misleading name
    count = 0
    for v in vals:
        if v > 50 and v % 5 == 0:
            count += 1
    return count

def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append((seq[i-1] + seq[i-2]) % 100)
    return seq if n > 2 else seq[:n]

def extract_features(text_blocks):
    features = []
    for block in text_blocks:
        words = block.split()
        lengths = [len(w.strip('.,!?')) for w in words]
        if lengths:
            avg_len = sum(lengths) / len(lengths)
            features.append(round(avg_len, 2))
    return features

def process_metrics(log_data, system_state):
    # Core relevant logic begins
    signal_pattern = [1, 0, 1, 1]
    sequence_code = "BX"
    coords = (13, 29)
    
    # Distractor variables
    temp_debug = merge_strings(['error', 'warning', 'info'])
    unused_calc = evaluate_thresholds([60, 75, 88, 92])
    dummy_val = dummy_analysis(42)
    
    # Relevant computations
    sig_metric = analyze_signal(signal_pattern)
    seq_metric = decode_sequence(sequence_code)
    coord_metric = transform_coordinates(coords)
    
    raw_values = [3, 6, 9, 12, 15]
    validated = validate_checksum(raw_values)
    
    entropy_value = compute_entropy(raw_values) if validated else 0.0
    
    fib_seq = generate_sequence(10)
    fib_sum = sum(fib_seq)
    
    text_data = ["System failure detected", "Reboot required immediately", "Hardware OK"]
    word_stats = extract_features(text_data)
    
    # Key aggregation
    base_score = sig_metric * 1000
    base_score += seq_metric * 100
    base_score += coord_metric * 10
    base_score += int(entropy_value * 10)
    base_score += fib_sum % 100
    
    # More distractions
    anomaly_records = [
        {'value': 10, 'status': 'active'},
        {'value': 20, 'status': 'inactive'},
        {'value': 30, 'status': 'active', 'flag': 1}
    ]
    filtered_vals = filter_anomalies(anomaly_records)
    
    # Final computation using multiple concepts
    adjustment = 0
    for i, stat in enumerate(word_stats):
        adjustment += int(stat) * (i + 1)
    
    final_diagnostic = base_score + adjustment
    
    # This print is required
    return final_diagnostic

# Simulated input data
log_data = {'timestamp': 12345, 'level': 'critical'}
system_state = {'power': 'on', 'mode': 'diagnostic'}

# Execution point
final_diagnostic = process_metrics(log_data, system_state)
print(f"Result: {final_diagnostic}")