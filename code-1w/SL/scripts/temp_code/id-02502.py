from itertools import cycle

def analyze_efficiency(metrics, thresholds):
    efficiency = 0
    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        if metric > threshold:
            efficiency += (i + 1) * 0.5
    return efficiency

def evaluate_performance(results, weights):
    weighted_sum = 0
    adjustment_factor = 0.85
    temp_buffer = []

    for idx, (res, w) in enumerate(zip(results, weights)):
        adjusted_val = res * w
        temp_buffer.append(adjusted_val)
        if idx % 2 == 0:
            adjusted_val -= 0.1 * res  # minor correction
        weighted_sum += adjusted_val

    # Irrelevant aggregation
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    spike_count = sum(1 for x in temp_buffer if x > 30)  # unused metric

    # Simulate recalibration (no effect on final result)
    recalibrated = [x * adjustment_factor for x in temp_buffer]
    recalibrated_sum = sum(recalibrated)  # dead computation

    # Key logic: apply bonus only if conditions met
    bonus = 10 if weighted_sum > 120 and len(results) >= 4 else 5
    final_score = int(weighted_sum + bonus)

    return final_score

# Main execution
base_metrics = [24.1, 35.6, 28.3, 41.2, 19.8]
base_thresholds = [22.0, 30.0, 25.0, 38.0, 20.0]
cycle_pattern = cycle([1, -1])

initial_efficiency = analyze_efficiency(base_metrics, base_thresholds)

# Generate synthetic task results with pattern
task_results = []
for val, cycle_val in zip(base_metrics, cycle_pattern):
    transformed = val * 0.75 + (cycle_val * 2.5)
    task_results.append(transformed)

# Unused transformation
inverted_results = [100 - x for x in task_results]  # red herring
smoothed = [round(x, 1) for x in task_results]  # not used

base_weights = [0.9, 1.1, 1.0, 1.2, 0.8]

# Dummy pre-check
valid_entries = [x for x in task_results if x > 10]
dropped_entries = [x for x in task_results if x <= 10]  # always empty

intermediate_total = sum(task_results[:3])  # irrelevant total

final_score = evaluate_performance(task_results, base_weights)
print(f"Target result: {final_score}")