from itertools import combinations

def preprocess_input(raw_values):
    # Irrelevant transformation (distractor)
    temp_normalized = [round(x * 0.987 for x in raw_values)]
    adjusted = [x + 1.5 for x in raw_values]
    filtered = [x for x in adjusted if x > 10]
    return filtered

def analyze_pattern(seq):
    # Semi-relevant analysis that doesn't affect final result
    pair_sums = []
    for a, b in combinations(seq, 2):
        pair_sums.append(a + b)
    avg_sum = sum(pair_sums) / len(pair_sums) if pair_sums else 0
    return avg_sum

def transform_sequence(data):
    # Complex but partially irrelevant transformation chain
    shifted = [x * 2 - 3 for x in data]
    exponentiated = [x ** 1.5 for x in shifted if x > 0]
    capped = [min(x, 100) for x in exponentiated]
    # But only the length matters later
    return len(capped), capped

def calculate_final_score(dataset):
    base_total = sum(dataset)
    penalty = 0
    
    # Real logic begins: find sequences with specific properties
    valid_triplets = 0
    for i in range(len(dataset)):
        for j in range(i+1, len(dataset)):
            for k in range(j+1, len(dataset)):
                triplet = sorted([dataset[i], dataset[j], dataset[k]])
                if triplet[2] < triplet[0] + triplet[1]:  # Triangle-like inequality
                    valid_triplets += 1
    
    # Distractor computation: unrelated statistics
    mean_val = sum(dataset) / len(dataset) if dataset else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in dataset) / len(dataset) if dataset else 0
    peak = max(dataset) if dataset else 0
    
    # Core scoring logic
    length_bonus = len(dataset) * 3
    triplet_multiplier = valid_triplets // 4
    
    score_component_1 = base_total + length_bonus
    score_component_2 = triplet_multiplier * 7
    final_score = score_component_1 + score_component_2
    
    # Dead code path (never executed due to logic above)
    if False and peak > 1000:
        final_score *= 1.1
    
    return int(final_score)

# Main execution
raw_input_data = [12, 15, 8, 20, 14, 9, 16]
processed_data = preprocess_input(raw_input_data)

# Additional irrelevant tracking
tracking_id = "TK-7890"
status_log = []
for val in processed_data:
    status_log.append(f"{tracking_id}: Stage A - Value {val}")

size_hint, detailed_output = transform_sequence(processed_data)
analysis_metric = analyze_pattern(processed_data)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")