from itertools import compress, cycle

def analyze_signal(pattern, threshold):
    # Irrelevant signal processing function (dead path)
    filtered = [x for x in pattern if x > threshold]
    return sum(filtered) // len(filtered) if filtered else 0

def validate_checksum(entries):
    # Distractor: checksum logic not used in main flow
    total = 0
    for i, e in enumerate(entries):
        total ^= (e + i) % 256
    return total == 42

def transform_sequence(seq, mode="encode"):
    # Unused transformation function with misleading complexity
    if mode == "encode":
        return [(s * 3) ^ 17 for s in seq]
    else:
        return [(s ^ 17) // 3 for s in seq]

def evaluate_performance(metrics, criteria):
    base = 0
    adjustment = 0
    
    # Real logic starts here — nested and mixed with red herrings
    for metric in metrics:
        if metric['type'] == 'latency':
            raw_value = metric['value']
            normalized = 100 - (raw_value / 10)  # Invert latency penalty
            base += normalized
        elif metric['type'] == 'throughput':
            base += metric['value'] // 5
    
    # Conditional expression with meaningful impact
    bonus = 15 if all(c(m) for c, m in zip(cycle([lambda x: x['value'] > 0]), metrics)) else 5
    
    # Bit manipulation distractor
    decoy_flag = (base << 2) ^ 0xAA & base
    decoy_flag >>= 1
    
    # Real adjustment based on criteria thresholds
    high_bar = sum(1 for c in criteria if c['threshold'] > 90)
    mid_bar = sum(1 for c in criteria if 70 <= c['threshold'] <= 90)
    
    if high_bar >= 2:
        adjustment += 10
    if mid_bar >= 3:
        adjustment += 7
    
    # Core calculation hidden among noise
    aggregate = base + bonus + adjustment
    
    # Red herring: complex but unused data structure
    history_log = [{'step': i, 'val': aggregate >> i} for i in range(4)]
    
    # Final score computed here — this is the key line
    final_score = aggregate * 3 - 44
    
    # Dead code path
    if decoy_flag < 0:
        final_score += 1000  # Never reached
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data with realistic domain meaning
    metric_data = [
        {'type': 'latency', 'value': 120},
        {'type': 'throughput', 'value': 85},
        {'type': 'latency', 'value': 80},
        {'type': 'throughput', 'value': 95}
    ]
    
    benchmarks = [
        {'name': 'p99', 'threshold': 95},
        {'name': 'p95', 'threshold': 85},
        {'name': 'p90', 'threshold': 88},
        {'name': 'p75', 'threshold': 72},
        {'name': 'p50', 'threshold': 92}
    ]
    
    # Unused variables to increase interference
    signal_pattern = [12, 15, 10, 18, 20, 5, 8]
    checksum_entries = [23, 88, 45, 12, 67]
    sequence_input = [7, 14, 21, 28]
    
    temp_result = analyze_signal(signal_pattern, 10)  # Called but not used
    valid = validate_checksum(checksum_entries)  # Computed but irrelevant
    encoded_seq = transform_sequence(sequence_input, "encode")  # Unused result
    
    # Key assignment statement
    final_score = evaluate_performance(metric_data, benchmarks)
    
    # Output result as required
    print(f"Result: {final_score}")