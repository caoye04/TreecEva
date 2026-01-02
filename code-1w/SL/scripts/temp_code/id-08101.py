def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > 0]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant signal processing branch (dead path)
def legacy_process(data):
    return [d * 2 for d in data if d < 50]

# Decoy function with misleading name
def evaluate_fitness(energy_levels):
    total = sum(energy_levels)
    average = total / len(energy_levels) if energy_levels else 0
    return average ** 2

# Core logic: pattern analysis using set operations and conditional transformations
def generate_threshold_map(base_values):
    mod_values = {v % 17 for v in base_values}  # Use set to eliminate duplicates
    extended = {v for v in mod_values if v != 0}
    shift_up = {v + 5 for v in extended}
    return shift_up.intersection({7, 8, 9, 10, 11, 12, 13})

def apply_mask(sequence, mask_set):
    result = []
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            transformed = val * 3
        elif i % 3 == 1:
            transformed = val + (13 if val in mask_set else 7)
        else:
            transformed = val ^ 1  # XOR with 1
        result.append(transformed)
    # Dead computation - no effect on final answer
    checksum = sum(result) % 1000
    return result

def analyze_pattern(seq, thresholds):
    temp_state = 0
    for idx, item in enumerate(seq):
        if item in thresholds:
            temp_state += (idx * item) // 2
        elif temp_state > 100:
            temp_state -= 23
        else:
            temp_state += item % 7
        
        # Nested conditional red herring
        if idx > 5 and item < 5:
            temp_state = temp_state | 4  # Bitwise or, rarely triggered

    # Complex transformation chain
    temp_state = (temp_state + 987) % 543
    if temp_state % 2 == 0:
        temp_state = temp_state // 3
    else:
        temp_state = temp_state * 2 + 1

    # Final adjustment based on set size influence
    influence = len(thresholds) * 11
    temp_state = (temp_state + influence) % 10000
    return temp_state

# Main execution flow
raw_data_stream = [23, 45, 67, 12, 8, 3, 99, 56, 14, 7]
scaled_data = preprocess_signal(raw_data_stream)

# Unused but plausible-looking diagnostic
health_metric = evaluate_fitness(raw_data_stream)

# Generate actual working components
base_keys = [100, 200, 300, 400, 500, 600]
threshold_set = generate_threshold_map(base_keys)  # Evaluates to {7, 8, 12}

logic_sequence = []
for x in scaled_data:
    if x > 0.5:
        logic_sequence.append(int(x * 10))
    elif x > 0.2:
        logic_sequence.append(int(x * 20))
    else:
        logic_sequence.append(1)

# Apply transformation with partial side effects
masked_seq = apply_mask(logic_sequence, threshold_set)

# Critical statement
final_diagnostic = analyze_pattern(masked_seq, threshold_set)
print(f"Result: {final_diagnostic}")