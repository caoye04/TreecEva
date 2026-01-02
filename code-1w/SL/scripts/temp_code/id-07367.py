from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    temp_sum = 0
    auxiliary_data = []
    
    for i in range(len(sequence)):
        if sequence[i] % 3 == 0:
            count += 1
            temp_sum += sequence[i]
        else:
            temp_sum -= sequence[i] % 4
    
    # Distractor: irrelevant transformation
    transformed = [x * 2 + 1 for x in sequence if x < 5]
    auxiliary_data.extend(transformed)

    # Real logic branch
    if count > 2:
        adjustment = sum(1 for a, b in combinations(sequence, 2) if a + b == 10)
        return temp_sum + adjustment * 2
    else:
        return temp_sum - len(auxiliary_data)

def compute_aggregate(data):
    base_value = sum(x for x in data if x > 0)
    penalty = 0
    
    # Misleading intermediate calculations
    inverted_map = {i: val for i, val in enumerate(reversed(data))}
    outlier_check = [val for val in data if abs(val - base_value / len(data)) > 5]
    
    if len(outlier_check) % 2 == 0:
        penalty += 3
    else:
        penalty -= 1

    # Core logic hidden among distractions
    filtered_pairs = list(combinations([x for x in data if x % 2 == 1], 2))
    pair_match_count = sum(1 for p in filtered_pairs if p[0] + p[1] == 8)

    # Dead code path (never executed due to data)
    special_case_flag = False
    if all(x < 0 for x in data):
        return -999  # unreachable with current input

    intermediate_result = analyze_pattern(data)
    final_score = base_value + intermediate_result - penalty + pair_match_count
    
    # Irrelevant string processing (distractor)
    status_log = "Processed: " + "-".join(str(x) for x in data)
    char_count = len(status_log)
    checksum = sum(ord(c) % 5 for c in status_log[:10])

    return final_score

# Main execution
input_sequence = [2, 3, 6, 1, 4, 5]
initial_weight = sum(input_sequence) / len(input_sequence)
dummy_matrix = [[i + j for j in range(3)] for i in range(3)]

final_score = compute_aggregate(input_sequence)
print(f"Result: {final_score}")