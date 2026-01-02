import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 49, 48]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017]

# Irrelevant auxiliary variables (distractors)
calibration_offset = 0.05
reference_voltage = 3.3
noise_floor_db = -95.7
max_iterations = 1000
temp_log_buffer = []

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    return [x / max(data) for x in data]

# Unused transformation function (decoy)
def frequency_shift(signal, shift=2):
    return [x << shift for x in map(int, signal)]

# Signal conditioning with red herrings
raw_signal_chain = []
for i in range(len(temperature_readings)):
    composite = temperature_readings[i] * 10 + humidity_readings[i]
    if composite > 240:  # Arbitrary threshold (distraction)
        raw_signal_chain.append(composite | 0x1F)
    else:
        raw_signal_chain.append(composite & 0x7F)

# Distractor: unused signal copy
backup_chain = raw_signal_chain.copy()

# Real processing begins here — relevant logic hidden among noise
filtered_signals = list(filter(lambda x: x % 2 == 1, raw_signal_chain))

# Apply scaling based on pressure baseline (key dependency)
baseline_pressure = sum(pressure_readings) / len(pressure_readings)
scale_factor = (baseline_pressure - 1000) / 10

scaled_signals = [int(x * scale_factor) for x in filtered_signals]

# Introduce list comprehension with conditional expression (required feature)
processed_signals = [
    x + 5 if x < 100 else x - 3 
    for x in scaled_signals 
    if x != 0
]

# Another decoy function that's defined but not used
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    return -sum((count / total) * log(count / total) for count in freq.values())

# Critical analysis function with nested logic and early returns
def analyze_readings(signals):
    if not signals:
        return -1
    
    # Compute rolling differences using itertools pairwise (required feature)
    paired_diffs = [b - a for a, b in itertools.pairwise(signals)]
    
    # Filter out small fluctuations (red herring operation)
    significant_changes = [diff for diff in paired_diffs if abs(diff) > 2]
    
    # Accumulate trend score — core of actual computation
    trend_accumulator = 0
    for change in paired_diffs:  # Note: uses full diffs, not filtered
        if change > 0:
            trend_accumulator += int(change ** 0.5)
        elif change < 0:
            trend_accumulator -= 1  # Fixed penalty

    # Secondary adjustment using signal magnitude
    magnitude_factor = sum(abs(s) for s in signals) // len(signals)
    
    # Tertiary logic: check alternating pattern (misleading branch)
    is_oscillating = all(
        signals[i] < signals[i+1] if i % 2 == 0 else signals[i] > signals[i+1]
        for i in range(len(signals)-1)
    )
    oscillation_bonus = 10 if is_oscillating else 0  # Never triggers due to data

    # Final computation (deterministic)
    result = trend_accumulator * 2 + magnitude_factor + oscillation_bonus
    
    # Early return guard (unused path)
    if result < 0:
        return 0
        
    return result

# Execute key statement
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")