import itertools

def analyze_trend(data, threshold):
    above_threshold = [x for x in data if x > threshold]
    trend_signal = len(above_threshold) / len(data) if data else 0
    noise_filter = sum(1 for a, b in itertools.pairwise(above_threshold) if b > a)
    return trend_signal, noise_filter

def compute_stability(metric_log):
    if not metric_log:
        return 0.0
    diffs = [abs(a - b) for a, b in itertools.pairwise(metric_log)]
    stability = 1 / (1 + sum(diffs) / len(diffs)) if diffs else 1.0
    return round(stability, 4)

def evaluate_response(base_rating, response_time):
    adjustment_factor = 0.95 if response_time < 100 else 0.8
    adjusted = base_rating * adjustment_factor
    penalty = 0.1 if response_time > 150 else 0
    return adjusted - penalty

def aggregate_performance(feedback_loop):
    raw_metrics = [entry['metric'] for entry in feedback_loop]
    timing_data = [entry['rt'] for entry in feedback_loop]
    
    # Irrelevant preprocessing: slicing and filtering unused data
    recent_slice = raw_metrics[-min(10, len(raw_metrics)):]  
    filtered_slice = [x for x in recent_slice if x % 2 == 0]
    phantom_sum = sum(filtered_slice) * 0.05  # Unused distraction
    
    # Core logic begins
    trend_strength, _ = analyze_trend(raw_metrics, threshold=50)
    stability_score = compute_stability(raw_metrics)
    
    cumulative_rating = 0
    for i, rt in enumerate(timing_data):
        base_val = raw_metrics[i] / 10
        cumulative_rating += evaluate_response(base_val, rt)
    
    avg_response_rating = cumulative_rating / len(timing_data) if timing_data else 0
    
    # Misleading intermediate calculation
    volatility_proxy = abs(raw_metrics[-1] - raw_metrics[0]) if len(raw_metrics) > 1 else 0
    damping_factor = 0.9 if volatility_proxy > 30 else 1.0  # Not actually used
    
    # Final composition
    performance_base = trend_strength * 100
    refined_score = performance_base * stability_score
    final_score = int(refined_score + avg_response_rating * 10)
    
    # Output required result
    print(f"Result: {final_score}")
    return final_score

# Simulated input data
log_entries = [
    {'metric': 65, 'rt': 80},
    {'metric': 70, 'rt': 95},
    {'metric': 58, 'rt': 110},
    {'metric': 82, 'rt': 75},
    {'metric': 60, 'rt': 130},
    {'metric': 77, 'rt': 90},
    {'metric': 88, 'rt': 105}
]

# Trigger execution
final_score = aggregate_performance(log_entries)