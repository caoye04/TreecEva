def preprocess_signal(data):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(data) for x in data]
    filtered = [x for x in normalized if x > 0.1]
    return [int(x * 100) for x in filtered]


def generate_checksum(seq):
    # Dead function - never used but looks important
    return sum(x * (i+1) for i, x in enumerate(seq)) % 1000

# Simulated sensor input (red herring)
sensor_readings = [150, 300, 450, 600, 750, 900]
processed_data = preprocess_signal(sensor_readings)

# Core logic disguised among noise
baseline = [8, 6, 7, 5, 3, 0, 9]
offset_key = sum(baseline[i] for i in range(0, len(baseline), 2))  # 8 + 7 + 3 + 9 = 27

# Decoy data structure
diagnostics_db = {
    'codes': {f'ERR_{i}': i*10 for i in range(1, 50)},
    'flags': set('XYZ')
}

# Another distraction: string-based key generation
device_id = 'SEN-TRX-9021'
key_fragment = ''.join([c for c in device_id if c.isdigit()])
activation_score = sum(int(c) for c in key_fragment) if key_fragment else 0  # 9+0+2+1=12

# Real logic starts here — pattern analysis with recursion
logic_sequence = [1, 1]
for i in range(2, 10):
    logic_sequence.append(logic_sequence[i-1] + logic_sequence[i-2])  # Fibonacci-like

# Hidden control flow with conditional expression
evaluation_mode = 'strict' if len(logic_sequence) > 8 else 'relaxed'

# Bit manipulation red herring
config_flag = 0b101010
mask_result = config_flag & 0b111100 | 0b000010

# Actual threshold derived from offset_key and activation_score (misleading combination)
threshold = abs(offset_key - activation_score)  # |27 - 12| = 15

# String method distractor
token_list = device_id.split('-')
valid_tokens = [t for t in token_list if t.startswith('TR')]

# Core recursive analyzer function
def analyze_pattern(seq, limit):
    if not seq or limit <= 0:
        return limit
    
    # Tuple unpacking and conditional expression
    head, *tail = seq
    adjusted_head = head if head % 2 == 0 else head + 1
    
    # Linear search simulation in small space
    found_index = -1
    for idx, val in enumerate(tail):
        if val > adjusted_head:
            found_index = idx
            break
    
    # Real computation hidden among irrelevant ones
    cumulative = adjusted_head
    for val in tail:
        if val < limit:
            cumulative += val // 2
    
    # Recursive reduction with modified limit
    if len(tail) > 3:
        recursive_contribution = analyze_pattern(tail[:3], limit - 5)
        cumulative += recursive_contribution
    
    # Sets used as distraction
    unique_remainders = {x % 7 for x in seq}
    bonus = len(unique_remainders) if 0 in unique_remainders else 0
    
    return cumulative + bonus

# Trigger execution point
temp_var = [x**2 for x in processed_data if x < 50]  # Unused list comprehension
flag_check = mask_result == 0b101010  # Misleading boolean

# Critical statement
final_diagnostic = analyze_pattern(logic_sequence, threshold)

print(f"Result: {final_diagnostic}")