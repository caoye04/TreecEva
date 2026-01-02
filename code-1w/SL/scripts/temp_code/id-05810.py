from itertools import cycle, islice

def analyze_signal_integrity(raw_samples):
    # Irrelevant preprocessing: normalize amplitudes (not used in final path)
    normalized = [round(x * 0.987 for x in raw_samples)]  
    threshold = sum(raw_samples) / len(raw_samples)

    # Distractor: complex but unused frequency sweep
    sweep_pattern = list(islice(cycle([1.1, -0.8, 0.3]), len(raw_samples)))
    weighted_sweep = [a * b for a, b in zip(raw_samples, sweep_pattern)]

    # Real logic begins: detect zero-crossings
    zero_crossings = 0
    for i in range(1, len(raw_samples)):
        if raw_samples[i-1] < 0 <= raw_samples[i]:
            zero_crossings += 1

    # Misleading intermediate: entropy-like calculation (dead end)
    entropy_approx = 0
    counts = {}
    for s in raw_samples:
        bucket = int(s * 10) % 5
        counts[bucket] = counts.get(bucket, 0) + 1
    for count in counts.values():
        if count > 0:
            entropy_approx -= (count / len(raw_samples)) * (count / len(raw_samples))

    # Key transformation chain
    filtered = [x for x in raw_samples if abs(x) > 0.5]
    squared_energy = sum(x * x for x in filtered)
    peak_magnitude = max(abs(x) for x in raw_samples)
    sample_rhythm = [i for i, x in enumerate(raw_samples) if x > 0.75]

    # Use enumerate and zip meaningfully in signal phase alignment
    phase_offsets = []
    for idx, val in enumerate(sample_rhythm):
        if idx > 0:
            phase_offsets.append(val - sample_rhythm[idx - 1])

    avg_phase_gap = sum(phase_offsets) / len(phase_offsets) if phase_offsets else 0

    # Decoy function call (has no side effects)
    def compute_harmonic_distortion(signal):
        return sum(abs(x) ** 3 for x in signal) / (sum(abs(x) for x in signal) + 1e-6)

    # Unused recursive red herring
    def recursive_peak_detect(data, depth=0):
        if depth >= 3 or len(data) < 2:
            return 0
        mid = len(data) // 2
        return (1 if data[mid-1] < data[mid] > data[mid+1] else 0) + recursive_peak_detect(data[:mid], depth+1)

    # Core diagnostic metrics
    aggregate_score = (squared_energy * zero_crossings) / (peak_magnitude + 1)
    
    # Correction based on phase regularity (only this affects final result)
    irregularity = abs(avg_phase_gap - round(avg_phase_gap))
    correction_factor = int(irregularity * 1000)

    # Final computation with key variables
    final_diagnostic = aggregate_score + correction_factor

    # Dead code path: obfuscation via alternate model
    backup_model_weighted = 0
    for i, x in enumerate(raw_samples):
        if i % 4 == 0:
            backup_model_weighted += x * 0.5
        elif i % 3 == 0:
            backup_model_weighted -= x * 0.2

    # Print required result
    print(f"Result: {final_diagnostic}")

# Simulated sensor input (deterministic)
raw_data_stream = [0.1, -0.3, 0.8, 1.2, -0.9, 0.6, -1.1, 0.7, 0.85, -0.05, 0.95]
analyze_signal_integrity(raw_data_stream)