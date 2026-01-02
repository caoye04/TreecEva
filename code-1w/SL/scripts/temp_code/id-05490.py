import math

# Simulated sensor data processing pipeline for aerospace telemetry
raw_readings = [3, 7, 1, 9, 2, 8, 4, 6]
offset_compensation = 1.5
scaling_factor = 2.0
calibration_sequence = (5, 3, 8, 1)

# Irrelevant statistical counters (distractors)
decoy_counter_a = 0
decoy_counter_b = 0
auxiliary_metric = 0
shadow_accumulator = 0

# Misleading pre-processing with dead-end logic
temp_buffer = []
for val in calibration_sequence:
    temp_buffer.append(val ** 2 - 2 * val + 1)

# Real signal transformation begins
filtered_readings = []
for x in raw_readings:
    corrected = (x + offset_compensation) * scaling_factor
    if corrected > 8:
        filtered_readings.append(int(corrected))

# Use of enumerate and zip: pairing with dummy indices (partial distractor)
indexed_data = list(enumerate(filtered_readings))
reference_peaks = [10, 12, 14, 16]
paired_deltas = []
for i, (idx, val) in enumerate(indexed_data):
    if i % 2 == 0 and i < len(reference_peaks):
        paired_deltas.append(reference_peaks[i] - val)

# Dummy set operations for interference
unique_deltas = set(paired_deltas)
overlap_check = {1, 2, 3} & unique_deltas
expansion_set = set()
for d in unique_deltas:
    expansion_set.add(d * 3)

# Decoy function that's never called
def legacy_normalization(data):
    global shadow_accumulator
    for item in data:
        shadow_accumulator += math.sqrt(item) if item > 0 else 0
    return [item / max(data) for item in data]

# Unused recursive red herring
def predict_next(value, depth):
    if depth == 0:
        return value
    return predict_next(value * 1.1 + 2, depth - 1)

# Begin actual frame processing chain
intermediate_frames = []
for delta in paired_deltas:
    frame = []
    for i in range(1, 5):
        # Nested logic with conditional expressions
        cell = (delta + i) if (delta + i) % 2 == 0 else (delta + i) // 2
        frame.append(cell)
    intermediate_frames.append(frame)

# Multiple assignments and unpacking (distractor-heavy)
aux_1, aux_2 = 0, 0
for frame in intermediate_frames:
    aux_sum = sum(frame)
    aux_1 += aux_sum
    aux_2 ^= len(frame)

# Real processing: transform frames using bit manipulation and filtering
processed_frames = []
bitmask = 0b1101
for f in intermediate_frames:
    transformed = []
    for v in f:
        # Bitwise operation mixed with arithmetic
        masked_val = (v & bitmask) ^ 2
        if masked_val > 3:
            transformed.append(masked_val * 2)
    if len(transformed) >= 2:
        processed_frames.append(transformed)

# Secondary decoy loop with no impact
aggregation_map = {}
for idx, pf in enumerate(processed_frames):
    if idx not in aggregation_map:
        aggregation_map[idx] = 0
    for num in pf:
        aggregation_map[idx] += num % 3

# Core analysis function with conditional branching
def analyze_signal(frames):
    total_power = 0
    spike_count = 0
    for frame in frames:
        frame_energy = 0
        for reading in frame:
            frame_energy += reading
        if frame_energy > 10:
            spike_count += 1
        total_power += frame_energy * 0.5
    
    # Final diagnostic computation
    baseline_offset = 4.0
    adjustment_factor = 1.25
    diagnostic_score = (total_power + baseline_offset) * adjustment_factor
    
    # Red herring: unused complex expression
    decoy_entropy = 0
    for i in range(1, int(diagnostic_score), 5):
        decoy_entropy += math.log(i) if i > 1 else 0
    
    return int(diagnostic_score)

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)
print(f"Target result: {final_diagnostic}")