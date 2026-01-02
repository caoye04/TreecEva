import math

def preprocess_inputs(raw_values):
    # Irrelevant preprocessing function (dead code path)
    return [x ** 0.5 for x in raw_values if x > 0]

def unused_helper(seq):
    # Decoy function that is never called
    return sum([i * 2 for i in seq if i % 2 == 0])

def transform_entry(entry):
    # Transform a single log entry using bitwise and arithmetic ops
    temp_a = (entry ^ 255) & 127
    temp_b = (temp_a >> 3) + 10
    return temp_b if temp_b > 20 else temp_b * 2

def validate_sequence(seq):
    # Misleading validation with side computation
    checksum = 0
    for item in seq:
        checksum ^= item
    # This looks important but doesn't affect main logic
    return checksum % 16 == 0

def calculate_entropy(values):
    # Complex distractor: computes entropy but not used in final score
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def calculate_final_score(log_entries, importance_weights):
    # Core logic buried within multiple layers
    transformed = []
    for val in log_entries:
        if val < 0:
            continue
        processed = transform_entry(val)
        transformed.append(processed)
    
    # Distracting conditional expression
    adjustment_factor = 1.5 if len(transformed) > 5 else 0.8
    
    # Accumulation with dictionary-based weighting
    weighted_sum = 0
    weight_map = {i: importance_weights[i % len(importance_weights)] for i in range(len(transformed))}
    
    for idx, value in enumerate(transformed):
        weighted_sum += value * weight_map[idx]
    
    # Secondary transformation
    normalized = weighted_sum / len(weight_map) if weight_map else 0
    
    # Red herring: entropy calculation included but not used
    _ = calculate_entropy(transformed)
    
    # Final nonlinear scaling
    if normalized > 30:
        final_score = int((normalized * adjustment_factor) - 12)
    else:
        final_score = int(normalized + 5)
    
    return final_score

# Simulated data log (bit patterns from sensor readings)
data_log = [42, 88, 156, 33, 201, 77, 144, 9]

# Weights for scoring (higher emphasis on early features)
weights = [0.7, 1.2, 0.9]

# Dead variables with plausible names
baseline_offset = 2.3
reference_pattern = [1, 1, 2, 3, 5, 8]
shadow_copy = data_log[::-1]

# Key execution point
final_score = calculate_final_score(data_log, weights)

# Print result for evaluation
print(f"Result: {final_score}")