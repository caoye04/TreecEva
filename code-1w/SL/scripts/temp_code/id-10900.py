def analyze_sequence(data):
    processed = set()
    temp_buffer = []
    for val in data:
        if val % 3 == 0 and val % 5 != 0:
            processed.add(val)
            temp_buffer.append(val * 2)
        elif val % 7 == 0:
            processed.discard(val - 1)
    return processed


def filter_candidates(elements, threshold):
    valid_set = set()
    invalid_set = set()
    for e in elements:
        if e > threshold:
            valid_set.add(e)
        else:
            invalid_set.add(e)
    # Dead code - never used
    cleanup = [x for x in invalid_set if x < 0]
    return valid_set


def compute_aggregate(s):
    total = 0
    multiplier = 1
    debug_trace = []
    for num in sorted(s):
        if num < 10:
            total += num ** 2
        elif num < 20:
            total += num * 3
        else:
            total += num
        multiplier *= (num % 7 + 1)  # Irrelevant to final result
        debug_trace.append(multiplier)  # Unused
    return total


def evaluate_performance(metrics):
    base = 0
    adjustment = 0
    for m in metrics:
        if m in {12, 15, 18, 21}:
            base += m // 3
        elif m > 25:
            adjustment += 1
    return base + adjustment * 5

# Main execution
raw_data = [9, 12, 14, 15, 18, 21, 28, 35]
filtered_data = filter_candidates(raw_data, 10)
sequence_metrics = analyze_sequence(filtered_data)

# Extraneous computation - does not affect final result
shadow_copy = {x + 1 for x in sequence_metrics}
duplicate_check = len(sequence_metrics) - len(shadow_copy) + 100

aggregate_value = compute_aggregate(sequence_metrics)
scaling_factor = 0.5  # Unused in logic

final_score = evaluate_performance(sequence_metrics)
print(f"Result: {final_score}")