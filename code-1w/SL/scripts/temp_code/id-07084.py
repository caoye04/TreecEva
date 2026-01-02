def preprocess_logs(raw):
    processed = []
    for entry in raw:
        if 'ERROR' in entry:
            processed.append(entry.strip().upper())
    return processed

raw_data = [
    '  error: disk full ',
    'warning: temperature high',
    'error: io timeout  ',
    'info: system rebooted'
]

# Irrelevant transformation - distractor
formatted = [x.replace(':', '=').strip() for x in raw_data]
decoys = {x.split(':')[0] for x in formatted}  # set operation (irrelevant)

log_entries = preprocess_logs(raw_data)

# Simulated system flags with red herring values
system_flags = {
    'disk_usage': 95,
    'mem_peak': 87,
    'errors_seen': len(log_entries),
    'last_reboot_code': 0x1A3,
    'safe_mode': False
}

# Decoy function - never called
def compute_health_score(metrics):
    score = 100
    for k, v in metrics.items():
        if 'usage' in k and v > 90:
            score -= 20
    return max(score, 0)

# Auxiliary diagnostic logic - partially relevant
flag_sum = sum(v for v in system_flags.values() if isinstance(v, int))
flag_sum += 1 if system_flags['safe_mode'] else -2  # minor adjustment

# Bit manipulation decoy
encoded_diagnostic = (flag_sum << 2) ^ 0xFF
redundant_check = encoded_diagnostic & 0b1111  # distraction

# Real computation path begins
abnormal_patterns = 0
for log in log_entries:
    words = log.split()
    if 'DISK' in words or 'IO' in words:
        abnormal_patterns += 1

# Hidden accumulation via string patterns
length_total = 0
for log in log_entries:
    clean = ''.join(filter(str.isalpha, log))  # string method chain
    length_total += len(clean)

# Conditional data restructuring - relevant
if len(log_entries) >= 2:
    temp_data = []
    for i in range(len(log_entries)):
        if i % 2 == 0:
            temp_data.append(length_total + abnormal_patterns * 10)
        else:
            temp_data.append(0)
    aggregated = sum(temp_data)
else:
    aggregated = length_total

# Core analysis function
def analyze_pattern(logs, flags):
    base = len(logs) * 100
    extra = 0
    
    # String-based pattern detection
    critical_keywords = {'DISK', 'IO', 'TIMEOUT'}
    keyword_found = False
    for log in logs:
        tokens = set(log.split())
        if tokens & critical_keywords:  # set intersection
            extra += 50
            keyword_found = True
    
    # Redundant branching - misleading
    if flags['disk_usage'] > 90 and not flags['safe_mode']:
        if keyword_found:
            extra += 20
        elif flags['mem_peak'] > 85:
            extra += 5  # dead path due to prior condition
    
    # Accumulation from prior computed values
    reference_value = aggregated  # brings in external state
    adjustment = reference_value // 50
    
    # Final composition
    result = base + extra + adjustment
    
    # Dead code block - distractor
    if result < 0:
        result = abs(result)
        for _ in range(3):
            result //= 2
    
    return result

# Trigger key computation
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Output requirement
print(f"Target result: {final_diagnostic}")