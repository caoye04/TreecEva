def analyze_pattern(sequence):
    if not sequence:
        return 0
    upper_count = sum(1 for c in sequence if c.isupper())
    lower_count = sum(1 for c in sequence if c.islower())
    digit_count = sum(1 for c in sequence if c.isdigit())
    total_length = len(sequence)
    
    # Irrelevant transformation (distractor)
    reversed_seq = sequence[::-1]
    shifted = ''.join(chr((ord(c) - ord('A') + 3) % 26 + ord('A')) if c.isalpha() and c.isupper() else c for c in reversed_seq)
    pseudo_hash = sum(ord(c) * (i + 1) for i, c in enumerate(shifted)) % 1000

    # Real logic branch (not obviously primary)
    if upper_count > lower_count and digit_count > 0:
        return (upper_count * 2 + digit_count) // 3
    else:
        return max(lower_count, digit_count) + total_length // 4

# Unused function (dead code path - distractor)
def validate_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, str):
            for c in item:
                checksum += ord(c)
    return checksum % 7 == 0

# Decoy data structure
temp_log = [
    {'id': 'TMP001', 'value': 'Xy9', 'status': 'inactive'},
    {'id': 'TMP002', 'value': 'Ab7', 'status': 'active'},
    {'id': 'TMP003', 'value': 'mN2', 'status': 'active'}
]

# Actual relevant data
collected_data = ['Alpha1', 'BETA2', 'gamma3', 'DELTA4', 'epsilon5']

# Misleading intermediate processing (looks important but isn't on critical path)
raw_scores = []
for entry in temp_log:
    raw_scores.append(sum(ord(c) for c in entry['id']) % 50)

average_score = sum(raw_scores) / len(raw_scores) if raw_scores else 0
adjusted_factor = int(average_score * 1.5)

# Complex mapping with red herring keys
threshold_map = {
    'critical': 85,
    'warning': 60,
    'info': 25,
    'debug': 10,  # unused level
    'legacy_mode': True,  # decoy flag
    'version': '2.1.0'   # irrelevant metadata
}

# Secondary distraction: bit manipulation that goes unused
def transform_value(n):
    n = n ^ 0xFF
    n = (n << 1) | (n >> 7)
    return n & 0xFF

# Core processing function with subtle control flow
def process_readings(readings, config):
    result = 0
    debug_trace = []
    
    for item in readings:
        # Case conversion as part of analysis
        normalized = item.upper()
        
        # Extract digit using string methods
        digits = [c for c in item if c.isdigit()]
        if not digits:
            continue
        
        num_val = int(digits[0])
        
        # String-based classification
        if 'BETA' in normalized or 'DELTA' in normalized:
            category = 'high_priority'
            # This path contributes to final result
            analysis_score = analyze_pattern(item)
            if analysis_score > config['warning']:
                result += num_val * 3
            elif analysis_score > config['info']:
                result += num_val * 2
            else:
                result += num_val
        elif 'Alpha' in item or 'gamma' in item:
            category = 'medium_priority'
            temp_result = 0
            for i, c in enumerate(item):
                if c.isalpha():
                    temp_result += (i + 1) * ord(c.lower())
            temp_result = (temp_result // 100) % 20
            result += temp_result  # Minor contribution
        else:
            category = 'low_priority'
            result -= 1  # Penalty
        
        debug_trace.append(f"{item}:{category}")
    
    # Final adjustment based on accumulated logic
    priority_count = sum(1 for x in debug_trace if 'high_priority' in x)
    if priority_count >= 2:
        result = (result * 110) // 100  # 10% bonus
    
    # Critical red herring: looks like correction but is never used
    verification_key = ''.join([str(len(x)) for x in debug_trace[:3]])
    verified_result = result ^ int(verification_key) if verification_key.isdigit() else result
    
    # Actual return (bypasses verification)
    return result

# Execution point of interest
final_diagnostic = process_readings(collected_data, threshold_map)
print(f"Result: {final_diagnostic}")