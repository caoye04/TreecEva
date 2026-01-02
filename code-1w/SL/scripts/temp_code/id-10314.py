from collections import defaultdict, Counter

# Simulated telemetry data from distributed sensors
telemetry_streams = {
    'sensor_a': [1, 1, 0, 1, 1, 0, 0],
    'sensor_b': [0, 1, 1, 0, 1, 1, 1],
    'sensor_c': [1, 0, 1, 1, 0, 1, 1]
}

# Irrelevant baseline thresholds (distractor)
thresholds = defaultdict(lambda: 0.5)
for k in telemetry_streams:
    thresholds[k] = sum(telemetry_streams[k]) / len(telemetry_streams[k])

# Correlation matrix placeholder (unused red herring)
correlation_map = [[0 for _ in range(3)] for _ in range(3)]

# Historical anomaly counts (partially used, partially irrelevant)
historical_anomalies = {'sensor_a': 12, 'sensor_b': 8, 'sensor_c': 15, 'sensor_d': 20}

# System event log with mixed signal patterns
log_data = [
    "ERROR:sync_fail", "INFO:retry_init", "WARN:latency_spike",
    "ERROR:sync_fail", "INFO:retry_success", "WARN:fluctuation",
    "ERROR:corrupt_frame", "INFO:reset_ok"
]

# Bitmask representations of system states (some misleading)
system_states = {
    'idle': 0b0001, 'active': 0b0010, 'syncing': 0b0100, 'error': 0b1000
}

# Flags indicating current operational status (mixed relevance)
system_flags = [
    system_states['active'] | system_states['syncing'],
    system_states['active'],
    system_states['error'] | system_states['active']
]

# Decoy function that appears important but is unused
def calculate_entropy(vector):
    total = sum(vector)
    if total == 0:
        return 0.0
    probs = [v / total for v in vector if v > 0]
    from math import log2
    return -sum(p * log2(p) for p in probs)

# Auxiliary transformation (used indirectly via string parsing)
def encode_state(flag):
    active_bits = []
    for name, mask in system_states.items():
        if flag & mask:
            active_bits.append(name)
    return ",".join(sorted(active_bits))

# Misleading counter that tracks non-critical events
false_positive_count = Counter()
for entry in log_data:
    level = entry.split(":")[0]
    false_positive_count[level] += 1

# Core processing function with conditional logic and distractors
def analyze_sequence(seq):
    # Compute moving average of window size 3 (only first result matters)
    moving_averages = []
    for i in range(len(seq) - 2):
        avg = sum(seq[i:i+3]) / 3
        moving_averages.append(round(avg, 2))
    trend_score = int(moving_averages[0] * 100) if moving_averages else 0
    
    # Secondary check: majority pattern?
    mode = max(set(seq), key=seq.count)
    stability = 'high' if seq.count(mode) >= len(seq) * 0.6 else 'low'
    
    return trend_score, stability

# Process string logs into categorical counts (key path)
def parse_log_severity(logs):
    severity_count = defaultdict(int)
    for log in logs:
        tag = log.split(":")[0].lower()
        if tag in ['error', 'warn']:
            severity_count[tag] += 1
    return severity_count

# Main metric processor - critical function
def process_metrics(logs, flags):
    # Parse log severities (relevant)
    parsed = parse_log_severity(logs)
    error_count = parsed.get('error', 0)
    warn_count = parsed.get('warn', 0)
    
    # Extract state encodings (only first flag is used)
    encoded_states = [encode_state(f) for f in flags]
    primary_state = encoded_states[0] if encoded_states else ''
    
    # Determine activation type based on state (conditional expression)
    activation_type = 'critical' if 'error' in primary_state else 'routine' if 'syncing' in primary_state else 'unknown'
    
    # Apply combinatorics: number of unique error-warn sequences possible
    from math import factorial
    total_events = error_count + warn_count
    if error_count == 0 or warn_count == 0:
        sequence_complexity = total_events
    else:
        # C(n,k) = n! / (k!(n-k)!), here we compute C(total, min(error, warn))
        k = min(error_count, warn_count)
        combinations = factorial(total_events) // (factorial(k) * factorial(total_events - k))
        sequence_complexity = combinations % 1000  # bounded impact
    
    # Analyze one sensor stream (only sensor_a is analyzed)
    trend_val, _ = analyze_sequence(telemetry_streams['sensor_a'])
    
    # Confounding adjustment factor (appears significant but has limited effect)
    adjustment = 0
    for state in encoded_states:
        if 'active' in state and 'error' not in state:
            adjustment += 5
    
    # Final diagnostic formula: combines multiple sources
    # Weights are disguised through operations
    diagnosis = (
        (error_count * 100)
        + (warn_count * 10)
        + trend_val
        + sequence_complexity
        + adjustment
    )
    
    # Dead code branch - never executed (red herring)
    if len(historical_anomalies) < 3:
        diagnosis -= 999  # unreachable
    
    # Distractor: modify correlation map (no downstream use)
    for i in range(3):
        for j in range(3):
            correlation_map[i][j] = (i + j) * adjustment
    
    return diagnosis

# Execute main computation
final_diagnostic = process_metrics(log_data, system_flags)
print(f"Target result: {final_diagnostic}")