import math

# Irrelevant utility function (decoy)
def normalize_signal(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Another decoy function with dead-end logic
def assess_purity_level(sample):
    purity = 0
    for element in sample:
        if isinstance(element, float):
            purity += int(element % 7)
    return purity * 0.1

# Simulated sensor array data (red herring)
sensor_readings = [0.87, 1.02, 0.94, 2.11, 3.05, 1.76]
baseline_offset = sum([abs(x - 1.0) for x in sensor_readings])
adjusted_baseline = baseline_offset * 1.5

# Real contamination detection logic hidden among noise
composite_sample = [4, 8, 15, 16, 23, 42]
detection_threshold = 10
temporal_weights = {i: math.exp(-i * 0.2) for i in range(6)}

# Distractor: unused complex transformation
transformed = list(map(lambda x: (x ** 2 + 3) // 2, composite_sample))
filtered_outliers = set([x for x in transformed if x > 200])

# Core analysis with multiple concepts
analytical_layers = [
    lambda s: [x for x in s if x > detection_threshold],
    lambda s: [x * 2 if x % 3 == 0 else x for x in s],
    lambda s: sorted(s, reverse=True)
]

intermediate_result = composite_sample.copy()
for process in analytical_layers:
    intermediate_result = process(intermediate_result)

# Bit manipulation red herring
bitmask = 0b101010
masked_values = [x ^ bitmask for x in composite_sample]
active_bits = bin(bitmask).count('1')

# Set operations used meaningfully but obscured by context
reference_set = {4, 16, 64}
overlap_count = len(set(intermediate_result) & reference_set)

# Final determination buried in logic chain
def analyze_contamination(sample, threshold):
    # Logical and arithmetic operations
    above_threshold = [x for x in sample if x > threshold]
    
    # Sequence transformation
    processed = []
    for val in above_threshold:
        if val % 2 == 0:
            processed.append(val // 2)
        else:
            processed.append(val * 3 + 1)
    
    # Further filtering using set logic
    safe_levels = {x for x in processed if x < 50}
    critical_levels = set(processed) - safe_levels
    
    # Final score calculation
    base_score = sum(safe_levels)
    penalty = len(critical_levels) * 7
    adjustment_factor = len(set(processed) & {4, 8, 16})  # Powers of two
    
    # Answer derived from multiple reasoning steps
    result = base_score - penalty + (adjustment_factor * 3)
    
    # Dead code path (misleading)
    if False:
        result = math.log(result + 1) * 100
        
    return result

# Unused variable assignment (distractor)
calibration_sequence = [(i, i**3 % 17) for i in range(10)]

# Key execution point
filtration_score = analyze_contamination(composite_sample, detection_threshold)

# Additional irrelevant computation
entropy_estimate = -sum([math.log(temporal_weights[i]+0.1) for i in range(6)])

# Output the target result
print(f"Result: {filtration_score}")