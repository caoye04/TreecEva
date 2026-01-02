import math

# Simulated system telemetry and diagnostic processing pipeline
def analyze_signal_strength(signal_data, threshold=0.75):
    strong_signals = [s for s in signal_data if abs(s) > threshold]
    return len(strong_signals) / len(signal_data) if signal_data else 0


def compute_phase_shift(frequency, time_offset):
    # Irrelevant trigonometric computation (distractor)
    return math.sin(2 * math.pi * frequency * time_offset)


def evaluate_harmonic_integrity(harmonics):
    total_power = sum([h ** 2 for h in harmonics])
    fundamental = harmonics[0] if harmonics else 1
    distortion_ratio = (total_power - fundamental ** 2) / total_power if total_power else 0
    return distortion_ratio < 0.15

# Unused recursive function - dead code path (red herring)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Misleading intermediate calculation with decoy variables
temp_calibration = 0
for i in range(5):
    temp_calibration += (i * 0.1) ** 2

baseline_reference = 1.85
adjusted_threshold = baseline_reference * 0.92

# Real data inputs
timing_log = [0.12, 0.33, 0.41, 0.76, 0.81, 0.94, 0.25, 0.68, 0.77]
system_flags = [True, False, True, True, False]

# Decoy list comprehensions and set operations (partial distractors)
redundant_pairs = [(x, y) for x in range(3) for y in range(2)]
flag_combinations = set(tuple(sorted(p)) for p in zip(system_flags, system_flags[1:]))

# Simulate auxiliary signal with no impact on final result
auxiliary_signal = []
for idx, val in enumerate(timing_log):
    shifted = val + 0.05 * math.cos(idx)
    auxiliary_signal.append(shifted)

# Spurious bit manipulation (irrelevant to outcome)
bit_analysis = 0
for i in range(len(timing_log)):
    bit_analysis ^= i << 2
    bit_analysis |= 0x0F

# Core logic disguised among distractions
def extract_temporal_anomalies(log, window_size=3):
    anomalies = []
    for i in range(len(log) - window_size + 1):
        window = log[i:i+window_size]
        avg = sum(window) / window_size
        if abs(window[1] - avg) > 0.1:
            anomalies.append(i)
    return anomalies

anomaly_indices = extract_temporal_anomalies(timing_log)

# Critical path begins here — meaningful computation chain
def generate_diagnostics(log, flags):
    # Step 1: Filter values above adjusted threshold
    active_windows = [v for v in log if v > adjusted_threshold]
    
    # Step 2: Map flag states with enumeration (key python idiom)
    flagged_events = []
    for i, flag in enumerate(flags):
        if i < len(active_windows) and flag:
            flagged_events.append(active_windows[i])
    
    # Step 3: Use zip to align diagnostics (pythonic pattern)
    paired_diagnostics = []
    for val, idx in zip(flagged_events, anomaly_indices[:len(flagged_events)]):
        score = val * (idx + 1) * 100
        paired_diagnostics.append(score)
    
    # Step 4: Aggregate using conditional logic
    aggregate = 0
    for d in paired_diagnostics:
        if d > 150:
            aggregate += int(d // 3)
        else:
            aggregate += int(d // 4)
    
    return aggregate

# Secondary distraction: unused complex transformation
decoy_magnitude = sum(math.log(1 + abs(x)) for x in timing_log if x > 0.5)

# Another red herring function involving set theory
def compute_coverage(log):
    rounded = [round(x, 1) for x in log]
    unique = set(rounded)
    expected = set([round(0.1 * i, 1) for i in range(1, 10)])
    return len(unique & expected)

coverage_index = compute_coverage(timing_log)  # Computed but unused

# Main aggregation function that determines answer
def aggregate_metrics(log, flags):
    # Step 1: Analyze signal strength (real dependency)
    signal_quality = analyze_signal_strength(log)
    
    # Step 2: Get raw diagnostic value from meaningful chain
    base_diagnostic = generate_diagnostics(log, flags)
    
    # Step 3: Apply harmonic validation (triggers inclusion)
    valid_harmonics = evaluate_harmonic_integrity([0.5, 0.1, 0.08, 0.03])
    
    # Step 4: Conditional amplification based on validation
    amplified = base_diagnostic * 2 if valid_harmonics else base_diagnostic
    
    # Step 5: Adjust by signal quality ratio
    adjusted = amplified * (signal_quality * 100)
    
    # Step 6: Floor to nearest integer
    final = int(adjusted)
    
    return final

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Output result as required
print(f"Target result: {final_diagnostic}")