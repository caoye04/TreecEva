from itertools import combinations

def preprocess_names(names):
    processed = []
    for name in names:
        cleaned = name.strip().lower().replace(' ', '_')
        if len(cleaned) > 3:
            processed.append(cleaned)
    return processed

def validate_entries(data):
    valid_count = 0
    for item in data:
        if isinstance(item, str) and item.isalpha():
            valid_count += 1
    return valid_count > 2

def compute_pair_metrics(seq):
    total_pairs = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if len(seq[i]) + len(seq[j]) > 5:
                total_pairs += 1
    return total_pairs

def calculate_ranking(candidates):
    base_values = [len(candidate) for candidate in candidates]
    adjusted = [val * 2 if val % 2 == 0 else val + 1 for val in base_values]
    
    # Irrelevant intermediate: string processing distraction
    formatted_names = preprocess_names(candidates)
    name_length_sum = sum(len(name) for name in formatted_names)
    
    # Dummy logic that doesn't affect final result
    if validate_entries(candidates):
        temp_result = compute_pair_metrics(formatted_names)
        temp_result *= 0.5
    
    # Core calculation
    cumulative = 0
    for idx, val in enumerate(adjusted):
        if idx % 2 == 0:
            cumulative += val
        else:
            cumulative -= val // 2
    
    # Secondary adjustment
    if len(candidates) > 3:
        cumulative += 10
    
    # Distractor: unused aggregation
    all_combinations = list(combinations(adjusted, 2))
    avg_combo = sum(sum(pair) for pair in all_combinations) / len(all_combinations) if all_combinations else 0
    
    final_score = int(cumulative + avg_combo * 0)  # Neutralized but looks relevant
    return final_score

# Input data
competitors = ['Alice Johnson', 'Bob', 'Charlie Lee', 'Diana Prince']

# Execution
final_score = calculate_ranking(competitors)
print(f"Result: {final_score}")