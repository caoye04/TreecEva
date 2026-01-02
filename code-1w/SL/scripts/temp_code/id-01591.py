def evaluate_performance(metrics, limits):
    temp_result = 0
    backup_log = []
    intermediate_values = []
    
    for key, value in metrics.items():
        if key == 'latency':
            normalized = (100 - value) * 1.5
            intermediate_values.append(normalized)
            if normalized > limits[key]:
                temp_result += int(normalized // 2)
            else:
                temp_result -= 1
        elif key == 'throughput':
            adjusted = value * 0.8 + 10
            intermediate_values.append(adjusted)
            if adjusted >= limits[key]:
                temp_result += 5
        elif key == 'error_rate':
            inverted = 100 - (value * 10)
            # Distractor: this list accumulates but isn't used
            backup_log.append(inverted)
            temp_result += max(0, int(inverted / 5))
    
    # Distractor computation: complex but irrelevant
    outlier_count = 0
    for val in intermediate_values:
        if val < 0 or val > 150:
            outlier_count += 1
    if outlier_count > 0:
        adjustment_factor = outlier_count * 0.5
        temp_result -= int(adjustment_factor)

    # Real logic continues
    final_adjustment = 0
    if 'latency' in metrics and metrics['latency'] < 40:
        final_adjustment += 3
    if 'throughput' in metrics and metrics['throughput'] > 120:
        final_adjustment += 2
    
    temp_result += final_adjustment

    # Bitwise interference - looks important but only minor effect
    flag = 0b1010
    if temp_result % 2 == 0:
        flag = flag ^ 0b1111  # toggle bits
    temp_result += flag & 1  # only adds 1 if LSB is set after XOR

    # Slicing distraction on a constructed list
    history = [i * 2 for i in range(10)]
    recent_history = history[-3:]  # unused slice
    temp_result += len(recent_history)  # side effect

    return temp_result

# Main data setup
metric_data = {
    'latency': 35,
    'throughput': 130,
    'error_rate': 2.5
}

thresholds = {
    'latency': 70,
    'throughput': 100,
    'error_rate': 5
}

initial_offset = sum([x for x in range(5)])  # distractor: equals 10
buffer_zone = set([1, 2, 3]) | {4, 5}  # unused set operation

final_score = evaluate_performance(metric_data, thresholds)
print(f"Target result: {final_score}")