def analyze_pattern(seq, threshold):
    count = 0
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] > seq[i+2]:
            count += 1
    return count > threshold

# Irrelevant helper (distractor)
def validate_checksum(data):
    checksum = 0
    for d in data:
        checksum = (checksum + d) % 257
    return checksum == 131

# Unused transformation function (dead code path)
def transform_legacy(items):
    result = []
    for item in items:
        if item % 3 == 0:
            result.append(item // 3)
        elif item % 2 == 0:
            result.append(item * 2)
    return result

# Decoy accumulator with misleading intermediate output
def accumulate_noise(values):
    temp_sum = 0
    noise_flag = False
    for v in values:
        temp_sum += v ^ 7
        if temp_sum > 100:
            noise_flag = True
    print(f"[DEBUG] Noise accumulation: {temp_sum}")  # Red herring output
    return temp_sum

# Core logic disguised among distractors
def extract_features(raw_data):
    features = []
    for x in raw_data[::2]:  # slicing: every second element
        if x % 4 == 0:
            features.append(x // 4)
        else:
            features.append(x % 4)
    return features

# Complex conditional processing with nested logic
def filter_candidates(candidates, rules):
    valid = []
    for c in candidates:
        passes = True
        if rules['min'] and c < rules['min']:
            passes = False
        if rules['max'] and c > rules['max']:
            passes = False
        if rules['parity'] == 'even' and c % 2 != 0:
            passes = False
        if rules['parity'] == 'odd' and c % 2 == 0:
            passes = False
        if passes:
            valid.append(c)
    return valid

# Main processing with multiple abstraction layers
def process_segments(data, cfg):
    segment_results = []
    
    # Irrelevant preprocessing block (distractor)
    shadow_buffer = [x * 2 + 1 for x in data[:10] if x % 5 == 0]
    accumulate_noise(shadow_buffer)  # Calls decoy function
    
    # Actual feature extraction
    extracted = extract_features(data)
    
    # Misleading control flow with unused branches
    temp_state = 0
    for e in extracted[:5]:
        if e > 3:
            temp_state += e ** 2
        elif e == 2:
            temp_state -= 5
        else:
            temp_state = temp_state // 2  # Integer division
    
    # Real computation hidden in complex logic
    segment_slice = data[3:12]  # slicing operation
    sum_val = sum(segment_slice)
    norm_factor = len(segment_slice)
    avg_val = sum_val / norm_factor
    
    # Conditional mutation based on modular pattern
    if sum_val % 7 == 0:
        adjustment = 3
    elif sum_val % 5 == 0:
        adjustment = -2
    else:
        adjustment = 1
    
    refined = int(avg_val) + adjustment
    
    # Secondary transformation
    secondary_data = [refined + i for i in range(4)]
    checksum_mod = sum(secondary_data) % 11
    
    # Final score calculation (target)
    final_score = (refined * 100) + checksum_mod
    
    # Dead code path with plausible-looking logging
    if final_score > 500:
        debug_log = f"High score detected: {final_score} from {refined}"
    else:
        debug_log = "Normal range"
    
    return final_score

# Global configuration (mix of relevant and irrelevant fields)
config = {
    'min': 5,
    'max': None,
    'parity': 'even',
    'threshold': 3,
    'debug_mode': True,
    'version': '2.1b',
    'legacy_compat': False
}

# Input data with embedded patterns
raw_input_stream = [16, 7, 12, 9, 20, 3, 8, 15, 4, 11, 6, 19, 2, 14, 5]

# Spurious data transformation (distractor)
segment_data = raw_input_stream.copy()
segment_data.reverse()
segment_data = segment_data[1:] + [segment_data[0]]  # Shift operation

# Additional red herring: string manipulation unrelated to result
log_tag = "TRACE-SEG"
timestamp_parts = log_tag.split('-')
if len(timestamp_parts) == 2:
    tag_code = ord(timestamp_parts[1][0]) - ord('A')
else:
    tag_code = 0

# Execute main logic
final_score = process_segments(segment_data, config)

# Print required result
print(f"Result: {final_score}")