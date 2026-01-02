from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [78, 92, 85, 76, 94, 88, 91, 87]
    outliers = [200, -50, 300]  # Irrelevant noisy data
    filtered = [x for x in raw_data if x >= 0]  # Only relevant data
    return filtered

def calculate_trend(values):
    trend = 0
    for i in range(1, len(values)):
        trend += values[i] - values[i-1]
    return trend  # Distractor: used nowhere

def analyze_distribution(data):
    freq = defaultdict(int)
    for val in data:
        freq[val // 10] += 1
    mode_class = max(freq, key=lambda k: freq[k])
    return mode_class * 10

def adjust_for_latency(value, delay=0.02):
    # Simulate small correction (irrelevant to final logic)
    import math
    adjusted = value * (1 - math.exp(-delay))
    return round(adjusted, 2)

def compute_variance(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance  # Dead-end computation

def generate_weight_profile(n):
    # Complex-looking but ultimately unused weight generation
    weights = [0.1] * n
    for i in range(n):
        weights[i] += 0.01 * i
        if i % 2 == 0:
            weights[i] *= 1.1
    return [w / sum(weights) for w in weights]  # Normalized but irrelevant

def normalize_scores(scores):
    min_val, max_val = min(scores), max(scores)
    if min_val == max_val:
        return [0.5] * len(scores)
    return [(s - min_val) / (max_val - min_val) for s in scores]

def apply_correction_factor(score_map):
    corrected = {}
    for k, v in score_map.items():
        if v > 0.8:
            corrected[k] = v * 0.95
        elif v < 0.3:
            corrected[k] = v * 1.2
        else:
            corrected[k] = v * 1.05
    return corrected  # Unused result

def evaluate_performance(metrics, base_weights):
    normalized = normalize_scores(metrics)
    
    # Key intermediate transformation
    weighted_sum = 0
    for i, score in enumerate(normalized):
        weight = base_weights[i % len(base_weights)]
        weighted_sum += score * weight
    
    # Secondary adjustment based on distribution mode
    mode_floor = analyze_distribution(metrics)
    adjustment_factor = 1.0
    if mode_floor >= 80:
        adjustment_factor = 1.1
    elif mode_floor <= 60:
        adjustment_factor = 0.9
    
    # Final aggregation
    final_score = weighted_sum * adjustment_factor
    
    # Decoy operations below
    temp_result = sum(normalized) * 100  # Misleading high-value calculation
    _ = adjust_for_latency(temp_result)  # Dead call
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Collect actual performance metrics
    metrics = collect_metrics()  # [78, 92, 85, 76, 94, 88, 91, 87]
    
    # Define primary weights (simple fixed set, ignoring generate_weight_profile)
    weights = [0.2, 0.3, 0.3, 0.2]
    
    # Compute variance (distractor, not used later)
    var = compute_variance(metrics)
    
    # Determine trend (completely irrelevant)
    trend = calculate_trend(metrics)
    
    # Normalize metrics
    norm_metrics = normalize_scores(metrics)
    
    # Apply fake correction (result ignored)
    _ = apply_correction_factor({i: m for i, m in enumerate(norm_metrics)})
    
    # Critical statement
    final_score = evaluate_performance(metrics, weights)
    
    print(f"Result: {final_score}")