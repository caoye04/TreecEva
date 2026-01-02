import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Decoy transformation with misleading intermediate result
def decoy_transform(seq):
    temp = [math.log(abs(x) + 1) for x in seq]
    shift = sum(temp) / len(temp)
    return [int(y - shift) for y in temp]

# Real processing function used in computation
def process_item(value, mode_flag):
    if mode_flag:
        return (value * 3) ^ 7
    else:
        return (value + 5) & 15

def validate_entry(code, threshold=10):
    # Complex validation logic with bit manipulation
    binary_rep = bin(code)[2:].zfill(8)
    ones = binary_rep.count('1')
    zeros = binary_rep.count('0')
    parity_check = (ones + zeros) % 2 == 0
    return ones >= threshold // 3 and parity_check

def main_pipeline(raw_sequence, config_mask):
    # Step 1: Initial filtering based on bitwise criteria
    prelim_filtered = [x for x in raw_sequence if (x & config_mask) != 0]
    
    # Step 2: Misleading normalization (distractor)
    normalized = [round(math.sin(x) * 100, 2) for x in prelim_filtered]
    avg_norm = sum(normalized) / len(normalized) if normalized else 0
    
    # Step 3: Actual signal extraction (relevant path)
    signal_candidates = []
    for idx, val in enumerate(prelim_filtered):
        if validate_entry(val, threshold=9):
            transformed = process_item(val, mode_flag=(idx % 2 == 0))
            signal_candidates.append(transformed)
    
    # Step 4: Red herring aggregation using zip and enumerate (partially irrelevant)
    indices = list(range(len(signal_candidates)))
    paired_data = list(zip(indices, signal_candidates))
    weighted_sum = sum(i * v for i, v in paired_data)  # Used only to distract
    
    # Step 5: Real filtering based on secondary condition
    filtered_data = [v for i, v in paired_data if bin(v).count('1') % 3 == 0]
    
    # Step 6: Control flags generation (complex but partially relevant)
    control_flags = []
    for num in filtered_data:
        flag = (num ^ 255) > 100
        suppression = (num & 1) == 0
        control_flags.append(flag and not suppression)
    
    # Step 7: Final processing
    final_output = process_results(filtered_data, control_flags)
    return final_output

def process_results(data_list, flags):
    if not data_list:
        return -1
    base = 0
    for val, flag in zip(data_list, flags):
        if flag:
            base += val * 2
        else:
            base -= int(math.sqrt(abs(val)))
    # Apply final transformation
    result = (base ^ 3456) + len(data_list)
    return result

# Unused global variables (distractors)
calibration_data = [math.exp(i) for i in range(5)]
threshold_matrix = [[i * j for j in range(3)] for i in range(3)]

# Input data with embedded logic
raw_input_sequence = [85, 170, 204, 51, 221, 136, 238, 153]
mask_config = 85  # Binary: 01010101

# Execute main logic
result_value = main_pipeline(raw_input_sequence, mask_config)

# Critical assignment point
final_output = process_results([x ^ 10 for x in [85, 170, 204]], [True, False, True])

# Print target result
print(f"Target result: {final_output}")