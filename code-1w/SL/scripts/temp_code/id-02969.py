import itertools

def analyze_trends(data, threshold=5):
    trends = []
    for i in range(1, len(data)):
        change = data[i] - data[i-1]
        if abs(change) > threshold:
            trends.append('significant')
        else:
            trends.append('minor')
    return trends

def calculate_baseline(values):
    # Irrelevant helper function (dead logic path)
    avg = sum(values) / len(values)
    adjusted = [v * 0.95 for v in values if v > avg]
    return sum(adjusted) / len(adjusted) if adjusted else avg

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    max_possible = sum(weights)
    
    # Simulate multi-step scoring with distractor variables
    normalized = [m / 100.0 for m in metrics]  # Normalize to 0-1 scale
    temp_debug_log = []
    
    for i, (metric, weight) in enumerate(zip(normalized, weights)):
        contribution = metric * weight
        weighted_sum += contribution
        
        # Distractor computation: logging unused diagnostics
        if metric > 0.8:
            status = 'exceeds'
        elif metric > 0.5:
            status = 'meets'
        else:
            status = 'needs_improvement'
        temp_debug_log.append(f'Metric {i}: {status}')

    # Additional irrelevant intermediate calculation
    bonus_eligibility = all(m > 75 for m in metrics)
    extra_bonus = 10 if bonus_eligibility else 0  # Not used in final score
    
    # Real logic continues
    penalty_factor = 0.9 if len([m for m in metrics if m < 50]) > 1 else 1.0
    final_score = weighted_sum * penalty_factor
    
    # Use list comprehension and itertools in a semi-relevant way
    combinations = list(itertools.combinations(metrics, 2))
    volatility_index = sum(abs(a - b) for a, b in combinations) / len(combinations) if combinations else 0
    
    # Final assignment
    final_score = round(final_score, 4)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution
metrics_data = [88, 92, 76, 81, 69]
weights_config = [0.2, 0.3, 0.15, 0.25, 0.1]

# Irrelevant preprocessing
shifted_data = [x + 2 for x in metrics_data]
sorted_pairs = sorted(zip(metrics_data, shifted_data), key=lambda x: x[1], reverse=True)
decay_adjusted = [metrics_data[i] * (0.95 ** i) for i in range(len(metrics_data))]

# Key call that produces the answer
final_score = evaluate_performance(metrics_data, weights_config)