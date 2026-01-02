def analyze_component(x, flag):
    if x < 10:
        return x * 2 + (3 if flag else 0)
    elif x < 25:
        return x + 5 - (2 if not flag else 0)
    else:
        return x // 3


def validate_sequence(seq):
    valid_count = 0
    for i, val in enumerate(seq):
        if val % 2 == 0 and i % 2 == 0:
            valid_count += 1
    return valid_count >= len(seq) // 2


def calculate_performance(data):
    temp_results = []
    adjustment_factor = 0.85
    dummy_counter = 0  # Distractor: not used in final logic
    offset_value = 1  # Semi-relevant: only used in one branch

    for idx, item in enumerate(data):
        processed = 0
        if idx % 2 == 0:
            processed = analyze_component(item, idx % 3 == 0)
        else:
            processed = item + (idx % 4)
            backup = item * 0.9  # Dead computation: never used

        if item > 15:
            processed = int(processed * adjustment_factor)

        temp_results.append(processed)

    # Secondary processing with zip
    paired = list(zip(temp_results, [x**0.5 for x in temp_results]))
    weighted_sum = 0
    weight_acc = 0

    for val, root in paired:
        weight = 1.0 if val > 10 else 0.5
        weighted_sum += val * weight
        weight_acc += weight

    average_score = weighted_sum / weight_acc if weight_acc > 0 else 0

    # Final scoring logic
    threshold_check = sum(1 for x in temp_results if x > 12)
    bonus = 10 if threshold_check > len(temp_results) // 2 else 0

    # Irrelevant string operation (distractor)
    status_msg = "Optimal" if bonus else "Suboptimal"
    char_count = len(status_msg)  # Not used beyond this
    scaling_factor = char_count * 0.1  # Computed but irrelevant

    final_score = int(average_score) + bonus
    return final_score

# Input data
benchmark_data = [8, 22, 14, 31, 9]

# Execution
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")