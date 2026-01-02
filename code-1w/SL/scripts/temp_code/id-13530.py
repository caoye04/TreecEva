import itertools

def process_logs(raw_data, filter_mask):
    # Irrelevant preprocessing step (distractor)
    sanitized = [x.strip().lower() for x in raw_data if x]
    filtered = []
    for i, entry in enumerate(sanitized):
        if i % 2 == 0 and len(entry) > 3:
            filtered.append(entry + '_filtered')
    return filtered

def compute_checksum(sequence):
    # Unused function - red herring
    chk = 0
    for char in ''.join(sequence):
        chk ^= ord(char)
    return chk

def decode_signal(patterns):
    # Distractor: complex but unused logic
    signal_map = {}
    for p in patterns:
        bits = [1 if c == '1' else 0 for c in p]
        rotated = bits[3:] + bits[:3]
        signal_map[p] = sum(rotated)
    return {k: v for k, v in signal_map.items() if v % 2 == 0}

def validate_sequence(seq):
    # Dead code path - never called
    if not seq:
        return False
    return all(s.isdigit() for s in seq)

# Simulated log entries with embedded numeric tags
temp_logs = [
    "ERR|415|retry=3",
    "INFO|201|retry=0",
    "WARN|307|retry=1",
    "CRIT|500|retry=5",
    "INFO|201|retry=0"
]

log_entries = [
    {'level': part[0], 'code': int(part[1]), 'retry': int(part[2].split('=')[1])}
    for line in temp_logs
    for part in [line.split('|')]
]

# System configuration with decoy values
system_id = 7
threshold_limit = 92
baseline_offset = -7
reference_key = [2, 3, 5, 7, 11]

# Misleading intermediate calculations
decoys = []
for i in range(5):
    temp_val = (i ** 3) & 7
    decoys.append(temp_val * 19)

# Hidden accumulator (key variable)
counter_state = 0
for entry in log_entries:
    if entry['level'] in ['ERR', 'CRIT']:
        counter_state += entry['code'] // (entry['retry'] + 1)

# Secondary distraction: unused data transformation
mapped_signals = list(itertools.chain.from_iterable(
    [(x['code'] >> 2), (x['retry'] << 1)] for x in log_entries if x['level'] == 'WARN'
))

# Core logic buried among noise
status_weights = {'INFO': 1, 'WARN': 3, 'ERR': 5, 'CRIT': 9}
aggregated = 0
for log in log_entries:
    weight = status_weights.get(log['level'], 0)
    penalty = log['retry'] * 2
    score = (log['code'] % 100) - penalty
    if log['code'] >= 400:
        score -= 10  # additional penalty
    aggregated += weight * max(score, 0)

# Final aggregation function with critical assignment
def aggregate_metrics(entries, sys_id):
    base = 0
    for e in entries:
        if e['retry'] > 0:
            base += e['code'] % (e['retry'] + 2)
    # Real answer computed here
    result = (base * sys_id) - 34
    return result

# Execution point of interest
final_diagnostic = aggregate_metrics(log_entries, system_id)

# Print required output
print(f"Target result: {final_diagnostic}")