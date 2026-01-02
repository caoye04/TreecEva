from itertools import combinations
from math import log

# Simulated network node performance metrics
node_a_latency = 120
node_b_latency = 95
node_c_latency = 140
node_d_latency = 88

# Irrelevant health indicators (distractor)
node_a_health = 0.97
node_b_health = 0.94
node_c_health = 0.89
node_d_health = 0.96

# Base throughput values (some relevant, some not)
throughput_base_a = 420
throughput_base_b = 380
throughput_base_c = 450
throughput_base_d = 390

# Weight adjustment factors (only some are used)
factor_x = 0.85
factor_y = 1.15
factor_z = 0.93

# Real-time signal quality scores
signal_q_a = 89
signal_q_b = 92
signal_q_c = 85
signal_q_d = 94

# Latency normalization function (used)
def normalize_latency(latency, target=100):
    return max(0.1, min(1.0, target / latency))

# Fake degradation estimator (dead code path - distractor)
def estimate_degradation(health, base):
    if health > 0.9:
        return base * 0.95
    else:
        return base * 0.7

# Signal-based boost multiplier (used in aggregation)
def signal_boost(signal_score):
    return 1 + (signal_score - 80) / 200

# Throughput efficiency calculator (used)
def compute_efficiency(base, latency_factor):
    return base * latency_factor

# Red herring: unused optimization heuristic
def optimize_route(nodes):
    return sum([n**2 for n in nodes]) // len(nodes)

# Core metric aggregator (used)
def aggregate_metrics(raw_values, method='weighted'):
    if method == 'median':
        sorted_vals = sorted(raw_values)
        mid = len(sorted_vals) // 2
        return sorted_vals[mid]
    else:
        return sum(raw_values) / len(raw_values)

# Unused data validation check (distractor)
def validate_inputs(*args):
    for arg in args:
        assert isinstance(arg, (int, float)) and arg > 0, "Invalid input"
    return True

# Main processing block
latency_factors = [
    normalize_latency(node_a_latency),
    normalize_latency(node_b_latency),
    normalize_latency(node_c_latency),
    normalize_latency(node_d_latency)
]

# Compute effective throughputs (relevant)
effective_tput_a = compute_efficiency(throughput_base_a, latency_factors[0])
effective_tput_b = compute_efficiency(throughput_base_b, latency_factors[1])
effective_tput_c = compute_efficiency(throughput_base_c, latency_factors[2])
effective_tput_d = compute_efficiency(throughput_base_d, latency_factors[3])

efficiencies = [effective_tput_a, effective_tput_b, effective_tput_c, effective_tput_d]

# Apply signal boosts (relevant)
boosted_scores = []
for idx, score in enumerate([signal_q_a, signal_q_b, signal_q_c, signal_q_d]):
    boosted = efficiencies[idx] * signal_boost(score)
    boosted_scores.append(boosted)

# Simulate redundant transformation (distractor)
transformed_scores = []
for s in boosted_scores:
    temp_val = s * factor_x
    temp_val -= 5
    temp_val = max(temp_val, 0)
    transformed_scores.append(temp_val)  # Not used later

# Generate combination insights (partially relevant)
comb_sets = list(combinations(boosted_scores, 2))
combo_products = [a * b for a, b in comb_sets]
avg_combo_product = sum(combo_products) / len(combo_products)

# Final weight vector (only final_weights is used)
temp_weights = [1.0, 0.8, 1.2, 0.9]
scaled_weights = [w * 1.1 for w in temp_weights]
final_weights = [w / sum(scaled_weights) for w in scaled_weights]

# Performance metrics to be aggregated
metrics = boosted_scores  # This is the real input
weights = final_weights

# Dead function call (distractor)
_ = optimize_route([node_a_latency, node_b_latency, node_c_latency, node_d_latency])

# Actual aggregation logic
weighted_sum = 0
for i in range(len(metrics)):
    weighted_sum += metrics[i] * weights[i]

performance_floor = 350
performance_ceiling = 500
clamped_performance = max(performance_floor, min(performance_ceiling, weighted_sum))

# Secondary adjustment based on combo insight
if avg_combo_product > 120000:
    adjustment = (avg_combo_product / 100000) * 0.05
    clamped_performance *= (1 + adjustment)

# Final scoring with logarithmic scaling
log_factor = log(clamped_performance - 340)
final_score = int(clamped_performance * log_factor) // 2

# Output result
print(f"Result: {final_score}")