def analyze_system_load(inputs):
    # Irrelevant function: simulates system load but unused
    cumulative = 0
    for val in inputs:
        if val > 50:
            cumulative += val * 0.1
        else:
            cumulative += val * 0.05
    return cumulative

# Unused data structures and variables (distractors)
server_logs = ['ERROR', 'INFO', 'DEBUG', 'WARNING']
network_queue = set(['packet_1', 'packet_3', 'packet_7'])
drop_rate = 0.02

# Relevant data disguised among irrelevant ones
event_codes = {101, 103, 104, 107, 110}
access_flags = [True, False, True]

# Real input data
metrics = [
    {'id': 'A', 'base': 85, 'weight': 0.4},
    {'id': 'B', 'base': 92, 'weight': 0.3},
    {'id': 'C', 'base': 78, 'weight': 0.3}
]

adjustments = {
    'bonus': lambda x: x + 5 if x < 80 else x,
    'penalty': lambda x: x - 3
}

def apply_corrections(data_list):
    # Distractor transformation with partial relevance
    corrected = []
    for item in data_list:
        temp_val = item['base']
        if 'A' in item['id']:
            temp_val = adjustments['bonus'](temp_val)
        elif 'C' in item['id']:
            temp_val = adjustments['penalty'](temp_val)
        corrected.append({**item, 'base': temp_val})
    return corrected

def compute_average(records):
    total = 0.0
    weights = 0.0
    for rec in records:
        total += rec['base'] * rec['weight']
        weights += rec['weight']
    return total / weights if weights else 0

def validate_entry(code_set):
    # Dead-end function, never called
    valid_set = {101, 104, 107}
    return code_set.intersection(valid_set)

def transform_labels(logs):
    # Unused string processing (distractor)
    return [entry.lower().replace('_', '-') for entry in logs if 'E' in entry]

# Simulated sorting of flags (irrelevant)
sorted_flags = sorted(access_flags, reverse=True)

# Key computation chain begins
adjusted_metrics = apply_corrections(metrics)
raw_avg = compute_average(adjusted_metrics)

# Bit manipulation red herring
event_key = 0
for code in event_codes:
    event_key ^= code  # Result is unused

event_key = event_key << 2  # More distraction

# Conditional decoy
if len(network_queue) > 3:
    raw_avg *= 0.95
else:
    raw_avg *= 1.0  # Neutral operation, looks important

# Core logic hidden in lambda and set operations
scoring_engine = lambda avg, flag_list: avg * (1.1 if sum(flag_list) >= 2 else 1.05)

# Final integration step
final_score = scoring_engine(raw_avg, access_flags)

# Additional noise: string method distractor
timestamp_log = "2023-10-05T14:23:00Z"
parts = timestamp_log.split('T')
time_only = parts[1].replace('Z', '').replace(':', '')

# Output the required result
print(f"Result: {final_score}")