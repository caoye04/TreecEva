def analyze_flow(sequence, limit):
    count = 0
    temp_values = []
    for i in range(len(sequence)):
        if sequence[i] > limit:
            count += 1
            temp_values.append(sequence[i] * 0.9)
    return count, temp_values

flow_data = [12, 15, 30, 25, 40, 22, 35, 18]
limit_threshold = 20

# Irrelevant analysis branch (dead-end computation)
if len(flow_data) > 5:
    dummy_sum = sum(x ** 0.5 for x in flow_data if x % 2 == 0)
    adjustment = dummy_sum / 10

# Real processing begins
valid_count, adjusted_flows = analyze_flow(flow_data, limit_threshold)

# Simulate capacity log with slicing and windowing
window_size = 3
capacity_log = []
for i in range(0, len(adjusted_flows), window_size):
    segment = adjusted_flows[i:i+window_size]
    capacity_log.append(sum(segment))

# Extraneous variable: not used in final result
redundant_metric = [x / 2 for x in capacity_log if x > 40]

# Threshold based on average flow
avg_flow = sum(adjusted_flows) / len(adjusted_flows) if adjusted_flows else 0
threshold = avg_flow * 0.8

# Misleading intermediate calculation (no effect on final result)
spurious_calc = 0
for x in capacity_log:
    if x < threshold:
        spurious_calc += x * 1.1

# Core logic: calculate remaining capacity above threshold
def calculate_remaining(log, thresh):
    total = 0
    for val in log:
        if val > thresh:
            total += val - thresh
    return total

# Final assignment
final_capacity = calculate_remaining(capacity_log, threshold)

# Print result as required
print(f"Target result: {final_capacity}")