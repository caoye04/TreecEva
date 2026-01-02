from itertools import compress, cycle
import math

def analyze_efficiency(values):
    # Irrelevant helper: computes efficiency but not used in final result
    base = sum(v ** 0.5 for v in values if v > 0)
    penalty = len([v for v in values if v < 5])
    return base - penalty * 0.5

def calculate_urgency(level, hours):
    # Semi-relevant: used to compute urgency_factor, which is later ignored
    urgency = level * math.log(hours + 1) if hours > 0 else 0
    adjustment = 2.5 if urgency > 10 else 0.3
    return urgency + adjustment

def evaluate_performance(output, risk):
    # Core logic: combines output and risk with weighting
    trend_data = [output * 0.8, output * 1.1, output * 0.9, output * 1.05]
    avg_trend = sum(trend_data) / len(trend_data)
    
    # Distractor: complex filtering using itertools
    mask = [i % 2 == 0 for i in range(len(trend_data))]
    filtered = list(compress(trend_data, mask))
    dummy_cycle = list(zip(filtered, cycle([1, -1])))  # Not used
    
    # Real computation begins
    stability = sum(abs(trend_data[i] - trend_data[i-1]) for i in range(1, len(trend_data)))
    normalized_stability = 1 / (1 + stability)  # Higher stability => higher score
    
    # Risk adjustment
    risk_penalty = 0
    if risk > 7:
        risk_penalty = 15
    elif risk > 4:
        risk_penalty = 8
    else:
        risk_penalty = 3
    
    # Final score calculation
    base_score = avg_trend * 10
    adjusted_score = base_score * normalized_stability
    final_score = adjusted_score - risk_penalty
    
    # Dead code path - misleading
    if output < 0:
        fallback = math.exp(output)
        final_score = max(final_score, fallback)
    
    return final_score

# Simulated input data
productivity = 12
risk_level = 5
hours_remaining = 3

# Irrelevant precomputations
urgency_factor = calculate_urgency(risk_level, hours_remaining)
efficiency_metric = analyze_efficiency([4, 7, 6, 8, 3])
baseline = math.ceil(productivity * 0.75)

# Key statement
final_score = evaluate_performance(productivity, risk_level)

# Additional distraction: unused set operations
valid_outputs = {10, 11, 12, 13, 14}
discounted_set = {x - 2 for x in valid_outputs if x > baseline}
overlap = valid_outputs & discounted_set  # Computed but unused

# Print result as required
print(f"Result: {final_score}")