from collections import defaultdict, Counter

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_readings = [127, 255, 0, 128, 64, 32, 16, 8, 4, 2, 1]

# Irrelevant sensor calibration constants (distractor)
CALIBRATION_A = 0.987
CALIBRATION_B = 1.013
OFFSET_X = 25
OFFSET_Y = -17

# System state flags (some relevant, some misleading)
system_state = {
    'active': True,
    'debug_mode': False,
    'cache_valid': True,
    'legacy_protocol': True,
    'overclocked': False,
    'fail_safe': True
}

# Log entries with mixed diagnostic levels
log_entries = [
    {'level': 'ERROR', 'code': 500, 'timestamp': 1623456780, 'module': 'power'},
    {'level': 'INFO',  'code': 200, 'timestamp': 1623456785, 'module': 'io'},
    {'level': 'WARN',  'code': 404, 'timestamp': 1623456790, 'module': 'net'},
    {'level': 'INFO',  'code': 200, 'timestamp': 1623456795, 'module': 'io'},
    {'level': 'ERROR', 'code': 503, 'timestamp': 1623456800, 'module': 'power'}
]

# Dead function - appears useful but unused in actual logic
def legacy_checksum(data):
    chk = 0
    for val in data:
        chk = (chk ^ val) * 13 % 257
    return chk

# Another decoy function with plausible naming
def validate_hierarchy(nodes):
    if not nodes:
        return False
    depth = 0
    for node in nodes:
        depth += (node % 3)
    return depth > 10

# Auxiliary transformation (partially used)
reading_pairs = list(zip(raw_readings[:-1], raw_readings[1:]))
gradient_chain = [b - a for a, b in reading_pairs]

# Bit manipulation red herring
obfuscated_key = 0
for i, val in enumerate(raw_readings[:8]):
    obfuscated_key ^= (val << 1) | (i & 1)

# Real processing begins here
error_count = sum(1 for log in log_entries if log['level'] == 'ERROR')
info_count = sum(1 for log in log_entries if log['level'] == 'INFO')
warning_count = len(log_entries) - error_count - info_count

code_distribution = defaultdict(int)
for log in log_entries:
    code_distribution[log['code']] += 1

total_codes = sum(code_distribution.values())
unique_codes = len(code_distribution)

# Conditional expression chain with meaningful and irrelevant parts
scaling_factor = 1.5 if system_state['active'] and not system_state['overclocked'] else 2.0
adjustment = OFFSET_X - OFFSET_Y if system_state['debug_mode'] else 0

# Meaningful aggregation
weighted_severity = 0
for log in log_entries:
    if log['level'] == 'ERROR':
        weighted_severity += 3
    elif log['level'] == 'WARN':
        weighted_severity += 2
    elif log['level'] == 'INFO':
        weighted_severity += 1

# Data structure cross-reference
module_activity = Counter(log['module'] for log in log_entries)
primary_module = module_activity.most_common(1)[0][1]  # most frequent count

# Critical intermediate computation (appears complex but only one path matters)
consistency_score = 0
for i, ts in enumerate(timestamps):
    if i > 0:
        delta = ts - timestamps[i-1]
        consistency_score += (delta == 5)

# Recursive validation (only called once, but looks important)
def verify_sequence(seq, index=0, acc=0):
    if index >= len(seq):
        return acc
    if seq[index]['code'] in [500, 503]:
        acc += 2
    return verify_sequence(seq, index + 1, acc)

# Misleading accumulation
phantom_accumulator = 0
for reading in raw_readings:
    phantom_accumulator += reading * CALIBRATION_A
    if phantom_accumulator > 1000:
        phantom_accumulator -= 500

# Core diagnostic logic disguised among noise
effective_stability = (primary_module * 10) + (30 if consistency_score == 4 else 0)

# Final processing step that determines answer
def process_metrics(logs, state):
    base = 0
    for entry in logs:
        base += entry['code'] % 7
    
    # Key branching logic
    if state['cache_valid'] and not state['legacy_protocol']:
        result = base * 17
    elif state['active']:
        result = base + effective_stability
    else:
        result = base ** 2
    
    # Only this path is actually taken
    anomaly_flag = any(entry['code'] == 503 for entry in logs)
    modifier = 3 if anomaly_flag else 1
    
    return result * modifier

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")