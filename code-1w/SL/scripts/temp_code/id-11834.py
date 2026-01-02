from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for aerospace telemetry
raw_readings = [3241, 872, 5931, 4482, 761, 3823, 6745, 2101, 934, 5055, 3182, 4721]
noise_floor = 987
calibration_offset = 23

# Irrelevant audio processing stub (distractor)
def apply_compression(samples):
    return [s * 0.88 for s in samples[:5]]

# Unused legacy filter (dead code path)
def legacy_filter(x):
    return x & 0x7FF if x > 500 else x

# Signal conditioning with red herring operations
tempered_readings = []
spike_count = 0
for val in raw_readings:
    adjusted = val - noise_floor + calibration_offset
    if adjusted > 4000:
        spike_count += 1
    # Meaningless phase shift (distractor)
    phase_shifted = (adjusted ^ 255) & 4095
    tempered_readings.append(phase_shifted)

# Frame construction with decoy logic
frame_segments = []
segment_buffer = []
for i, tv in enumerate(tempered_readings):
    segment_buffer.append(tv)
    if (i + 1) % 3 == 0 or i == len(tempered_readings) - 1:
        padded = segment_buffer + [0] * (3 - len(segment_buffer))
        frame_segments.append(tuple(padded))
        segment_buffer = []

# Decoy checksum (never used)
for fs in frame_segments:
    checksum = 0
    for item in fs:
        checksum = (checksum ^ item) * 13 % 10007

# Actual relevant processing begins here
processed_frames = []
for frame in frame_segments:
    # Extract and sort values
    sorted_vals = sorted([v for v in frame if v > 0])
    if len(sorted_vals) < 2:
        continue
    # Compute interquartile spread (real work)
    q1 = sorted_vals[len(sorted_vals) // 4]
    q3 = sorted_vals[3 * len(sorted_vals) // 4]
    iqr = q3 - q1
    # Normalize using logarithmic scale
    if iqr > 0:
        normalized_iqr = round(math.log(iqr) * 100, 2)
    else:
        normalized_iqr = 0
    processed_frames.append(normalized_iqr)

# Red herring: frequency analysis on unrelated pattern
frequency_map = defaultdict(int)
for pf in processed_frames:
    bucket = int(pf // 10)
    frequency_map[bucket] += 1
mode_bucket = max(frequency_map, key=lambda k: frequency_map[k])

# Another distraction: simulate packet loss statistics
packet_stats = Counter()
for idx, f in enumerate(frame_segments):
    if sum(f) % 7 == 0:
        packet_stats['dropped'] += 1
    else:
        packet_stats['transmitted'] += 1
loss_ratio = packet_stats['dropped'] / (packet_stats['dropped'] + packet_stats['transmitted'])

# Core diagnostic algorithm (uses processed_frames only)
def analyze_signal(frames):
    if not frames:
        return -1
    # Weighted average with exponential decay
    weighted_sum = 0.0
    decay_factor = 1.0
    total_weight = 0.0
    for i, reading in enumerate(reversed(frames)):
        weight = decay_factor * (0.7 ** i)
        weighted_sum += reading * weight
        total_weight += weight
    # Final transformation
    avg = weighted_sum / total_weight if total_weight > 0 else 0
    # Apply gain and round to nearest integer
    final_score = int(round(avg * 1.618))
    return final_score

# Critical execution point
final_diagnostic = analyze_signal(processed_frames)
print(f"Target result: {final_diagnostic}")