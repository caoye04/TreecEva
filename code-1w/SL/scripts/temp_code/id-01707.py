def analyze_feedback(responses):
    # Irrelevant sentiment analysis (dead path)
    positive_count = sum(1 for r in responses if r > 3)
    negative_count = sum(1 for r in responses if r < 3)
    neutral_count = len(responses) - positive_count - negative_count
    
    # Distractor transformation
    scaled = [r * 0.75 for r in responses]
    offset = sum(scaled) / len(scaled) if scaled else 0
    adjusted = [s + offset for s in scaled]

    # Real logic buried here: count how many times feedback improved consecutively
    improvements = 0
    for i in range(1, len(responses)):
        if responses[i] > responses[i-1]:
            improvements += 1
    return improvements

# Legacy system metrics (irrelevant)
def compute_legacy_metric(data):
    acc = 0
    for x in data:
        while acc < 5 and x > 0:
            acc += x % 2
            x //= 3
    return acc

# Core evaluation engine
def evaluate_performance(weights, outcomes):
    # weights: importance of each KPI
    # outcomes: actual results across same dimensions
    
    # Irrelevant normalization branch
    if sum(weights) == 0:
        return -999
    
    normalized_weights = [w / sum(weights) for w in weights]
    
    # Dummy aggregation (misleading)
    simple_avg = sum(outcomes) / len(outcomes)
    weighted_sum = sum(w * o for w, o in zip(normalized_weights, outcomes))
    
    # Secondary adjustment based on trend (real dependency)
    trend_boost = 0
    if len(outcomes) >= 2:
        recent_rise = all(outcomes[i] <= outcomes[i+1] for i in range(len(outcomes)-1))
        if recent_rise:
            trend_boost = 1.5
    
    # Hidden logic: feedback loop from improvement counter
    mock_responses = [2, 3, 4, 3, 5]
    improvement_count = analyze_feedback(mock_responses)
    
    # Critical red herring: legacy metric used in decoy calculation
    legacy = compute_legacy_metric([7, 2, 8])
    decoy_score = simple_avg * legacy / (weighted_sum + 0.1)
    
    # Actual formula (non-obvious due to distractions)
    base = weighted_sum + trend_boost
    penalty = 0.5 if improvement_count < 3 else 0  # Threshold hidden in logic
    final = base - penalty
    
    # Additional distraction: unused data structure
    history_log = {
        'entries': [
            {'version': '1.0', 'score': base * 0.8},
            {'version': '1.1', 'score': base * 0.9}
        ]
    }
    
    return round(final, 6)

# Simulated input data
metric_weights = [0.1, 0.3, 0.4, 0.2]  # Weight distribution across KPIs
raw_outcomes = [80, 75, 90, 85]        # Actual performance scores

# Misleading preliminary calculations
baseline = sum(raw_outcomes) // len(raw_outcomes)
deviation = max(raw_outcomes) - min(raw_outcomes)
adjusted_baseline = baseline * (1 + deviation / 100)

# Dead code path invocation (no impact)
_ = compute_legacy_metric([1, 2, 3])

# Key statement
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Output result
print(f"Result: {final_score}")