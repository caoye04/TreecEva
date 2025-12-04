from collections import Counter

def calculate_base_score(items):
    # Irrelevant computation that creates distraction
    temp_sum = sum(x * 2 for x in range(5, 15))  # Dead code - result unused
    
    # Main logic: count occurrences and apply scoring rules
    counter = Counter(items)
    base_score = 0
    
    for item, count in counter.items():
        if count >= 2:
            base_score += count * 10
        elif item % 3 == 0:
            base_score += item * 2  # Misleading path - rarely triggered
        
        # Distractor operation
        unused_var = item ** 2 - count * 5  # Completely irrelevant
    
    return base_score

def score_adjustment(data, modifier):
    # Multiple irrelevant computations
    fake_total = len(data) * modifier + 7
    decoy_score = fake_total // 3 + 25  # Dead end calculation
    
    # Real adjustment logic
    if modifier > 5:
        adjustment = modifier * 2
    else:
        adjustment = modifier * 3
    
    # More distraction
    unused_array = [x for x in range(adjustment, adjustment + 10)]
    
    base = calculate_base_score(data)
    final = base + adjustment
    
    # Final irrelevant operation that might confuse
    misleading_final = final * 0 + decoy_score  # Never used
    
    return final

# Main execution
input_data = [3, 7, 3, 12, 7, 8, 3, 5, 12, 7]
bonus_modifier = 4

# Distractor variables and operations
fake_data = [x + 1 for x in input_data]
dummy_counter = Counter(fake_data)
useless_sum = sum(dummy_counter.values()) * 2

final_score = score_adjustment(input_data, bonus_modifier)
print(f"Result: {final_score}")