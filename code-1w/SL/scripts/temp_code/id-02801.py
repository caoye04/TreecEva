def preprocess_signal(raw_samples):
    # Irrelevant transformation (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.3]
    return [int(x * 100) for x in filtered]

# Misleading data setup (red herring)
data_log = [
    "event:startup;status:ok",
    "event:ping;value:123",
    "event:debug;matrix=4,7,2,9"
]

def extract_timestamp(event_str):
    # Unused function - dead code path
    tokens = event_str.split(';')
    for token in tokens:
        if token.startswith('time:'):
            return int(token.split(':')[1])
    return -1

# Decoy data structure with string processing (distractor)
system_tags = ['A1', 'B2', 'C3', 'D4']
tag_checksum = sum(ord(c) for c in ''.join(system_tags)) % 57

# Core signal data (relevant)
primary_sequence = [16, 24, 32, 40, 48]

# Irrelevant combinatorics (misleading complexity)
def count_combinations(n, r):
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result

# Bit manipulation decoy (false lead)
current_flag = 0b10101010
toggle_mask = 0b11110000
masked_flag = current_flag ^ toggle_mask  # Never used beyond here

# Real processing begins here
transformed_data = []
for val in primary_sequence:
    temp = val // 8
    if temp % 2 == 0:
        transformed_data.append(temp + 1)
    else:
        transformed_data.append(temp - 1)

# String-based switch logic (uses string method - required feature)
def get_mode(tag):
    if tag.endswith('X'):
        return 1
    elif tag.lower().startswith('debug'):
        return -1
    return 0

mode = get_mode("diagnostic_mode_X")  # Returns 1, affects downstream

# Central analysis function (key logic)
def analyze_pattern(data):
    accumulator = 0
    shift_factor = mode  # Depends on string evaluation above
    
    for i, item in enumerate(data):
        # Mix of arithmetic and bitwise ops
        squared = item * item
        shifted = squared << shift_factor
        masked = shifted & 0xFF  # Keep lower 8 bits
        
        # Conditional early exit (control flow)
        if masked > 200 and i > 2:
            break
            accumulator += 1000  # Dead code after break
        
        # Relevant accumulation
        accumulator += masked
    
    # Additional transformation (needed for final answer)
    if len(data) >= 4:
        correction = len(data) * 7
        accumulator -= correction
    
    return accumulator

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data)

# Output requirement
print(f"Result: {final_diagnostic}")