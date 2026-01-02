from itertools import combinations

def analyze_patterns(sequence):
    # Irrelevant pattern analysis (distractor)
    pattern_count = {}
    for i in range(2, len(sequence) + 1):
        for combo in combinations(sequence, i):
            s = sum(combo)
            pattern_count[s] = pattern_count.get(s, 0) + 1
    return pattern_count

def preprocess_input(raw_values):
    # Misleading transformation chain
    temp_a = [x ** 2 - x for x in raw_values]
    temp_b = [y for y in temp_a if y % 2 == 0]
    filtered = [z for z in temp_b if z > 10]
    
    # Actual relevant computation begins here
    base_weights = [v // 4 for v in filtered]
    checksum = 0
    for idx, val in enumerate(base_weights):
        checksum ^= (val * (idx + 1))  # Bitwise accumulation
    
    # Dead code path (distractor)
    if checksum < 0:
        base_weights = [abs(x) for x in base_weights]

    return base_weights, checksum

def compute_final_score(data_list):
    running_total = 0
    history = []
    
    # Real logic with moderate nesting
    for step in range(3):
        stage_sum = 0
        for val in data_list:
            transformed = (val + step) * 1.5
            if transformed % 2 == 0:
                stage_sum += int(transformed)
            else:
                stage_sum -= int(transformed // 1.2)
        
        # Accumulate result
        running_total += stage_sum
        history.append(stage_sum)
    
    # Final adjustment using modular arithmetic
    adjustment = len(history) * (running_total % 7)
    final_value = running_total + adjustment
    
    # Unused variable (distractor)
    outlier_flag = any(abs(x) > 1000 for x in history)
    
    return int(final_value)

# Main execution flow
raw_input_data = [5, 8, 12, 14, 19, 21]
processed_data, _ = preprocess_input(raw_input_data)

# Red herring: unused complex structure
pattern_analysis = analyze_patterns(raw_input_data)
suspicious_pairs = list(combinations([x for x in raw_input_data if x % 3 == 0], 2))

# Key statement
final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")