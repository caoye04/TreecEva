import math

# Simulated quantum sensor readings over time
temporal_readings = [3, 7, 1, 9, 4, 8, 2]

# System event log with timestamps and status flags
system_logs = [
    {'time': 1623456000, 'event': 'startup', 'critical': False},
    {'time': 1623456060, 'event': 'pulse_init', 'critical': True},
    {'time': 1623456120, 'event': 'sync_fail', 'critical': True},
    {'time': 1623456180, 'event': 'realign', 'critical': False}
]

# Irrelevant astronomical constants (distractor)
planck_length = 1.616e-35
light_speed_mps = 186282

# Legacy calibration factors from deprecated module (dead code path)
calibration_v1 = {'a': 0.5, 'b': 1.2, 'c': 3.0}
def apply_legacy_calib(x):
    return x * calibration_v1['a'] + calibration_v1['b']

# Quantum state sequence derived from temporal readings
quantum_sequence = []
for val in temporal_readings:
    if val % 2 == 0:
        quantum_sequence.append(int(math.pow(val, 2) / 2))
    else:
        quantum_sequence.append(int(math.sqrt(val ** 3)))

# Decoy function: looks important but unused
def compute_entropy(data):
    entropy = 0.0
    total = sum(data)
    for x in data:
        prob = x / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

# Auxiliary diagnostic map (red herring)
diagnostic_map = {
    'voltage': [110, 115, 120],
    'phase_shift': 45,
    'tolerance_window': (0.05, 0.95),
    'checksum_history': {1, 2, 4, 8, 16}
}

# Unused bit manipulation routine (distractor)
def scramble_bits(n):
    n = ((n << 3) & 0xFF) | (n >> 5)
    n ^= 0xA7
    return n & 0xFF

# Core analysis engine
status_weights = {'critical': 3, 'warning': 1, 'info': 0}

# Historical weights (misleading intermediate values)
historical_weights = {
    'v1': {'critical': 2, 'warning': 1},
    'v2': {'critical': 4, 'warning': 0},  # This one is never used
    'v3': {'critical': 3, 'warning': 1}
}

# Simulate fault propagation matrix (complex distraction)
fault_matrix = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i != j:
            fault_matrix[i][j] = (i + j) % 4

# Real-time anomaly scoring
anomaly_scores = []
for entry in system_logs:
    base_score = 1
    if entry['critical']:
        base_score *= 3
    if 'fail' in entry['event']:
        base_score *= 2
    anomaly_scores.append(base_score)

# Compute aggregated risk level (intermediate, partially relevant)
risk_level = sum(anomaly_scores) * len([x for x in temporal_readings if x > 5])

# Character frequency map in events (seemingly relevant but not directly used)
event_chars = {}
for entry in system_logs:
    for c in entry['event']:
        event_chars[c] = event_chars.get(c, 0) + 1

# Conditional expression chain with nested logic
trigger_condition = any(
    math.log(entry['time']) > 21.2 and entry['critical']
    for entry in system_logs
)

# Key processing function
threshold_reference = 7


def evaluate_coherence(seq):
    coherence = 0
    for i in range(1, len(seq)):
        diff = abs(seq[i] - seq[i-1])
        if diff > threshold_reference:
            coherence -= 1
        else:
            coherence += 2
    return max(coherence, 0)


def count_critical_events(logs):
    return sum(1 for e in logs if e['critical'])


def analyze_system_state(q_seq, logs):
    # Step 1: Base integrity from quantum sequence sorting
    sorted_qs = sorted(q_seq)
    integrity = sorted_qs[2] if len(sorted_qs) > 2 else 0  # Third smallest

    # Step 2: Event-derived multiplier
    critical_count = count_critical_events(logs)
    multiplier = 2 if critical_count >= 2 else 1

    # Step 3: Coherence bonus
    coherence_bonus = evaluate_coherence(q_seq)

    # Step 4: Apply combinatoric adjustment based on even/odd pattern
    even_count = sum(1 for x in q_seq if x % 2 == 0)
    odd_count = len(q_seq) - even_count
    combinatoric_factor = math.comb(even_count + 1, min(odd_count, 3)) if even_count >= odd_count else 1

    # Step 5: Final integration
    raw_diagnostic = (integrity * multiplier) + coherence_bonus
    
    # Step 6: Final adjustment (key execution point)
    final_diagnostic = raw_diagnostic * combinatoric_factor
    
    return int(final_diagnostic)

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_sequence, system_logs)

# Print result as required
print(f"Target result: {final_diagnostic}")