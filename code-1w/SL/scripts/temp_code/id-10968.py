def preprocess_logs(raw):
    processed = []
    noise_counter = 0
    for item in raw:
        if isinstance(item, str) and 'ERR' in item:
            processed.append((noise_counter, item.strip()))
            noise_counter += 1
    return processed

system_flags = {'active': True, 'debug': False, 'legacy_mode': False}

log_entries = [
    'INFO: system boot',
    'ERR: disk failure at sector 42',
    'WARN: high latency',
    'ERR: checksum mismatch in packet 7',
    'INFO: user login'
]

# Irrelevant transformation - distractor
transformed = [x.upper().replace(':', ';') for x in log_entries if 'WARN' in x]
shadow_var = len(transformed) * 2 if transformed else -1

# Unused recursive function - red herring
def calculate_entropy(data, depth=0):
    if depth > 2 or not data:
        return 0
    mid = len(data) // 2
    return data[mid] + calculate_entropy(data[:mid], depth + 1)

# Dummy counters with misleading names
error_tally = sum(1 for entry in log_entries if 'ERR' in entry)
diag_level = 5 if error_tally > 1 else 3

# Real processing begins here
indexed_logs = preprocess_logs(log_entries)

status_map = {0: 'CRITICAL', 1: 'WARNING', 2: 'INFO'}
severity_score = 0
for idx, log in indexed_logs:
    if 'disk' in log:
        severity_score += 7
    elif 'checksum' in log:
        severity_score += 5

# Bit manipulation decoy
bit_fiddling = (severity_score << 2) ^ 0x5A
ignored_mask = bit_fiddling & 0xFF

# Conditional expression with zip and enumerate - required python feature
analysis_pairs = list(zip(
    enumerate([severity_score, diag_level, shadow_var]),
    ['primary', 'fallback', 'auxiliary']
))

mode_flag = 'legacy' if system_flags['legacy_mode'] else 'modern'

# Dictionary operations - required feature
diagnostic_codes = {
    'modern': {7: 101, 5: 205},
    'legacy': {7: 99, 5: 199}
}

lookup_key = diagnostic_codes[mode_flag].get(severity_score, 0)

# Complex conditional expression - required feature
fallback_value = lookup_key if lookup_key else (lambda x: x * 2 + 3)(len(indexed_logs))

# Critical computation path
interim_result = fallback_value + sum(key[0] for key, _ in analysis_pairs)

# Final function call that computes the answer
def analyze_pattern(entries, flags):
    temp_result = interim_result
    if flags['active']:
        scaling_factor = 1.5 if flags['debug'] else 2.0
        temp_result = int(temp_result * scaling_factor)
    
    # Additional check using dictionary .get() with default
    offset = flags.get('offset', -4)
    temp_result += offset
    
    # Redundant control flow - distractor
    if temp_result < 0:
        temp_result = abs(temp_result)
    else:
        temp_result -= 1  # This executes
    
    return temp_result

final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Result: {final_diagnostic}")