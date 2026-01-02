import itertools

# System health monitoring simulation with data transformation and pattern analysis

# Raw sensor inputs (simulated)
sensor_a = [1, 0, 1, 1]
sensor_b = [0, 1, 1, 0]
sensor_c = [1, 1, 0, 0]

# Irrelevant calibration constants (distractors)
calib_factor_x = 2.3
calib_factor_y = -1.7
calib_offset_z = 42
temp_threshold = 75.5
voltage_norm = 3.3

# Misleading preprocessing path (dead code - never used)
def deprecated_normalize(data):
    return [x / max(data) for x in data if max(data) > 0]

# Simulate time-series alignment
time_frames = list(itertools.product(sensor_a, sensor_b, sensor_c))

# Transform raw frames into composite signals
composite_signals = []
for frame in time_frames:
    primary = frame[0] ^ frame[1]  # XOR for anomaly detection
    secondary = frame[1] | frame[2] # OR for fault propagation
    tertiary = (frame[0] + frame[2]) % 2  # Parity check
    composite_signals.append((primary, secondary, tertiary))

# Extract sequences for pattern analysis
sequence_x = [s[0] for s in composite_signals]
sequence_y = [s[1] for s in composite_signals]
sequence_z = [s[2] for s in composite_signals]

# Red herring: unused frequency analysis
fft_placeholder = [abs(sum(sequence_x)), abs(sum(sequence_y)), abs(sum(sequence_z))]
noise_floor = sum(fft_placeholder) / len(fft_placeholder)

# Real processing begins: transform sequences using conditional logic
decision_map = [
    1 if x and y else (-1 if not x and z else 0)
    for x, y, z in zip(sequence_x, sequence_y, sequence_z)
]

# Apply moving window sum (window size = 3) with padding
padded_map = [0] + decision_map + [0]
window_sums = [
    padded_map[i] + padded_map[i+1] + padded_map[i+2]
    for i in range(len(decision_map))
]

# Filter significant events
significant_events = [val for val in window_sums if val != 0]

# Secondary transformation: map to diagnostic codes
transformed_data = []
for idx, event in enumerate(significant_events):
    if event > 0:
        transformed_data.append((idx * event) % 7)
    elif event < 0:
        transformed_data.append((-1) * ((idx + event) ** 2 % 5))
    else:
        transformed_data.append(3)

# Dead function - looks important but unused
def compute_entropy(data):
    from math import log
    if not data:
        return 0.0
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [d / total for d in set(data)]
    return -sum(p * log(p, 2) for p in probs if p > 0)

# Another red herring: system status aggregation (unused)
system_flags = {
    'overload': len([x for x in window_sums if x > 2]) > 3,
    'instability': any(abs(w) == 3 for w in window_sums),
    'sync_loss': len(time_frames) % 2 == 1
}

# Critical analysis function
def analyze_pattern(data):
    if not data:
        return -1
    
    # Conditional expression chain with bit manipulation
    base_score = sum(
        (val << 1) ^ idx if val >= 0 else (val >> 1) | idx
        for idx, val in enumerate(data)
    )
    
    # Secondary adjustment using itertools.cycle for phase alignment
    cycle_phases = list(itertools.islice(itertools.cycle([1, -1, 2]), len(data)))
    adjusted_score = sum(
        d * p if d != 0 else 1
        for d, p in zip(data, cycle_phases)
    )
    
    # Final heuristic: combine scores conditionally
    final_weight = len(data) if base_score > 0 else -len(data)
    return base_score + (adjusted_score * final_weight // (abs(final_weight) if final_weight != 0 else 1))

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data)

# Print result as required
print(f"Result: {final_diagnostic}")