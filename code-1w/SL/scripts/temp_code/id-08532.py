def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > 0]
    normalized = [x / sum(filtered) for x in filtered]
    return normalized

# Irrelevant helper (distractor)
def smooth_data(data):
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-1):min(i+2, len(data))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Unused transformation (dead code path)
def frequency_encode(seq):
    encoding = {}
    for idx, val in enumerate(seq):
        encoding[idx] = val * (idx + 1)
    return encoding

def analyze_pattern(sequence):
    # Character counting via string representation of digits
    digit_trace = ''.join([str(int(x * 100)) for x in sequence])
    count_map = {c: digit_trace.count(c) for c in set(digit_trace)}
    
    # Boolean logic with red herring conditions
    has_repetition = any(count_map[k] > 2 for k in count_map)
    is_balanced = abs(sum(sequence) - 0.5) < 0.1
    
    # Misleading intermediate computation (not used in final result)
    shadow_metric = 0
    for k, v in count_map.items():
        if int(k) % 2 == 0:
            shadow_metric += v * int(k)
    shadow_metric = shadow_metric ** 0.5 if shadow_metric > 0 else 0

    # Key logic chain begins
    base_score = 0
    for char, cnt in count_map.items():
        base_score += int(char) * cnt
    
    # Composite calculation with string method distraction
    str_score = str(base_score)
    if str_score.startswith('1') and len(str_score) > 2:
        base_score -= int(str_score[1])
    
    # Conditional nesting with decoy branches
    adjustment = 0
    if len(sequence) > 5:
        if has_repetition:
            if is_balanced:
                adjustment = 10
            else:
                adjustment = -5  # Dead branch (not taken due to logic)
        else:
            adjustment = len(count_map) // 2
    else:
        adjustment = 100  # Never reached
    
    # Bit manipulation decoy
    bit_fiddle = base_score ^ 255
    bit_fiddle = bit_fiddle & 127
    
    # Final computation uses only base_score and adjustment
    final_value = base_score + adjustment
    
    # Tuple unpacking distraction
    meta, payload = ('diagnostic', final_value)
    return payload

# Main execution flow
raw_input = [0.12, 0.08, 0.31, 0.19, 0.25, -0.05, 0.14, 0.16]
processed = preprocess_signal(raw_input)

# Simulate entropy buffer from signal
entropy_buffer = []
for val in processed:
    if val >= 0.1:
        entropy_buffer.append(val)

# Decoy list comprehension with no effect
_ = [x for x in processed if x < 0.1]

# Critical statement
final_diagnostic = analyze_pattern(entropy_buffer)

print(f"Result: {final_diagnostic}")