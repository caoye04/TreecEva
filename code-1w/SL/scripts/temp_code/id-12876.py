from collections import defaultdict
import math

def preprocess_data(raw):
    # Irrelevant preprocessing step with distractor logic
    temp_result = defaultdict(int)
    for k, v in raw.items():
        if len(k) % 2 == 0:
            temp_result[k] = v * 1.5
        else:
            temp_result[k] = v * 0.8
    return temp_result

def filter_outliers(values):
    # Semi-relevant function: computes mean but doesn't alter main flow
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    threshold = mean_val - 2 * std_dev
    return [v for v in values if v >= threshold]

def calculate_entropy(vals):
    # Dead code path — never used in final computation
    total = sum(vals)
    probs = [v / total for v in vals]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def calculate_final_score(entries, importance_weights):
    base_scores = []
    adjustment_factor = 0.9
    
    for key, value in entries.items():
        # Core logic begins
        char_sum = sum(ord(c) for c in key)
        weighted_val = value * importance_weights.get(key, 1.0)
        
        # Distractor: complex but unused transformation
        transformed = (weighted_val ** 2 + char_sum) % 7
        
        # Relevant calculation
        normalized = weighted_val / (char_sum % 5 + 1)
        base_scores.append(normalized)
    
    # Filtering has minor effect but not critical
    filtered_scores = filter_outliers(base_scores)
    
    # Final score depends only on sum and fixed adjustment
    raw_total = sum(filtered_scores)
    final_score = int(raw_total * adjustment_factor * 100)  # Key result
    
    # Extra assignments to increase cognitive load
    debug_info = {'count': len(filtered_scores), 'raw_sum': raw_total}
    log_entry = f"Score computed at {final_score}"
    
    return final_score

# Main execution block
if __name__ == '__main__':
    data = {
        'alpha': 12,
        'beta': 18,
        'gamma': 15,
        'delta': 23
    }
    weights = {
        'alpha': 1.2,
        'beta': 0.9,
        'gamma': 1.1,
        'delta': 1.3
    }

    # Irrelevant intermediate steps
    processed = preprocess_data(data)
    entropy_estimate = calculate_entropy(list(data.values()))  # Computed but unused
    
    # Key statement
    final_score = calculate_final_score(data, weights)
    
    # Output result as required
    print(f"Result: {final_score}")