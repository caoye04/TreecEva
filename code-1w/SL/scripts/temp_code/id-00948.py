import itertools

def analyze_trends(values, threshold):
    """Irrelevant function: analyzes trends but not used in final computation."""
    moving_avg = [sum(values[i:i+3]) / 3 for i in range(len(values)-2)]
    return [v for v in moving_avg if v > threshold]


def preprocess_inputs(raw):
    """Decoy preprocessing that modifies input but is ultimately unused."""
    cleaned = [x % 100 for x in raw if x > 0]
    normalized = [(x - min(cleaned)) / (max(cleaned) - min(cleaned)) for x in cleaned]
    return [int(n * 100) for n in normalized]


def calculate_weighted_sum(entries, weights=None):
    if not weights:
        weights = [1] * len(entries)
    weighted = 0
    for i, entry in enumerate(entries):
        if i % 2 == 0:
            weighted += entry * (weights[i] + 0.1)
        else:
            weighted -= entry * 0.5
    return weighted


def filter_outliers(data, limit=3):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= limit * std_dev], std_dev

def evaluate_performance(metrics, baseline):
    # Real metric processing begins here
    adjusted = [m * 1.1 for m in metrics if m >= 50]  # Only consider passing scores
    
    # Distractor: irrelevant transformation
    temp_log_analysis = [round((x * 0.01) ** 0.5, 4) for x in adjusted if x > 60]
    
    # Actual relevant logic path
    boosted = []
    for idx, val in enumerate(adjusted):
        if idx in [i for i in range(0, len(adjusted), 3)]:  # every third element gets extra boost
            boosted.append(val * 1.25)
        elif val > baseline:
            boosted.append(val * 1.15)
        else:
            boosted.append(val)
    
    # Use itertools to pair with dummy indices (some distraction)
    indexed_pairs = list(zip(itertools.count(start=100, step=10), boosted))
    extracted_values = [val for _, val in indexed_pairs]
    
    # Final aggregation
    raw_total = sum(extracted_values)
    penalty = 0
    for v in extracted_values:
        if v > 90:
            penalty += v * 0.05
    net_score = raw_total - penalty
    
    # Secondary adjustment based on modular condition
    if len(extracted_values) % 4 == 0:
        net_score *= 0.95
    elif len(extracted_values) % 4 == 1:
        net_score *= 1.02
    
    # This is the actual answer variable
    final_score = round(net_score, 4)
    
    # Dead code path - never reached due to prior logic
    if False:
        fallback = calculate_weighted_sum(extracted_values)
        final_score = fallback
        
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Simulated dataset
    raw_input_stream = [88, 72, 91, 45, 83, 77, 95, 68, 81, 74, 89, 76]
    
    # Irrelevant preprocessing (output not used)
    _ = preprocess_inputs(raw_input_stream)
    
    # Filter outliers - actually used
    clean_metrics, dispersion = filter_outliers(raw_input_stream, limit=2)
    
    # Some decoy variables to distract
    trend_window = analyze_trends(raw_input_stream, threshold=70)
    summary_stats = {"count": len(clean_metrics), "spread": round(dispersion, 2)}
    
    # Key data for evaluation
    metric_data = [x for x in clean_metrics if x >= 65]  # Further filtering
    
    # Critical statement
    final_score = evaluate_performance(metric_data, baseline=75)
    
    print(f"Result: {final_score}")