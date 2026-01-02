import math

# Irrelevant helper function (dead code path)
def unused_signal_processor(x):
    return [i ** 2 for i in x if i % 3 == 0]

# Misleading diagnostic with decoy logic
def false_diagnostic(seq):
    accumulator = 0
    for i in range(len(seq)):
        if seq[i] % 4 == 0:
            accumulator += seq[i] // 4
    return accumulator * 2

# Core transformation function with distractors
def transform_sequence(raw):
    temp_result = []
    offset = 7
    # Real transformation begins
    for val in raw:
        shifted = (val << 1) + 3  # Bit manipulation
        normalized = shifted % 19
        temp_result.append(normalized)
    
    # Irrelevant sorting (does not affect outcome)
    temp_result.sort(reverse=True)
    
    # More red herring operations
    decoy_sum = sum([x ** 0.5 for x in temp_result if x % 2 == 0])
    scaling_factor = math.sin(math.pi / 6)  # Constant: 0.5
    adjusted = [int(x * scaling_factor) for x in temp_result]
    
    # This sort is actually meaningful (required for correct pattern analysis)
    adjusted.sort()  # Critical step disguised among noise
    return adjusted

# Recursive pattern analyzer (key logic)
def analyze_pattern(data, index=0, acc=0):
    if index >= len(data):
        return acc
    current = data[index]
    if current % 3 == 1:
        acc += current * 2
    elif current % 5 == 0:
        acc -= current // 5
    else:
        acc += (current + 1) // 2
    
    # Early termination red herring (never triggered due to data constraints)
    if acc > 1000:
        return -999  
    
    return analyze_pattern(data, index + 1, acc)

# Decoy data structures
auxiliary_map = {i: i * i for i in range(15)}
shadow_buffer = [0] * 20

# Input data (appears arbitrary but designed for deterministic output)
raw_sensor_data = [12, 8, 5, 21, 16, 4, 7]

# Apply transformation
transformed_data = transform_sequence(raw_sensor_data)

# Unused intermediate results (distractors)
baseline_score = sum(transformed_data) / len(transformed_data)
outlier_flags = [x for x in transformed_data if x > 15]

# Key computation: this is where the answer is determined
final_diagnostic = analyze_pattern(transformed_data)

# Print result for evaluation
print(f"Result: {final_diagnostic}")