import itertools

# Simulated sensor data processing for aerospace telemetry
raw_readings = [0.7, 1.2, 0.3, 1.8, 2.1, 0.9, 1.4, 2.5]
base_frequency = 42.0
time_stamps = [0.1 * i for i in range(len(raw_readings))]

# Irrelevant auxiliary variables (distractors)
calibration_offset = 0.042
redundant_buffer = [0] * len(raw_readings)
system_flag = True
legacy_mode = False
checksum_lookup = {i: i ^ 2 for i in range(10)}

# Real processing begins here
filtered_readings = [x for x in raw_readings if x > 0.5]
scaled_readings = [round(x * base_frequency, 3) for x in filtered_readings]

# Frame construction with zip and enumerate (relevant)
indexed_frames = list(enumerate(zip(time_stamps, raw_readings), start=1))
processed_frames = []

for idx, (t, val) in indexed_frames:
    if idx % 2 == 0:
        # Even frames undergo transformation
        transformed = val * 3.1 + 0.05
    else:
        # Odd frames are preserved but tagged
        transformed = val
    processed_frames.append((idx, t, transformed))

# Dead code path - never executed due to system_flag logic (misleading)
if legacy_mode and system_flag:
    backup_result = sum(redundant_buffer)
    for k in checksum_lookup:
        backup_result += k * calibration_offset
else:
    pass  # Placeholder - distractor

# Bit manipulation red herring (irrelevant to final result)
status_word = 0b110101
status_word ^= 0b111111
parity_check = bin(status_word).count('1') % 2

# Decoy function that looks important but isn't used
def compute_legacy_metric(data):
    return sum(d ** 2 for d in data) / len(data) if data else 0

# Real analysis function
def analyze_signal(frames):
    # Extract only the third component (transformed values)
    signals = [frame[2] for frame in frames]

    # Use itertools to group consecutive similar magnitudes
    grouped = []
    for key, group in itertools.groupby(signals, key=lambda x: x >= 1.0):
        grouped.append((key, len(list(group))))

    # Set operation: find unique signal characteristics
    unique_caps = set(int(s * 10) // 10 for s in signals)  # truncate to nearest 0.1

    # Complex conditional logic chain (6 steps)
    accumulator = 0
    for i, (is_high, count) in enumerate(grouped):
        if is_high and count >= 2:
            accumulator += 17 * (i + 1)
        elif not is_high and i % 2 == 1:
            accumulator -= 5
        else:
            accumulator += 3

    # Final computation involving set size and accumulated pattern
    adjustment = len(unique_caps) * 0.5
    intermediate = accumulator * 1.1

    # Introduce a tuple-based dispatch (red herring)
    mode_dispatch = {'A': 1.0, 'B': 0.9, 'C': 1.2}
    selected_mode = 'X'  # Invalid key - fallback used
    multiplier = mode_dispatch.get(selected_mode, 1.05)

    # Actual answer computation
    final_value = intermediate + adjustment
    return int(final_value * 1000) / 1000  # round to 3 decimals

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)

# Print result as required
print(f"Result: {final_diagnostic}")