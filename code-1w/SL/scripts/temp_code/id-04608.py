def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return [x ** 2 for x in filtered]


def normalize(values):
    max_val = max(values)
    return [v / max_val for v in values]


def compute_moving_average(series, window=3):
    smoothed = []
    for i in range(len(series) - window + 1):
        smoothed.append(sum(series[i:i+window]) / window)
    return smoothed

# Irrelevant helper (distractor)
def predict_next_value(history):
    if len(history) < 2:
        return 0
    slope = history[-1] - history[-2]
    return history[-1] + slope

# Unused transformation (dead code path)
def transform_scale(value, mode='linear'):
    if mode == 'log':
        import math
        return math.log(value) if value > 0 else 0
    elif mode == 'sqrt':
        return value ** 0.5
    return value * 2

# Core logic disguised among distractions
def assess_complexity(sequence):
    score = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0 and val > 0:
            score += val * (i + 1)
        else:
            score -= val
    return score

# Distractor: unrelated diagnostic
def run_diagnostics(config):
    print("Running system diagnostics...")
    return {"status": "OK", "issues": [], "timestamp": 12345}

# Real computation buried in noise
def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = sum(weights)
    
    # Normalize weights
    normalized_weights = [w / total_weight for w in weights]
    
    # Apply transformations with red herrings
    adjusted_metrics = []
    for idx, (m, w) in enumerate(zip(metrics, normalized_weights)):
        temp_val = m
        if idx % 2 == 0:
            temp_val = (m + 1) ** 2  # Some arbitrary adjustment
        else:
            temp_val = m * 0.9 + 0.1
        adjusted_metrics.append(temp_val)
    
    # Additional irrelevant scaling
    scaled_metrics = [x * 1.0 for x in adjusted_metrics]  # No-op with distraction
    
    # Actual scoring logic
    final_component = 0
    for i, am in enumerate(scaled_metrics):
        contribution = am * normalized_weights[i]
        if i in [0, 2]:
            contribution *= 1.1  # Bonus factor
        final_component += contribution
    
    # Final nonlinear mapping
    if final_component > 5:
        final_component = 5 + (final_component - 5) ** 0.5
    
    # Critical line
    final_score = int(final_component * 1000) / 1000  # Round to 3 decimals
    
    # Dead code: never used
    debug_info = {'raw': metrics.copy(), 'processed': scaled_metrics}
    metadata_log = f"Evaluated at {len(metrics)} points"
    
    return final_score

# Misleading data setup
dataset = [-0.3, 0.8, -1.2, 0.5, 0.7]
signal_analysis = analyze_signal(dataset, 0.4)
normalized_signal = normalize(signal_analysis)
moving_avg = compute_moving_average(normalized_signal, 2)

# Fake pipeline
system_config = {"mode": "test", "verbosity": 2}
diag_result = run_diagnostics(system_config)

# Real inputs buried in noise
raw_sequence = [0.6, 0.9, 1.1, 0.4]
metrics = [assess_complexity(raw_sequence)] + normalize([len(raw_sequence), sum(raw_sequence), max(raw_sequence)])
benchmark_weights = [3, 1, 2, 4]  # Aligned with metrics

# Key execution point
final_score = evaluate_performance(metrics, benchmark_weights)

# Output result
print(f"Result: {final_score}")