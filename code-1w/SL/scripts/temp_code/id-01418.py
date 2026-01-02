def analyze_metrics(data_points, filter_mask):
    processed = set()
    temp_sum = 0
    for val in data_points:
        if val & filter_mask:  # bitwise filtering
            processed.add(val % 17)  # modular arithmetic with prime
        temp_sum += val * 2  # irrelevant accumulation (distractor)

    return processed


def calculate_baseline(offset, iterations):
    result = 0
    for i in range(iterations):
        result += (i ** 2) % 9
    result += offset
    return result  # used to seed something unrelated


def track_state(history, current):
    history.append(current)
    return len(history) > 5  # state tracking side effect


def evaluate_performance(metrics, threshold):
    score = 0
    penalty = 0
    
    for m in metrics:
        if m > threshold:
            score += m * 3
        elif m == threshold:
            score += m
        else:
            penalty += m // 2
    
    # Complex but irrelevant cleanup
    temp_data = [x for x in metrics if x % 2 == 0]
    temp_data.reverse()
    _ = [x * x for x in temp_data]  # dead computation

    return score - penalty

# Main execution
raw_values = [23, 45, 12, 67, 34, 89, 21]
mask = 15
metric_set = analyze_metrics(raw_values, mask)

base_threshold = calculate_baseline(4, 8) % 20  # derive threshold via modular arithmetic

history_log = [base_threshold]
_ = track_state(history_log, len(raw_values))
_ = track_state(history_log, sum(raw_values) % 100)

# Key statement
final_score = evaluate_performance(metric_set, base_threshold)

# Irrelevant final transformation block (distractor)
if len(metric_set) > 3:
    adjustment = 0
    for x in metric_set:
        if x % 3 == 0:
            adjustment += 1
    base_threshold += adjustment  # does not affect final_score

print(f"Result: {final_score}")