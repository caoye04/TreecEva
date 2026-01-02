import math

# Simulated sensor data processing with diagnostic analysis
data_stream = [142, 89, 211, 73, 199, 65, 222, 54]

# Irrelevant baseline metrics (distractors)
baseline_avg = 120
noise_floor = 45
calibration_offset = 7
temp_buffer = [0] * len(data_stream)

# Data transformation pipeline
def transform(x, mode='advanced'):
    if mode == 'basic':
        return (x >> 2) + 3
    elif mode == 'advanced':
        return ((x ^ 25) * 3) + int(math.sqrt(x % 17 + 1))
    else:
        return x

# Misleading preprocessing path (dead code - never used)
def legacy_process(arr):
    result = []
    for val in arr:
        result.append((val // 3) * 2 + 1)
    return result

# Real transformation function
def apply_filter(seq, func):
    return [func(x, 'advanced') for x in seq]

# Higher-order threshold generator (looks important but partially irrelevant)
def make_threshold(base):
    scale = 1.618
    def check(val):
        return val > (base * scale) + 5
    return check

# Decoy state tracker (red herring)
current_state = {
    'active': True,
    'mode': 'diagnostic',
    'flags': [0, 0, 0],
    'counter': 0
}

def update_state(step):
    global current_state
    current_state['counter'] += 1
    if step % 2 == 0:
        current_state['flags'][0] ^= 1

# Unused recursive validator (distractor)
def validate_sequence(seq, idx=0):
    if idx == len(seq) - 1:
        return seq[idx] > 0
    if seq[idx] >= seq[idx + 1]:
        return False
    return validate_sequence(seq, idx + 1)

# Core analysis logic with critical computation
def analyze_pattern(data_list, threshold_fn):
    count_above = 0
    sum_contributions = 0
    
    # Nested conditional processing with early breaks
    for i, val in enumerate(data_list):
        if val <= 0:
            break
        
        # Conditional expression with lambda side-use
        modifier = (lambda x: x * 0.85 if x > 200 else x * 1.15)(val)
        
        if threshold_fn(val):
            count_above += 1
            sum_contributions += int(modifier)
        
        # Simulated intermediate adjustment (partially relevant)
        if i % 3 == 0 and val > 100:
            sum_contributions += 5
        
        # Early termination condition (not triggered in this case)
        if count_above > 5:
            sum_contributions -= 20
            break
    
    # Final aggregation uses integer division and rounding
    if count_above == 0:
        return 0
    else:
        average_effect = sum_contributions // count_above  # Integer division
        return round(average_effect * 1.23, 2)

# Orchestration block with decoy operations
transformed_data = apply_filter(data_stream, transform)

# Irrelevant buffer fill (distractor)
for i in range(len(temp_buffer)):
    temp_buffer[i] = (data_stream[i] + calibration_offset) // 2

# Define threshold function using closure (partially distracting)
threshold_func = make_threshold(baseline_avg)

# Update state through unused loop (misleading side effect)
for j in range(3):
    update_state(j)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

# Print result as required
print(f"Target result: {final_diagnostic}")