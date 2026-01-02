def evaluate_performance(metrics, threshold):
    # Initialize relevant and irrelevant variables
    count_above = 0
    total_weight = 0.0
    temp_buffer = []
    outlier_count = 0  # distractor: not used in final logic

    weights = {key: len(key) for key in metrics}  # weight by metric name length

    for metric in metrics:
        raw_value = len(metric) * (4 if 'x' in metric else 3)  # arbitrary scaling
        normalized = raw_value % 17

        # Irrelevant computation block (distractor)
        temp_buffer.append(normalized * 2)
        if normalized > 10:
            outlier_count += 1  # dead-end tracking

        # Relevant logic
        if normalized > threshold:
            count_above += 1
        total_weight += weights[metric]

    # More distraction: unused aggregation
    avg_buffer = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    stability_index = avg_buffer / (count_above + 1)  # not used

    # Core result calculation
    adjustment = len(metrics.intersection({'x_perf', 'x_load', 'x_timing'}))
    base_score = count_above * int(total_weight // len(metrics))
    final_score = base_score + adjustment

    return final_score


# Setup data
metric_set = set()
metric_set.add('response_time')
metric_set.add('throughput')
metric_set.add('error_rate')
metric_set.add('x_perf')
metric_set.add('reliability')

base_threshold = 5

# Dead code path: simulates alternative logic but never called
def debug_mode():
    return sum([i**2 for i in range(5)])  # irrelevant

aux_data = [1, 2, 3]
event_log = {'events': aux_data, 'active': False}  # unused structure

# Key execution point
final_score = evaluate_performance(metric_set, base_threshold)

# Output result
print(f"Result: {final_score}")