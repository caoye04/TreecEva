def process_log_segment(segment):
    lines = segment.strip().split('\n')
    total_chars = sum(len(line) for line in lines)
    empty_lines = sum(1 for line in lines if not line.strip())
    avg_line_length = total_chars / len(lines) if lines else 0
    return total_chars, empty_lines, avg_line_length

log_entry = '''USER_SESSION_START\naction:initiate;time=0.0\ndata_payload: a37b2c\n\nstatus:active\naction:ping;time=1.2\n\nUSER_SESSION_END'''

initial_load = 150
buffer_limit = 200
maintenance_overhead = 23

# Extract payload for analysis
tokens = log_entry.split('data_payload: ')
payload_line = tokens[1].split('\n')[0] if len(tokens) > 1 else ''

char_frequency = {c: payload_line.count(c) for c in set(payload_line)}
distinct_chars = len(char_frequency)

# Simulate checksum (irrelevant to final result)
checksum = 0
for i, c in enumerate(payload_line):
    checksum += ord(c) * (i + 1)
checksum %= 1000

# Parse time entries from log
import math
times = []
for line in log_entry.split('\n'):
    if 'time=' in line:
        try:
            t_val = float(line.split('time=')[1].split(';')[0])
            times.append(t_val)
        except:
            continue

max_time = max(times) if times else 0
min_time = min(times) if times else 0
time_range = max_time - min_time if times else 0

# Auxiliary function with red herring logic
def analyze_session_risk(time_span, threshold=2.0):
    if time_span < threshold:
        return 'LOW'
    elif time_span < 5.0:
        return 'MEDIUM'
    else:
        return 'HIGH'

risk_level = analyze_session_risk(time_range)

# Core capacity logic
base_reduction = len(times) * 5
size_penalty = distinct_chars * 2 if distinct_chars > 5 else 10

intermediate_buffer = buffer_limit - maintenance_overhead - base_reduction

# Distractor: unused intermediate calculation
estimated_growth = math.ceil(intermediate_buffer * 0.15)
safety_margin = 12

if risk_level == 'LOW':
    safety_margin += 5
else:
    safety_margin -= 3

# Final computation chain
temp_capacity = intermediate_buffer - size_penalty
final_capacity = temp_capacity - safety_margin

# Additional misleading state tracking
session_summary = {
    'valid': True,
    'peak_usage': buffer_limit - temp_capacity,
    'final_capacity': final_capacity,
    'checksum_flag': checksum > 500
}

Result: {final_capacity}