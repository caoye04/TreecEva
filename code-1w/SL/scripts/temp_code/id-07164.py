from collections import defaultdict
from itertools import cycle

# Simulate sensor data stream with timestamps and readings
timestamps = [101, 102, 103, 104, 105, 106, 107, 108]
raw_readings = [23.4, 24.1, 22.9, 25.6, 26.3, 24.8, 23.9, 25.1]

# Irrelevant auxiliary data (distractor)
status_flags = ['OK', 'OK', 'WARN', 'OK', 'ERROR', 'OK', 'OK', 'OK']
flag_counter = defaultdict(int)
for flag in status_flags:
    flag_counter[flag] += 1

# Misleading preprocessing step (partially unused)
normalized = []
for val in raw_readings:
    if val > 25.0:
        normalized.append(round(val * 0.98, 2))
    else:
        normalized.append(round(val * 1.02, 2))

# Core processing: extract anomalies based on rolling threshold
anomalies = []
moving_avg_window = []
for reading in raw_readings:
    moving_avg_window.append(reading)
    if len(moving_avg_window) > 3:
        moving_avg_window.pop(0)
    
    if len(moving_avg_window) == 3:
        avg = sum(moving_avg_window) / 3
        if abs(reading - avg) > 1.5:
            anomalies.append(reading)

# Secondary transformation: map anomalies to quantized levels
quantized_anomalies = []
for a in anomalies:
    level = int((a - 20) * 2)  # Scale for discretization
    quantized_anomalies.append(level)

# Distractor loop: computes unused statistics
histogram = defaultdict(int)
for q in quantized_anomalies:
    histogram[q] += 1

# Tuple-based encoding of anomaly events
encoded_events = []
for i, q in enumerate(quantized_anomalies):
    encoded_events.append((i, q, q % 3))

# Real computation begins: process only even-indexed encoded events
processed_data = []
event_cycle = cycle([1, -1])
for idx, (pos, val, mod) in enumerate(encoded_events):
    if pos % 2 == 0:
        shift = next(event_cycle)
        processed_data.append((val + shift) * 10)

# Checksum function using modular arithmetic and string methods (red herring inclusion)
def compute_checksum(data_list):
    base_str = ''.join(str(d) for d in data_list)
    digit_sum = sum(int(d) for d in base_str if d.isdigit())
    
    # Extra distraction: use string operations that don't affect final logic
    padded = base_str.ljust((len(base_str) + 3) // 4 * 4, '0')
    chunks = [padded[i:i+4] for i in range(0, len(padded), 4)]
    chunk_sums = [sum(int(x) for x in chunk) for chunk in chunks]
    
    # Actual checksum logic
    total = 0
    for i, num in enumerate(data_list):
        total += num * (i + 1)
    return total % 97

# Final computation
final_checksum = compute_checksum(processed_data)

print(f"Result: {final_checksum}")