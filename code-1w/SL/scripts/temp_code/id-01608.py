import math

# System telemetry and decoy data
telemetry_feed = [14, 7, 22, 5, 93, 12, 8]
decoy_matrix = [[i * j for j in range(4)] for i in range(4)]
scaling_factor = 1.87
offset_correction = -0.33

# Core quantum state buffer (relevant)
quantum_buffer = [
    {'state': 1, 'phase': 0.0, 'magnitude': 4.2},
    {'state': 0, 'phase': 3.14, 'magnitude': 2.1},
    {'state': 1, 'phase': 1.57, 'magnitude': 3.5}
]

# System log with mixed relevant/irrelevant entries
system_log = [
    {'event': 'INIT', 'level': 'INFO', 'timestamp': 1001},
    {'event': 'FLUX_ADJUST', 'level': 'WARN', 'timestamp': 1005},
    {'event': 'STATE_READ', 'level': 'DEBUG', 'timestamp': 1007},
    {'event': 'CORE_STABILIZE', 'level': 'INFO', 'timestamp': 1010}
]

# Irrelevant audio processing stubs
audio_samples = [0.1 * i + 0.05 for i in range(20)]
def process_audio(buf):
    return sum([math.sin(x) for x in buf]) / len(buf)

# Unused transformation chains
def legacy_transform(x):
    return (x ** 2 + 1) // 3

def deprecated_encode(seq):
    return [legacy_transform(n) for n in seq if n % 2 == 1]

# Distractor statistical summary (never used)
bogus_stats = {
    'mean': sum(telemetry_feed) / len(telemetry_feed),
    'max': max(telemetry_feed),
    'min': min(telemetry_feed),
    'range': max(telemetry_feed) - min(telemetry_feed),
    'median': sorted(telemetry_feed)[len(telemetry_feed)//2]
}

# Real processing logic begins here
status_weights = {'INFO': 1, 'WARN': 3, 'ERROR': 5, 'DEBUG': 0}

# Count diagnostic-relevant events
alert_count = 0
event_score = 0
for entry in system_log:
    if entry['event'] != 'INIT':
        alert_count += 1
        event_score += status_weights.get(entry['level'], 1)

# Hidden bit manipulation path (red herring)
crypto_key = 0
for i in range(8):
    crypto_key ^= (i * 13) & (i | 7)
crypto_key = (crypto_key << 3) | (crypto_key >> 5)

# Decoy dictionary accumulation
summary_cache = {}
for item in telemetry_feed:
    key = f"item_{item % 5}"
    if key not in summary_cache:
        summary_cache[key] = 0
    summary_cache[key] += item * 0.7

# Real analysis: compute phase coherence from quantum buffer
coherence = 0.0
active_states = 0
for q in quantum_buffer:
    if q['state'] == 1:
        adjusted_phase = math.cos(q['phase']) ** 2
        coherence += q['magnitude'] * adjusted_phase
        active_states += 1

# Secondary computation: derive stability index from logs
last_timestamp = system_log[-1]['timestamp']
first_timestamp = system_log[0]['timestamp']
duration = last_timestamp - first_timestamp or 1
stability_index = alert_count / (duration + 1)

# Tertiary distractor: unused recursive function
def trace_propagation(depth, val):
    if depth <= 0:
        return val
    return trace_propagation(depth - 1, val ^ (val % (depth + 1)))

unused_trace = trace_propagation(5, 12)

# Critical function that computes the actual answer
def analyze_system_state(buffer, log):
    # Step 1: Base coherence from quantum states
    total_coherence = 0.0
    for q in buffer:
        if q['state'] == 1:
            weight = q['magnitude'] * math.exp(-q['phase'] / 3.14)
            total_coherence += weight
    
    # Step 2: Modify by event impact
    critical_events = 0
    for e in log:
        if e['level'] in ['WARN', 'ERROR']:
            critical_events += 1
    
    # Step 3: Apply damping based on event frequency
    time_span = (log[-1]['timestamp'] - log[0]['timestamp']) or 1
    event_rate = critical_events / time_span
    
    # Step 4: Final integration
    result = total_coherence * (1 - 0.25 * event_rate)
    
    # Step 5: Discretize to integer diagnostic code
    return int(result * 100) // 1

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_buffer, system_log)
print(f"Target result: {final_diagnostic}")