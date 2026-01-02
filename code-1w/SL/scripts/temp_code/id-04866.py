import math

# Irrelevant helper function (dead code path)
def unused_energy_calculator(x):
    return sum([i ** 2 for i in range(x)]) if x > 5 else 0

# Decoy function with misleading intermediate results
def decoy_thermal_model(data):
    temp = 0
    for i in range(len(data)):
        temp += data[i] * (i + 1)
    scaling = 0.95
    normalized = temp * scaling if temp > 100 else temp / 2
    return int(normalized)  # Never used

# Core logic: bit manipulation + conditional slicing + recursion
def shift_register(sequence, offset=3):
    """Apply circular shift using slicing, then filter noise"""
    shifted = sequence[-offset:] + sequence[:-offset]  # Circular shift right
    filtered = [x for x in shifted if x & 1]  # Keep only odd values
    return filtered

# Recursive transformation with early termination
def recursive_amplifier(val, depth=0):
    if depth >= 5 or val <= 1:
        return val * 1.5
    if val % 2 == 0:
        next_val = val // 2
        return recursive_amplifier(next_val, depth + 1) + (val * 0.1)
    else:
        next_val = 3 * val + 1
        return recursive_amplifier(next_val, depth + 1) - (val * 0.05)

# Main calculation chain
def calculate_thermal_output(seq):
    # Step 1: Apply bit-level filtering
    processed = [x for x in seq if (x >> 2) & 1]  # Only numbers with bit 2 set
    
    # Step 2: Conditional slicing based on length
    mid_idx = len(processed) // 2
    segment = processed[mid_idx:] if len(processed) > 6 else processed[:mid_idx] if mid_idx > 0 else [0]
    
    # Step 3: Apply recursive amplifier to each element
    amplified = [recursive_amplifier(x) for x in segment]
    
    # Step 4: Aggregate with weighted sum and trigonometric correction
    weights = [math.cos(i * 0.1) for i in range(len(amplified))]
    weighted_sum = sum(a * w for a, w in zip(amplified, weights))
    
    # Step 5: Apply shift register transformation
    int_values = [int(abs(a)) for a in amplified]
    shifted_ints = shift_register(int_values, 2)
    
    # Step 6: Combine weighted sum with bit count from shifted result
    bit_count = sum(bin(x).count('1') for x in shifted_ints)
    final_adjustment = weighted_sum + bit_count * 0.25
    
    # Red herring: unused complex expression
    entropy_score = -sum((x / sum(amplified)) * math.log2(x / sum(amplified)) 
                        for x in amplified if x > 0) if sum(amplified) > 0 else 0
    
    # Final output
    return round(final_adjustment, 6)

# Simulated sensor input sequence (real data)
sensor_readings = [12, 7, 15, 3, 8, 11, 14, 6, 9, 13, 4, 10]

# Unused variables (distractors)
optimal_threshold = 8.5
baseline_correction = [x - 2 for x in sensor_readings if x % 3 == 0]
aggregated_diagnostic = sum(baseline_correction) * 1.2

# Key computation path
filtered_readings = [x for x in sensor_readings if x >= 6]
process_sequence = filtered_readings[::-1]  # Reverse the sequence

# Critical execution point
thermal_capacity = calculate_thermal_output(process_sequence)

# Print result as required
print(f"Result: {thermal_capacity}")