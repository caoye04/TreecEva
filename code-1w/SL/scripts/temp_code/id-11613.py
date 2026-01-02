def analyze_workload_efficiency(timestamps, loads, thresholds):
    cumulative_load = 0
    peak_moment = None
    for i, (t, load) in enumerate(zip(timestamps, loads)):
        if load > thresholds.get(t % 24, 0):
            cumulative_load += load * 1.1
            if peak_moment is None or load > loads[peak_moment]:
                peak_moment = i

    adjustment_factor = 0.95 if cumulative_load > 500 else 1.0
    return cumulative_load * adjustment_factor, peak_moment


def calculate_allocation_score(configurations, base_score=100):
    score = base_score
    for config in configurations:
        if len(config) > 3:
            score -= len([c for c in config if c < 0])
        else:
            score += sum(config)
    return score

# Simulated system resource data
timestamps = list(range(8, 20)) + list(range(20, 24)) + list(range(0, 8))
loads = [45, 60, 75, 88, 95, 105, 120, 130, 140, 135, 125, 110, 90, 70, 
         55, 50, 48, 47, 46, 45, 44, 43, 42, 41]
thresholds = {h: 100 if 9 <= h <= 18 else 80 for h in range(24)}

# Irrelevant configuration set (distractor)
configurations = [
    [1, 2, 3],
    [-1, 4, 5, 6],
    [0, 1],
    [7, 8, 9, 10, -2]
]

# Real-time usage log and allocation map
usage_log = loads[2:18:2]  # Slicing: every 2nd element from index 2 to 18
allocation_map = {i: 200 - i*10 for i in range(len(usage_log))}

# Secondary derived metrics (mostly unused)
window_size = 4
rolling_averages = []
for i in range(len(loads) - window_size + 1):
    window_avg = sum(loads[i:i+window_size]) / window_size
    rolling_averages.append(round(window_avg, 2))

# Auxiliary state tracking (distractor)
current_state = {
    "active": True,
    "mode": "balanced",
    "priority": 2,
    "buffer": [x % 15 for x in loads[:10]]
}

# Key computation chain
raw_efficiency, peak_idx = analyze_workload_efficiency(timestamps, loads, thresholds)

# Mid-level transformation with slicing
temp_slice = usage_log[1:-1]  # Remove first and last
slice_mean = sum(temp_slice) / len(temp_slice) if temp_slice else 0

# Allocation scoring (irrelevant but plausible)
score = calculate_allocation_score(configurations)
offset_correction = len(rolling_averages) - len(usage_log)

# Core logic determining final capacity
base_capacity = 1000
used_capacity = sum(usage_log) * 1.05
reserved_margin = 0.15 * base_capacity

# Final computation
final_capacity = base_capacity - used_capacity - reserved_margin

# Additional noise
if current_state["active"]:
    final_capacity *= 0.98
    extra_buffer = offset_correction * 2.5
    final_capacity -= extra_buffer  # Minor reduction based on length diff

# Print result as required
print(f"Result: {final_capacity}")