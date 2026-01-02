from itertools import combinations

def analyze_patterns(sequence, threshold):
    count = 0
    total_pairs = 0
    temp_result = []
    # Irrelevant tracking variables (distractors)
    max_run = 0
    current_run = 0
    prev_val = None

    for val in sequence:
        if prev_val is not None and val == prev_val:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 1
        prev_val = val

    # Real logic: count ascending pairs
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            count += 1

    # Semi-relevant: generate all 2-combinations (not directly used later but plausible)
    comb = list(combinations(sequence, 2))
    for a, b in comb:
        if a + b > threshold:
            total_pairs += 1

    return count, total_pairs


def compute_aggregate(data_set, mode="strict"):
    flat_data = []
    shape_info = []
    # Distractor: complex unpacking and enumeration
    for idx, row in enumerate(data_set):
        shape_info.append((idx, len(row)))
        for elem in row:
            flat_data.append(elem)

    # Misleading normalization step (unused)
    normalized = [x / (max(flat_data) + 1e-5) for x in flat_data]

    # Real computation begins
    unique_vals = set(flat_data)
    filtered = [x for x in flat_data if x % 2 == 1]  # Keep odd values

    # Use of zip to align shifted sequences
    paired_diffs = []
    for a, b in zip(filtered, filtered[1:]):
        paired_diffs.append(abs(b - a))

    avg_diff = sum(paired_diffs) / len(paired_diffs) if paired_diffs else 0

    # Secondary analysis with distractor threshold
    _, extra_metric = analyze_patterns(flat_data, threshold=15)

    # Final score computation — only some components are relevant
    base_score = len(unique_vals)
    penalty = len(flat_data) - len(filtered)  # Even number penalty
    bonus = 10 if avg_diff > 2.0 else 5

    # Dead code branch (never executed due to mode)
    adjustment = 0
    if mode == "experimental":
        adjustment = extra_metric // 5

    final_score = base_score * 3 - penalty + bonus + adjustment
    return final_score

# Main execution
input_grid = [
    [4, 7, 3],
    [7, 2, 9],
    [1, 8, 5]
]

result = compute_aggregate(input_grid, mode="strict")
print(f"Result: {result}")