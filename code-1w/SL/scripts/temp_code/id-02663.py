from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for length in range(2, len(sequence) + 1):
        for subset in combinations(sequence, length):
            if sum(subset) % 3 == 0:
                count += 1
    return count

def calculate_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log2(prob)
    return round(entropy, 4)

def calculate_final_score(data, weights):
    base_score = 0
    temp_result = 0
    
    # Irrelevant pattern analysis (distractor)
    pattern_count = analyze_patterns([3, 6, 9, 12])
    unused_metric = calculate_entropy([1, 2, 4, 8])
    
    # Core logic begins
    weighted_sum = 0
    weight_total = 0
    for i in range(len(data)):
        if data[i] > 50:
            adjusted_value = data[i] * 0.9
        else:
            adjusted_value = data[i] * 1.1
        weighted_sum += adjusted_value * weights[i]
        weight_total += weights[i]
    
    base_score = weighted_sum / weight_total
    
    # Secondary adjustment based on conditional rules
    bonus = 0
    if base_score > 75:
        bonus = 10
    elif base_score > 60:
        bonus = 5
    else:
        bonus = 2
    
    # Tertiary interference: dead code path (never executed due to fixed input)
    debug_flags = [False, True, False]
    if all(debug_flags):
        temp_result = base_score * 0.95
    
    # Final computation
    final_score = int(base_score + bonus)
    
    # Extra irrelevant variable
    scaling_factor = 1.05  # Not used
    
    return final_score

# Main execution
raw_data = [45, 70, 85, 60]
importance_weights = [0.2, 0.3, 0.4, 0.1]

final_score = calculate_final_score(raw_data, importance_weights)
print(f"Result: {final_score}")