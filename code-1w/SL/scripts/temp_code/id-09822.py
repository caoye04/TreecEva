import itertools

# Simulated sensor data processing with red herrings and complex transformations
def collect_readings():
    raw_signals = [i * 0.7 for i in range(30)]
    noise_floor = sum([x % 2.3 for x in raw_signals[:10]])
    filtered = [x for x in raw_signals if x > 5.0]
    return filtered

# Irrelevant auxiliary function – dead code path (decoy)
def legacy_calibrate(data):
    adjustment = 0
    for val in data:
        if val > 10:
            adjustment += 0.1
    return [v + adjustment for v in data]

# Unused transformation – misleading intermediate result
def smooth_data(seq):
    smoothed = []
    for i in range(1, len(seq)-1):
        smoothed.append((seq[i-1] + seq[i] + seq[i+1]) / 3)
    return smoothed

# Core logic disguised among distractions
def generate_sequence(base, length):
    sequence = []
    a, b = base, base + 1.1
    for _ in range(length):
        sequence.append(a)
        a, b = b, a + b * 0.1
    return sequence

# Key transformation function used in main flow
def transform_readings(signal):
    shifted = [(x * 1.05) ** 2 for x in signal]
    # Apply windowing effect using itertools.cycle as distraction
    mask = [m for m, _ in zip(itertools.cycle([0.9, 1.0, 1.1]), range(len(shifted)))]
    applied = [s * m for s, m in zip(shifted, mask)]
    return applied

# Diagnostic analyzer – only one that affects final answer
def analyze_pattern(data, threshold):
    count = 0
    running_sum = 0.0
    for val in data:
        if val > threshold:
            count += 1
            running_sum += val
        elif val < threshold * 0.5:
            count -= 1  # rare case, but possible
    return int(running_sum / (count or 1))

# Unused recursive variant – decoy to mislead reasoning
def recursive_count(lst, idx=0, acc=0):
    if idx >= len(lst):
        return acc
    return recursive_count(lst, idx + 1, acc + (1 if lst[idx] > 10 else 0))

# Main execution flow
if __name__ == "__main__":
    # Irrelevant initialization – distractor variables
    calibration_offset = 0.0034
    system_flags = {"debug": False, "legacy_mode": True, "safe_override": False}
    temp_buffer = [0] * 15

    # Real data source
    readings = collect_readings()

    # Generate secondary pattern – appears important but unused
    phantom_sequence = generate_sequence(2.1, 20)
    processed_phantom = [x * 0.8 for x in phantom_sequence if x > 6]

    # Actual transformation chain
    transformed_data = transform_readings(readings)

    # Multiple thresholds computed – only one matters
    avg_val = sum(transformed_data) / len(transformed_data)
    peak = max(transformed_data)
    key_threshold = (avg_val + peak) / 2.5  # critical threshold

    # Final diagnostic calculation – this produces the answer
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)

    # Print result as required
    print(f"Target result: {final_diagnostic}")
