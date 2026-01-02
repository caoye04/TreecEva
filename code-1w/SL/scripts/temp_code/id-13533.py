import math

# Simulated sensor data preprocessing with distractions
def acquire_signal(raw=True):
    if raw:
        return [0.7, -1.2, 3.5, -0.3, 2.8, 1.1, -2.0, 4.6]
    else:
        return []

# Irrelevant transformation — looks important but unused later
def deprecated_normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Distractor function: appears useful but not used in critical path
def moving_average(signal, window=3):
    result = []
    for i in range(len(signal) - window + 1):
        result.append(sum(signal[i:i+window]) / window)
    return result

# Core transformation function with conditional logic and slicing
def extract_features(data, mode='primary'):
    length = len(data)
    mid = length // 2
    
    # Primary processing branch
    if mode == 'primary':
        # Use slicing and conditional expression
        left_half = data[:mid] if len(data) > 5 else data
        right_half = [abs(x) for x in data[mid:]]
        
        # Apply lambda-based filtering
        filter_positive = lambda vals: [v for v in vals if v > 0.5]
        filtered = filter_positive(left_half + right_half)
        
        # Bitwise red herring: operates on floats converted to int (distraction)
        magic_offset = 0
        for val in filtered:
            intval = int(abs(val))
            magic_offset ^= (intval << 1) | 1  # XOR and bit shift — unused later
        
        # Actual relevant computation
        magnitude = sum([math.log(1 + x) for x in filtered])
        return magnitude
    else:
        return sum(data) ** 2

# Secondary transformation with decoy control flow
def enhance_resolution(seq):
    enhanced = []
    for x in seq:
        if x < 0:
            enhanced.append(math.sin(x))
        elif x == 0:
            enhanced.append(0.0)
        else:
            enhanced.append(math.sqrt(x))  # Only this branch is meaningfully used
    
    # Dead code path — never reached due to structure above
    if len(enhanced) > 100:
        enhanced = [round(e, 2) for e in enhanced]
    
    return enhanced

# Main processing with multiple concepts and distractors
def process_signal(data, limit):
    # Step 1: feature extraction (only magnitude matters)
    feature_score = extract_features(data, mode='primary')
    
    # Step 2: irrelevant character counting distraction
    diagnostic_tag = 'SIG_PROC_V2'
    char_count = sum(1 for c in diagnostic_tag if c in 'AEIOU')  # Always 3 — unused
    
    # Step 3: resolution enhancement
    resolved = enhance_resolution(data)
    
    # Step 4: conditional data correction (uses slicing and conditionals)
    corrected = resolved[:]
    for i in range(len(corrected)):
        if i % 2 == 0 and corrected[i] > 1.0:
            corrected[i] -= 0.5
    
    # Step 5: integration with threshold logic
    total_power = sum([c**2 for c in corrected])
    
    # Step 6: apply threshold filter using lambda and conditional expression
    active_components = list(filter(lambda x: x >= limit, corrected))
    
    # Step 7: final aggregation — only this affects output
    adjustment_factor = 1.75 if len(active_components) > 2 else 0.85
    base_result = feature_score * adjustment_factor
    
    # Step 8: final rounding and assignment
    final_value = round(base_result + total_power, 4)
    
    # Red herring: bitwise operation on float cast (distractor)
    temp_int = int(final_value)
    checksum = (temp_int & 0xFFFF) ^ (temp_int >> 16)
    _ = checksum  # Unused
    
    return final_value

# Unused recursive function — looks important but not called
def recursive_decay(n, factor=0.9):
    if n <= 1:
        return n
    return factor * recursive_decay(n - 1, factor)

# --- Critical Execution Path Begins ---
raw_sensor_data = acquire_signal(raw=True)

# Transform data through non-linear enhancements
transformed_data = [math.exp(x / 3) for x in raw_sensor_data]

# Threshold computed via distraction-heavy expression
initial_threshold = abs(-3) * (2 + (1 if len(transformed_data) % 2 == 0 else 0))  # = 6
threshold = initial_threshold / 10  # = 0.6

# Key statement: compute final output
final_output = process_signal(transformed_data, threshold)

# Print result for evaluation
print(f"Result: {final_output}")