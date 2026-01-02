from collections import defaultdict

def preprocess_data(raw):
    # Irrelevant transformation (not used in final logic)
    temp_map = defaultdict(int)
    for item in raw:
        temp_map[item] += 1
    normalized = [x / 2 for x in raw if x > 0]
    return normalized

def filter_outliers(seq):
    mean_val = sum(seq) / len(seq)
    return [x for x in seq if abs(x - mean_val) < 2 * mean_val]

def apply_weighting(values, factors):
    # Some bitwise manipulation for obfuscation
    masked_factors = [f ^ 3 for f in factors]  # XOR with 3 - not actually affecting final use
    weighted = []
    for i in range(len(values)):
        weighted.append(values[i] * factors[i])
    return weighted

def count_high_bits(num_list):
    # Distractor function: counts set bits above threshold
    total_bits = 0
    for num in num_list:
        if num > 5:
            total_bits += bin(num).count('1')
    return total_bits  # Never used

def calculate_final_score(data, weights):
    processed = preprocess_data(data)
    filtered = filter_outliers(processed)
    adjusted_weights = [w + 0.1 for w in weights]
    
    # Introduce irrelevant intermediate variables
    temp_sum = sum([x // 2 for x in data if x % 2 == 0])  # Dead computation
    bit_count = count_high_bits(data)  # Unused
    
    weighted_values = apply_weighting(filtered, adjusted_weights[:len(filtered)])
    base_score = sum(weighted_values)
    
    # Core logic step 1: apply penalty if average exceeds threshold
    avg = sum(data) / len(data)
    penalty = 0
    if avg > 10:
        penalty = 5
    elif avg > 5:
        penalty = 2
    
    # Core logic step 2: bonus for even-odd pattern
    even_odd_transition = 0
    for i in range(len(data) - 1):
        if (data[i] % 2) != (data[i+1] % 2):
            even_odd_transition += 1
    
    bonus = 1 if even_odd_transition >= 3 else 0
    
    final_score = int(base_score - penalty + bonus)
    
    # Execution point of interest
    return final_score

# Main execution
raw_data = [12, 14, 7, 3, 22, 9]
weights = [1, 2, 1, 3, 2, 1]

# Misleading pre-computations
shadow_copy = [x * 2 for x in raw_data]
duplicate_filter = [y for y in shadow_copy if y < 20]

final_score = calculate_final_score(raw_data, weights)
print(f"Target result: {final_score}")