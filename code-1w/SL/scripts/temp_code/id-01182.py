def analyze_signal(samples, threshold, gain):
    """Process sensor signal with noise filtering and amplification."""
    amplified = [s * gain for s in samples]
    filtered = [val for val in amplified if abs(val) > threshold]
    shifted = [(x >> 2) for x in filtered if x > 0]  # Only positive values get bit-shifted

    # Irrelevant transformations (distractors)
    inverted_phase = [-v for v in samples[::2]]
    envelope = max(amplified) - min(amplified)
    dummy_bins = [0] * 10
    for idx, val in enumerate(inverted_phase):
        dummy_bins[idx % 10] += int(abs(val)) % 3

    # Unused statistical branches
    if len(filtered) > 5:
        mean_val = sum(filtered) / len(filtered)
        variance_proxy = sum((x - mean_val) ** 2 for x in filtered) / len(filtered)
    else:
        mean_val = 0
        variance_proxy = 0

    # Dead code path — never used
    def legacy_calibrate(x):
        return (x + 1) * 0.9

    # Another red herring: frequency simulation
    cycle_count = 0
    temp_buffer = []
    for i in range(len(amplified) - 1):
        if amplified[i] < 0 <= amplified[i + 1]:
            cycle_count += 1
        temp_buffer.append(abs(amplified[i] - amplified[i + 1]))

    return filtered


def aggregate_metrics(data, offset):
    """Compute weighted diagnostic score from processed data."""
    base = offset
    multiplier = len(data) % 7 if data else 1

    # Complex transformation chain
    squared_sum = sum(x ** 2 for x in data)
    avg_square = squared_sum / len(data) if data else 0
    root_avg = avg_square ** 0.5

    # Distractor: unused peak tracking
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            peaks.append(i)

    # More irrelevant logic
    if len(peaks) > 3:
        peak_values = [data[p] for p in peaks]
        adjustment = sum(peak_values[:2]) / 2
    else:
        adjustment = 0

    # Core calculation (depends on offset and RMS-like value)
    intermediate = root_avg + (base * 0.3)
    final_score = int(intermediate * multiplier)

    # Decoy assignment
    final_score = final_score ^ 0  # No-op XOR

    return final_score

# Simulate system telemetry stream
raw_readings = [0.5, -1.2, 3.4, 2.1, -0.3, 4.5, 1.8, -2.2, 6.1, 0.9]

# Irrelevant pre-processing branch
if any(x < 0 for x in raw_readings):
    normalized = [x / max(abs(min(raw_readings)), abs(max(raw_readings))) for x in raw_readings]
else:
    normalized = raw_readings

# Unused buffer transformation
rotated = normalized[3:] + normalized[:3]
duplicate_check = dict(zip(normalized, rotated))

# Key execution flow
processed_signal = analyze_signal(raw_readings, threshold=1.0, gain=2.5)
baseline_offset = 17

# Critical statement
final_diagnostic = aggregate_metrics(processed_signal, baseline_offset)

print(f"Result: {final_diagnostic}")