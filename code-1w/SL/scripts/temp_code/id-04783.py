def preprocess_logs(raw):
    processed = {}
    temp_sum = 0
    for i, val in enumerate(raw):
        if i % 3 == 0:
            temp_sum += val ^ 5
        elif i % 7 == 0:
            temp_sum -= val >> 2
    processed['checksum'] = temp_sum
    processed['size'] = len(raw)
    return processed

system_flags = {
    'ACTIVE': True,
    'DEBUG_MODE': False,
    'ENCRYPTION_ON': True,
    'FIREWALL_ACTIVE': True,
    'REDUNDANCY_CHECK': False
}

log_entries = [12, 8, 15, 3, 9, 6, 11, 4, 7, 2, 5, 13, 10, 1, 14]

# Irrelevant transformation chain (red herring)
def encrypt_data(data):
    result = 0
    for x in data:
        result ^= (x * 3) & 0xFF
    return result

def validate_integrity(data):
    count = 0
    for x in data:
        if x > 10:
            count += 1
    return count > 5

# Unused function (dead code path)
def deprecated_analysis(seq):
    return sum(x for x in seq if x % 2 == 0) * 2

# Distractor: complex but unused bitwise cascade
temp_flag = 0
for key, active in system_flags.items():
    if active:
        temp_flag ^= len(key) << 2

# Secondary distractor: character counting in keys (irrelevant)
char_count = sum(len(k) for k in system_flags.keys())

# Real logic begins here — deeply nested and interwoven with noise
def evaluate_thresholds(entries):
    stats = {'high': 0, 'medium': 0, 'low': 0}
    for val in entries:
        if val >= 10:
            stats['high'] += 1
        elif val >= 5:
            stats['medium'] += 1
        else:
            stats['low'] += 1
    return stats

def compute_entropy(values):
    total = 0.0
    for v in values:
        if v != 0:
            total += v * (v.bit_length() / (len(values) + 1))
    return round(total, 6)

def filter_anomalies(entries, threshold=5):
    anomalies = []
    for e in entries:
        if e < threshold and e % 2 == 1:
            anomalies.append(e)
    return set(anomalies)

# Core analysis function — contains relevant logic amidst distractions
def analyze_pattern(logs, flags):
    # Step 1: Evaluate value distribution
    dist = evaluate_thresholds(logs)
    
    # Step 2: Compute weighted entropy
    entropy_score = compute_entropy(logs)
    
    # Step 3: Find rare odd anomalies below 5
    rare_set = filter_anomalies(logs, 5)
    
    # Step 4: Extract checksum from preprocessing (uses logs)
    prep = preprocess_logs(logs)
    base_check = prep['checksum']
    
    # Step 5: Use only specific flag states (ignore others)
    active_count = 0
    for k, v in flags.items():
        if k in ['ACTIVE', 'FIREWALL_ACTIVE'] and v:
            active_count += 1

    # Step 6: Combine dist metrics
    magnitude = dist['high'] * 100 + dist['medium'] * 10 + dist['low']
    
    # Step 7: Apply conditional offset based on entropy parity
    offset = 0
    if int(entropy_score * 1000000) % 2 == 0:
        offset += 50
    else:
        offset -= 25
    
    # Step 8: Incorporate rare set size as multiplier factor
    multiplier = len(rare_set) if len(rare_set) > 0 else 1
    
    # Step 9: Final computation
    intermediate = (magnitude + base_check + offset) * multiplier
    
    # Step 10: Mask with active flag count (bitwise AND)
    final_value = intermediate & ((active_count << 3) - 1)
    
    # Step 11: Add dummy adjustment that cancels out
    dummy_shift = char_count - char_count  # Always zero
    final_value += dummy_shift
    
    # Step 12: Return true answer
    return final_value

# Execution point of interest
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Result: {final_diagnostic}")