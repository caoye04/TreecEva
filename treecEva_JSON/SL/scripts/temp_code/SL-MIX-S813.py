from collections import defaultdict

def process_signal_segment(segment_value):
    adjusted = (segment_value & 0xFF) | ((segment_value >> 8) & 0xFF)
    return adjusted ^ (adjusted >> 4)

signal_segments = [0x1A2B, 0x3C4D, 0x5E6F, 0x7890]
encoding_map = defaultdict(int)
bandwidth_accumulator = 0

for idx, segment in enumerate(signal_segments):
    if segment > 0x3000 and (segment & 0xF0F0) != 0:
        processed = process_signal_segment(segment)
        encoding_map[idx] = processed
        bandwidth_accumulator += processed if processed & 1 else processed >> 1
    else:
        continue

optimized_bandwidth = bandwidth_accumulator
if len(encoding_map) >= 2:
    optimized_bandwidth ^= (encoding_map[1] << 2) & 0xFFFF

print(f"Result: {optimized_bandwidth}")