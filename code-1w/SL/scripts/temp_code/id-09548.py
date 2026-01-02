from itertools import combinations

# Simulate system performance metrics under varying load conditions
def generate_metrics(base_load, stress_factor):
    linear_component = base_load * 1.8
    nonlinear_component = (base_load ** 1.5) * stress_factor / 100
    penalty = 0
    if base_load > 40:
        penalty = (base_load - 40) * 0.5
    adjusted = linear_component + nonlinear_component - penalty
    return round(adjusted, 3)

# Apply dynamic weighting based on stability thresholds
def calculate_weight(metric_value, threshold=65):
    if metric_value < threshold:
        return 1.2
    else:
        return 0.85

# Assess overall performance from multiple metrics
def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Secondary validation: check for outlier suppression
    outliers = []
    for val in metrics:
        if abs(val - sum(metrics)/len(metrics)) > 20:
            outliers.append(val)
    
    # Only use non-outliers in final calculation
    filtered_metrics = [m for m in metrics if m not in outliers]
    filtered_weights = [weights[i] for i, m in enumerate(metrics) if m not in outliers]
    
    temp_product = 1
    for m, w in zip(filtered_metrics, filtered_weights):
        weighted_sum += m * w
        total_weight += w
        temp_product *= (w % 1)  # distractor: unused computation
    
    # Additional irrelevant tracking
    convergence_steps = 0
    temp_val = total_weight
    while temp_val > 1:
        temp_val /= 2
        convergence_steps += 1  # dead code path
    
    if total_weight == 0:
        return 0.0
    return round(weighted_sum / total_weight, 3)

# Main execution flow
base_loads = [35, 42, 33, 55, 28]
stress_factors = [1.1, 0.9, 1.2, 0.7, 1.3]

# Generate raw performance data
detailed_logs = []
metrics = []
for load, factor in zip(base_loads, stress_factors):
    raw_score = generate_metrics(load, factor)
    detailed_logs.append({'load': load, 'score': raw_score})
    metrics.append(raw_score)

# Compute individual weights
weights = [calculate_weight(m) for m in metrics]

# Analyze correlation pairs (distractor block)
correlation_pairs = list(combinations(metrics, 2))
total_pairs = len(correlation_pairs)
high_correlation_count = 0
for a, b in correlation_pairs:
    if abs(a - b) < 5:
        high_correlation_count += 1

# Tracking auxiliary statistic (not used later)
avg_pair_diff = 0
if total_pairs > 0:
    avg_pair_diff = round(sum(abs(a-b) for a,b in correlation_pairs) / total_pairs, 3)

# Key evaluation point
final_score = evaluate_performance(metrics, weights)

# Irrelevant formatting step
output_template = "Result: {value}"
print(output_template.format(value=final_score))