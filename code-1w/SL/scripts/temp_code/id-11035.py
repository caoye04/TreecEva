def analyze_text_composition(text):
    vowels = {c for c in text.lower() if c in 'aeiou'}
    consonants = {c for c in text.lower() if c.isalpha() and c not in vowels}
    digit_count = sum(1 for c in text if c.isdigit())
    special_char_ratio = len([c for c in text if not c.isalnum()]) / max(len(text), 1)
    return len(vowels), len(consonants), digit_count, special_char_ratio


def transform_metrics(raw):
    a, b, c, d = raw
    adjusted_a = a * 2 + c
    adjusted_b = b * 3 - a
    adjusted_c = (c + 1) ** 2
    adjusted_d = int(d * 100)
    temp_result = (adjusted_a & adjusted_b) ^ adjusted_c  # Bit manipulation red herring
    scaling_factor = 1.5 if adjusted_d > 50 else 0.8
    return adjusted_a, adjusted_b, adjusted_c, adjusted_d, scaling_factor


def compute_legacy_index(x, y, z):
    # Unused function - dead code path
    return (x + y * 2) % z


def filter_outliers(data_list):
    mean_val = sum(data_list) / len(data_list)
    stdev = (sum((x - mean_val) ** 2 for x in data_list) / len(data_list)) ** 0.5
    return [x for x in data_list if abs(x - mean_val) <= 2 * stdev]


def generate_auxiliary_map(keys):
    # Distractor: builds a map but mostly unused
    aux_map = {}
    for k in keys:
        aux_map[k] = bin(k).count('1') if isinstance(k, int) else len(k)
    return aux_map.get('mode', 0)


def evaluate_performance(metrics):
    m1, m2, m3, m4, scale = metrics
    base = m1 + m2
    bonus = 0
    
    if m3 > 10:
        bonus += 5
    elif m3 == 1:
        bonus -= 3
    
    intermediate = (base * scale) + bonus
    
    # Conditional expression with distractor logic
    penalty = 10 if m4 > 75 and intermediate > 100 else (5 if m4 > 50 else 0)
    
    # Critical computation path
    temp_var_x = (intermediate - penalty) * 2
    temp_var_y = temp_var_x + 17
    
    # Decoy bitwise operation
    decoy_flag = (temp_var_y & 1) == 1
    final_score_candidate = temp_var_y if decoy_flag else temp_var_y + 100
    
    # Final override based on hidden rule
    final_score = final_score_candidate
    
    # Irrelevant transformations below
    shadow_copy = final_score * 0.9
    shadow_copy = int(shadow_copy) + 5
    
    return final_score

# Main execution flow
input_string = "SecureLogix_2048!@@"

# Step 1: Analyze composition
composition_result = analyze_text_composition(input_string)

# Step 2: Transform to numerical metrics
transformed = transform_metrics(composition_result)

# Step 3: Generate irrelevant auxiliary data
aux_value = generate_auxiliary_map([10, 20, 'mode', 40])  # Returns 4

# Step 4: Filter dummy outliers
dummy_data = filter_outliers([10, 12, 14, 15, 100])  # Removes 100

# Step 5: Evaluate performance - this sets final_score
final_score = evaluate_performance(transformed)

# Output result
print(f"Target result: {final_score}")