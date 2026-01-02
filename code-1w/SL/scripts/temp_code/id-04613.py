def preprocess_sequence(seq):
    return [x ^ 3 for x in seq if x % 2 == 1]

# Irrelevant helper function (dead code path)
def compute_entropy(data):
    import math
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Unused but misleading diagnostic flag
diagnostic_mode = True
override_threshold = 7
baseline_offset = 12

# Real signal data and decoy transformations
raw_input = [8, 5, 12, 15, 3, 10, 7]
pattern_log = []

for i, val in enumerate(raw_input):
    if val < 10:
        # Apply transformation and log index
        transformed = (val + i) * 2
        pattern_log.append(transformed)
    else:
        # Decoy operation with unused list
        temp_buffer = []
        temp_buffer.append(val // 2)

# Another irrelevant computation
checksum = 0
for num in raw_input:
    checksum = (checksum + num * 3) % 17

# Validation key derived from bitwise manipulation
validation_key = 0
key_source = [6, 3, 1, 7]
for k in key_source:
    validation_key ^= k << 1

# Fake accumulation to mislead reasoning
cumulative_bias = 0
for x in range(5):
    cumulative_bias += x * 2
    if cumulative_bias > 10:
        cumulative_bias = 0

# Real analysis function
def analyze_signal(log, key):
    result = 0
    status_flags = {}
    
    # Use of enumerate and zip (required Python features)
    for idx, (a, b) in enumerate(zip(log[:-1], log[1:])):
        diff = abs(a - b)
        if diff > 4:
            result += diff * (idx + 1)
        status_flags[idx] = diff % 3 == 0
    
    # Secondary adjustment using dictionary operations
    adjustment = 0
    flag_values = list(status_flags.values())
    for j, flag in enumerate(flag_values):
        if flag:
            adjustment += key >> j
    
    # Final computation combining multiple concepts
    final_score = result + adjustment
    
    # Red herring: unused conditional branch
    if final_score < 0:
        final_score *= -2
    
    # Key distractor variables
    shadow_result = final_score ^ 999
    debug_trace = []
    for _ in range(3):
        debug_trace.append('trace')
    
    return final_score

# Execution point of interest
final_diagnostic = analyze_signal(pattern_log, validation_key)

# Print required output
print(f"Result: {final_diagnostic}")