from collections import defaultdict

# Simulate system performance evaluation with noise filtering and scoring
def preprocess_metrics(raw_readings):
    filtered = []
    noise_floor = 0.1
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)


def calculate_entropy(values):
    from math import log2
    freq = defaultdict(int)
    total = len(values)
    for v in values:
        freq[v] += 1
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def evaluate_trend(stability_log):
    trend_score = 0
    for i in range(1, len(stability_log)):
        if stability_log[i] >= stability_log[i-1]:
            trend_score += 1
        else:
            trend_score -= 0.5
    return max(trend_score, 0)

# Irrelevant helper: simulates unused diagnostic trace
def generate_diagnostic_trace(n):
    trace = []
    for i in range(n):
        trace.append((i, (i**2 + 3*i + 7) % 19))
    return trace  # Never used in main logic

# Main evaluation function
def evaluate_performance(metrics, threshold):
    high_priority = [m for m in metrics if m > threshold]
    medium_priority = [m for m in metrics if m <= threshold and m > threshold * 0.5]
    
    # Compute derived scores
    focus_bonus = len(high_priority) * 1.5
    spread_penalty = len(medium_priority) * 0.7
    
    entropy = calculate_entropy(metrics)
    trend = evaluate_trend(high_priority)
    
    # Dummy state tracking (only some used)
    state_tracker = defaultdict(int)
    state_tracker['high_count'] = len(high_priority)
    state_tracker['entropy_flag'] = 1 if entropy > 2.0 else 0
    state_tracker['trend_strength'] = trend

    # Unused intermediate calculations (distractors)
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    peak_noise_ratio = (max(metrics) / (min(metrics) + 1e-5)) if metrics else 0
    diagnostic_summary = [x for x in metrics if x > avg_metric]  # Computed but unused
    
    # Final scoring formula
    base_score = focus_bonus - spread_penalty + entropy * 2 + trend
    adjustment_factor = 0.9 if state_tracker['entropy_flag'] else 1.1
    final_score = int(round(base_score * adjustment_factor))
    
    return final_score

# Input data
raw_system_data = [0.05, 0.3, 0.3, 0.7, 0.15, 0.9, 0.9, 0.2, 0.08, 0.7]
base_threshold = 0.5

# Preprocess
metric_data = preprocess_metrics(raw_system_data)

# Evaluate performance
final_score = evaluate_performance(metric_data, base_threshold)

# Output result
print(f"Result: {final_score}")