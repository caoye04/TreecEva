def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val + 1e-8) for x in data] if max_val > min_val else [0.5] * len(data)

# Irrelevant helper function dealing with string patterns
def extract_patterns(text_list):
    patterns = {}
    for text in text_list:
        words = text.lower().split()
        for word in words:
            if len(word) >= 3:
                prefix = word[:3]
                patterns[prefix] = patterns.get(prefix, 0) + 1
    return {k: v for k, v in patterns.items() if v > 1}

# Another distraction: bit manipulation with no real impact
def obscure_transform(value):
    temp = value ^ 0b10101010
    temp = (temp << 2) | (temp >> 6)
    return temp & 0xFF

# Real logic begins — performance metric evaluator
def calculate_efficiency(counts, base):
    total = sum(counts)
    if total == 0:
        return 0.0
    weighted_sum = sum((i + 1) * cnt for i, cnt in enumerate(counts))
    return weighted_sum / total / base

def validate_stability(ratios):
    if not ratios:
        return 0
    avg = sum(ratios) / len(ratios)
    variance = sum((r - avg) ** 2 for r in ratios) / len(ratios)
    return 1 if variance < 0.1 else 0.5 if variance < 0.25 else 0.1

def evaluate_performance(metrics, weights):
    # Normalize each metric series
    normalized = [normalize(series) for series in metrics]
    
    # Extract last values as current state
    current_vals = [series[-1] for series in normalized]
    
    # Distraction: process dummy logs
    dummy_logs = ["error init", "retry success", "timeout warn"]
    log_stats = extract_patterns(dummy_logs)
    ignored_result = len(log_stats.keys()) * 0.05  # Unused
    
    # More distractions: bitwise noise
    noise_buffer = [obscure_transform(i) for i in range(len(current_vals))]
    masked_vals = [cv ^ (nb / 255.0) for cv, nb in zip(current_vals, noise_buffer)]  # Not actually used
    
    # Actual calculation uses only first three metrics
    efficiency_component = calculate_efficiency([int(v * 10) for v in current_vals[:3]], base=15)
    stability_component = validate_stability(current_vals)
    
    # Final score computation
    raw_score = (efficiency_component * weights[0] + 
                stability_component * weights[1] + 
                current_vals[2] * weights[2])
    
    # Apply non-linear boost if fourth metric exceeds threshold
    if len(current_vals) > 3 and current_vals[3] > 0.7:
        raw_score *= 1.25
    
    final_score = int(round(raw_score * 100))
    
    # Dead code branch — never reached due to prior logic
    if final_score < 0:
        final_score = 0  # unreachable
    
    return final_score

# Main execution
metrics_data = [
    [12, 15, 18, 20],           # throughput over time
    [95, 90, 88, 85],           # accuracy percentages
    [4, 5, 6, 7],               # resource units
    [0.6, 0.65, 0.72, 0.78]     # consistency scores
]

weights_config = [0.4, 0.3, 0.3]

# Unused variables — red herrings
baseline_ref = [0.8, 0.7, 0.6]
depth_map = {'layer1': 0.44, 'layer2': 0.56, 'layer3': 0.33}
shadow_factor = sum(depth_map.values()) / len(depth_map)

# Key statement
final_score = evaluate_performance(metrics_data, weights_config)
print(f"Result: {final_score}")