def preprocess_values(raw):
    return [x for x in raw if x > 0]

def normalize(seq):
    total = sum(seq)
    return [round(x / total, 4) for x in seq]

def calculate_final_score(values, importance):
    # Irrelevant transformation (distractor)
    temp_debug = [v * 2 for v in values]
    processed = preprocess_values(values)
    normalized_weights = normalize(importance[:len(processed)])
    
    # Accumulate weighted score
    accumulated = 0
    for i in range(len(processed)):
        accumulated += processed[i] * normalized_weights[i]
    
    # Red herring computation (not used)
    outlier_check = len([x for x in values if x > 100])
    adjustment_factor = 1.0
    if outlier_check > 0:
        adjustment_factor = 0.95
    
    # Final calculation (not affected by adjustment_factor due to logic path)
    final_score = round(accumulated * 100, 2)
    return final_score

# Input data
raw_data = [10, -5, 25, 30, 0, 45]
weights = [1, 3, 2, 4, 5, 6]

# Misleading initialization
initial_analysis = sum([x**2 for x in raw_data if x > 10])
duplicate_flag = False

# Key execution point
final_score = calculate_final_score(raw_data, weights)

# Output result
print(f"Result: {final_score}")