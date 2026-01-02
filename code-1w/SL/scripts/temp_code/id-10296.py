from itertools import combinations

def analyze_pattern(sequence, threshold=3):
    """ Analyze sequence for hidden patterns (distractor function) """
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if abs(sequence[i] - sequence[j]) < threshold:
                count += 1
    return count

def transform_data(data_list):
    """ Apply irrelevant transformation to mislead reasoning """
    temp_result = []
    for item in data_list:
        if item % 2 == 0:
            temp_result.append(item * 1.5)
        else:
            temp_result.append(item * 0.8)
    return [x for x in temp_result if x > 5]

def evaluate_condition(x, y, z):
    """ Redundant logical evaluation with misleading significance """
    if x < y and not (z > x or y == z):
        return x * 2
    elif x >= y and z != x:
        return y + z
    else:
        return z - x

def calculate_entropy(values):
    """ Fake entropy calculation - dead end logic """
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 3)

def generate_pairs(limit):
    """ Create unused pairs for distraction """
    return list(combinations(range(limit), 2))

def calculate_aggregate(input_seq, mode='strict'):
    # Core relevant logic starts here
    base_values = [x for x in input_seq if x % 3 == 0]  # Filter multiples of 3
    
    # Irrelevant filtering (looks important but unused later)
    filtered_temp = [x for x in input_seq if x > 10 and x % 4 != 0]
    
    # Distractor: complex-looking but unused transformation
    transformed = transform_data(base_values)
    pattern_count = analyze_pattern(base_values)
    
    # Real computation path begins
    adjusted = []
    for val in base_values:
        if val == 0:
            adjusted.append(1)
        else:
            # Nested conditional expression (required python feature)
            adjustment = val // 2 if val > 0 else -(-val // 2)
            adjusted.append(val + adjustment)
    
    # Simulate early termination condition (never triggers due to data)
    if mode == 'early' and len(adjusted) > 10:
        return sum(adjusted[:10])
    
    # Key accumulation step
    cumulative = 0
    for idx, adj_val in enumerate(adjusted):
        multiplier = 1 if idx % 2 == 0 else -1
        cumulative += multiplier * adj_val
    
    # Secondary manipulation that actually matters
    final_shift = evaluate_condition(cumulative, len(base_values), pattern_count)
    
    # Final computation using conditional expression
    final_score = cumulative + (final_shift if cumulative > 0 else -final_shift)
    
    # Critical execution point
    return final_score

# Unused but plausible-looking data structures
historical_logs = [12, 15, 18, 21, 24, 27, 30]
metadata_cache = {'version': '2.1', 'active': True, 'flags': [1, 0, 1]}

# Generate unused combinatorial pairs (heavy distractor)
decoy_pairs = generate_pairs(8)

# Actual input data
primary_input = [6, 9, 0, 12, 15, 18, -3, 21]

# Execute main logic
result_buffer = calculate_entropy(primary_input)
score_snapshot = analyze_pattern(primary_input, threshold=4)

# Key execution point
final_score = calculate_aggregate(primary_input, mode='strict')

# Output result as required
print(f"Result: {final_score}")