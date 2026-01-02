import math

# Simulated sensor data processing with embedded logic chain
def preprocess_signal(raw_values):
    filtered = [x for x in raw_values if x > 0.5]
    normalized = [(val - min(filtered)) / (max(filtered) - min(filtered)) for val in filtered]
    return [round(v * 100) for v in normalized]

# Irrelevant helper - dead path
def deprecated_calibrate(x):
    return (x + 45) % 17

# Noise injection simulation (unused)
signal_noise_floor = 0.03
baseline_offset = sum([i * 0.01 for i in range(10)])

# Core transformation: bit manipulation and modular arithmetic
def encode_value(x):
    shifted = (x << 2) & 255
    toggled = shifted ^ 135
    wrapped = (toggled + 18) % 211
    return wrapped if wrapped % 2 == 0 else wrapped + 1

# Distractor function: looks important but unused
def validate_checksum(data):
    checksum = 0
    for d in data:
        checksum = (checksum ^ d) * 13 % 97
    return checksum > 50

# Data generation with conditional expressions
raw_input_data = [0.3, 0.6, 0.4, 0.9, 1.1, 0.2, 0.8]
processed = preprocess_signal(raw_input_data)

# Multiple assignments and distractor variables
total_samples, peak_value = len(processed), max(processed)
avg_sample = sum(processed) / total_samples if total_samples > 0 else 0
dummy_flag = True if avg_sample > 50 else False

# Unused intermediate transformations
mirror_image = [100 - p for p in processed]
mod_series = [p % 7 for p in processed]

# Key sequence generation with nested logic
encoded_sequence = []
for val in processed:
    temp = val
    if temp < 30:
        temp = (temp + 12) * 2
    elif temp > 70:
        temp = int(math.sqrt(temp) * 5)
    else:
        temp = (temp // 3) + 25
    encoded_sequence.append(encode_value(temp))

# Red herring: complex-looking but irrelevant calculation
correlation_score = sum([encoded_sequence[i] ^ encoded_sequence[i-1] 
                          for i in range(1, len(encoded_sequence))]) / 10.0

# Threshold computed via misleading multi-step process
threshold_base = sum(encoded_sequence) / len(encoded_sequence)
adjustment_factor = (max(encoded_sequence) - min(encoded_sequence)) // 20
threshold = threshold_base - adjustment_factor if adjustment_factor > 5 else threshold_base + 3

# Conditional expression in assignment (required feature)
mode_setting = 'aggressive' if threshold > 65 else 'conservative'

# Core analysis function with interdependent logic steps
def analyze_pattern(seq, limit):
    # Nesting Level 1
    if not seq:
        return 0
    
    count_a = 0
    running_sum = 0
    
    # Nesting Level 2
    for item in seq:
        # Nesting Level 3
        if item > limit:
            # Bitwise and modular combo
            transformed = ((item & 127) + (item >> 3)) % 89
            # Nesting Level 4
            if transformed % 4 == 0:
                count_a += 1
                running_sum += transformed
            elif transformed % 3 == 0:
                running_sum += transformed // 2
            else:
                running_sum -= (transformed % 7)
    
    # Final computation with conditional expression
    adjustment = running_sum // count_a if count_a > 0 else 0
    final_score = running_sum + (adjustment * 2)
    
    # Decoy operations
    sanity_check = (final_score ^ 255) % 1000
    debug_trace = [final_score, sanity_check, count_a]
    
    # Actual answer contribution
    outlier_count = len([x for x in seq if x > (limit + 10)])
    penalty = 15 if outlier_count > 2 else 5
    
    # Critical statement
    final_diagnostic = final_score - penalty
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_pattern(encoded_sequence, threshold)

# Output requirement
print(f"Target result: {final_diagnostic}")