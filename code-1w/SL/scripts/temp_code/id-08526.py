from itertools import compress, cycle

def analyze_trend(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append(1)
        elif data[i] < data[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

def calculate_volatility(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs) if diffs else 0

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    total_weight = sum(weights)
    
    # Irrelevant intermediate computation (distractor)
    temp_analysis = [x * 2 + 1 for x in metrics if x > 5]
    temp_analysis_filtered = list(filter(lambda x: x % 3 == 0, temp_analysis))
    
    # Actual scoring logic
    adjusted_metrics = [m ** 0.5 if m > 0 else 0 for m in metrics]
    for i, (metric, weight) in enumerate(zip(adjusted_metrics, weights)):
        contribution = metric * weight
        weighted_sum += contribution
    
    # Extra distraction: unused volatility tracking
    volatility_proxy = calculate_volatility(metrics)
    noise_level = volatility_proxy * 0.1
    
    # Conditional adjustment based on trend pattern
    trend_sequence = analyze_trend(metrics)
    positive_momentum = sum(1 for t in trend_sequence[-3:] if t == 1)
    
    bonus_factor = 1.1 if positive_momentum >= 2 else 1.0
    
    final_score = weighted_sum / total_weight if total_weight else 0
    final_score *= bonus_factor
    
    # Additional red herring: bitwise masking with no effect
    mask = 0b11111111
    masked_value = int(final_score) & mask
    
    # Normalize to two decimal places
    final_score = round(final_score, 4)
    
    return final_score

# Simulated input data
metrics = [8, 12, 15, 9, 11]
weights = [0.1, 0.3, 0.25, 0.15, 0.2]

# Unused but plausible-looking alternative weighting (dead code path)
default_weights = [0.2, 0.2, 0.2, 0.2, 0.2]
legacy_scaling = list(zip(default_weights, cycle([1.0, 0.9])))

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")