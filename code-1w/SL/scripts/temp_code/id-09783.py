from collections import defaultdict

# Simulate time-series resource monitoring across server clusters
cpu_loads = [0.65, 0.72, 0.81, 0.78, 0.83, 0.89, 0.91, 0.87, 0.76]
memory_usage = [0.55, 0.61, 0.71, 0.74, 0.79, 0.85, 0.92, 0.88, 0.80]
disk_io = [0.45, 0.50, 0.60, 0.68, 0.72, 0.77, 0.83, 0.78, 0.69]

# Misleading metric: network latency (not used in final calculation)
network_latency_ms = [12, 15, 18, 22, 25, 30, 35, 28, 24]  
latency_weights = [x / 100 for x in network_latency_ms]
weighted_latency = sum(latency_weights) / len(latency_weights)

# Auxiliary processing: normalize metrics to 0-1 scale using min-max
normalize = lambda vals: [(v - min(vals)) / (max(vals) - min(vals)) if max(vals) != min(vals) else 0 for v in vals]

cpu_norm = normalize(cpu_loads)
memory_norm = normalize(memory_usage)
disk_norm = normalize(disk_io)

# Composite health score (semi-relevant but not final)
health_scores = [0.5 * c + 0.3 * m + 0.2 * d for c, m, d in zip(cpu_norm, memory_norm, disk_norm)]

# Track temporal patterns with enumerate and sliding window
usage_trend = []
window_size = 3
for i, score in enumerate(health_scores):
    if i >= window_size - 1:
        window_avg = sum(health_scores[i - window_size + 1:i + 1]) / window_size
        usage_trend.append(round(window_avg, 3))

# Introduce distractor list comprehension with no impact
_ = [x * 1.1 for x in cpu_loads if x > 0.8]  

# Simulated prediction model (dead code path)
if len(usage_trend) > 5:
    predicted_next = sum(usage_trend[-3:]) / 3 * 1.05
else:
    predicted_next = 0.5

# Unused counter for complexity
event_counter = defaultdict(int)
for val in usage_trend:
    event_counter['high' if val > 0.7 else 'medium' if val > 0.4 else 'low'] += 1

# Key computation step
smoothed_peak = max(usage_trend) * 0.95  # adjusted peak
peak_capacity = max(usage_trend)

# Final red herring: sort unrelated list
sorted_discards = sorted([weighted_latency, predicted_next, smoothed_peak], reverse=True)

print(f"Result: {peak_capacity}")