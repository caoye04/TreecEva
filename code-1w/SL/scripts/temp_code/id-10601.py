from collections import defaultdict
import math

def analyze_pattern(sequence):
    freq = defaultdict(int)
    for item in sequence:
        freq[item] += 1
    return {k: v for k, v in freq.items() if v > 1}

def transform_values(raw_list):
    # Misleading transformation that isn't used in final result
    shifted = [x ** 2 - x for x in raw_list]
    normalized = [round(math.log(x + 1), 3) for x in shifted if x > 0]
    return normalized

def calculate_baseline(input_data):
    total = 0
    count = 0
    temp_buffer = []
    for val in input_data:
        if val % 3 == 0 and val > 0:
            total += val
            count += 1
            temp_buffer.append(val * 0.1)  # Distractor: buffer not used later
    return total // count if count else 0

def calculate_performance(data):
    # Core logic with distractors
    averages = []
    outliers = []
    cumulative = 0

    for chunk in data:
        filtered = [x for x in chunk if x > 10]  # List comprehension
        if len(filtered) >= 3:
            segment_avg = sum(filtered) / len(filtered)
            averages.append(segment_avg)
            cumulative += segment_avg
        else:
            outliers.extend(filtered)

    # Semi-relevant processing
    adjusted_cumulative = cumulative * 1.1

    # Irrelevant slicing operations (distractor)
    mirror_slice = averages[::-1]
    mid_section = mirror_slice[1:-1] if len(mirror_slice) > 2 else []

    # Final computation
    base_ref = calculate_baseline([item for sublist in data for item in sublist])
    scaling_factor = len(averages) or 1
    final_score = int((adjusted_cumulative / scaling_factor) + base_ref)

    # Red herring: unused variable with complex derivation
    theoretical_peak = max([max(chunk) for chunk in data if chunk]) ** 2 / 100

    return final_score

# Main execution
raw_input_data = [
    [5, 12, 18, 24, 6],
    [14, 20, 9],
    [16, 22, 30, 11],
    [7, 8, 4, 13]
]

# Transform but do not use (distractor call)
unused_transform = transform_values([item for sublist in raw_input_data for item in sublist])

# Actual used data
benchmark_data = [
    [x * 2 for x in row] for row in raw_input_data  # Element-wise doubling
]

# Critical statement
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")