def preprocess_logs(raw):
    # Distractor: Heavy preprocessing that isn't fully used
    cleaned = []
    noise_counter = 0
    for entry in raw:
        if 'ERROR' in entry:
            noise_counter += 1
        if 'TRACE' not in entry:
            cleaned.append(entry.replace('[WARN]', '[WARNING]'))
    scaling_factor = max(1, noise_counter // 3)
    return cleaned, scaling_factor

# Irrelevant data structures
temporary_cache = {f'key_{i}': i * 1.5 for i in range(100)}
decoys = [pow(x, 3) - x for x in range(10)]

log_data = [
    '[INFO] System boot',
    '[WARN] Memory pressure rising',
    '[ERROR] Disk I/O timeout',
    '[INFO] Network reconnected',
    '[ERROR] Failed to write buffer',
    '[INFO] Recovery initiated'
]

# Misleading analysis path
def legacy_diagnose(logs):
    score = 0
    for log in logs:
        if 'ERROR' in log:
            score += 100
        elif 'WARN' in log:
            score += 10
    return score // len(logs) if logs else 0

legacy_result = legacy_diagnose(log_data)  # Dead end

# Unused recursive function (red herring)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fib_sequence = [fibonacci(i) for i in range(8)]  # Computation with no impact

# Real processing begins here
processed_logs, factor = preprocess_logs(log_data)

event_map = {
    'INFO': [],
    'WARNING': [],
    'ERROR': []
}

for idx, entry in enumerate(processed_logs):
    if 'INFO' in entry:
        event_map['INFO'].append(idx)
    elif 'WARNING' in entry:
        event_map['WARNING'].append(idx)
    elif 'ERROR' in entry:
        event_map['ERROR'].append(idx)

# Bit manipulation decoy
bit_fiddling = 0
for i in range(len(event_map['INFO'])):
    bit_fiddling ^= (i << 2) | 7

# Conditional red herrings
threshold = 5
if len(event_map['ERROR']) > 0 and len(event_map['WARNING']) == 1:
    threshold = 12
else:
    threshold = 8  # This branch actually taken

# Core logic buried in distractions
sequence_gaps = []
for error_idx in event_map['ERROR']:
    closest_prior_info = None
    for info_idx in event_map['INFO']:
        if info_idx < error_idx:
            closest_prior_info = info_idx
    if closest_prior_info is not None:
        sequence_gaps.append(error_idx - closest_prior_info)

# Another layer of misdirection
checksum = 0
for num in sequence_gaps + event_map['WARNING']:
    checksum = (checksum * 31 + num) % 1000

def analyze_pattern(entries, flags):
    # Main relevant logic
    error_count = len(event_map['ERROR'])
    warning_count = len(event_map['WARNING'])
    info_count = len(event_map['INFO'])
    
    # Critical calculation
    base_score = 0
    if info_count > 0:
        base_score = (error_count * 1000) + (warning_count * 100)
        
        # Adjustment based on gap analysis
        if sequence_gaps:
            avg_gap = sum(sequence_gaps) / len(sequence_gaps)
            base_score += int(avg_gap * 50)
    
    # Multiple returns - early one is a distractor
    if flags.get('safe_mode', False):
        return base_score // 2
        
    # Actual execution path
    adjustment = 0
    if error_count >= 2:
        adjustment += 250
    if len(sequence_gaps) == 2:
        adjustment += 75
        
    final_value = base_score + adjustment
    
    # Hidden dependency on dictionary length
    metadata_tags = {'source': 'sensor', 'version': '2.1', 'mode': 'active'}
    final_value -= len(metadata_tags) * 3  # Subtle correction
    
    return final_value

system_flags = {'debug': True, 'verbose': False}  # safe_mode missing -> False

# Key statement
final_diagnostic = analyze_pattern(processed_logs, system_flags)

# Output requirement
print(f"Result: {final_diagnostic}")