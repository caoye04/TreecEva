from collections import defaultdict
from itertools import combinations

# Simulate system health monitoring with performance scoring
def collect_metrics():
    metrics = defaultdict(float)
    metrics['response_time'] = 120.5
    metrics['error_rate'] = 0.03
    metrics['throughput'] = 850
    metrics['cpu_load'] = 75.2
    metrics['memory_usage'] = 60.1
    metrics['disk_io'] = 45.8
    return metrics

# Irrelevant function: generates unused combinatorial patterns
def generate_combinations(data):
    combo_count = 0
    for r in range(1, len(data)+1):
        for _ in combinations(data, r):
            combo_count += 1
    return combo_count  # Never used

# Misleading transformation: looks important but is a red herring
def normalize_values(values):
    max_val = max(values)
    return [v / max_val for v in values]

# Bit manipulation decoy: simulates low-level optimization
def compute_checksum(data_list):
    checksum = 0
    for val in data_list:
        if isinstance(val, (int, float)):
            int_val = int(val * 100) % 256
            checksum ^= int_val  # XOR into checksum
    return checksum + 1000  # Distractor computation

# Unused recursive function: creates illusion of complexity
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Core weighting logic - only this matters
weight_map = {
    'response_time': -0.4,      # Lower is better
    'error_rate': -0.6,
    'throughput': 0.3,          # Higher is better
    'cpu_load': -0.2,
    'memory_usage': -0.15,
    'disk_io': -0.1
}

# Primary evaluation function
def evaluate_performance(metrics, weights):
    score = 0.0
    for key, weight in weights.items():
        raw_value = metrics[key]
        
        # Normalize response time (target base: 100ms)
        if key == 'response_time':
            normalized = max(0, 100 - (raw_value - 100))
            score += normalized * abs(weight)
        elif key == 'error_rate':
            # Convert to percentage and invert
            inverted = (1 - raw_value) * 100
            score += inverted * abs(weight)
        elif key == 'throughput':
            # Scale throughput to 0-100 scale
            scaled = min(100, raw_value / 8.5)
            score += scaled * weight
        else:
            # For cpu_load, memory_usage, disk_io: lower is better
            inverted = max(0, 100 - raw_value)
            score += inverted * abs(weight)
    
    # Critical adjustment: apply bitwise tweak based on evenness of integer part
    int_part = int(score)
    if int_part & 1:  # If odd
        score = score * 0.95
    else:             # If even
        score = score * 1.02
    
    return round(score, 4)

# Dead code path: never executed
if __name__ == "unused_main":
    debug_data = [120, 3, 850, 75, 60, 45]
    norm_debug = normalize_values(debug_data)
    chk = compute_checksum(norm_debug)

# Main execution flow
metrics = collect_metrics()

# Generate meaningless combos (distraction)
dummy_combos = generate_combinations(list(metrics.keys()))

# Compute irrelevant checksum
side_checksum = compute_checksum(list(metrics.values()))

# Useless recursive call (never reaches deep)
shallow_fib = fibonacci(5)

# --- KEY STATEMENT ---
final_score = evaluate_performance(metrics, weight_map)

# Output the target result
print(f"Target result: {final_score}")