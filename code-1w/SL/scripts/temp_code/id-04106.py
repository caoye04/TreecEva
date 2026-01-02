from itertools import combinations
from math import log

# Simulate system health metrics and evaluation weights
def calculate_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * log(v)
    return round(total, 4)

def extract_diagnostic_pairs(logs):
    pairs = []
    for i in range(len(logs) - 1):
        pairs.append((logs[i], logs[i+1]))
    return pairs

def filter_anomalies(records):
    # Irrelevant filtering for distraction
    return [r for r in records if r % 3 != 0]

def generate_triplets(data):
    # Dead code path - never used
    return list(combinations(data, 3))

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    adjustment_factor = 0.85
    
    # Misleading intermediate computation (not used in final logic)
    temp_buffer = [m ** 2 for m in metrics if m < 0.7]
    temp_stats = {
        'max_temp': max(temp_buffer) if temp_buffer else 0,
        'count_low': len([x for x in metrics if x < 0.5])
    }
    
    # Core logic embedded with distractions
    base_scores = []
    for i, metric in enumerate(metrics):
        if i % 2 == 0:
            # Apply weight only on even indices
            base_scores.append(metric * weights[i])
        else:
            # Transform odd-indexed metrics using bitwise and shift ops
            transformed = int((metric * 100) & 63) >> 1  # Mask and shift
            base_scores.append(transformed / 100.0)
    
    # Additional irrelevant set operation
    unique_bases = list(set(base_scores))
    sorted_bases = sorted(unique_bases, reverse=True)
    trimmed = sorted_bases[1:-1] if len(sorted_bases) > 2 else sorted_bases
    
    # Final score calculation depends only on original weighted logic
    for i, score in enumerate(base_scores):
        weighted_sum += score * adjustment_factor
    
    # Key execution point
    final_score = int(round(weighted_sum * 100))
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution block
if __name__ == "__main__":
    # Real input data
    system_logs = [0.92, 0.45, 0.68, 0.71, 0.33, 0.52]
    config_weights = [1.0, 0.8, 1.2, 0.9, 1.1, 0.7]
    
    # Distraction variables
    debug_trace = extract_diagnostic_pairs(system_logs)
    entropy_value = calculate_entropy(system_logs)
    filtered_data = filter_anomalies([12, 15, 18, 21, 24])
    
    # Trigger key statement
    final_score = evaluate_performance(system_logs, config_weights)