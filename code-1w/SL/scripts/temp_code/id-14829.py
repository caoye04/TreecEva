def preprocess_signal(raw_data):
    filtered = []
    for x in raw_data:
        if x % 3 == 0 and x > 0:
            filtered.append(x * 2)
    return filtered

# Irrelevant sensor calibration data (distractor)
calibration_offset = 0.0037
baseline_readings = [113, 205, 307, 409, 511]
system_health_score = sum([x % 17 for x in baseline_readings])

# Real signal processing path
raw_input_stream = list(range(1, 68, 3))
processed_signal = preprocess_signal(raw_input_stream)

# Bit manipulation red herring
defective_flag_mask = 0b101010
activation_key = defective_flag_mask ^ 0b111111
redundant_check = bin(activation_key).count('1')

# String-based decoy transformation (uses string method)
timestamp_code = "2023-10-25T14:30:45"
split_parts = timestamp_code.split('T')
date_part = split_parts[0].replace('-', '')
time_signature = int(date_part) % 1000  # Misleading use

# Actual sequence generation
encrypted_sequence = []
for i, val in enumerate(processed_signal):
    shift = i % 4
    if shift == 0:
        encrypted_sequence.append(val + time_signature)
    elif shift == 1:
        encrypted_sequence.append(val * 2)
    elif shift == 2:
        encrypted_sequence.append(val - 5)
    else:
        encrypted_sequence.append(val // 2)

# Threshold computed via irrelevant health metric
health_weight = system_health_score / 100
threshold = int(50 + health_weight * 10)  # Evaluates to 54

# Decoy function with unused logic
def validate_checksum(data):
    checksum = 0
    for item in data:
        while item > 0:
            checksum += item % 10
            item //= 10
    return checksum % 7 == 0

# Core analysis function with nested logic
def analyze_pattern(seq, limit):
    count = 0
    total = 0
    temp_buffer = []
    
    for num in seq:
        if num < limit:
            continue
        mod_val = num % 13
        if mod_val in [2, 3, 5, 7, 11]:  # Prime residues
            count += 1
            total += num
        temp_buffer.append(mod_val * 2)  # Fills but not used later
    
    # Secondary filter based on bit count (real contribution)
    adjusted_total = 0
    for n in [total, count]:
        bits = bin(n).count('1')
        adjusted_total += n * bits
    
    # Final transformation
    if adjusted_total > 1000:
        result = adjusted_total // 100
    else:
        result = adjusted_total // 10
    
    # Unused diagnostic trace (red herring)
    log_entry = f"Diag: {len(temp_buffer)} entries, last={temp_buffer[-1] if temp_buffer else 0}"
    debug_tag = log_entry.upper().split(':')[0]
    
    return result

# Critical execution point
final_diagnostic = analyze_pattern(encrypted_sequence, threshold)
print(f"Result: {final_diagnostic}")