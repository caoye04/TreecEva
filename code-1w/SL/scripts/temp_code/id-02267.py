from collections import defaultdict

# Simulate system performance logs with timestamps and event types
data_log = [
    (100, 'read', 45), (101, 'write', 12), (102, 'read', 33), (103, 'compute', 8),
    (104, 'read', 56), (105, 'write', 19), (106, 'compute', 5), (107, 'read', 41)
]

# Threshold for high-load operations
threshold = 20

# Track operation counts by type
op_count = defaultdict(int)
# Track cumulative load per type
load_profile = defaultdict(int)
# Misleading metric: peak timestamp gap (not used in final score)
timestamp_gaps = []
prev_time = data_log[0][0]

for entry in data_log:
    ts, op, load = entry
    op_count[op] += 1
    load_profile[op] += load
    if ts > prev_time:
        gap = ts - prev_time
        timestamp_gaps.append(gap)  # Dead code path — not used later
    prev_time = ts

# Calculate average load across all operations
total_load = sum(load_profile[op] for op in load_profile)
operation_count = len(data_log)
avg_load = total_load / operation_count if operation_count else 0

# Identify high-load operations above threshold
high_load_ops = list(filter(lambda x: x[2] > threshold, data_log))
high_load_count = len(high_load_ops)

# Compute efficiency score: ratio of high-load ops to total, adjusted by avg_load
# If average load is below 30, boost score by 1.5x (favoring balanced systems)
efficiency_score = high_load_count / operation_count if operation_count else 0
if avg_load < 30:
    efficiency_score *= 1.5  # Adjustment based on system-wide load

# Distractor computation: normalize op count variance (unused)
op_variance = sum((cnt - avg_load / len(op_count))**2 for cnt in op_count.values())
normalized_var = op_variance / (avg_load + 1)  # Not used anywhere

# Final processing function
def process_metrics(log, thresh):
    read_total = sum(load for ts, op, load in log if op == 'read')
    write_total = sum(load for ts, op, load in log if op == 'write')
    compute_ratio = sum(1 for _, op, _ in log if op == 'compute') / len(log)
    
    # Secondary adjustment: if reads dominate and compute ratio is low, reduce score
    if read_total > 2 * write_total and compute_ratio < 0.2:
        return int(efficiency_score * 0.8)
    return int(efficiency_score)

final_output = process_metrics(data_log, threshold)
Result: {final_output}