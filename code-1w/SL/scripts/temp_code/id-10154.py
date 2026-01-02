from collections import defaultdict, Counter

def analyze_readings(sensor_data):
    readings = [x for x in sensor_data if x > 0]
    avg = sum(readings) / len(readings) if readings else 0
    anomalies = [r for r in readings if abs(r - avg) > 2]
    return len(anomalies)

def compute_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) % 256
    return checksum

def dummy_transformation(arr):
    # Irrelevant transformation
    return [x * 1.5 for x in arr]

def detect_patterns(values):
    pattern_count = 0
    for i in range(len(values) - 2):
        if values[i] < values[i+1] > values[i+2]:
            pattern_count += 1
    return pattern_count

def filter_relevant_entries(logs):
    filtered = defaultdict(int)
    for entry in logs:
        if 'status' in entry and entry['status'] == 'active':
            filtered[entry['id']] += 1
    return filtered

def evaluate_performance(metrics):
    score = 0
    temp_result = set()
    
    # Real computation path
    data_stream = [3, 6, 9, 12, 15, 18, 21]
    shift_offset = 2
    shifted = [(x << 1) + shift_offset for x in data_stream]
    
    # Meaningful intermediate: bit manipulation
    xor_accum = 0
    for val in shifted:
        xor_accum ^= val
    temp_result.add(xor_accum % 100)
    
    # Use of zip and enumerate together
    indexed_pairs = list(enumerate(zip(shifted[:-1], shifted[1:]), start=1))
    for idx, (a, b) in indexed_pairs:
        if idx % 2 == 0 and (b - a) == 6:
            score += a // 3
    
    # Set operations with distractor sets
    base_set = {1, 3, 6, 9, 12, 15}
    extra_set = {2, 4, 6, 8, 10, 12}
    metric_set = base_set.union(extra_set).difference({1, 2})
    
    decoy_score = sum([x ** 0.5 for x in metric_set if x % 3 == 0])
    
    # Core logic hidden among distractions
    prime_like = [n for n in metric_set if all(n % i != 0 for i in range(2, int(n**0.5)+1))]
    score += sum(prime_like)
    
    # Red herring: unused complex structure
    history_log = [
        {'event': 'init', 'value': compute_checksum([1,2,3])},
        {'event': 'fail', 'value': analyze_readings([1, -1, 2, -2, 3])}
    ]
    
    # Distractor: irrelevant list comprehension
    _ = [dummy_transformation([i*2 for i in range(5)]) for _ in range(3)]
    
    # Final calculation
    final_score = score * 2 - 7
    
    # Dead code path (never executed)
    if False:
        final_score = detect_patterns([5, 4, 6, 3, 7]) * 100
    
    return final_score

def main():
    # Simulated metrics input (not used directly but looks relevant)
    metrics = [
        {'type': 'latency', 'value': 45},
        {'type': 'throughput', 'value': 89}
    ]
    
    # Trigger evaluation
    final_score = evaluate_performance(metrics)
    print(f"Target result: {final_score}")

if __name__ == "__main__":
    main()