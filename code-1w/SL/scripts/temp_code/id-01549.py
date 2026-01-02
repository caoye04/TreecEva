def analyze_sequence(pattern):
    """Irrelevant helper function for sequence analysis (dead code path)."""
    if len(pattern) < 3:
        return False
    return all(p % 2 == 0 for p in pattern)

# System telemetry data (simulated)
telemetry_stream = [127, 255, 192, 168, 10, 0, 1, 254]

# Irrelevant buffer transformation
temp_buffer = ''.join([chr(b & 127) for b in telemetry_stream if b > 100])
encoded_tag = temp_buffer.encode('utf-8').hex()[:6]  # Distractor variable

# Core diagnostic thresholds
critical_threshold = 200
warning_base = 50

# Simulated log entries with mixed content
log_data = [
    {'level': 'INFO', 'code': 101, 'payload': 'startup'},
    {'level': 'WARN', 'code': 150, 'payload': 'fluctuation'},
    {'level': 'ERROR', 'code': 210, 'payload': 'outlier'},
    {'level': 'INFO', 'code': 99, 'payload': 'nominal'},
    {'level': 'ERROR', 'code': 230, 'payload': 'critical_drift'}
]

# System operational state
system_state = {
    'active_nodes': 4,
    'replication_factor': 3,
    'quorum_reached': True,
    'is_degraded': False,
    'version': 'v2.1.5'
}

# Auxiliary mapping table (partially used)
severity_map = {
    'INFO': 1,
    'WARN': 2,
    'ERROR': 3
}

# Bit manipulation for checksum (red herring)
checksum = 0
for item in log_data:
    code = item['code']
    checksum ^= (code << 2) | (code >> 6)
corrected_checksum = checksum & 0xFF  # Unused result

# Extract and transform error codes using list comprehension
error_codes = [entry['code'] for entry in log_data if entry['level'] == 'ERROR']

# Calculate derived metrics
high_severity_count = len(error_codes)
max_code = max(error_codes) if error_codes else 0

# Secondary computation: cumulative warning score (misleading)
warning_score = sum(
    entry['code'] - warning_base 
    for entry in log_data 
    if entry['level'] == 'WARN'
)

# Case conversion chain on version string (distractor)
version_upper = system_state['version'].upper()
version_clean = version_upper.replace('V', '').replace('.', '')
build_id = int(version_clean)  # Looks important but isn't used

# Determine status weight based on quorum and node count
if system_state['quorum_reached']:
    base_weight = system_state['active_nodes'] * 10
    if system_state['replication_factor'] >= 3:
        base_weight += 15
else:
    base_weight = 5

# Additional logic: degraded mode penalty
penalty = 10 if system_state['is_degraded'] else 0
adjusted_weight = base_weight - penalty

# Real-time drift index calculation (key relevant path)
drift_values = [code for code in error_codes if code > critical_threshold]
drift_index = sum(d - critical_threshold for d in drift_values)

# Weighted diagnostic score
severity_bonus = high_severity_count * 17

# Main processing function
def process_metrics(logs, state):
    # Nested conditional with distractors
    temp_flag = False
    if 'v2' in state['version']:
        for c in [65, 66, 67]:  # ASCII values - irrelevant loop
            if chr(c) in 'ABC':
                temp_flag = True
    
    # Character counting distraction
    payload_chars = ''.join([entry['payload'] for entry in logs])
    char_freq = {c: payload_chars.count(c) for c in set(payload_chars)}
    rare_chars = [c for c in char_freq if char_freq[c] == 1]  # Unused
    
    # Actual signal extraction
    error_sum = sum(entry['code'] for entry in logs if entry['level'] == 'ERROR')
    level_scores = [severity_map[entry['level']] for entry in logs]
    total_level_score = sum(level_scores)
    
    # Critical formula
    if error_sum > 0:
        base_diagnostic = (error_sum // len(logs)) + total_level_score
    else:
        base_diagnostic = 10
    
    # Incorporate system weight
    node_factor = state['active_nodes']
    final_value = base_diagnostic + adjusted_weight + drift_index - node_factor
    
    # Dead branch (never taken due to data)
    if temp_flag and build_id > 10000:
        final_value *= 2  # Decoy modification
    
    return final_value

# Execute main logic
total_logs = len(log_data)
final_diagnostic = process_metrics(log_data, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")