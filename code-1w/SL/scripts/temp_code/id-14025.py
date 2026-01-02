import itertools

# Simulated sensor array data from a satellite subsystem
def collect_telemetry():
    return [0.88, 0.76, 0.91, 0.83, 0.77, 0.89, 0.92, 0.79]

# Legacy function – appears important but unused in critical path
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) * 1.5 for x in data]

# Red herring: calculates an irrelevant health metric
def compute_health_index(stream):
    cumulative = 0
    for i, val in enumerate(stream):
        if i % 3 == 0:
            cumulative += val * 0.1
        elif i % 5 == 0:
            cumulative -= val * 0.05
    return round(cumulative, 4)

# Decoy buffer that looks like it's being updated but isn't used
buffer_cache = [0] * 16
for idx in range(len(buffer_cache)):
    buffer_cache[idx] = (idx * 7 + 11) % 13

# Real processing begins here
raw_metrics = collect_telemetry()

# Irrelevant transformation chain (distractor)
shifted_data = [x + 0.02 for x in raw_metrics]
doubled_pairs = list(itertools.product(shifted_data[:4], repeat=2))
filtered_pairs = [p for p in doubled_pairs if p[0] > 0.85 and p[1] < 0.9]
pair_count = len(filtered_pairs)  # Looks important, never used later

# Actual signal extraction via slicing and thresholds
valid_range = raw_metrics[1:6]  # Slice out unstable first and last readings
cleaned = [x for x in valid_range if 0.75 <= x <= 0.9]

# Bit manipulation red herring
flag_register = 0b101010
flag_register ^= 0b1111
flag_register |= 0b100000
active_flags = bin(flag_register).count('1')

# Benchmark reference profile (simulated)
benchmark_data = [0.81, 0.78, 0.85, 0.80, 0.76]

# Conditional expression mix with min/max logic
adjusted_benchmark = [
    x * 1.05 if x < 0.79 else x * 0.98 for x in benchmark_data
]

# Core evaluation logic
metrics = {
    'avg_raw': sum(cleaned) / len(cleaned),
    'length': len(raw_metrics),
    'stability': max(cleaned) - min(cleaned)
}

# Unused recursive distraction
def recursive_weight(depth, factor):
    if depth <= 1:
        return factor
    return factor + recursive_weight(depth - 1, factor * 0.7)

# Real scoring function
def evaluate_performance(mets, ref):
    base = mets['avg_raw']
    penalty = 0.0
    
    # Comparison logic with short-circuiting
    if mets['stability'] > 0.1 or len(ref) == 0:
        penalty += 0.05
    if base > 0.85 and all(x < 0.9 for x in ref):
        penalty -= 0.02
    
    # Conditional expression integration
    adjustment = 0.95 if mets['length'] >= 7 else 1.05
    
    # Critical calculation hidden among noise
    intermediate = (base * adjustment) - penalty
    
    # Final mapping to integer score scale (0-1000)
    return int(intermediate * 1000)

# Execution point of interest
final_score = evaluate_performance(metrics, benchmark_data)

# Dead code branch that looks active
if __name__ == "__main__":
    debug_mode = False
    if debug_mode:
        print("Debug:", compute_health_index(raw_metrics))

print(f"Result: {final_score}")