def analyze_text_patterns(input_str):
    # Irrelevant string analysis (distractor)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in input_str.lower() if c in vowels)
    upper_case_count = sum(1 for c in input_str if c.isupper())
    reversed_str = input_str[::-1]
    palindrome_check = input_str.lower() == reversed_str.lower()

    # Semi-relevant preprocessing
    cleaned = ''.join(c for c in input_str if c.isalnum()).lower()
    unique_chars = len(set(cleaned))

    return unique_chars


def calculate_entropy(data_list):
    from math import log2
    total = sum(data_list)
    if total == 0:
        return 0.0
    entropy = 0.0
    for x in data_list:
        if x > 0:
            p = x / total
            entropy -= p * log2(p)
    return round(entropy, 4)

# Simulated system metrics over time (distractor: complex setup)
metrics_history = [
    {'cpu': 75, 'mem': 60, 'disk': 30},
    {'cpu': 80, 'mem': 65, 'disk': 35},
    {'cpu': 85, 'mem': 70, 'disk': 40}
]

# Current performance snapshot
metrics = {
    'response_time_ms': 120,
    'throughput_ops': 250,
    'error_rate': 0.02,
    'concurrent_users': 1500,
    'data_volume_mb': 450
}

baseline = {
    'response_time_ms': 100,
    'throughput_ops': 200,
    'error_rate': 0.05,
    'concurrent_users': 1000,
    'data_volume_mb': 300
}

# Distractor: historical trend analysis not used in final score
historical_improvement = []
for i in range(1, len(metrics_history)):
    prev, curr = metrics_history[i-1], metrics_history[i]
    improvement = sum(curr[k] - prev[k] for k in prev)
    historical_improvement.append(improvement)

# Auxiliary function with red herring parameters
def adjust_for_environment(value, env_factor=1.0, deprecated_mode=False):
    environment_flags = ['prod', 'staging', 'dev']
    load_adjustment = 0.95 if env_factor > 1.1 else 1.05
    return value * load_adjustment

# Core evaluation logic
threshold_breaches = 0
weights = {
    'response_time_ms': 0.3,
    'throughput_ops': 0.25,
    'error_rate': 0.35,
    'concurrent_users': 0.05,
    'data_volume_mb': 0.05
}

# Evaluate deviations from baseline
normalized_scores = {}
for key in metrics:
    if key == 'error_rate':
        # Lower is better
        normalized = min(metrics[key] / baseline[key], 2.0)
    else:
        # Higher is better
        normalized = max(metrics[key] / baseline[key], 0.5)
    normalized_scores[key] = normalized

# String-based config signature (semi-relevant)
config_tag = "PERF_EVAL_V2"
decay_factor = 0.98 ** len(config_tag)  # Minor adjustment

# Compute weighted performance delta
performance_delta = 0.0
for key, weight in weights.items():
    base_norm = 1.0
    current_norm = normalized_scores[key]
    change = current_norm - base_norm
    performance_delta += weight * change

# Apply decay and convert to scaled score
raw_score = (1 + performance_delta) * decay_factor
scaled_score = int(raw_score * 100)

# Additional signal from string pattern in tag (minor contribution)
bonus_multiplier = 1.0
if config_tag.endswith('V2') and 'EVAL' in config_tag:
    bonus_multiplier = 1.05

# Final scoring with distractor variables present but not critical
interim_value = scaled_score * bonus_multiplier
clamped_score = max(1, min(interim_value, 200))  # Clamp between 1 and 200

# Dead code path (distractor)
if False:
    fallback = sum(len(str(v)) for v in baseline.values())
    clamped_score = fallback

# Critical statement
final_score = evaluate_performance(metrics, baseline)

# Actual implementation of evaluate_performance (must be defined before use)
def evaluate_performance(m, b):
    # Reuse logic above but simplify for clarity in actual function
    temp_normalized = {}
    for k in m:
        if k == 'error_rate':
            temp_normalized[k] = min(m[k] / b[k], 2.0)
        else:
            temp_normalized[k] = max(m[k] / b[k], 0.5)
    
    w = {
        'response_time_ms': 0.3,
        'throughput_ops': 0.25,
        'error_rate': 0.35,
        'concurrent_users': 0.05,
        'data_volume_mb': 0.05
    }
    
    delta = sum(w[k] * (temp_normalized[k] - 1) for k in m)
    raw = (1 + delta) * (0.98 ** len("PERF_EVAL_V2"))
    score = int(raw * 100)
    if "EVAL" in "PERF_EVAL_V2" and "PERF_EVAL_V2".endswith("V2"):
        score = int(score * 1.05)
    return max(1, min(score, 200))

print(f"Target result: {final_score}")