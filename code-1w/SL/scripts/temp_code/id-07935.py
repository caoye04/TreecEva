from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with red herrings
def legacy_checksum(values):
    # Irrelevant legacy function (dead code path)
    return sum(v ** 2 for v in values) % 100

def validate_sequence(seq):
    # Misleading validation not used in main logic
    return all(x > 0 for x in seq if isinstance(x, int))

def decode_signal(pattern):
    # Unused decoy transformation
    base = ''.join(str(int(b)) for b in pattern)
    return int(base, 2) if len(base) > 0 else 0

def apply_filter(dataset, mode='strict'):
    # Real but indirectly used filter
    if mode == 'loose':
        return [x for x in dataset if x % 3 != 0]
    return [x for x in dataset if x % 2 == 0]

# Initialization of various distracting variables
raw_metrics = [12, 18, 24, 36, 48, 72, 84, 96]
diagnostic_trace = ['OK', 'OK', 'FAULT', 'OK']
error_count = len([t for t in diagnostic_trace if t == 'FAULT'])  # Distractor

# Fake state machine (not actually impacting final result)
current_state = 'INIT'
state_log = []
for _ in range(3):
    if current_state == 'INIT':
        current_state = 'WAIT'
    elif current_state == 'WAIT':
        current_state = 'PROCESS'
    state_log.append(current_state)

# Core configuration (some values are distractions)
control_flags = {
    'enable_enhancement': False,
    'use_legacy_mode': True,  # Misleading flag (not actually used)
    'skip_validation': False,
    'debug_trace': True  # Unused
}

# Data generation with embedded logic red herrings
temp_buffer = []
for i in raw_metrics:
    if i > 30:
        temp_buffer.append(i // 3)
    else:
        temp_buffer.append(i // 2)

# String-based side channel (irrelevant to outcome)
status_word = "CALIBRATED"
parity_check = sum(ord(c) for c in status_word) % 7

# Actual relevant data structure initialization
data_pipeline = defaultdict(list)
for idx, val in enumerate(temp_buffer):
    key = 'group_A' if val % 4 == 0 else 'group_B'
    data_pipeline[key].append(val * 1.5)

# Secondary transformation with conditional expression
transformed = []
for group in data_pipeline.values():
    transformed.extend([
        math.log(x) if x > 10 else math.sqrt(x) + 2
        for x in group
    ])

# Decoy set operations (no impact on final output)
unique_set_a = {x for x in transformed if x < 5}
unique_set_b = {x for x in transformed if x > 5}
symmetric_diff = unique_set_a ^ unique_set_b  # Dead end

# Bit manipulation distraction
defective_mask = 0b1101
activation_code = defective_mask & 0b1011
is_active = activation_code >> 2

# Real processing chain begins here
filtered_values = apply_filter([int(x) for x in transformed if x.is_integer()])

# Conditional expression mix
scaling_factor = 2.5 if control_flags['enable_enhancement'] else 1.8
scaled = [v * scaling_factor for v in filtered_values]

# Critical aggregation step
distinct_counter = Counter(scaled)
aggregated = sum(distinct_counter.keys())

# Final computation with string method red herring
log_entry = "Timestamp: 2023-12-04T10:15:00 | Node: X7"
execution_id = log_entry.split('|')[1].strip().split(':')[1].strip()  # Distraction

# Key statement
final_output = int(aggregated + len(data_pipeline['group_A']) * 3.7)

print(f"Result: {final_output}")