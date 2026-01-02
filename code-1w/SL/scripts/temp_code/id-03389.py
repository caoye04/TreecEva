import math

def preprocess_values(raw_list):
    temp_result = []
    cumulative_shift = 0
    
    for i, val in enumerate(raw_list):
        shifted = val + (i % 4)
        if shifted > 10:
            shifted = shifted // 2
        temp_result.append(shifted)
        
        # Distractor: tracking sum that isn't used later
        cumulative_shift += shifted * 0.1
    
    return temp_result

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 2 + 3 * x + 1

def transform_pairs(data):
    paired = list(zip(data[::2], data[1::2]))
    transformed = []
    
    for a, b in paired:
        diff = abs(a - b)
        prod = a * b
        # Semi-relevant transformation
        if diff > 0:
            transformed.append(prod / diff)
        else:
            transformed.append(0)
    
    # Distractor variable
    avg_transform = sum(transformed) / len(transformed) if transformed else 0
    
    return transformed

def calculate_entropy(values):
    # Not actually used in final score but looks important
    total = sum(values)
    if total == 0:
        return 0
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def calculate_final_score(components):
    base = sum(components)
    
    # Apply non-linear adjustment
    adjustment_factor = 1.0
    if base > 20:
        adjustment_factor = 0.85
    elif base < 10:
        adjustment_factor = 1.2
    
    score = base * adjustment_factor
    
    # Secondary adjustment based on component count
    length_bonus = len(components) * 0.5
    
    # Key distractor: complex-looking but unused calculation
    variance_proxy = sum((x - base/len(components))**2 for x in components) / len(components) if components else 0
    normalized_var = math.sqrt(variance_proxy) if variance_proxy > 1 else 0
    
    # Final score computation (variance not actually used)
    final = score + length_bonus
    
    return final

# Main execution
raw_input = [3, 7, 2, 9, 4, 6]

# Step 1: Preprocess
processed_data = preprocess_values(raw_input)

# Step 2: Transform into pairs
pair_results = transform_pairs(processed_data)

# Step 3: Calculate entropy (unused in final score - red herring)
entropy_value = calculate_entropy(pair_results)

# Step 4: Compute final score
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")