def analyze_data(records):
    # Irrelevant data transformation (distractor)
    processed = [r['value'] * 0.85 for r in records if r['status'] == 'active']
    avg = sum(processed) / len(processed) if processed else 0
    return avg * 1.15

# Unused helper function (dead code path)
def normalize(v, min_val, max_val):
    return (v - min_val) / (max_val - min_val) if max_val != min_val else 0

# Misleading metric calculation with red herring logic
def compute_risk_factor(data):
    risk = 0
    for item in data:
        if item > 100:
            risk += 5
        elif item > 50:
            risk += 2
        else:
            risk -= 1
    return risk // 2  # Not actually used later

# Core logic buried among distractions
def evaluate_performance(metrics, weights):
    weighted_sum = 0
    total_weight = 0
    
    # Real computation with list comprehension and lambda filtering
    valid_pairs = [(m, w) for m, w in zip(metrics, weights) if w >= 0]
    filtered_metrics = list(map(lambda x: x[0], valid_pairs))
    filtered_weights = list(map(lambda x: x[1], valid_pairs))
    
    # Actual relevant logic
    for i in range(len(filtered_metrics)):
        metric = filtered_metrics[i]
        weight = filtered_weights[i]
        if metric >= 70:
            bonus = (metric - 70) // 10 * 0.5
        else:
            bonus = -((70 - metric) // 15) * 0.3
        weighted_sum += (metric + bonus) * weight
        total_weight += weight
    
    return int(weighted_sum / total_weight) if total_weight else 0

# Decoy variables and irrelevant initializations
baseline = [65, 72, 80, 90]
data_log = [{'value': 120, 'status': 'active'}, {'value': 80, 'status': 'inactive'}]
shadow_metrics = [95, 45, 78, 63]
weights_map = [0.2, 0.3, 0.3, 0.2]

# Red herring function call
junk_value = analyze_data(data_log)

# Another distraction: unused complex expression
temp_result = (lambda x: x ** 2 + 2 * x + 1)(len(shadow_metrics))

# Key data used in final calculation
metrics_input = [88, 76, 92, 64]  # Performance scores in order
weights_input = [0.1, 0.4, 0.3, 0.2]  # Weight distribution

# Critical execution point
final_score = evaluate_performance(metrics_input, weights_input)

# Output result as required
print(f"Result: {final_score}")