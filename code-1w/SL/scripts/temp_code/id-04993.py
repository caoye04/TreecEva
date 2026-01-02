from itertools import combinations
import math

def analyze_pattern(sequence):
    magnitude = sum([x ** 2 for x in sequence])
    threshold = 100
    adjustment_factor = 0.85
    weighted_sum = 0
    temp_result = []

    for i, val in enumerate(sequence):
        if i % 2 == 0:
            weighted_sum += val * (i + 1)
        else:
            weighted_sum -= val * 0.5

    # Distractor: Irrelevant transformation
    transformed = list(map(lambda x: math.sqrt(abs(x)) * adjustment_factor, sequence))
    temp_result.extend(transformed)

    # Real computation branch
    if magnitude > threshold:
        magnitude /= len(sequence)

    return magnitude, weighted_sum

def calculate_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return entropy

def process_metrics(raw_data):
    filtered_data = [x for x in raw_data if x > 0]
    sample_pairs = list(combinations(filtered_data, 2))
    
    # Distractor: unused pair analysis
    high_diff_count = 0
    for a, b in sample_pairs:
        if abs(a - b) > 10:
            high_diff_count += 1

    base_metric, auxiliary_score = analyze_pattern(filtered_data)
    entropy_measure = calculate_entropy(filtered_data)

    # Secondary distractor variables
    normalization_constant = len(sample_pairs) if sample_pairs else 1
    dummy_aggregate = sum([a + b for a, b in sample_pairs[:5]]) if len(sample_pairs) >= 5 else 0

    # Core logic chain
    raw_efficiency = base_metric * (1 + entropy_measure)
    adjusted_efficiency = raw_efficiency - (auxiliary_score * 0.1)
    
    # Final computation step
    efficiency_score = int(round(adjusted_efficiency + normalization_constant * 0.05))

    # This print is required to expose the answer
    print(f"Target result: {efficiency_score}")
    return efficiency_score

# Input data
data_points = [4, 7, -3, 12, 0, 9, -5, 6]
final_output = process_metrics(data_points)