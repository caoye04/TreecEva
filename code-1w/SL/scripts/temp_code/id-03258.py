def preprocess_logs(raw):    
    # Irrelevant transformation chain
    cleaned = [r.strip().lower() for r in raw if len(r) > 3]
    filtered = [c for c in cleaned if 'error' not in c]
    stats = {'total': len(cleaned), 'filtered': len(filtered)}
    summary = ''.join([f[0] for f in filtered])  # Decoy summary
    return filtered

# Simulated log input with red herrings
raw_logs = [
    '  Startup OK  ',
    'WARNING: Low memory',
    'INFO: User login',
    'ERROR: Disk failure',
    '  Task completed  ',
    'DEBUG: Variable x=7',
    'CRITICAL: System halt'
]

log_data = preprocess_logs(raw_logs)

# Bit manipulation decoy function (never used)
def encrypt_flag(f):
    return (f << 3) ^ 0xA5 | (f & 0x1F)

# Unused data structure with misleading content
diagnostic_matrix = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]

# Real processing begins here
system_flags = 0b1101
flag_count = sum(1 for i in range(4) if system_flags & (1 << i))

# Distractor: complex but unused calculation
entropy_score = 0
for i in range(1, 6):
    entropy_score += (i * flag_count) % 7
entropy_score = round(entropy_score / 6, 3)

# Actual signal extraction from logs
signal_codes = []
for entry in log_data:
    words = entry.split()
    for word in words:
        if word.isdigit():
            signal_codes.append(int(word))
        elif len(word) == 6 and word.isalpha():
            # Extracts 'status' from 'Startup' -> no such word
            signal_codes.append(len(word))

# Another decoy accumulator
shadow_accum = 0
for val in signal_codes:
    shadow_accum = (shadow_accum * 3 + val) % 1000

# Key computation path
primary_signal = sum(signal_codes) if signal_codes else 42

# Conditional red herring
if len(log_data) > 10:
    primary_signal *= 2
elif system_flags & 0b1000:
    # This branch is taken
    temp = system_flags ^ 0xFF
    primary_signal += bin(temp).count('1')
else:
    primary_signal -= 5

# String-based filtering (uses string method)
valid_entries = [e for e in log_data if e.upper().startswith('TASK') or 'complete' in e.lower()]

# Misleading intermediate
aggregated = 0
for entry in valid_entries:
    aggregated += len(entry)

# Core diagnostic logic
sequence = [primary_signal, flag_count, len(valid_entries)]
checksum = sequence[0] ^ sequence[1]
checksum = (checksum * 3) + sequence[2]

# Final transformation with distractor variables
auxiliary_weight = len(diagnostic_matrix) * 2  # Unused but looks important
normalization_factor = 1.0  # Red herring

# Critical statement
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Function definition comes after usage (adds confusion)
def analyze_pattern(entries, flags):
    # Actual logic hidden in a function defined late
    count_complete = sum(1 for e in entries if 'complete' in e.lower())
    flag_bits = bin(flags).count('1')
    digit_sum = sum(int(w) for e in entries for w in e.split() if w.isdigit())
    base_score = count_complete * 100 + flag_bits * 10 + digit_sum
    
    # Use of string method in actual logic
    has_critical = any('critical' in e.lower() for e in entries)
    if has_critical:
        base_score -= 50
    
    # Additional real adjustment
    if 'warning' in ''.join(entries).lower():
        base_score -= 20
        
    return base_score

# Reassign global to fix forward reference
final_diagnostic = analyze_pattern(log_data, system_flags)

print(f"Target result: {final_diagnostic}")