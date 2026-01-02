from itertools import combinations

def analyze_segments(data, threshold):
    segments = []
    temp_sum = 0
    segment_count = 0
    for val in data:
        temp_sum += val
        if temp_sum >= threshold:
            segments.append(temp_sum)
            temp_sum = 0
            segment_count += 1
    return segments if segments else [0]


def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 4)


def compute_final_score(data_segments):
    base_score = 0
    adjustment_factor = 0.85
    # Misleading computation - not used in final result
    redundant_calc = sum([x ** 2 for x in data_segments if x > 10])
    temp_result = 0
    for x in data_segments:
        if x % 2 == 0:
            base_score += x * 1.1
        else:
            base_score += x * 0.9
    # Another distraction: unused state tracking
    history_log = [base_score * 0.1] * len(data_segments)
    final_score = int(base_score * adjustment_factor)
    return final_score

# Main execution flow
raw_input = [3, 7, 2, 8, 5, 6, 4, 9]
noise_floor = 10

# Simulate signal segmentation
filtered_data = [x + 1 for x in raw_input if x > 2]
segmented = analyze_segments(filtered_data, noise_floor)

# Extraneous combinatorics (distraction)
possible_pairs = list(combinations(segmented, 2))
dummy_metric = sum([abs(a - b) for a, b in possible_pairs])

# Core processing path
processed_data = [x + 2 for x in segmented]

# Redundant entropy check (not influencing score)
entropy_diagnostic = compute_entropy(processed_data)

# Key assignment statement
final_score = compute_final_score(processed_data)

print(f"Result: {final_score}")