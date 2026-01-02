from itertools import combinations
from math import log

# Simulated performance metrics from a model evaluation suite
test_results = [0.88, 0.92, 0.76, 0.85, 0.94, 0.67]
metric_names = ['precision', 'recall', 'f1', 'accuracy', 'mcc', 'log_loss']
baseline_thresholds = {name: 0.8 for name in metric_names}
baseline_thresholds['log_loss'] = 0.3

# Auxiliary data — some irrelevant processing
dummy_data = [x ** 2 for x in range(5)]
dummy_pairs = list(combinations(dummy_data, 2))
sum_dummy = sum([a + b for a, b in dummy_pairs if (a + b) % 2 == 0])

# Weight assignment based on importance
weight_map = {name: 1.0 for name in metric_names}
weight_map['f1'] = 1.5
weight_map['accuracy'] = 1.2
weight_map['mcc'] = 1.3

# Transform log_loss to positive utility scale (lower is better → higher is better)
adjusted_results = [r for r in test_results[:-1]]
log_loss_val = test_results[-1]
adjusted_log_loss = max(0, 1 - (log_loss_val / weight_map['mcc']))
adjusted_results.append(adjusted_log_loss)

# Boolean flags for threshold compliance
above_baseline = [adjusted_results[i] >= baseline_thresholds[metric_names[i]] for i in range(len(metric_names))]
compliance_rate = sum(above_baseline) / len(above_baseline)

# Create misleading interaction features
interaction_boost = 0
for i in range(len(adjusted_results)):
    for j in range(i+1, len(adjusted_results)):
        if above_baseline[i] and not above_baseline[j]:
            interaction_boost += adjusted_results[i] * 0.1

# Normalize results to [0,1] range using min-max scaling
min_val, max_val = min(adjusted_results), max(adjusted_results)
normalized_results = [(r - min_val) / (max_val - min_val + 1e-8) for r in adjusted_results]

# Introduce distractor: unused normalization method
z_score_normalized = [(r - min_val) / (max_val - min_val + 1e-8) for r in adjusted_results]

# Define benchmark weights
benchmark_weights = [weight_map[name] for name in metric_names]

# Compute weighted harmonic mean as primary metric
inv_weighted_sum = sum(benchmark_weights[i] / (normalized_results[i] + 1e-6) for i in range(len(normalized_results)))
total_weight = sum(benchmark_weights)
harmonic_performance = total_weight / inv_weighted_sum

# Secondary arithmetic mean for red herring
arithmetic_mean = sum(normalized_results[i] * benchmark_weights[i] for i in range(len(normalized_results))) / total_weight

# Additional conditional logic with partial relevance
if compliance_rate > 0.7:
    adjustment_factor = 1.1
else:
    adjustment_factor = 0.95

# Simulate penalty for low recall
recall_idx = metric_names.index('recall')
if test_results[recall_idx] < 0.8:
    adjustment_factor *= 0.9

# Set of metrics to evaluate
metric_set = set(name.upper() for name in metric_names if len(name) > 3)
metric_set.add('CUSTOM_METRIC_X')
metric_set.discard('CUSTOM_METRIC_X')

# Core evaluation function
def evaluate_performance(metrics, weights):
    base = 0.0
    boost = 0.0
    for i, m in enumerate(metric_names):
        upper_m = m.upper()
        if upper_m in metrics:
            norm_val = normalized_results[i]
            w = weights[i]
            base += w * norm_val
            # Extra boost if precision and recall are both strong
            prec_idx = metric_names.index('precision')
            rec_idx = metric_names.index('recall')
            if upper_m == 'F1' and normalized_results[prec_idx] > 0.7 and normalized_results[rec_idx] > 0.7:
                boost += 0.05
    return (base / sum(weights)) * adjustment_factor + boost + (harmonic_performance * 0.01)

# Final computation step
dummy_calc = sum([x * y for x, y in zip(dummy_data, reversed(dummy_data))])
final_score = evaluate_performance(metric_set, benchmark_weights)

# Output result
print(f"Result: {final_score}")