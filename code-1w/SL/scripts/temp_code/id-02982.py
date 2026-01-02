from collections import defaultdict
from itertools import cycle

# Simulated sensor data processing with checksum validation
def process_sensor_data(raw_frames):
    frame_stats = defaultdict(int)
    temp_buffer = []
    rolling_hash = 0
    data_sum = 0
    correction_factor = 1.05
    baseline_offset = 25
    decay_rate = 0.9

    # Irrelevant statistical tracking
    outlier_count = 0
    smoothed_values = []
    history_log = []

    for i, frame in enumerate(raw_frames):
        if len(frame) < 4:
            continue

        # Real computation: sum relevant payload bytes
        payload = frame[1:-1]  # Exclude header and footer
        frame_data_sum = sum(payload)
        data_sum += frame_data_sum

        # Update statistics (distractor)
        frame_stats['total_frames'] += 1
        frame_stats['byte_volume'] += len(frame)

        # Rolling hash (red herring)
        for b in frame:
            rolling_hash = (rolling_hash * 31 + b) % 10007

        # Smoothing algorithm (dead path)
        avg_val = sum(frame) / len(frame)
        if abs(avg_val - baseline_offset) > 10:
            outlier_count += 1
        else:
            smoothed = avg_val * correction_factor
            smoothed_values.append(smoothed)
            baseline_offset = decay_rate * baseline_offset + (1 - decay_rate) * smoothed

        # Buffer manipulation (irrelevant)
        temp_buffer.extend(payload)
        if len(temp_buffer) > 16:
            temp_buffer = temp_buffer[-8:]

        # History logging (decoy)
        history_log.append({
            'index': i,
            'size': len(frame),
            'sum': frame_data_sum
        })

    # Complex mask generation with bit manipulation (partially relevant)
    prime_seed = 65537
    mask = 0
    for shift in [1, 3, 7]:
        mask |= (prime_seed >> shift) & 0xFF
    
    # Apply XOR and bitmask (critical execution point)
    checksum = (data_sum ^ mask) & 0xFFFF

    # Unused derived values (distractors)
    inverted_checksum = (~checksum) & 0xFFFF
    checksum_shift_chain = (checksum << 5) ^ (checksum >> 3)
    final_diagnostic = len(smoothed_values) + frame_stats['total_frames']

    # Dead code branches
    if False:
        debug_dump = {
            'raw': raw_frames,
            'buffer': temp_buffer,
            'hash': rolling_hash
        }
    
    if len(history_log) > 100:
        aggregate = sum(len(entry['size']) for entry in history_log)
    
    return checksum

# Input data - deterministic sensor frames
sensor_frames = [
    [0xAA, 0x12, 0x34, 0x56, 0xFF],
    [0xAA, 0x23, 0x45, 0x67, 0xFF],
    [0xAA, 0x34, 0x56, 0x78, 0xFF],
    [0xAA, 0x45, 0x67, 0x89, 0xFF]
]

# Execute and print result
current_checksum = process_sensor_data(sensor_frames)
print(f"Result: {current_checksum}")