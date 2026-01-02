from itertools import combinations
from math import log

# Simulate system performance metrics over time
metrics = [89.4, 92.1, 88.7, 94.3, 90.5, 93.0, 87.2]
baseline = 90.0

def analyze_trend(data):
    trend_scores = []
    for i in range(1, len(data)):
        trend_scores.append(data[i] - data[i-1])
    return sum(trend_scores) / len(trend_scores)

def calculate_stability(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    stability = 100 - (sum(diffs) / len(diffs))
    return stability if stability > 0 else 0

def generate_pairs(data):
    # Irrelevant helper: generates pairs but not used in final logic
    return list(combinations(data, 2))

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered  # Used indirectly via preprocessing

def compute_entropy(data):
    # Distractor function: computes entropy but unused
    total = sum(data)
    probs = [x / total for x in data]
    entropy = -sum(p * log(p) for p in probs if p > 0)
    return round(entropy, 4)

def evaluate_performance(raw_metrics, reference):
    # Preprocess: remove potential outliers
    clean_data = filter_outliers(raw_metrics, threshold=1.5)
    
    # Key derived values
    above_baseline = len([x for x in clean_data if x >= reference])
    below_baseline = len(clean_data) - above_baseline
    hit_rate = above_baseline / len(clean_data)
    
    # Auxiliary tracking variables (some irrelevant)
    adjustment_factor = 0.85 if hit_rate >= 0.6 else 0.6
    penalty_buffer = (below_baseline * 2.5) if below_baseline > 2 else 0
    
    # Core calculation with slicing and set operations
    recent_period = clean_data[-4:]  # Last four measurements
    improvement_set = {i for i, val in enumerate(recent_period) if val > reference}
    regression_set = {i for i, val in enumerate(recent_period) if val <= reference}
    net_progress = len(improvement_set - regression_set)
    
    # Use of set difference and slicing to derive weight
    trend = analyze_trend(clean_data)
    stability = calculate_stability(clean_data)
    
    # Composite score with weighted components
    base_score = sum(clean_data) / len(clean_data)
    bonus = net_progress * 3.7
    adjusted_score = base_score + bonus - penalty_buffer
    
    # Final nonlinear transformation
    if adjusted_score > reference:
        final_score = adjusted_score * adjustment_factor + stability * 0.1
    else:
        final_score = adjusted_score - bonus * 0.3
    
    # Red herring: unused intermediate
    peak_pair = generate_pairs(clean_data[:3])
    entropy_value = compute_entropy([len(clean_data), len(peak_pair)])
    
    return round(final_score, 2)

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")