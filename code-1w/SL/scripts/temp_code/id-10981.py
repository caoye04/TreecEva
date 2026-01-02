def preprocess_logs(raw):
    processed = []
    for item in raw:
        if isinstance(item, dict) and 'timestamp' in item:
            item['timestamp'] = item['timestamp'].replace('-', '')
            item['level'] = item['level'].upper()
            processed.append(item)
    return processed

system_flags = [True, False, True]
dummy_cache = {'temp': 42, 'mode': 'debug', 'active': False}

log_entries = [
    {'id': 1, 'timestamp': '2023-05-01', 'level': 'info', 'value': 8},
    {'id': 2, 'timestamp': '2023-05-02', 'level': 'warn', 'value': 16},
    {'id': 3, 'timestamp': '2023-05-03', 'level': 'error', 'value': 32},
    {'id': 4, 'timestamp': '2023-05-04', 'level': 'info', 'value': 64}
]

# Irrelevant transformation chain
transformed = []
for entry in log_entries:
    transformed.append({k: str(v).swapcase() for k, v in entry.items()})

# Fake aggregation (dead path)
def fake_aggregate(data):
    total = 0
    for d in data:
        if 'VALUE' in d:
            total += len(d['VALUE'])
    return total + 1000

# Unused recursive function (distractor)
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 2)

# Real processing begins here
filtered = [e for e in preprocess_logs(log_entries) if e['level'] != 'INFO']

# Bit manipulation red herring
event_mask = 0
for i, flag in enumerate(system_flags):
    if flag:
        event_mask |= (1 << i)

# Decoy metric calculation
temp_metric = 0
for i, entry in enumerate(filtered):
    temp_metric += entry['value'] ^ (i * 7)

def compute_severity(level):
    mapping = {'info': 1, 'warn': 2, 'error': 4}
    return mapping.get(level, 0)

# Conditional branch with meaningful logic hidden inside distractions
status_codes = []
for entry in filtered:
    code = 0
    if entry['level'] == 'WARN':
        code = compute_severity(entry['level']) * 10
    elif entry['level'] == 'ERROR':
        code = compute_severity(entry['level']) * 15
    status_codes.append(code)

# Real key computation
severity_scores = [compute_severity(e['level']) for e in filtered]
values = [e['value'] for e in filtered]

# Complex zip and enumerate usage (core relevant logic)
weighted_sum = 0
for idx, (score, val) in enumerate(zip(severity_scores, values)):
    weighted_sum += (idx + 1) * score * val

baseline = sum(values) // len(values) if values else 0
correction_factor = sum(1 for f in system_flags if f) * 2.5

# Final diagnostic depends on weighted_sum, baseline, and correction_factor
final_diagnostic = int(weighted_sum - baseline + correction_factor)

# Misleading print statements (distractors)
_ = fake_aggregate(transformed)
_ = recursive_sum(10)

# Critical execution point
final_diagnostic = aggregate_metrics(log_entries, system_flags)

# This function is actually just a wrapper to obscure the real logic
def aggregate_metrics(entries, flags):
    # Repeats the same computation to mislead tracing
    filtered_local = [e for e in preprocess_logs(entries) if e['level'] != 'INFO']
    scores = [compute_severity(e['level']) for e in filtered_local]
    vals = [e['value'] for e in filtered_local]
    total = 0
    for i, (s, v) in enumerate(zip(scores, vals)):
        total += (i + 1) * s * v
    avg = sum(vals) // len(vals) if vals else 0
    factor = sum(1 for f in flags if f) * 2.5
    return int(total - avg + factor)

print(f"Result: {final_diagnostic}")