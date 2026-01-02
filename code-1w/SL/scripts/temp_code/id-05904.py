def analyze_contributions(raw_series, weights):
    adjusted = [x * w for x, w in zip(raw_series, weights)]
    return sum(adjusted) / len(adjusted)

# Irrelevant utility function (dead code path)
def legacy_normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Misleading intermediate computation
temp_offset = 0
for i in range(5):
    temp_offset += (i ** 3) % 7

# Unused but plausible-looking transformation
shadow_buffer = [0] * 8
for idx in range(len(shadow_buffer)):
    shadow_buffer[idx] = (idx * temp_offset) ^ 23

# Core data structures
baseline_metrics = {"throughput": 89, "latency": 42, "jitter": 6, "energy": 15}
validation_keys = set(baseline_metrics.keys())
metric_set = set(["throughput", "latency", "energy", "reliability"])

# Bitwise decoy calculation
mask = 0b1101
bit_noise = 0
for shift in range(4):
    bit_noise |= (mask << shift) & 0b101010

# Conditional expression red herring
penalty_factor = 1.2 if len(validation_keys & metric_set) < 3 else 0.8

# Simulated benchmark data with distractor fields
benchmark_data = {
    "raw_values": [0.88, 0.91, 0.76],
    "weights": [0.5, 0.3, 0.2],
    "flags": [True, False, True],
    "version_tag": "v2.1-alpha"
}

# Decoy list comprehension with side-effect-free mutation
_ = [x for x in benchmark_data["flags"] if not x]

# Unused recursive helper (distractor)
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n - 2) + (n % 3)

# Real logic hidden among noise
def evaluate_performance(metrics, data):
    # Determine overlap but use it indirectly
    common_dims = metrics & validation_keys  # yields {'throughput', 'latency', 'energy'}
    
    # Extract weighted performance
    base_score = analyze_contributions(data["raw_values"], data["weights"])
    
    # Key conditional expression using set difference
    if "reliability" in metrics and "jitter" not in common_dims:
        adjustment = -5
    else:
        adjustment = 3
    
    # Critical bitwise operation: encode dimension count
    dimension_flag = len(common_dims) ^ 7  # 3 ^ 7 = 4
    
    # Final composition
    raw_total = int(base_score * 100) + adjustment  # 87 + (-5) = 82
    final_modifier = dimension_flag & 3  # 4 & 3 = 0
    
    return raw_total + final_modifier  # 82 + 0 = 82

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)

# Output requirement
print(f"Result: {final_score}")