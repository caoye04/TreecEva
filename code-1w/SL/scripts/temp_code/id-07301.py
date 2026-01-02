def process_telemetry_chunk(raw_data, threshold=0.75):
    filtered = [x for x in raw_data if x > threshold]
    return [int(x * 100) % 7 for x in filtered]

system_flags = {"ERROR": 5, "WARN": 3, "INFO": 1}
diagnostic_codes = [2, 5, 8, 3, 5, 9, 1, 5]

# Irrelevant transformation chain (distractor)
def legacy_encode(values):
    acc = 0
    for v in values:
        acc = (acc + v) * 2 % 97
    return acc

temporal_weights = [0.1, 0.3, 0.4, 0.2]
aggregated_diagnostics = []

for i in range(4):
    chunk = [x + i * 0.01 for x in [0.65, 0.76, 0.82, 0.91, 0.54]]
    processed = process_telemetry_chunk(chunk)
    score = sum(processed) / len(processed) if processed else 0
    aggregated_diagnostics.append(score)

# Dead code path - never called (red herring)
def compute_health_score(logs):
    return sum(len(str(x)) for x in logs) // 3

# Unused but plausible-looking diagnostic function
def validate_consistency(trace):
    return trace == trace[::-1]

# Simulated sensor drift compensation (irrelevant but realistic)
calibration_offset = 0
for i in range(50):
    calibration_offset += (i * 0.03) % 0.5

calibrated = False
if calibration_offset > 10:
    calibrated = True  # Unreachable under current logic

# Core data structure with meaningful and irrelevant parts
log_entry_template = {
    'timestamp': None,
    'level': 'INFO',
    'code': 0,
    'redundant_checksum': 0  # Unused field
}

diagnostic_log = []
for code in diagnostic_codes:
    entry = log_entry_template.copy()
    entry['code'] = code
    entry['redundant_checksum'] = (code * 7) % 13
    if code == system_flags["ERROR"]:
        entry['level'] = 'ERROR'
    elif code == system_flags["WARN"]:
        entry['level'] = 'WARN'
    diagnostic_log.append(entry)

# Real computation buried in noise
error_count = sum(1 for e in diagnostic_log if e['level'] == 'ERROR')
warn_indices = [i for i, e in enumerate(diagnostic_log) if e['level'] == 'WARN']

# Bit manipulation decoy
def scramble_index(idx, size):
    return ((idx << 2) ^ 0x5) % size

scrambled_positions = [scramble_index(i, len(diagnostic_log)) for i in warn_indices]

# Set operations (required feature) - one relevant, one distractor
unique_codes = set(d['code'] for d in diagnostic_log)
expected_set = {1, 2, 3, 5, 8, 9}
missing_in_log = expected_set - unique_codes  # Distractor

effective_codes = unique_codes & {2, 3, 5, 8}  # Relevant: filter valid fault types

code_frequency = {}
for c in [d['code'] for d in diagnostic_log]:
    code_frequency[c] = code_frequency.get(c, 0) + 1

# Slicing operation (required feature) - partial relevance
recent_events = diagnostic_log[-5:]
suspect_codes = [e['code'] for e in recent_events][::2]  # Every other in recent

# Auxiliary calculation with red herring variables
baseline_reference = 4
drift_compensation_factor = 0.987

# Key algorithm buried in distractions
def analyze_fault_sequence(log, flags):
    # Extract only ERROR codes
    errors = [e['code'] for e in log if e['level'] == 'ERROR']
    if not errors:
        return -1
    
    # Use frequency map computed earlier
    total_errors = sum(code_frequency[code] for code in errors)
    
    # Apply slicing-derived pattern
    influence = 0
    for idx, code in enumerate(suspect_codes):
        if code in errors:
            influence += idx + 1
    
    # Combine with set-derived effective code count
    base_metric = len(effective_codes)
    
    # Final formula: mix of relevant components
    result = (base_metric * total_errors) + influence
    
    # Red herring: unused alternate path
    if result > 20:
        alt = legacy_encode(list(unique_codes))
        result = (result + alt) // 2  # Never reached in this case
    
    return result

# Critical assignment - target of question
final_diagnostic = analyze_fault_sequence(diagnostic_log, system_flags)

# Print required output
print(f"Result: {final_diagnostic}")