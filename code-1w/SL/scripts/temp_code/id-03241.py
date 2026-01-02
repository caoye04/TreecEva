from collections import defaultdict
import math

def preprocess_metrics(raw_values):
    # Normalize values using z-score (distractor: not actually used in final logic)
    mean_val = sum(raw_values) / len(raw_values)
    variance = sum((x - mean_val) ** 2 for x in raw_values) / len(raw_values)
    std_dev = math.sqrt(variance)
    z_scores = [(x - mean_val) / std_dev for x in raw_values] if std_dev != 0 else [0] * len(raw_values)
    return z_scores

def filter_outliers(data, threshold=3):
    # Dead code path - never called
    return [x for x in data if abs(x) <= threshold]

def evaluate_performance(metrics, base_threshold):
    count_above = 0
    temp_sum = 0.0
    penalty_factor = 1.0

    # Simulate historical performance (semi-relevant but overridden)
    history_tracker = defaultdict(int)
    for idx, val in enumerate(metrics):
        history_tracker[f'entry_{idx % 5}'] += val

    # Actual logic begins here
    sorted_metrics = sorted(metrics, reverse=True)
    top_quartile_index = len(sorted_metrics) // 4 or 1
    top_performers = sorted_metrics[:top_quartile_index]

    # Secondary filtering based on dynamic threshold
    dynamic_floor = base_threshold * 0.8

    for val in top_performers:
        if val > base_threshold:
            count_above += 1
            temp_sum += val
        elif val < dynamic_floor:
            penalty_factor *= 0.9  # Minor penalty decay

    # Irrelevant set operation (distractor)
    unique_caps = set(math.ceil(x) for x in metrics)
    excess_count = len(unique_caps) - len(metrics) // 2
    adjustment = excess_count if excess_count > 0 else 0

    # Core computation
    raw_score = temp_sum * count_above * penalty_factor
    normalized_score = raw_score / (len(metrics) or 1)

    # Additional red herring: complex list comprehension with no effect
    _ = [math.log(1 + x) for x in metrics if x > 0 and x % 2 == 0]

    final_score = int(normalized_score + adjustment)  # Final assignment point
    return final_score

# Main execution
if __name__ == '__main__':
    raw_data_stream = [85, 92, 78, 96, 88, 79, 94, 91, 87, 83]
    base_line = 85

    # Unused preprocessing step (interference)
    standardized = preprocess_metrics(raw_data_stream)

    # Key statement
    final_score = evaluate_performance(raw_data_stream, base_line)
    
    print(f"Result: {final_score}")