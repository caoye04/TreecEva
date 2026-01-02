def analyze_system_load(usage_data):
    # Irrelevant function analyzing system load with decoy logic
    peak = max(usage_data)
    avg = sum(usage_data) / len(usage_data)
    threshold_alert = [u for u in usage_data if u > 80]
    return len(threshold_alert) > 3

# Decoy data structures
temp_logs = [76, 85, 90, 67, 88, 94, 73]
dummy_weights = {'latency': 0.1, 'bandwidth': 0.3, 'jitter': 0.6}

# Actual relevant data
metrics = {
    'accuracy': 94.2,
    'throughput': 87.5,
    'consistency': 91.8,
    'response_time': 85.0
}

weights = [0.3, 0.25, 0.2, 0.25]  # Weight distribution across four metrics

# Dead function - never called
def calculate_composite(data_dict, factor=1.0):
    total = 0.0
    for key, val in data_dict.items():
        if 'time' in key:
            total += val * 0.8
        else:
            total += val * 1.1
    return total * factor

# Distractor list comprehension
shadow_values = [x ** 0.5 for x in range(100) if x % 11 == 0]

# Unused bitwise manipulation
flag_register = 0b1010
flag_register ^= 0b1100  # Toggle bits
flag_register |= 0b0001

# Lambda-based processor (partially used)
processor = lambda f, w: [f[i] * w[i] for i in range(len(f))]

# Simulated network hops (irrelevant)
network_hops = [(1, 5), (2, 8), (3, 6)]
hop_map = {src: dst for src, dst in network_hops}

# Character frequency distractor
text_sample = "performance evaluation metric"
freq_count = {}
for char in text_sample:
    freq_count[char] = freq_count.get(char, 0) + 1

# Core evaluation function with nested logic
def evaluate_performance(met, weight_vec):
    ordered_keys = ['accuracy', 'throughput', 'consistency', 'response_time']
    base_vals = [met[key] for key in ordered_keys]
    
    # Apply non-linear adjustment to consistency (critical step)
    adjusted_vals = []
    for i, val in enumerate(base_vals):
        if i == 2:  # consistency index
            adjusted = val * (1 + (val - 90) / 100) if val > 90 else val
        elif i == 3:  # response_time
            adjusted = val * 0.95  # slight penalty
        else:
            adjusted = val
        adjusted_vals.append(adjusted)
    
    # Misleading normalization step (not actually affecting final result)
    normalized = [v / 100.0 for v in adjusted_vals]
    
    # Apply weighted sum using lambda processor
    weighted_components = processor(adjusted_vals, weight_vec)
    raw_sum = sum(weighted_components)
    
    # Final nonlinear boost based on throughput threshold
    if adjusted_vals[1] >= 87.0:
        raw_sum *= 1.02
    
    return round(raw_sum, 4)

# Red herring dictionary update
metrics['accuracy'] += 5.0  # This would matter if used later, but isn't

# Another dead-end calculation
aggregate = sum([len(str(int(v))) for v in metrics.values()])

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Print required output
print(f"Target result: {final_score}")