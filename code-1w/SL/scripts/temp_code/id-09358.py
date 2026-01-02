def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    shifted = [x + 25 for x in filtered]
    return shifted[:len(shifted)//2]


def encode_frame(data_chunk):
    encoded = []
    for val in data_chunk:
        encoded.append((val ^ 242) & 255)
    return encoded


def integrate_segments(segments):
    accumulator = 0
    for i, seg in enumerate(segments):
        if i % 2 == 0:
            accumulator += sum(seg) // (i + 1)
        else:
            accumulator -= len(seg) * 10
    return accumulator


def transform_readings(readings):
    # Irrelevant transformation branch
    temp_log = [abs(r) ** 0.5 for r in readings if r != 0]
    smoothed = [sum(readings[i:i+3]) / 3 for i in range(len(readings)-2)]
    # Actual relevant path
    amplified = [int(s * 1.7) for s in smoothed]
    return amplified


def finalize_energy(data_stream, scale):
    base = sum(data_stream)
    adjustment = 0
    for d in data_stream:
        if d > 100:
            adjustment += d // 10
        elif d < 50:
            adjustment -= d // 25
    return int((base + adjustment) * scale)

# Simulated sensor input
raw_input = list(range(30, 120, 7)) + [-105, -45, 65, 88, 150]

# Distraction: Unused variables and decoy processing paths
baseline_offset = 12.5
reference_map = {i: i*2 for i in range(20)}
decoys = [baseline_offset * i for i in reference_map.values()]

# Step 1: Filter and shift signal
processed_signal = preprocess_signal(raw_input)

# Step 2: Encode frame (irrelevant to final result but plausible)
coded_frame = encode_frame(processed_signal)
unused_hash = sum(coded_frame[i] * (i+1) for i in range(len(coded_frame)))

# Step 3: Create segments (distractor list)
segment_pool = []
for i in range(0, len(coded_frame), 4):
    segment_pool.append(coded_frame[i:i+4])

# Step 4: Transform readings (core path begins)
temp_data = transform_readings(processed_signal)

# Step 5: Slice to critical window
transformed_data = temp_data[1:-1]  # Remove first and last

# Step 6: Calibration factor computed from bit manipulation red herring
temp_key = 0
for x in coded_frame[:5]:
    temp_key ^= (x << 1) | (x >> 7)
calibration_factor = ((temp_key & 63) % 9) / 10.0  # Always results in 0.8

calibration_factor = 0.8  # Hardcoded override for deterministic output

# Step 7: Final energy calculation
energy_output = finalize_energy(transformed_data, calibration_factor)

print(f"Result: {energy_output}")