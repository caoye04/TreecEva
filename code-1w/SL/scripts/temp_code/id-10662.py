from collections import defaultdict

# Simulate hourly resource usage across multiple servers
current_load = [12, 15, 10, 20, 25, 30, 22, 18, 24, 27, 33, 35]
server_ids = ['srvA', 'srvB', 'srvC', 'srvD', 'srvE']
downtime_logs = {hour: [] for hour in range(24)}

# Initialize trackers
usage_tracker = defaultdict(int)
efficiency_scores = []
baseline_offset = 5

# Process each hour's load data
for hour, load in enumerate(current_load):
    normalized_load = load - baseline_offset
    
    # Assign load distribution across active servers
    for i, sid in enumerate(server_ids):
        slot = (hour + i) % 24
        weighted_contribution = (normalized_load // len(server_ids)) + (1 if i < normalized_load % len(server_ids) else 0)
        usage_tracker[slot] += weighted_contribution

    # Irrelevant computation: log simulated latency spikes (not used later)
    if load > 25:
        downtime_logs[hour].append('high-latency')
    elif load < 15:
        downtime_logs[hour].append('low-utilization')

    # Misleading efficiency metric (never used in final result)
    temp_score = (load ** 0.5) * 0.7 + 10
    efficiency_scores.append(round(temp_score, 2))

# Dead code path: would adjust tracker but condition never met
temporary_shift = False
if len(efficiency_scores) > 15:
    adjusted_tracker = {k+1: v for k, v in usage_tracker.items()}
    temporary_shift = True

# Final peak detection (key statement)
peak_capacity = max(usage_tracker.values())

# Print result
print(f"Result: {peak_capacity}")