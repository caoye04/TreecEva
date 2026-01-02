import math

# Simulated sensor data and system diagnostics (irrelevant variables)
raw_readings = [0.85, 0.76, 0.91, 0.64, 0.77]
dummy_checksum = sum(x ** 2 for x in raw_readings)  # Distractor computation
temp_buffer = list(map(lambda x: math.log(x + 1), raw_readings))  # Unused preprocessing

# System state flags (some relevant, some misleading)
system_state = {
    'active': True,
    'overload': False,
    'redundancy_active': True,
    'phase_shift': 3,
    'legacy_mode': True  # Dead flag, not used in logic
}

# Historical log entries with metadata (mixed relevance)
log_data = [
    {'event': 'START', 'level': 1, 'payload': 'init', 'timestamp': 1001},
    {'event': 'CALIBRATE', 'level': 2, 'payload': '0101', 'timestamp': 1005},
    {'event': 'TRANSFER', 'level': 4, 'payload': 'ABCD', 'timestamp': 1010},
    {'event': 'UPDATE', 'level': 3, 'payload': 'done', 'timestamp': 1012}
]

# Irrelevant utility function (decoy)
def validate_payload(p):
    return isinstance(p, str) and p.isalnum()

# Another decoy: checksum calculator for unused security layer
def compute_security_hash(data):
    h = 0
    for entry in data:
        for ch in entry['payload']:
            h ^= ord(ch)
    return h + 1000  # Never actually used

# Core processing pipeline
processing_pipeline = [
    lambda x: x * 1.5 if x > 0.7 else x * 0.8,
    lambda x: round(x, 2),
    lambda x: x + 0.1
]

# Data transformation chain (partially relevant)
transformed = []
for val in raw_readings:
    temp = val
    for func in processing_pipeline:
        temp = func(temp)
    transformed.append(temp)

# Misleading intermediate aggregate (red herring)
avg_transformed = sum(transformed) / len(transformed)
threshold_breach = avg_transformed > 1.0  # Looks important, isn't used

# Actual critical function

def extract_numeric_level(events):
    total = 0
    for e in events:
        if 'level' in e:
            total += e['level']
    return total

# Bit manipulation decoy (never invoked)
def shift_diagnostic_code(code, direction='left'):
    if direction == 'left':
        return code << 2
    else:
        return code >> 1

# Real metric processor with hidden logic

def process_metrics(events, state):
    base_score = extract_numeric_level(events)
    
    # Conditional adjustment based on state
    if state['active']:
        base_score *= 2
    if state['overload']:
        base_score -= 10
    else:
        base_score += 3
    
    # Hidden dependency on phase_shift
    modifier = 1
    for i in range(state['phase_shift']):
        modifier *= 1.1
    
    intermediate = base_score * modifier
    
    # String-based switch using payload length from last event
    last_payload = events[-1]['payload']
    if len(last_payload) == 4 and last_payload.isupper():
        intermediate += 5
    
    # Final adjustment using dictionary lookup (real path)
    adjustments = {
        1: -2,
        2: 0,
        3: 1,
        4: 3
    }
    level_count = len([e for e in events if 'level' in e])
    intermediate += adjustments.get(level_count, -1)
    
    # Redundant but looks important: string operation distraction
    tag = ''.join([e['event'][0] for e in events if e['level'] > 1]).lower()
    if 'u' in tag:
        intermediate -= 1.5  # Not triggered
    
    return int(intermediate)  # Critical: conversion to integer

# Decoy assignment (misleads flow understanding)
final_diagnostic = -999

# Actual computation
final_diagnostic = process_metrics(log_data, system_state)

# Output requirement
print(f"Target result: {final_diagnostic}")