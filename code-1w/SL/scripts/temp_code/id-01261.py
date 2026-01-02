from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [15, 23, 18, 47, 29, 33, 41, 12]
    processed = []
    temp_sum = 0

    for val in raw_data:
        if val % 2 == 0:
            temp_sum += val * 0.5
        else:
            processed.append(val + 2)
    
    # Distractor: irrelevant transformation
    shifted = [x - 1 for x in processed if x > 20]
    shifted.append(temp_sum)

    metrics = defaultdict(int)
    for i, val in enumerate(processed):
        metrics[f'entry_{i}'] = val * (i + 1)
    
    return metrics

# Analyze and filter based on dynamic threshold
def compute_threshold(data):
    base = sum(data.values()) / len(data)
    adjustment = len([v for v in data.values() if v > 30])
    dummy_calc = adjustment ** 0.5 if adjustment > 0 else 0
    return int(base) + 5

# Main evaluation logic with early exits
def evaluate_performance(metrics, threshold):
    count_above = 0
    total_contrib = 0.0
    rolling_buffer = []

    for key in sorted(metrics.keys()):
        value = metrics[key]
        
        # Irrelevant slicing operation (distractor)
        sliced_part = str(value)[::-1]
        try:
            reversed_val = int(sliced_part)
        except:
            reversed_val = value

        if value > threshold:
            count_above += 1
            total_contrib += value / threshold
        else:
            rolling_buffer.append(value % 7)

        # Early exit condition (semi-relevant but not always triggered)
        if count_above >= 4:
            break

    # Secondary computation that seems important but isn't fully used
    buffer_avg = sum(rolling_buffer) / len(rolling_buffer) if rolling_buffer else 0

    # Core result derivation
    base_score = int(total_contrib * 100)
    penalty = abs(len(rolling_buffer) - count_above)
    final_score = base_score - penalty * 2

    # Additional red herring calculation
    phantom_score = 0
    for i in range(3):
        phantom_score += (base_score // (i + 1)) if i > 0 else 0

    return final_score

# Execution flow
metrics = collect_metrics()
threshold = compute_threshold(metrics)
final_score = evaluate_performance(metrics, threshold)
print(f"Target result: {final_score}")