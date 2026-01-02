import itertools

# Simulated sensor array data (hex-encoded readings)
sensor_packets = [
    'A3E4', 'B2F7', 'C1D9', '90E3', 'F5A1',
    'D4C6', 'E7B8', '8A2F', '3K9L', 'X5Y2'
]

# Irrelevant backup configuration
backup_thresholds = {
    'temp': 75.5,
    'pressure': 101.3,
    'humidity': 45.0
}

# Data cleansing: filter valid hex strings (distractor: some invalid entries)
clean_packet = lambda x: all(c in '0123456789ABCDEF' for c in x)
filtered_data = [p for p in sensor_packets if clean_packet(p)]

# Decoy function – never called
def legacy_decode(data):
    return sum(int(d[:2], 16) for d in data if d.startswith('A'))

# Calibration map using dictionary and bit manipulation
calibration_map = {i: (i ^ 21) & 15 for i in range(16)}
calibration_key = sum(int(c) for c in '7341')  # red herring sum: 15

# Auxiliary transformation (partially relevant)
def hex_to_diagnostic(s):
    val = int(s, 16)
    a = (val >> 8) & 0xF
    b = val & 0xF
    c = (val >> 4) & 0xF
    # Complex but partially irrelevant transformation chain
    x = calibration_map[a] * 3
    y = calibration_map[b] + 7
    z = calibration_map[c] ** 2
    return (x - y) ^ z  # actual contribution to result

# Another decoy: unused data structure
diagnostic_tree = {
    'nodes': [
        {'id': 1, 'payload': lambda: hex_to_diagnostic('A3E4')},
        {'id': 2, 'payload': lambda: None}  # dead code
    ]
}

# Real processing function
processed_values = []
for packet in filtered_data:
    code_sum = sum(ord(c) for c in packet) % 100  # distraction
    diagnostic_score = hex_to_diagnostic(packet)
    if diagnostic_score > 10:
        processed_values.append(diagnostic_score)

# Secondary filtering based on frequency (using itertools)
freq_counter = {}
for v in processed_values:
    freq_counter[v] = freq_counter.get(v, 0) + 1

top_pairs = list(itertools.combinations(freq_counter.keys(), 2))
relevance_score = sum(abs(a - b) for a, b in top_pairs[:3]) if len(top_pairs) >= 3 else 0

# Final computation path
aggregated = sum(processed_values) // len(processed_values) if processed_values else 0
dynamic_offset = len(filtered_data) * 3

# Key statement
final_diagnostic = process_readings(filtered_data, calibration_key) if 'process_readings' in globals() else aggregated + dynamic_offset

# Correction: define the missing function (was referenced before definition - now fixed)
def process_readings(data_list, key):
    base = 0
    for item in data_list:
        high_nibble = int(item[0], 16)
        low_nibble = int(item[-1], 16)
        # Use lambda in non-trivial way
        transform = lambda x, k: (x + k) ^ (k % 7)
        base += transform(high_nibble, key) * transform(low_nibble, key)
    return base + relevance_score

# Recompute final_diagnostic after function definition
final_diagnostic = process_readings(filtered_data, calibration_key)

print(f"Result: {final_diagnostic}")