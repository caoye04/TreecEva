def preprocess_logs(raw):    
    cleaned = []
    for entry in raw:
        if 'ERROR' in entry:
            cleaned.append(entry.strip().lower())
    return cleaned

raw_data = [
    '  ERROR: Disk failure detected ',
    'WARNING: High CPU usage',
    '  ERROR: Memory overflow  ',
    'INFO: System rebooted',
    'ERROR: Disk failure detected',
    'ERROR: Checksum mismatch in sector 7B'
]

# Irrelevant preprocessing path (dead function)
def legacy_filter(data):
    result = []
    for item in data:
        parts = item.split(':')
        if len(parts) > 1 and parts[1].strip() != '':
            result.append(len(parts[1]))
    return result

# Unused transformation
token_counts = [len(x.split()) for x in raw_data]
dummy_weights = [0.5 ** i for i in range(len(raw_data))]
weighted_sum = sum(token_counts[i] * dummy_weights[i] for i in range(len(raw_data)))

# Real processing begins here
cleaned_logs = preprocess_logs(raw_data)
log_entries = [entry.replace('error:', '').strip() for entry in cleaned_logs]

# Decoy statistical analysis
error_frequency = {}
for log in log_entries:
    words = log.split()
    for word in words:
        error_frequency[word] = error_frequency.get(word, 0) + 1

# Misleading entropy calculation (not used in final result)
import math
total = sum(error_frequency.values())
entropy = 0
for count in error_frequency.values():
    p = count / total
    entropy -= p * math.log2(p) if p > 0 else 0

# System flags with red herring values
system_flags = {
    'overload': False,
    'degraded': True,
    'legacy_mode': True,
    'checksum_errors': 2,
    'disk_errors': 0
}

# Another decoy: unused recursive function
def count_substrings(text, pattern, index=0):
    if index > len(text) - len(pattern):
        return 0
    if text[index:index+len(pattern)] == pattern:
        return 1 + count_substrings(text, pattern, index + 1)
    return count_substrings(text, pattern, index + 1)

# String-based diagnostic rules
severity_map = {
    'disk': 40,
    'memory': 35,
    'checksum': 45,
    'failure': 50,
    'overflow': 30
}

# Critical distraction: complex but unused bit manipulation
def compute_integrity_score(flag_dict):
    score = 0
    for val in flag_dict.values():
        if isinstance(val, int):
            score ^= (val << 2) | (val >> 1)
    return score & 0xFF

integrity_probe = compute_integrity_score(system_flags)  # Never used

# Actual analysis function
def analyze_pattern(entries, flags):
    base_score = 0
    unique_issues = set()
    
    for entry in entries:
        words = entry.split()
        for word in words:
            if word in severity_map:
                base_score += severity_map[word]
                unique_issues.add(word)
    
    # Secondary effect: counting repeated errors
    error_types = []
    for entry in log_entries:
        for key in severity_map:
            if key in entry:
                error_types.append(key)
    
    duplicate_penalty = len(error_types) - len(set(error_types))
    
    # Tertiary logic: special rule for disk failures
    disk_related = any('disk' in e or 'failure' in e for e in entries)
    if disk_related and flags['degraded']:
        base_score += 25
    
    # Final computation
    adjustment = len(unique_issues) * 3
    final_value = base_score + adjustment - (duplicate_penalty * 2)
    
    # Dead code branch inside critical function
    if flags['legacy_mode'] and False:  # Always skipped
        final_value = int(final_value * 0.8)
    
    return final_value

# Key execution point
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Result: {final_diagnostic}")