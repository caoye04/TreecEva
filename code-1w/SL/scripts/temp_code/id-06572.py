import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(x ** 2 for x in data if x > 0) // len(data)

# Misleading intermediate transformation
def preprocess_signal(signal):
    filtered = [x for x in signal if abs(x) > 0.5]
    normalized = [x / max(filtered) for x in filtered]
    return normalized[::-1]  # Reverse order – irrelevant to final result

# Decoy function that looks important but isn't used in critical path
def compute_risk_factor(values):
    running_total = 0
    for i, v in enumerate(values):
        if i % 3 == 0:
            running_total += math.sin(v) * 100
    return int(running_total) % 1000

# Real processing function with key logic buried under distractions
def evaluate_performance(metrics, baseline):
    # Irrelevant slicing and manipulation
    window = metrics[3:10][::-1]  # Reverse slice – not actually needed
    offset = len(metrics) % 7

    # Distractor variables
    temp_result = 0
    accumulator = []
    for idx, val in enumerate(metrics):
        if idx % 2 == 0:
            temp_result += int(math.log(abs(val) + 1, 2))
        else:
            temp_result -= (val % 4)
        accumulator.append(temp_result)
    
    # Meaningless grouping operation
    groups = {}
    for i, x in enumerate(accumulator):
        key = i % 5
        if key not in groups:
            groups[key] = []
        groups[key].append(x)

    # Core logic hidden among noise
    threshold = baseline * 0.85
    count_above = 0
    squared_sum = 0
    
    for m in metrics:
        if m > threshold:
            count_above += 1
            squared_sum += m ** 2

    # Real answer derivation (non-obvious due to surrounding noise)
    avg_sq = squared_sum / count_above if count_above > 0 else 0
    adjustment = math.floor(avg_sq ** 0.5)
    
    # Key statement
    final_score = adjustment * 3 + len([x for x in metrics if x < 0])

    # More red herrings
    checksum = sum(accumulator[i] for i in range(0, len(accumulator), 4)) % 100
    diagnostic_flag = True if checksum > 50 else False

    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data with mixed positive/negative, realistic pattern
    telemetry_data = [12, -3, 15, 8, -6, 22, 11, 9, 14, 7, 5, 18]
    base_ref = 10

    # Unused transformations (distractors)
    processed_data = preprocess_signal([x / 3.5 for x in telemetry_data])
    risk_code = compute_risk_factor(telemetry_data)

    # Critical execution point
    final_score = evaluate_performance(telemetry_data, base_ref)
    
    # Output result as required
    print(f"Target result: {final_score}")