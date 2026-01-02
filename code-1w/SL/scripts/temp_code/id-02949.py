import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([x ** 2 for x in data if x > 0])

# Misleading precomputed constant (distractor)
baseline_offset = 42.5

# Simulated sensor readings with embedded patterns
def generate_sensor_profile(length):
    profile = []
    for i in range(length):
        if i % 5 == 0:
            profile.append(int((i * 1.7) + 3))
        elif i % 3 == 0:
            profile.append(int((i * 0.9) - 1))
        else:
            profile.append(int(math.sqrt(i) * 2))
    return profile[:length]

# Red herring: Unused transformation matrix
def build_interference_matrix(n):
    matrix = [[(i * j) % 7 for j in range(n)] for i in range(n)]
    return matrix  # Never used in main logic

# Core processing: Recursive filter for unstable readings
def recursive_stabilize(seq, depth=0):
    if depth >= 3 or len(seq) < 2:
        return seq
    filtered = [seq[i] for i in range(1, len(seq)) if seq[i] >= seq[i-1] or (i > 1 and seq[i] != seq[i-2])]
    return recursive_stabilize(filtered, depth + 1)

# Character counting side-channel (irrelevant but plausible)
def count_chars_in_label(label):
    return sum(1 for c in label if c.isalpha())

# Main evaluation logic with slicing and conditional branching
def evaluate_thermal_response(matrix, threshold):
    flat_data = [item for row in matrix for item in row]  # Flatten
    sorted_data = sorted(flat_data)
    
    # Apply threshold filter using comparison and slicing
    trimmed = sorted_data[len(sorted_data)//4 : -(len(sorted_data)//4)]  # Remove quartiles
    valid_range = [x for x in trimmed if x > threshold - 5 and x < threshold + 20]
    
    # Secondary filter using recursion
    stabilized = recursive_stabilize(valid_range)
    
    # Compute capacity using arithmetic and bitwise mix
    raw_sum = sum(stabilized)
    adjustment_factor = len(stabilized) ^ 7  # Bitwise interference
    if len(stabilized) % 2 == 0:
        capacity = (raw_sum / adjustment_factor) * 1.2
    else:
        capacity = (raw_sum * 0.8) / max(1, adjustment_factor // 2)
    
    # Final tweak based on character logic (misdirection)
    label = "THRM-CTRL-V8"
    char_count = count_chars_in_label(label)
    capacity += (char_count & 3)  # Only adds 2
    
    return capacity

# Initialize simulation parameters
threshold_level = 18
logistical_matrix = []
for i in range(6):
    row = generate_sensor_profile(8)
    offset_row = [x + (i * 2) for x in row]  # Introduce variation
    logistical_matrix.append(offset_row)

# Dead code: Unused matrix analysis
interference_matrix = build_interference_matrix(5)
diagnostic_score = baseline_offset * 1.1  # Distractor variable

# Critical execution point
thermal_capacity = evaluate_thermal_response(logistical_matrix, threshold_level)

# Print result as required
print(f"Result: {thermal_capacity}")