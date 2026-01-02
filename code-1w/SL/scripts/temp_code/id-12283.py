import itertools

def analyze_pattern(sequence):
    # Irrelevant helper: counts consecutive duplicates (not used in final result)
    count = 0
    for a, b in itertools.pairwise(sequence):
        if a == b:
            count += 1
    return count

def transform_values(data_list):
    # Semi-relevant transformation with distractors
    temp_result = [x * 2 + 1 for x in data_list if x % 3 != 0]  # Skip multiples of 3
    shifted = [val >> 1 for val in temp_result]  # Bit shift right by 1
    
    # Dead code path - never executed due to fixed condition
    if False:
        shifted.append(sum(shifted) // len(shifted))
        
    return shifted

def filter_and_group(values):
    # Group even and odd, but only even matters later
    even_vals = [v for v in values if v % 2 == 0]
    odd_vals = [v for v in values if v % 2 == 1]
    
    # Extra computation on odd (distractor)
    odd_sum = sum(odd_vals)
    _ = [odd_sum * i for i in range(1, 4)]  # Unused list comprehension
    
    return even_vals

def calculate_final_score(clean_data):
    base = sum(clean_data)
    penalty = len(clean_data) if len(clean_data) > 5 else 0
    bonus = 10 if any(x > 100 for x in clean_data) else 0
    
    # Core logic step
    score = base - penalty + bonus
    
    # Red herring adjustment (no effect due to condition)
    debug_mode = False
    if debug_mode:
        score -= sum([score % d for d in range(2, 5)])
    
    return score

# Main execution flow
raw_input = [12, 15, 18, 21, 24, 27, 30, 33]

# Step 1: Remove multiples of 3 via transformation
processed_data = transform_values(raw_input)

# Step 2: Filter groups, keep only even values
processed_data = filter_and_group(processed_data)

# Step 3: Analyze pattern (completely irrelevant call)
dummy_metric = analyze_pattern(raw_input)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")