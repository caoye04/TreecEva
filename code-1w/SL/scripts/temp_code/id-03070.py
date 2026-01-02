def analyze_efficiency(data, threshold=0.75):
    """Irrelevant analysis function (distractor)"""
    count = 0
    for val in data:
        if val > threshold:
            count += 1
    return count / len(data) if data else 0


def preprocess_signals(signals):
    """Another distractor: signal normalization"""
    normalized = []
    total_power = sum([s**2 for s in signals])
    for s in signals:
        normalized.append(round(s / (total_power**0.5), 6) if total_power > 0 else 0)
    return normalized

# Decoy metrics and unused weight sets (red herrings)
decoy_metrics = [0.81, 0.77, 0.68, 0.92, 0.54]
decoy_weights = [0.1, 0.1, 0.2, 0.3, 0.3]

# Actual performance metrics from system modules
metrics = [0.89, 0.94, 0.76, 0.83, 0.91]  # accuracy, latency, memory, throughput, stability
weights = [0.3, 0.2, 0.15, 0.25, 0.1]   # priority-based weighting

# Irrelevant transformation chain
transformed_metrics = []
for i, m in enumerate(metrics):
    if i % 2 == 0:
        transformed_metrics.append(m ** 1.1)
    else:
        transformed_metrics.append(m ** 0.95)

# Dummy structure for distraction
system_log = {
    'timestamp': '2023-11-05T10:15:30',
    'module_load': [1.0, 0.8, 0.95, 0.7],
    'retries': 3,
    'cached_result': None
}

# Unused recursive helper (dead code path)
def calculate_depth(tree):
    if not tree or isinstance(tree, str):
        return 0
    return 1 + max(calculate_depth(child) for child in tree)

# Core evaluation logic buried among noise
def evaluate_performance(raw_scores, importance_weights):
    adjusted = []
    for idx, (score, weight) in enumerate(zip(raw_scores, importance_weights)):
        penalty = 0.0
        if score < 0.8:
            penalty = (0.8 - score) * 0.5
        adjusted.append((score - penalty) * weight)
    
    base = sum(adjusted)
    
    # Bonus logic based on consistency
    consecutive_high = 0
    max_consecutive = 0
    for s in raw_scores:
        if s >= 0.85:
            consecutive_high += 1
            max_consecutive = max(max_consecutive, consecutive_high)
        else:
            consecutive_high = 0
    
    bonus = 0.02 if max_consecutive >= 3 else 0.0
    
    # Hidden normalization step using enumerate
    norm_factor = 0.0
    for i, w in enumerate(importance_weights):
        norm_factor += w * (i + 1)  # weighted position index
    norm_factor = norm_factor / len(importance_weights)
    
    final_value = (base + bonus) * (1.0 + 0.05 * (norm_factor > 1.5))
    
    # Additional decoy calculation
    fake_adjustment = 0
    for i in range(len(raw_scores)):
        fake_adjustment += (i+1) * raw_scores[i] * 0.01
    
    return round(final_value, 6)

# Simulated preprocessing (irrelevant but plausible)
signal_data = [0.5, 0.8, 1.2, 0.9, 0.3]
normalized_signal = preprocess_signals(signal_data)

# Spurious list comprehension with zip (distraction)
combined_analysis = [
    (m * w) ** 0.5 for m, w in zip(decoy_metrics, decoy_weights)
    if m > 0.7
]

# Key execution point buried in logic flow
final_score = evaluate_performance(metrics, weights)

# Output required format
print(f"Target result: {final_score}")