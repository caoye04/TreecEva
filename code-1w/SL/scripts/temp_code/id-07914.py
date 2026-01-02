from itertools import combinations
from functools import reduce

# Simulate system health metrics from sensor array
def collect_metrics(base_load, threshold_factor=0.85):
    raw_data = [base_load * 1.2, base_load * 0.7, base_load * 1.5, base_load * 0.9]
    filtered = [x for x in raw_data if x > base_load * threshold_factor]
    normalized = list(map(lambda x: round(x / max(filtered), 3), filtered))
    return normalized

def calculate_redundancy_score(n):
    # Irrelevant helper function – computes combinatorial count
    return len(list(combinations(range(n), 2))) if n > 1 else 0

def analyze_stability(ratios):
    # Computes variance-like measure but not directly used
    mean_ratio = sum(ratios) / len(ratios)
    deviation_sq = sum((r - mean_ratio) ** 2 for r in ratios)
    pseudo_variance = round(deviation_sq / len(ratios), 4)
    
    # Distractor logic with dead branch
    if pseudo_variance < 0.05:
        adjustment = 1.1
    elif pseudo_variance > 0.2:
        adjustment = 0.9
    else:
        adjustment = 1.0  # This path always taken
        temp_debug = [x * adjustment for x in ratios]  # Unused variable
    
    return pseudo_variance

def apply_weighting(values, weights):
    # Apply weighted product using modular arithmetic for cyclic emphasis
    weighted_product = 1
    for i, val in enumerate(values):
        weight = weights[i % len(weights)]
        weighted_product *= (val ** weight) + (i % 3)  # Artificial inflation
    
    # Normalize via logarithmic scaling
    if weighted_product > 1:
        scaled = round(weighted_product ** (1 / len(values)), 4)
    else:
        scaled = weighted_product
        
    return scaled

def detect_anomalies(data_stream):
    # Bitwise anomaly detection (distractor)
    anomalies = 0
    for i in range(len(data_stream) - 1):
        diff = int(abs(data_stream[i] - data_stream[i+1]) * 100)
        if diff & 1 and diff % 7 == 0:  # XOR alternative pattern
            anomalies ^= 1  # Toggle
    return anomalies  # Not used later

def evaluate_performance(metrics, weights):
    # Core logic begins
    adjusted = []
    for i, m in enumerate(metrics):
        temp_val = m * weights[i % len(weights)]
        if temp_val > 0.5:
            temp_val = temp_val ** 0.5  # dampen high values
        adjusted.append(round(temp_val, 4))
    
    # Intermediate distractor computation
    cumulative_xor = 0
    for a in adjusted:
        cumulative_xor ^= int(a * 1000) % 16  # Truncates precision, irrelevant
    
    # Real aggregation
    aggregate = reduce(lambda acc, x: acc + x, adjusted, 0.0)
    
    # Final transformation
    if aggregate > 2.0:
        final_score = int((aggregate * 100) // len(adjusted))
    else:
        final_score = int((aggregate * 120) // len(adjusted))
    
    # Critical assignment point
    final_score = final_score ^ 15  # Final bit-flip adjustment
    
    return final_score

# Main execution
if __name__ == "__main__":
    base_system_load = 72
    weights = [2, 3, 1, 4]
    
    # Collect performance metrics
    metrics = collect_metrics(base_system_load)
    
    # Irrelevant intermediate steps
    redundancy_count = calculate_redundancy_score(len(metrics))
    stability_index = analyze_stability(metrics)
    anomaly_flag = detect_anomalies(metrics)
    
    # Key computation
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")