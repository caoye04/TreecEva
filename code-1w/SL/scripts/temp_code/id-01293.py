from collections import defaultdict
import math

def preprocess_records(raw_entries):
    # Irrelevant transformation (distractor)
    temp_log = [math.log(x + 1) for x in raw_entries if x > 0]
    counted = defaultdict(int)
    for val in raw_entries:
        counted[val] += 1
    # Only this line matters
    return [x * 1.5 for x in raw_entries if x % 2 == 0]

def validate_sequence(seq):
    # Dead code path — never alters main flow
    if len(seq) < 5:
        return False
    checksum = sum(seq[i] * (i + 1) for i in range(len(seq)))
    return checksum % 7 == 0

def calculate_final_score(data_list, weight_map):
    base_total = 0
    multiplier_shift = 0
    
    # Real logic begins
    for i, val in enumerate(data_list):
        if i % 2 == 0:
            base_total += val * weight_map['even_factor']
        else:
            base_total -= val * weight_map['odd_factor']
    
    # Distractor: complex but unused calculation
    outlier_count = len([x for x in data_list if x > 50])
    adjustment_pool = set([int(base_total / (i + 1)) for i in range(1, 4)])
    buffer_zone = adjustment_pool.intersection(set(range(10, 20)))
    
    # This affects final result
    if len(buffer_zone) > 2:
        multiplier_shift = 1.1
    else:
        multiplier_shift = 0.9
    
    # Final score computation
    final_score = int((base_total * multiplier_shift) + weight_map['bonus_offset'])
    return final_score

# Main execution
raw_data = [12, 8, 23, 16, 44, 31, 50]
config_weights = {
    'even_factor': 3,
    'odd_factor': 2,
    'bonus_offset': 7
}

# Unused validation (distractor)
validity = validate_sequence(raw_data)

# Key processing steps
filtered_interim = [x for x in raw_data if x < 40]  # Filters 44 and 50
processed_data = preprocess_records(filtered_interim)
# At this point, processed_data = [12*1.5, 8*1.5, 16*1.5] = [18.0, 12.0, 24.0]

final_score = calculate_final_score(processed_data, config_weights)
print(f"Target result: {final_score}")