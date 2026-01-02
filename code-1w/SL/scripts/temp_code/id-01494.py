from itertools import combinations

def analyze_patterns(sequence):
    pattern_count = 0
    temp_sum = 0
    for i in range(2, len(sequence) + 1):
        for combo in combinations(sequence, i):
            if sum(combo) % 3 == 0:
                pattern_count += 1
    return pattern_count

def calculate_entropy(data):
    # Irrelevant helper function (dead code path)
    import math
    total = sum(data)
    entropy = 0
    for x in data:
        if x > 0:
            prob = x / total
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

def calculate_final_score(data):
    base_score = 0
    adjustment_factor = 0
    
    # Real logic begins
    filtered = [x for x in data if x % 2 == 1]  # Keep odds
    
    # Distractor: complex but unused computation
    mirrored_pairs = [(x, y) for x in data for y in data if str(x).endswith('3') and str(y).startswith('7')]
    pair_count = len(mirrored_pairs)
    
    # Actual contribution
    for val in filtered:
        base_score += val ** 2
        
    # Conditional adjustment
    if len(filtered) > 3:
        adjustment_factor = 5
    else:
        adjustment_factor = -2
    
    # Secondary processing with string operations
    str_values = ''.join([str(x) for x in data])
    digit_frequency = {d: str_values.count(d) for d in '0123456789'}
    
    # Another distraction: uses itertools but doesn't affect final result
    three_digit_combs = list(combinations([1, 2, 3, 4], 3))
    comb_size = len(three_digit_combs)
    
    # Final score calculation
    noise_offset = digit_frequency.get('7', 0) * 3  # Only digit '7' count matters
    final_score = base_score + adjustment_factor + noise_offset
    
    return final_score

# Main execution
raw_input = [12, 15, 23, 8, 71, 44, 39]
processed_data = []
for num in raw_input:
    if num > 10:
        processed_data.append(num % 25)

# Call the key function
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")