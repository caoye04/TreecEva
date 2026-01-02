def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return [x ** 2 for x in sequence if x % 2 == 0]

# Distractor variables (irrelevant data)
dummy_weights = [0.1, 0.3, 0.6]
scaling_factor = 1.75
temp_buffer = (9, 8, 7, 6)

# Real data structures involved in computation
event_log = [
    {'type': 'click', 'value': 5},
    {'type': 'hover', 'value': 2},
    {'type': 'click', 'value': 8},
    {'type': 'scroll', 'value': 1}
]

# Decoy function with misleading name
def calculate_engagement(raw_data):
    total = 0
    for item in raw_data:
        if item['type'] == 'hover':
            total += item['value'] * 0.5
    return total * 2.0  # Never actually used

# Lambda for filtering relevant events (used)
valid_event = lambda e: e['type'] in ['click', 'scroll']
filtered_actions = list(filter(valid_event, event_log))

# Bit manipulation red herring
obfuscation_key = 23
scrambled = [e['value'] ^ obfuscation_key for e in event_log]
unrelated_sum = sum(scrambled) >> 2  # Dead-end computation

# Tuple unpacking distraction
a, b, c, d = temp_buffer
offset = (a - c) * (d + 1)  # Unused offset

# Core logic disguised among noise
metric_data = []
for entry in filtered_actions:
    points = entry['value']
    if entry['type'] == 'click':
        points *= 3
    elif entry['type'] == 'scroll':
        points *= 1
    metric_data.append(points)

# Another decoy list comprehension
shadow_copy = [x for x in metric_data if x > 10]  # Unused

# Actual evaluation function
threshold_map = { 'low': 5, 'high': 15 }

def evaluate_performance(metrics):
    base = sum(metrics)
    adjustment = 0
    
    # Nested conditional logic with distractions
    if base > threshold_map['high']:
        adjustment += 2
        # Redundant bitwise check
        if (base & 1) == 0:  # Even?
            adjustment -= 1  # Misleading correction
    elif base > threshold_map['low']:
        adjustment += 1
    else:
        adjustment -= 1
    
    # Final transformation using lambda (actual use)
    modifier = lambda x: x * 1.1 if x > 10 else x * 0.95
    result = modifier(base + adjustment)
    
    # Interference: string operations with no effect
    log_tag = "PERF"
    tag_code = ''.join([chr(ord(c)+1) for c in log_tag])  # DEAD END
    
    return int(result)  # Critical assignment happens here

# Execution point of interest
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")