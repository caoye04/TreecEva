import itertools

def analyze_sequence(seq):
    """Irrelevant function: analyzes sequence patterns but not used in main logic"""
    count = 0
    for i, j in zip(seq, seq[1:]):
        if i < j:
            count += 1
    return count

def deprecated_calc(values):
    """Dead code path: never called"""
    return sum(x ** 0.5 for x in values)

# Misleading initialization with plausible-looking metrics
temp_buffer = [128, 256, 512, 1024]
decoys = {f"dummy_{i}": i * 17 for i in range(10)}
scaling_factor = 3.14159  # Unused constant (red herring)

log_data = [
    {'time': 100, 'errors': 5, 'load': 80},
    {'time': 200, 'errors': 3, 'load': 90},
    {'time': 150, 'errors': 7, 'load': 75}
]

weights = {
    'efficiency': 0.5,
    'stability': -0.2,  # Note: negative weight
    'throughput': 0.3
}

# Irrelevant transformation using enumerate and zip
indexed = list(enumerate([d['time'] for d in log_data]))
deltas = [b - a for a, b in zip([d['errors'] for d in log_data], [d['errors'] for d in log_data][1:])]

# Complex but unused data structure
cross_metrics = {}
for i, entry in enumerate(log_data):
    cross_metrics[i] = {}
    for key in entry:
        cross_metrics[i][key] = entry[key] * (i + 1)

# Core logic hidden among distractions
def compute_efficiency(time_val):
    return 1000 / time_val if time_val > 0 else 0

def assess_stability(error_count, load_level):
    return 10 - error_count - (load_level // 10)

def calculate_throughput(index, time_val):
    return (index + 1) * 100 / time_val

# Main processing function with nested logic
def process_metrics(entries, weight_map):
    raw_values = {}
    
    for idx, entry in enumerate(entries):
        # Compute multiple metrics, some masked by others
        efficiency = compute_efficiency(entry['time'])
        stability = assess_stability(entry['errors'], entry['load'])
        throughput = calculate_throughput(idx, entry['time'])
        
        # Aggregate per entry using weighted sum
        local_score = (
            efficiency * weight_map['efficiency'] +
            stability * weight_map['stability'] +
            throughput * weight_map['throughput']
        )
        
        # Use bitwise masking on index as obfuscation (has minor effect)
        masked_idx = idx ^ 3 & 7  # XOR and AND to alter contribution pattern
        raw_values[masked_idx] = local_score
    
    # Final aggregation uses sorted order and itertools.cycle for distraction
    sorted_keys = sorted(raw_values.keys())
    cyclic_weights = itertools.cycle([0.9, 1.1])  # Alternating adjustment
    total = 0.0
    for k in sorted_keys:
        weight_factor = next(cyclic_weights)
        total += raw_values[k] * weight_factor
    
    # Additional correction based on parity of sum of keys (subtle but deterministic)
    key_parity = sum(sorted_keys) % 2
    total += 5.5 if key_parity else -2.5
    
    return int(total)  # Final score is integer

# Critical execution point
final_score = process_metrics(log_data, weights)

# Distractor computation that looks important but is unused
aggregate_snapshot = {
    'max_time': max(d['time'] for d in log_data),
    'total_error_rate': sum(d['errors'] for d in log_data) / len(log_data),
    'average_load': sum(d['load'] for d in log_data) / len(log_data)
}

# Output the correct result
print(f"Result: {final_score}")