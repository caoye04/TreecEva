def preprocess_logs(raw):    
    cleaned = []
    for entry in raw:
        if 'ERROR' in entry:
            cleaned.append(entry.strip().upper())
    return cleaned

raw_data = [
    '  error: disk_read_failed ',
    'warning: low_battery',
    'error: timeout_exceeded  ',
    'info: user_login'
]

# Irrelevant preprocessing path (dead function)
def extract_timestamps(logs):
    timestamps = []
    for log in logs:
        for char in log:
            if char.isdigit():
                timestamps.append(char)
    return ''.join(timestamps)

# Unused transformation (distractor)
formatted_data = [line.replace('_', ' ').title() for line in raw_data]

# Real processing begins here
log_entries = preprocess_logs(raw_data)

# System flags with bit manipulation red herring
flag_a = 0b101010
flag_b = 0b110011
flag_c = flag_a ^ flag_b  # Decoy operation
flag_d = (flag_a << 2) & 0xff  # Another decoy
system_flags = len(log_entries) + (flag_a & 0b111)  # Only this part matters

# Character frequency analysis (distractor)
char_freq = {}
for entry in raw_data:
    for c in entry:
        if c.isalpha():
            char_freq[c] = char_freq.get(c, 0) + 1

# Linear search for specific pattern (actually used)
def contains_critical_error(entries, pattern):
    count = 0
    for e in entries:
        if pattern in e:
            count += 1
    return count > 0

# Decoy data structure
error_matrix = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        error_matrix[i][j] = i * j + system_flags  # Misleading computation

# Set operations (required feature) - partially relevant
unique_errors = set()
for entry in log_entries:
    words = entry.split(':')
    if len(words) > 1:
        code_part = words[1].strip()
        unique_errors.add(code_part)

duplicate_check = set()
duplicates_found = 0
for item in unique_errors:
    if item in duplicate_check:
        duplicates_found += 1
    duplicate_check.add(item)

# String method chain with distraction
transformed = []
for e in log_entries:
    step1 = e.replace('ERROR', 'CRITICAL')
    step2 = step1.title()
    step3 = step2.replace(' ', '_')
    transformed.append(step3)  # Collected but not used directly

# Core logic buried in distractions
def compute_severity(errors):
    base = len(errors)
    modifier = 0
    for err in errors:
        if 'TIMEOUT' in err:
            modifier += 3
        elif 'DISK' in err:
            modifier += 5
    return base * (modifier + 1)

# Secondary calculation with decoy control flow
def evaluate_stability(flags):
    level = 0
    if flags > 10:
        level = 7
    elif flags > 5:
        level = 4
    else:
        level = 1
    # Dead branch
    if False:
        level = 999  # Unreachable
    return level

# Main analysis combining multiple concepts
def analyze_pattern(entries, config):
    severity = compute_severity(entries)
    stability = evaluate_stability(config)
    
    # Use of set length and string length as factors
    error_chars = sum(len(e) for e in unique_errors)
    transform_hint = len(transformed[0]) if transformed else 0  # Uses transformed
    
    # Actual answer computation buried here
    intermediate = severity + stability * 2
    adjustment = error_chars % 7
    final = intermediate - adjustment + system_flags
    
    # Red herring: complex bit manipulation that doesn't affect result
    if final > 10:
        masked = final & 0xFFFF
        shifted = (masked << 1) ^ 0xAA
        final = shifted & 0xFFFF  # But then overwritten below
    
    # The real assignment
    final = len(log_entries) * 100 + len(unique_errors) * 10 + (error_chars % 10)
    
    return final

# Critical execution point
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")