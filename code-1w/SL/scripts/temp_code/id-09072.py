from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:  # distractor logic
                count += 1
    return count

def calculate_final_score(ranks, multiplier):
    base = sum(ranks)
    adjustment = 0
    rank_set = set(ranks)
    
    # Real logic: count pairs with difference 3
    valid_pairs = 0
    for a, b in combinations(rank_set, 2):
        if abs(a - b) == 3:
            valid_pairs += 1
    
    # Distractor: unused transformation
    transformed = [x * 2 + 1 for x in ranks if x % 2 == 0]
    dummy_sum = sum(transformed)  # irrelevant
    
    # Real adjustment
    if valid_pairs > 2:
        adjustment = 15
    else:
        adjustment = 5
    
    # More distraction: complex but unused dictionary
    stats = {
        'max': max(ranks),
        'min': min(ranks),
        'range': max(ranks) - min(ranks),
        'dummy_metric': len(transformed) * 3
    }
    
    return base * multiplier + adjustment

# Main execution
rank_data = [4, 7, 1, 4, 10]
balance_factor = 2.5  # unused variable
bonus_multiplier = 3

# Irrelevant preprocessing
duplicates_removed = list(set(rank_data))
duplicate_count = len(rank_data) - len(duplicates_removed)

# Key computation
final_score = calculate_final_score(rank_data, bonus_multiplier)

# Output
print(f"Result: {final_score}")