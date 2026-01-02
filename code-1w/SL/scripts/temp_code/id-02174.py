from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 150, 130, 160, 90]
    adjustments = [0.9, 1.1, 1.0, 0.95, 1.05]
    processed = []
    for i in range(len(raw_data)):
        temp_val = raw_data[i] * adjustments[i]
        if temp_val > 140:
            temp_val *= 0.8  # Throttling penalty
        processed.append(temp_val)
    return processed

# Weighting strategy for different components
def generate_weights(n):
    base_weights = [0.2] * n
    scaling_factor = 1.0 / sum(base_weights)
    adjusted = [w * scaling_factor for w in base_weights]
    # Dummy computation - irrelevant to final logic
    dummy_sum = sum([x**2 for x in adjusted])
    normalized = [w + 0.01 for w in adjusted]  # Slight bias
    return normalized[:n]

# Misleading diagnostic function (never called)
def diagnose_anomalies(data):
    anomaly_count = 0
    for val in data:
        if val < 100 or val > 150:
            anomaly_count += 1
    return anomaly_count

# Core evaluation logic
def evaluate_performance(metrics, weights):
    cumulative = 0.0
    weighted_total = 0.0
    for i in range(min(len(metrics), len(weights))):
        contribution = metrics[i] * weights[i]
        weighted_total += contribution
        
    # Secondary adjustment based on trend
    trend_boost = 0.0
    for i in range(1, len(metrics)):
        if metrics[i] > metrics[i-1]:
            trend_boost += 5.0
    
    # Apply boost only if average metric exceeds threshold
    avg_metric = sum(metrics) / len(metrics)
    if avg_metric > 125:
        cumulative = weighted_total + trend_boost
    else:
        cumulative = weighted_total
        
    # Irrelevant tracking variable (distractor)
    peak_contribution = max([metrics[i] * weights[i] for i in range(len(metrics))])
    
    return int(cumulative)

# Auxiliary counter for monitoring (not used in result)
execution_counter = defaultdict(int)
execution_counter['attempts'] += 1

# Main execution flow
raw_metrics = collect_metrics()
weights = generate_weights(len(raw_metrics))

# Diagnostic check (result unused)
diag_result = diagnose_anomalies(raw_metrics)

# Key computational statement
final_score = evaluate_performance(raw_metrics, weights)

# Print result as required
print(f"Result: {final_score}")