from collections import defaultdict, Counter
import math

# Simulated system log analyzer with diagnostic scoring

def preprocess_logs(raw_logs):
    processed = []
    for entry in raw_logs:
        if 'ERROR' in entry['level']:
            processed.append({'type': 'critical', 'code': entry['code'], 'ts': entry['timestamp']})
        elif 'WARN' in entry['level']:
            processed.append({'type': 'warning', 'code': entry['code'], 'ts': entry['timestamp']})
    return processed

# Irrelevant helper - decoy function (never called)
def legacy_score_calc(errors):
    total = 0
    for e in errors:
        total += hash(e['code']) % 7
    return total * 1.5

# Another red herring: unused data transformation
def encrypt_timestamps(logs):
    return [str(l['ts'] ^ 0xABCDEF) for l in logs if 'ts' in l]

# Core analysis logic
def count_anomalies(entries):
    counts = defaultdict(int)
    for e in entries:
        counts[e['type']] += 1
        counts['total'] += 1
    return counts

# Bit manipulation distraction
def compute_checksum(flag_list):
    chk = 0
    for f in flag_list:
        chk ^= (f * 3) + (f << 1) & 0xFFFF
    return chk >> 4

# String-based pattern extractor (partially relevant)
def extract_patterns(logs):
    patterns = []
    for log in logs:
        msg = log.get('msg', '')
        words = msg.upper().split()
        for word in words:
            if len(word) > 4 and word.isalpha():
                patterns.append(word)
    return patterns

# Main diagnostic engine
def analyze_pattern(log_entries, system_flags):
    # Step 1: Preprocess logs - filter and categorize
    critical_path = preprocess_logs(log_entries)
    
    # Distractor: encrypt timestamps (computed but not used)
    encrypted_ts = encrypt_timestamps(critical_path)
    
    # Step 2: Count anomaly types
    anomaly_counts = count_anomalies(critical_path)
    
    # Step 3: Extract linguistic patterns from original logs
    linguistic_patterns = extract_patterns(log_entries)
    pattern_freq = Counter(linguistic_patterns)
    
    # Distractor: compute checksum on flags (looks important, minimal impact)
    flag_checksum = compute_checksum(system_flags)
    
    # Step 4: Calculate base score from anomalies
    base_score = 0
    if anomaly_counts['critical'] > 0:
        base_score += anomaly_counts['critical'] * 13
    if anomaly_counts['warning'] > 0:
        base_score += anomaly_counts['warning'] * 5
    
    # Step 5: Apply pattern-based multiplier
    dominant_pattern_count = max(pattern_freq.values()) if pattern_freq else 1
    multiplier = math.log(dominant_pattern_count + 1, 2)
    
    # Step 6: Adjust with fake security parameter (distractor integration)
    security_offset = flag_checksum & 0x1F  # Only lower 5 bits matter
    adjusted_score = base_score * multiplier + security_offset
n    # Step 7: Final diagnostic via bit twist (key step)
    temp_var = int(adjusted_score) ^ 0x5A5A
    final_diagnostic = (temp_var + (temp_var >> 3)) & 0xFFFF
    
    # Dead code path - never executed
    if False:
        fallback = legacy_score_calc(critical_path)
        final_diagnostic = min(final_diagnostic, fallback)
    
    return final_diagnostic

# Simulated input data
log_entries = [
    {'timestamp': 1001, 'level': 'INFO', 'code': 200, 'msg': 'User login successful'},
    {'timestamp': 1002, 'level': 'WARN', 'code': 404, 'msg': 'Resource not found'},
    {'timestamp': 1003, 'level': 'ERROR', 'code': 500, 'msg': 'Internal server error'},
    {'timestamp': 1004, 'level': 'ERROR', 'code': 500, 'msg': 'Internal server error'},
    {'timestamp': 1005, 'level': 'WARN', 'code': 403, 'msg': 'Permission denied'},
    {'timestamp': 1006, 'level': 'WARN', 'code': 404, 'msg': 'Page not found'},
    {'timestamp': 1007, 'level': 'ERROR', 'code': 500, 'msg': 'Internal server error'},
    {'timestamp': 1008, 'level': 'WARN', 'code': 404, 'msg': 'Missing asset reference'}
]

system_flags = [0x12, 0x34, 0x56, 0x78]

# Execution point of interest
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Output result
print(f"Target result: {final_diagnostic}")