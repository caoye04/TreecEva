import heapq
import statistics

temperature_readings = [23.5, 25.1, 22.8, 24.3, 26.7, 21.9, 25.0, 23.8, 24.9, 22.4]
window_size = 3
stability_heap = []
thermal_readings = []

# Process temperature windows and calculate stability metrics
for i in range(len(temperature_readings) - window_size + 1):
    window = temperature_readings[i:i+window_size]
    mean_temp = statistics.mean(window)
    variance_temp = statistics.variance(window) if len(window) > 1 else 0
    stability_metric = mean_temp / (1 + variance_temp)
    heapq.heappush(stability_heap, (-stability_metric, i))  # Max heap using negative values

# Calculate thermal index from most stable periods
thermal_weights = {i: 0.0 for i in range(len(temperature_readings))}
top_stable_periods = min(3, len(stability_heap))

for _ in range(top_stable_periods):
    neg_metric, start_idx = heapq.heappop(stability_heap)
    stability_value = -neg_metric
    for j in range(window_size):
        idx = start_idx + j
        if idx < len(temperature_readings):
            thermal_weights[idx] += stability_value * (window_size - j) / window_size

thermal_index = sum(weight * temp for weight, temp in zip(thermal_weights.values(), temperature_readings))
thermal_index = round(thermal_index, 2)

print(f"Result: {thermal_index}")