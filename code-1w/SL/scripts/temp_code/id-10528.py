def preprocess_log(raw):    
    # Irrelevant transformation
    cleaned = raw.strip().lower().replace('error', 'warning')
    tokens = cleaned.split(':')
    return [t.strip() for t in tokens if t.strip()]

# Decoy function - never called
def legacy_calculate(x):
    accumulator = 0
    for i in range(x):
        accumulator += i * (i - 1) // 2
    return accumulator

# Unused utility
def sort_alphanumeric(data):
    return sorted(data, key=lambda x: (x[0], len(x)))

# Main processing chain
log_data = 'CRITICAL:ERROR:WARNING:INFO:DEBUG:ERROR:WARNING'
system_state = [1, 0, 1, 1, 0]
config_threshold = 42

# Distractor variables
buffer_cache = [0] * 100
overflow_flag = False
temp_result = None
recovery_sequence = ['init', 'check', 'retry', 'halt']

# Real work begins here
entries = preprocess_log(log_data)
entry_count = len(entries)
error_count = sum(1 for e in entries if 'error' in e)
warning_count = sum(1 for e in entries if 'warning' in e)
info_count = sum(1 for e in entries if 'info' in e)

# Bit manipulation decoy
flag_register = 0
for bit in system_state:
    flag_register = (flag_register << 1) | bit

# Simulate diagnostic scan with red herring calculations
scan_results = []
for i in range(len(entries)):
    if i % 2 == 0:
        scan_results.append(len(entries[i]) * 3)
    else:
        scan_results.append(len(entries[i]) + 5)

# Unused sorting path
decoy_sorted = sorted(scan_results, reverse=True)
median_val = decoy_sorted[len(decoy_sorted)//2] if decoy_sorted else 0

# Actual pattern analysis (core logic)
def analyze_pattern(logs, flags):
    pattern_score = 0
    
    # String method usage
    joined = ''.join(logs).upper()
    critical_pos = joined.find('CRITICAL')
    
    if critical_pos != -1:
        pattern_score += 17
    
    # Boolean logic and counting
    has_recovery = any('retry' in tag for tag in recovery_sequence)
    if has_recovery and overflow_flag:  # overflow_flag is always False
        pattern_score += 100
    
    # Conditional branch with early return red herring
    if len(logs) > 10:
        return -1  # dead path
    
    # Real computation
    unique_segments = set(logs)
    segment_bonus = len(unique_segments) * 5
    
    active_modules = sum(flags)
    module_multiplier = active_modules if active_modules > 0 else 1
    
    # Counting/grouping with distraction
    letter_freq = {}
    for char in joined:
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char, 0) + 1
    
    max_freq = max(letter_freq.values()) if letter_freq else 0
    
    # Final calculation (only this matters)
    pattern_score += segment_bonus
    pattern_score *= module_multiplier
    pattern_score -= max_freq  # 'E' appears most frequently
    
    return pattern_score

# Key execution point
final_diagnostic = analyze_pattern(entries, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")