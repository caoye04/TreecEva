def analyze_pattern(sequence):
    # Irrelevant pattern analyzer (dead-end function)
    if len(sequence) < 5:
        return False
    return all(x % 2 == 0 for x in sequence[:3])


def preprocess_input(raw_data):
    # Distractor: complex preprocessing that isn't used in final path
    normalized = [x / max(raw_data) for x in raw_data]
    filtered = [x for x in normalized if x > 0.1]
    transformed = [round(x * 100) for x in filtered]
    return transformed

# Decoy data structures
test_trials = [[1,2,3], [4,5,6], [7,8,9]]
baseline_metrics = {'p90': 0.85, 'p50': 0.45, 'p10': 0.15}

# Actual relevant data
primary_sequence = [8, 12, 5, 19, 3, 11, 7, 14]

# Misleading intermediate calculation
counterfeit_sum = sum([i**2 for i in range(6)]) // 3  # Unused later

# Key slicing operation (relevant)
segment_a = primary_sequence[1:6:2]  # [12, 19, 11]
segment_b = primary_sequence[-3::-3]  # [11, 12]

# Set operations with overlap (relevant)
unique_a = set(segment_a)
unique_b = set(segment_b)
common_elements = unique_a & unique_b  # {11, 12} ∩ {11} → actually {11}

# Accumulation with distraction
accumulator = 0
for val in primary_sequence:
    if val in common_elements:
        accumulator += val * 2
    elif val > 10:
        accumulator += val // 3  # Minor contribution

# Red herring: unused recursive function
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n-2)

# Simulated diagnostic set with multiple fields
diagnostic_set = {
    'readings': primary_sequence,
    'flags': [False, True, False],
    'mode': 'advanced',
    'checksum': 999  # decoy value
}

# Another irrelevant transformation
shifted_values = [x << 1 for x in segment_a if x > 10]  # [24, 38]

# Core evaluation logic (depends on prior steps)
def evaluate_performance(data):
    readings = data['readings']
    
    # More slicing: extract every second element starting at index 2
    sample_window = readings[2::2]  # [5, 3, 7]
    
    # String distraction (irrelevant conversion)
    status_label = "_".join(["item", "proc", "done"]).upper().replace("_", "-")
    
    # Real accumulation
    total = accumulator  # Inherits from earlier loop
    
    # Additional logic using set result
    if len(common_elements) >= 1:
        total += len(sample_window) * 17  # 3 * 17 = 51
    
    # Conditional bit manipulation (relevant)
    trigger_val = readings[0]  # 8
    if trigger_val & 7 == 0:  # 8 & 7 = 0 → True? No: 8 & 7 = 0 → Yes!
        total += 5
    else:
        total -= 3
    
    # Final adjustment via case-sensitive logic
    mode_flag = data['mode']
    if mode_flag.lower() == 'advanced':
        total *= 2
    
    return total

# Execution point of interest
final_score = evaluate_performance(diagnostic_set)

# Print required output
print(f"Result: {final_score}")