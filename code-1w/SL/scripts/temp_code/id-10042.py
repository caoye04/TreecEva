from collections import defaultdict, Counter

def analyze_sequence(data):
    count = defaultdict(int)
    for item in data:
        count[item] += 1
    return dict(count)

def compute_hash(s):
    # Irrelevant helper function with misleading purpose
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 1000000
    return h

def filter_outliers(values, threshold=2):
    mean = sum(values) / len(values)
    std = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean) <= threshold * std]

def transform_coordinates(coords):
    # Unused geometric transformation (dead code path)
    return [(y * 2, x // 2) for x, y in coords]

def generate_pattern(n):
    # Distractor: generates Fibonacci-like sequence but not used in final logic
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def merge_dicts(dicts):
    result = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            result[k] += v
    return dict(result)

def validate_entries(entries):
    valid = []
    for e in entries:
        if isinstance(e, dict) and 'id' in e and 'status' in e:
            if e['status'] == 'active':
                valid.append(e['id'])
    return valid

def calculate_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).bit_length()  # Simplified approximation
    return round(entropy, 6)

def shift_cipher(text, key):
    # Another red herring: string manipulation not directly related
    result = ''
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result += chr((ord(c) - base + key) % 26 + base)
        else:
            result += c
    return result

def process_timestamps(ts_list):
    # Processes time-like integers with modular arithmetic (distractor)
    adjusted = []
    for ts in ts_list:
        sec = ts % 60
        min_val = (ts // 60) % 60
        hr = (ts // 3600) % 24
        adjusted.append((hr, min_val, sec))
    return adjusted

def evaluate_performance(metrics, baseline):
    # Core logic begins here — this is where final_score is computed
    adjusted_metrics = {}
    scaling_factor = 1.75

    for k, v in metrics.items():
        if k in ['throughput', 'accuracy', 'latency']:
            if k == 'latency':
                adjusted_metrics[k] = round(baseline[k] / max(v, 1), 4)  # Inverse relation
            else:
                adjusted_metrics[k] = round(v / baseline[k], 4)

    # Apply weighted scoring
    weights = {'throughput': 0.4, 'accuracy': 0.35, 'latency': 0.25}
    weighted_sum = 0.0
    for key, weight in weights.items():
        weighted_sum += adjusted_metrics[key] * weight

    # Final transformation using modular adjustment and bit manipulation
    raw_score = int(weighted_sum * 1000)
    masked_score = raw_score ^ 0xFFFF  # Bitwise XOR with mask
    mod_score = (masked_score + 512) % 8192
    final_score = (mod_score * scaling_factor) // 1.5  # Integer division

    # Introduce a decoy variable that looks important but isn't used
    diagnostic_trace = {
        'hash_check': compute_hash('perf_eval_2024'),
        'outlier_count': len(metrics) - len(filter_outliers(list(metrics.values()))),
        'pattern_sync': generate_pattern(10)[-1]
    }

    return int(final_score)

# Main execution flow
if __name__ == '__main__':
    # Simulated input data
    metrics = {
        'throughput': 980,
        'accuracy': 0.92,
        'latency': 45,
        'reliability': 0.99,  # Irrelevant field (ignored in processing)
        'jitter': 8           # Also ignored
    }

    baseline = {
        'throughput': 800,
        'accuracy': 0.85,
        'latency': 60
    }

    # Dead code section: complex but unused structure
    coordinates = [(120, 80), (240, 160), (360, 240)]
    transformed_coords = transform_coordinates(coordinates)

    log_data = ['event_start', 'polling_active', 'event_start', 'shutdown']
    frequency_map = analyze_sequence(log_data)
    entropy_value = calculate_entropy(log_data)

    timestamps = [3661, 7200, 10805, 1800]
    time_components = process_timestamps(timestamps)

    ciphered = shift_cipher('evaluate', 7)

    # This list contains irrelevant entries
    system_entries = [
        {'id': 101, 'status': 'active'},
        {'id': 102, 'status': 'inactive'},
        {'id': 103, 'status': 'active'}
    ]
    active_ids = validate_entries(system_entries)

    # Key statement: evaluation of performance
    final_score = evaluate_performance(metrics, baseline)

    # Print final result as required
    print(f"Target result: {final_score}")