def analyze_sequence(data):
    """Irrelevant helper that computes sequence properties."""
    if len(data) < 3:
        return 0
    diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
    return sum(d ** 2 for d in diffs if d % 2 == 0)

# Irrelevant constants and decoy data
DECOY_THRESHOLD = 773
TEMP_BUFFER = [0] * 15
system_uptime_hours = 982
maintenance_window_active = False

# Real input data
log_entries = [
    {'timestamp': 1648567800, 'level': 'ERROR', 'code': 404},
    {'timestamp': 1648567805, 'level': 'INFO', 'code': 200},
    {'timestamp': 1648567810, 'level': 'WARN', 'code': 403},
    {'timestamp': 1648567815, 'level': 'ERROR', 'code': 500},
    {'timestamp': 1648567820, 'level': 'INFO', 'code': 200}
]

# System flags with red herring values
system_flags = {
    'debug_mode': True,
    'cache_enabled': False,
    'legacy_protocol': True,
    'overclocked': None,
    'degraded_mode': False
}

# Distractor: unused function (dead code path)
def legacy_checksum(seq):
    acc = 0
    for i, val in enumerate(seq):
        acc += val * (i + 1)
    return acc % 1024

# Distractor: irrelevant list processing
event_codes = [entry['code'] for entry in log_entries]
duplicate_check = set(event_codes) - {200}
filtered_codes = sorted(list(duplicate_check))

# Real logic begins here — metric extraction based on level frequency
def count_levels(entries):
    counts = {}
    for e in entries:
        lvl = e['level']
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

# Extract timestamps for time window analysis
timestamps = [e['timestamp'] for e in log_entries]
time_gaps = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
valid_intervals = [gap for gap in time_gaps if gap < 10]

# Distractor: complex but unused bitwise transformation
flag_state = 0
for i, (k, v) in enumerate(system_flags.items()):
    if v is True:
        flag_state |= (1 << i)
    elif v is False:
        flag_state &= ~(1 << i)
    else:
        flag_state ^= (1 << (i//2))

# Another decoy variable
checksum_intermediate = sum(time_gaps) ^ len(log_entries)

# Real processing: compute diagnostic score
def evaluate_stability(levels_count, intervals):
    error_count = levels_count.get('ERROR', 0)
    warn_count = levels_count.get('WARN', 0)
    info_count = levels_count.get('INFO', 0)
    base_score = 100 - (error_count * 15) - (warn_count * 5)
    
    # Adjustment based on timing consistency
    timing_bonus = 10 if all(gap == 5 for gap in intervals) else -5
    return base_score + timing_bonus + info_count

# Distractor: tuple unpacking with irrelevant data
data_stream = [(1, 'A'), (2, 'B'), (3, 'C')]
indices, labels = zip(*data_stream)

# Real function using set operations and slicing
def process_metrics(entries, flags):
    # Use set to deduplicate codes
    unique_codes = set(e['code'] for e in entries)
    
    # Slicing: only consider first 4 entries for weight calculation
    recent = entries[:4]
    level_freq = count_levels(recent)
    
    # Conditional logic with boolean expressions
    high_severity = any(e['code'] >= 500 for e in entries)
    debug_influence = 5 if flags['debug_mode'] and not flags['cache_enabled'] else 0
    
    # Core computation
    stability = evaluate_stability(level_freq, time_gaps)
    code_diversity = len(unique_codes)
    
    # Final combination
    raw_diagnostic = stability * code_diversity + debug_influence
    
    # Misleading rounding operation (not actually needed)
    rounded_hint = round(raw_diagnostic / 3.0) * 3
    
    # Actual answer
    final_value = int(raw_diagnostic + (1 if rounded_hint > 100 else -2))
    
    return final_value

# Key execution point
final_diagnostic = process_metrics(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")