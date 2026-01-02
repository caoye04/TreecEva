from collections import defaultdict
import itertools

# Simulate system performance metrics over time
timestamps = list(range(10))
data_packets = [120, 135, 140, 128, 150, 160, 145, 130, 138, 142]
errors = [2, 5, 4, 6, 3, 7, 5, 4, 3, 5]
latencies = [45, 52, 49, 55, 43, 60, 54, 48, 46, 50]

# Distractor: irrelevant network parameters
bandwidth_mbps = 1000
packet_size_bytes = 1500
max_queue_size = 256

# Compute derived metrics with some red herrings
success_rate = [(data_packets[i] - errors[i]) / data_packets[i] for i in range(len(data_packets))]
avg_latency = sum(latencies) / len(latencies)
throughput_bps = [pkts * packet_size_bytes * 8 for pkts in data_packets]  # unused

# Real metric computation begins
metrics = defaultdict(float)
metrics['stability'] = max(data_packets) - min(data_packets)
metrics['error_trend'] = sum(errors[i] <= errors[i+1] for i in range(len(errors)-1))
metrics['responsive'] = sum(1 for lat in latencies if lat < avg_latency)

# Distractor: complex but unused data structure
history_log = list(itertools.combinations_with_replacement(['event_a', 'event_b'], 2))
log_summary = {k: v for k, v in enumerate(history_log)}  # dead code

# Weight assignment with misleading normalization
raw_weights = {'stability': 0.4, 'error_trend': 0.35, 'responsive': 0.25}
total_weight = sum(raw_weights.values())
weights = {k: v / total_weight for k, v in raw_weights.items()}  # normalized but same ratio

# Helper function with extra parameters (some unused)
def calculate_component(value, weight, adjustment_factor=1.0, debug_mode=False):
    temp_adjust = adjustment_factor * 1.0  # red herring
    return value * weight * 1.0  # no real adjustment

# Another distractor function (never called)
def analyze_bandwidth_utilization():
    utilization = []
    for i in range(len(throughput_bps)):
        util = throughput_bps[i] / (bandwidth_mbps * 1e6)
        utilization.append(util)
    return utilization

# Core evaluation logic
component_scores = {}
for metric, value in metrics.items():
    # Deliberately verbose call with default args
    component_scores[metric] = calculate_component(value, weights[metric], adjustment_factor=1.0)

# Final aggregation
final_score = sum(component_scores.values())

# Irrelevant post-processing
rounded_final = round(final_score, 4)
score_category = "High" if final_score > 30 else "Low"
metadata_entry = {"run_id": "sim_2024_001", "score_type": "performance"}  # unused

# Output target result
print(f"Result: {final_score}")