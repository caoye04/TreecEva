import itertools

# Simulated sensor data processing with diagnostic routines
def collect_sensor_data():
    raw_ticks = [i for i in range(100, 200) if i % 3 == 0]
    noise_floor = sum([t % 7 for t in raw_ticks[:50]])
    clean_signal = [t for t in raw_ticks if t % 11 != 0]
    return clean_signal

# Irrelevant auxiliary function - dead code path
def deprecated_calibrate(x):
    return (x * 0.97) + 2.1

# Signal conditioning with red herrings
def condition_signal(data):
    shifted = [(d >> 2) for d in data]
    filtered = [s for s in shifted if s > 20]
    checksum = sum(filtered) % 1000
    # Decoy transformation
    inverted = [~f & 0xFF for f in filtered]
    normalized = [round(f / 3.0, 2) for f in filtered]
    return filtered, normalized

# Frame segmentation logic with distraction variables
def segment_frames(signal):
    frames = []
    temp_buffer = []
    for val in signal:
        temp_buffer.append(val)
        if len(temp_buffer) == 5:
            avg_frame = sum(temp_buffer) / 5
            frames.append(avg_frame)
            temp_buffer = []
    # Unused leftover buffer
    residual_energy = sum(temp_buffer) if temp_buffer else 0
    return frames

# Misleading diagnostic routine (not actually used)
def legacy_diagnostic(frames):
    peak = max(frames)
    base = min(frames)
    return (peak - base) * len(frames)

# Core processing chain
processed_data = collect_sensor_data()
signal_core, human_readable = condition_signal(processed_data)
segmented_frames = segment_frames(signal_core)

# Distractor: fake aggregation metrics
aggregation_metrics = {
    'total_power': sum([f**2 for f in segmented_frames]),
    'spectral_entropy': len(set([int(f) for f in human_readable])),
    'temporal_drift': abs(segmented_frames[-1] - segmented_frames[0])
}

# Fake parallel processing simulation
fake_replicas = list(itertools.permutations([1, 2, 3], 3))
dummy_checksum = sum([p[0] + p[2] for p in fake_replicas])

# Actual analysis function buried among distractions
def analyze_signal(frames):
    # Key computation: harmonic coherence index
    weighted_sum = 0
    for i, frame in enumerate(frames):
        weight = (i + 1) ** 1.5
        contribution = frame * weight
        weighted_sum += contribution
    
    # Secondary adjustment based on frame count
    adjustment_factor = len(frames) // 2
    intermediate = int(weighted_sum // 10)
    
    # Final transformation
    final_index = (intermediate ^ adjustment_factor) + 333
    return final_index

# Critical execution point
final_diagnostic = analyze_signal(segmented_frames)

# Print result as required
print(f"Target result: {final_diagnostic}")