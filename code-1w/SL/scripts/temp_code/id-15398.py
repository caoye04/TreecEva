from collections import defaultdict, Counter
import math

# Irrelevant sensor simulation data (distractor)
sensor_readings = [0.1, 0.3, 0.4, 0.2, 0.8, 0.9, 1.1, 1.3]
baseline_offset = 0.5
adjusted_readings = [x - baseline_offset for x in sensor_readings]
valid_readings = [x for x in adjusted_readings if x > 0]

# Unused diagnostic thresholds (red herring)
diag_thresholds = {
    'low': 0.1,
    'medium': 0.4,
    'high': 0.7
}

# Dummy transformation function never called (dead code path)
def unused_transform(data):
    return [math.sin(x) * 2 for x in data]

# Misleading intermediate computation (decoy result)
temp_analysis = sum([int(x * 10) for x in sensor_readings]) // len(sensor_readings)
impact_score = temp_analysis * 17  # Looks important but unused

# Core logic disguised among noise
data_stream = [8, 3, 12, 7, 14, 6, 9, 11]
shift_register = [(x << 2) ^ 5 for x in data_stream]  # Bit manipulation

# Conditional filtering with distractor branches
filtered_candidates = []
for val in shift_register:
    if val > 30:
        filtered_candidates.append(val)
    elif val % 3 == 0:  # Red herring branch
        filtered_candidates.append(val + 1)
    else:
        continue  # Early break in irrelevant case

# Another decoy structure (never accessed)
status_map = defaultdict(lambda: 'unknown')
for i in range(5):
    status_map[f'node_{i}'] = 'idle'

# Real signal hidden in complexity
def generate_signature(seq):
    counts = Counter(seq)
    total = sum(counts.values())
    entropy = sum((count / total) * math.log2(total / count) for count in counts.values())
    return round(entropy * 100)

signature_code = generate_signature(shift_register)

# Simulated control flags with redundant entries
control_flags = {
    'enable_x': True,
    'enable_y': False,
    'mode_alpha': True,
    'debug_trace': True,  # Unused
    'validate_io': False  # Unused
}

# Transform data using set operations and filtering
data_set_a = {x for x in data_stream if x > 7}
data_set_b = {x + 1 for x in data_stream if x % 2 == 0}
overlap = data_set_a & data_set_b  # Set intersection
transformed_data = list(overlap)

def analyze_pattern(data, config):
    if not config.get('enable_x'):
        return -1
    
    # Complex conditional expression
    base = sum(data) if config.get('mode_alpha') else max(data)
    adjustment = 0
    
    # Nested logic with early returns
    for item in data:
        if item > 20:
            adjustment += 2
        elif item > 10:
            adjustment += 1
        else:
            break  # Critical early break
    
    # Final computation combining arithmetic and logic
    raw_result = (base * 3) + (adjustment ^ 7)  # XOR operation
    return int(raw_result / 2) if raw_result > 50 else raw_result * 2

# Key execution point
final_diagnostic = analyze_pattern(transformed_data, control_flags)

# Output requirement
print(f"Target result: {final_diagnostic}")