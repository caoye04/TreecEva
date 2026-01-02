def analyze_phase_shift(data, threshold):
    """Irrelevant helper function for signal analysis."""
    count = 0
    for val in data:
        if val > threshold:
            count += 1
    return count


def compute_entropy(sequence):
    """Unused function to calculate Shannon entropy."""
    from collections import Counter
    freqs = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for f in freqs.values():
        p = f / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just misleading
    return entropy

# Simulated sensor readings over time (irrelevant data)
sensor_readings = [23.1, 24.5, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3]

# Historical thresholds (unused)
historical_max = max(sensor_readings)
historical_min = min(sensor_readings)
avg_reading = sum(sensor_readings) / len(sensor_readings)

# System event log with timestamps and states
logged_events = [
    {'time': 1, 'state': 'idle', 'temp': 22.0},
    {'time': 2, 'state': 'active', 'temp': 35.1},
    {'time': 3, 'state': 'active', 'temp': 42.3},
    {'time': 4, 'state': 'cooling', 'temp': 38.7},
    {'time': 5, 'state': 'idle', 'temp': 24.0}
]

# Red herring: unused mapping table
state_weights = {
    'idle': 0.1,
    'active': 0.8,
    'cooling': 0.3,
    'error': 0.0
}

# Decoy list comprehension with no side effects
[{'weighted_temp': evt['temp'] * state_weights[evt['state']]} for evt in logged_events if evt['state'] != 'error']

# Another distraction: bit manipulation on timestamps
timestamp_flags = 0
for event in logged_events:
    timestamp_flags ^= event['time'] << 2

# Calibration factor derived from non-obvious but deterministic computation
calibration_factor = 0
for i, event in enumerate(logged_events):
    if event['state'] == 'active':
        calibration_factor += event['temp'] * (i + 1)

# Unused recursive function to add noise
def generate_noise(level, depth):
    if depth <= 0:
        return 0
    return level + generate_noise(level * 0.9, depth - 1)

# Real work begins here — evaluating system thermal dynamics
def evaluate_system_response(events, factor):
    base_capacity = 100.0
    adjustment = 0.0
    temp_changes = []

    # Extract temperature sequence
    temps = [e['temp'] for e in events]
    
    # Compute deltas using enumerate
    for i, t in enumerate(temps):
        if i > 0:
            temp_changes.append(t - temps[i - 1])
    
    # Use zip to pair consecutive changes for interaction effect
    interactions = 0
    for delta_prev, delta_curr in zip(temp_changes, temp_changes[1:]):
        if delta_prev > 0 and delta_curr < 0:
            interactions += 1

    # Main logic path: multiple conditions affect capacity
    active_count = 0
    for e in events:
        if e['state'] == 'active':
            active_count += 1
            if e['temp'] > 40.0:
                adjustment -= 15.0  # Overheat penalty
    
    if active_count >= 2:
        adjustment += 20.0
    
    if interactions >= 1:
        adjustment += 10.5

    # Final capacity calculation
    base_capacity += adjustment
    base_capacity *= (1 + (factor / 1000))

    # Store intermediate result in irrelevant structure
    results_log = {}
    results_log['raw_adjustment'] = adjustment
    results_log['thermal_capacity'] = base_capacity  # Logged but not yet used

    # Return final computed value
    return base_capacity

# Execute critical statement
thermal_capacity = evaluate_system_response(logged_events, calibration_factor)

# Print result as required
print(f"Result: {thermal_capacity}")