import itertools
from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def collect_telemetry(batches):
    raw_signals = []
    for b in batches:
        phase_data = [x * 1.05 for x in b if x > 0]
        filtered = list(itertools.dropwhile(lambda x: x < 10, sorted(phase_data)))
        raw_signals.extend([(i, val) for i, val in enumerate(filtered)])
    return raw_signals

# Irrelevant auxiliary function – dead code path (red herring)
def compute_efficiency_rating(data):
    total = sum(x[1] for x in data)
    count = len(data)
    return total / count if count else 0

# Signal correlation engine with decoy logic
def correlate_signals(telemetry, threshold=15.0):
    correlations = defaultdict(int)
    magnitudes = [t[1] for t in telemetry]
    avg_mag = sum(magnitudes) / len(magnitudes) if magnitudes else 0
    
    # Misleading intermediate computation (not used later)
    anomaly_score = 0
    for m in magnitudes:
        if m > threshold:
            anomaly_score += (m - threshold) ** 0.5
    
    # Real transformation: categorize by magnitude bands
    for mag in magnitudes:
        if mag < 8:
            correlations['low'] += 1
        elif mag < 20:
            correlations['medium'] += 1
        else:
            correlations['high'] += 1

    return dict(correlations), anomaly_score  # anomaly_score not used downstream

# State transition simulator with red herring control flags
def update_system_state(initial, events):
    state = initial.copy()
    temp_buffer = []  # unused buffer (distractor)
    flag_log = []
    
    for e in events:
        if 'error' in e:
            state['status'] = 'degraded'
            flag_log.append(e)
        elif 'recovery' in e:
            state['status'] = 'active'
        state['version'] += 0.1  # version drift
    
    # Dead computation block (misleading)
    if len(flag_log) > 2:
        state['quarantined'] = True
    else:
        state['quarantined'] = False

    # This field is never actually used
    state['diagnostics'] = {"log_depth": len(temp_buffer), "flags_seen": len(flag_log)}

    return state

# Core diagnostic aggregator – where the answer originates
def aggregate_metrics(log, flags, sys):
    base_score = len(log) * 17
    penalty = 0
    
    # Relevant conditionals contributing to final result
    if sys['status'] == 'degraded':
        penalty += 95
    if flags['timeout'] > 0:
        penalty += flags['timeout'] * 22
    if flags['checksum'] > 2:
        penalty -= 41  # correction factor
    
    # Critical calculation step
    severity_index = base_score - penalty
    
    # Decoy floating-point distraction
    decay_factor = 0.98 ** len(log)
    adjusted_severity = severity_index * decay_factor  # looks important, but truncated below
    
    # Final integer diagnostic code
    return int(adjusted_severity)

# --- MAIN EXECUTION WITH DISTRACTORS ---

# Simulated input data
batch_sequence = [
    [3, -1, 12, 7, 23],
    [-5, 8, 0, 16],
    [4, 11, 29, 6]
]

event_stream = [
    'ping', 'error_timeout', 'retry_initiated',
    'error_timeout', 'error_checksum', 'error_checksum',
    'error_timeout', 'recovery_2xx'
]

initial_system_state = {
    'node_id': 'NXA-7721',
    'status': 'active',
    'role': 'primary',
    'version': 2.1,
    'diagnostics': {}
}

# STEP 1: Collect telemetry (generates signal log)
timing_log = collect_telemetry(batch_sequence)

# STEP 2: Correlate signals – captures output but only uses part of it
corr_results, score_hint = correlate_signals(timing_log, threshold=13.5)

# Extract meaningful statistics (used later)
failure_flags = {
    'timeout': event_stream.count('error_timeout'),
    'checksum': event_stream.count('error_checksum'),
    'retry_count': len([e for e in event_stream if 'retry' in e])
}

# Introduce irrelevant counter (distractor)
action_counter = Counter(event_stream)

# STEP 3: Update system state (triggers status change)
system_state = update_system_state(initial_system_state, event_stream)

# STEP 4: Compute efficiency (dead end – never used)
efficiency_diagnostic = compute_efficiency_rating(timing_log)

# STEP 5: Generate final diagnostic code (ANSWER GENERATED HERE)
final_diagnostic = aggregate_metrics(timing_log, failure_flags, system_state)

# Output target result
print(f"Target result: {final_diagnostic}")