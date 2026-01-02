import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, 1.8, 4.6, 2.1, 5.7, 3.3, 2.9, 4.0, 5.1, 3.6]
baseline_shift = 2.5
calibration_factor = 1.08
noise_floor = 0.4

# Irrelevant auxiliary variables (distractors)
temp_buffer = [0] * len(raw_readings)
scaling_exponent = 1.3
normalization_constant = sum([math.log(x + 1) for x in raw_readings]) / len(raw_readings)
placeholder_matrix = [[i * j for j in range(3)] for i in range(len(raw_readings))]

# Signal preprocessing pipeline
filtered_readings = []
for reading in raw_readings:
    corrected = (reading - baseline_shift) * calibration_factor
    if abs(corrected) > noise_floor:
        filtered_readings.append(max(corrected, 0.1))

# Frame segmentation based on dynamic thresholds (relevant)
adaptive_threshold = sum(filtered_readings) / len(filtered_readings) * 0.7
frames = []
current_frame = []

for idx, value in enumerate(filtered_readings):
    if value > adaptive_threshold:
        current_frame.append(value)
    else:
        if current_frame:
            frames.append(current_frame)
            current_frame = []
if current_frame:
    frames.append(current_frame)

# Dead code path - never executed due to logic above (red herring)
reconstruction_chain = []
for segment in placeholder_matrix:
    integrated = 0
    for elem in segment:
        integrated += math.sin(elem) * scaling_exponent
    reconstruction_chain.append(integrated)  # Unused

# Tuple unpacking and zip usage (required Python feature)
frame_stats = []
for i, frame in enumerate(frames):
    energy = sum([x ** 2 for x in frame])
    duration = len(frame)
    avg_power = energy / duration if duration else 0
    frame_stats.append((i, energy, duration, avg_power))

# Destructuring with enumerate and zip (required features)
indices, energies, durations, powers = zip(*[(idx, e, d, p) for idx, e, d, p in frame_stats])

# Complex conditional aggregation with bit manipulation (mixed paradigm)
consistency_flags = 0
aggregate_diagnostic = 0.0
valid_frame_count = 0

for i, (energy, duration, power) in enumerate(zip(energies, durations, powers)):
    # Bitwise tracking of frame characteristics (energy high, duration odd, power stable)
    flag = 0
    flag |= (1 if energy > 2.0 else 0)
    flag |= (2 if duration % 2 == 1 else 0)
    flag |= (4 if power > 0.5 else 0)
    consistency_flags ^= flag  # XOR accumulation (irrelevant but plausible)

    # Only frames with even index and sufficient energy contribute
    if i % 2 == 0 and energy > 1.5:
        aggregate_diagnostic += power * (duration & 3)  # Bitwise AND with 3
        valid_frame_count += 1

# Decoy function - looks important but unused (distractor)
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

shannon_entropy = compute_entropy(raw_readings)  # Computed but not used

# Final normalization using irrelevant intermediate values (misleading)
theoretical_max = normalization_constant * scaling_exponent
empirical_ratio = aggregate_diagnostic / (valid_frame_count or 1)

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)

# Redefine function to make it self-contained
def analyze_signal(frames_list):
    result = 0.0
    for frame in frames_list:
        peak = max(frame)
        base = min(frame)
        span = peak - base
        if span > 0.5:
            result += span * 10
    return int(result)  # Deterministic integer output

processed_frames = frames  # Assignment at end to simulate delayed binding

# Recompute final_diagnostic after definition
final_diagnostic = analyze_signal(processed_frames)

print(f"Result: {final_diagnostic}")