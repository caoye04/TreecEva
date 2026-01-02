from itertools import cycle

def analyze_response_time(raw_logs):
    baseline = 1.5
    adjusted_times = []
    for entry in raw_logs:
        timestamp, duration = entry
        if duration < baseline:
            adjusted_times.append(duration * 0.8)
        else:
            adjusted_times.append(duration * 1.1)
    return adjusted_times

def evaluate_consistency(ratios):
    trend = [abs(ratios[i+1] - ratios[i]) for i in range(len(ratios)-1)]
    return sum(trend) / len(trend) if trend else 0.0

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered or [mean_val]

def compute_weighted_average(values, weights=None):
    if not weights:
        weights = [1] * len(values)
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    return sum(v * w for v, w in zip(values, weights)) / total_weight

def aggregate_performance(feedback_sequence):
    # Simulate processing multiple feedback rounds with distraction logic
    durations = [entry[1] for entry in feedback_sequence]
    response_times = analyze_response_time(feedback_sequence)
    
    # Distractor: Irrelevant string processing (simulating log parsing)
    labels = ['event_A', 'event_B', 'event_C', 'event_D']
    label_cycle = cycle(labels)
    categorized = {next(label_cycle): [] for _ in enumerate(feedback_sequence)}
    
    # Distractor: Misleading consistency check on unrelated metric
    fake_ratios = [durations[i] / durations[i-1] for i in range(1, len(durations))] if len(durations) > 1 else [1.0]
    noise_level = evaluate_consistency(fake_ratios)
    
    # Actual relevant logic starts here
    clean_durations = filter_outliers(durations, threshold=1.8)
    normalized_scores = [(5.0 - min(max(t, 1.0), 5.0)) for t in clean_durations]
    
    # Weighting by position (more recent = higher weight)
    positional_weights = [i**1.2 for i in range(1, len(normalized_scores)+1)]
    performance_base = compute_weighted_average(normalized_scores, positional_weights)
    
    # Secondary correction based on count
    adjustment_factor = 0.9 if len(clean_durations) > 3 else 1.1
    final_score = performance_base * adjustment_factor
    
    # Red herring: unused computation involving string methods
    metadata_tag = "FEEDBACK_LOG_2024"
    checksum = sum(ord(c) for c in metadata_tag.lower() if c.isalpha()) % 17
    
    # Final result
    return round(final_score, 4)

# Main execution
raw_feedback = [
    ('start', 2.3),
    ('input_ready', 1.8),
    ('process', 4.1),
    ('confirm', 2.0),
    ('finalize', 3.2)
]

result_sequence = analyze_response_time(raw_feedback)
sample_ratios = [1.2, 0.9, 1.5, 1.1]
consistency_metric = evaluate_consistency(sample_ratios)

final_score = aggregate_performance(raw_feedback)
print(f"Result: {final_score}")