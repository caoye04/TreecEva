from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(187):
        if i % 7 == 0:
            signals.append(f'ERR_{(i * 3) % 43}')
        elif i % 5 == 2:
            signals.append(f'WARN_{(i + 10) % 19}')
        else:
            signals.append(f'OK_{i % 11}')
    return signals

def parse_signal(signal):
    status, code = signal.split('_')
    return status, int(code)

def extract_errors(logs):
    errors = []
    error_count = 0
    temp_accumulator = 0
    
    for entry in logs:
        if entry.startswith('ERR'):
            _, val = parse_signal(entry)
            errors.append(val)
            error_count += 1
            temp_accumulator += val ** 2
    
    # Irrelevant aggregation (distraction)
    avg_square = temp_accumulator / error_count if error_count else 0
    
    # Dead path: never used later
    if len(errors) > 100:
        return [e * 2 for e in errors]
    
    return errors

def compute_entropy(values):
    if not values:
        return 0.0
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 6)

def filter_anomalies(data):
    # Complex filtering with red herring logic
    anomalies = []
    baseline = sum(data) // len(data) if data else 0
    threshold = baseline * 1.3
    
    decoy_result = 0
    for x in data:
        # Misleading condition that looks important
        if x > threshold and (x & 7) == 3:
            anomalies.append(x)
        elif x < 5:
            decoy_result ^= x  # unused beyond this
    
    # Another dead computation
    sorted_anomalies = sorted(anomalies, reverse=True)
    if len(sorted_anomalies) >= 5:
        mid_val = sorted_anomalies[len(sorted_anomalies)//2]
        decoy_result += mid_val
    
    return [a for a in anomalies if a % 2 == 1]  # only odd anomalies kept

def build_frequency_map(entries):
    # Distractor function: builds map but not fully used
    freq_map = defaultdict(int)
    for e in entries:
        freq_map[e] += 1
    
    # Extra irrelevant transformations
    squared_totals = sum(k**2 for k in freq_map.keys()) % 97
    decoy_sum = sum(v * 2 for v in freq_map.values()) % 41
    
    # Only this part matters: return top 3 most common statuses
    status_counts = defaultdict(int)
    for entry in entries:
        status = entry.split('_')[0]
        status_counts[status] += 1
    
    return dict(status_counts)

def validate_sequence(pattern):
    # Unused validation routine (dead path)
    balance = 0
    max_depth = 0
    for p in pattern:
        if 'ERR' in p:
            balance -= 1
        elif 'OK' in p:
            balance += 1
        max_depth = max(max_depth, abs(balance))
    return balance == 0 and max_depth <= 10

def analyze_pattern(log_data, flags):
    # Core analysis with multiple distractions
    parsed_logs = [parse_signal(entry) for entry in log_data if '_' in entry]
    
    # Extract error codes (key path)
    error_codes = extract_errors(log_data)
    
    # Compute entropy of errors (important)
    entropy_metric = compute_entropy(error_codes)
    
    # Filter anomalous high values (key step)
    filtered_anomalies = filter_anomalies(error_codes)
    
    # Use list comprehension to isolate rare anomalies (relevant)
    rare_anomalies = [fa for fa in filtered_anomalies if error_codes.count(fa) == 1]
    
    # Build frequency profile (partially relevant)
    freq_profile = build_frequency_map(log_data)
    normal_count = freq_profile.get('OK', 0)
    warning_count = freq_profile.get('WARN', 0)
    
    # Fake correlation metric (distractor)
    synthetic_index = 0
    for i, code in enumerate(error_codes):
        if i % 4 == 0 and code > 20:
            synthetic_index += (code * i) % 17
    
    # Decoy state machine (irrelevant)
    state = 0
    for c in 'diagnostics_active':
        state = (state + ord(c)) % 13
    
    # Critical calculation chain
    base_score = len(rare_anomalies) * 100
    adjustment = int(entropy_metric * 10)
    if warning_count > normal_count * 0.1:
        adjustment += 25
    
    # Final diagnostic is deterministic
    final_diagnostic = base_score + adjustment - len(error_codes)
    
    # Other variables created to mislead
    debug_snapshot = {
        'timestamp': 1699999999,
        'checksum': sum(final_diagnostic.to_bytes(4, 'little')) ^ 42,
        'version': 'D-1.8'
    }
    
    # Print required at end
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate system flags (unused in computation but looks important)
system_flags = {
    'enable_strict_mode': True,
    'debug_override': None,
    'audit_level': 'FULL',
    'timeout_ns': 999999,
    'retry_limit': 3
}

# Generate input datalog_entries = generate_telemetry()

# Key execution pointfinal_diagnostic = analyze_pattern(log_entries, system_flags)