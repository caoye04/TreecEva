import itertools

# Simulate sensor array data processing with noise filtering and phase analysis
def analyze_sensor_readings(readings):
    baseline = sum(readings[::2]) / len(readings[::2])  # Irrelevant: even-indexed average
    offset = sum(readings[1::2]) / len(readings[1::2])  # Irrelevant: odd-indexed average
    adjusted = [x - baseline for x in readings]         # Normalize around baseline

    # Compute rolling window averages (distraction)
    windows = [adjusted[i:i+3] for i in range(len(adjusted)-2)]
    smoothed = [sum(w) / len(w) for w in windows]

    # Extract oscillation phases using trigonometric transformation
    phases = []
    for val in adjusted:
        if val >= 0:
            phase = (val ** 0.5) % 3.14159
        else:
            phase = (-((-val) ** 0.5)) % 3.14159
        phases.append(round(phase, 5))

    # Dummy transformation chain (dead path)
    transformed = list(itertools.accumulate(phases, lambda a, b: (a + b) * 0.5))
    normalized_transform = [t % 1.0 for t in transformed]  # Nowhere used

    return phases

# Signal processor that filters based on energy thresholds
def process_signal(phases, threshold):
    # Map phases to cyclic energy levels
    energies = [(1 + (phase / 3.14159)) / 2 for phase in phases]
    
    # Identify high-energy segments
    active_mask = [e > threshold for e in energies]
    
    # Use zip and enumerate to detect onset sequences
    onsets = []
    for i, (energy, active) in enumerate(zip(energies, active_mask)):
        if active and (i == 0 or not active_mask[i-1]):
            onsets.append(i)
    
    # Compute inter-onset intervals (distraction)
    intervals = [onsets[i] - onsets[i-1] for i in range(1, len(onsets))]  # Unused
    avg_interval = sum(intervals) / len(intervals) if intervals else 0   # Red herring

    # Filter phases by activity mask
    filtered = [phases[i] for i, active in enumerate(active_mask) if active]
    
    # Final aggregation: weighted sum based on position (only last value matters)
    cumulative = 0
    for idx, f in enumerate(filtered):
        weight = 1 + (idx * 0.1)
        cumulative += f * weight
    
    # Critical result derived from filtered phases
    final_value = cumulative / len(filtered) if filtered else 0
    
    return round(final_value, 5)

# Generate synthetic signal (reproducible)
raw_readings = [12, -8, 16, -4, 25, -1, 9, -18, 30, -22, 14, -6]

# Step 1: Extract phase information from raw sensor data
detected_phases = analyze_sensor_readings(raw_readings)

# Step 2: Apply threshold-based signal processing
target_level = 0.75
filtered_phase = process_signal(detected_phases, threshold=target_level)

# Misleading secondary computations
baseline_metric = sum(itertools.islice(detected_phases, 0, None, 2))  # Even indices only
auxiliary_score = len([p for p in detected_phases if p > 2.0])  # Decoy metric

# Final output
print(f"Result: {filtered_phase}")