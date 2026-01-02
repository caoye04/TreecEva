def analyze_pattern(stream, criteria):
    matched = 0
    for item in stream:
        if all((item & mask) == (target & mask) for (mask, target) in criteria):
            matched += 1
    return matched

# Simulated sensor data stream (bit-encoded readings)
data_stream = [0b110101, 0b110011, 0b101101, 0b110111, 0b101010, 0b110101]

# Filter rules: (bitmask, expected_value)
filters = [
    (0b111000, 0b110000),
    (0b000111, 0b000101)
]

# Irrelevant pre-processing: amplitude normalization (dead code path)
normalized = [x / max(data_stream) for x in data_stream]
baseline_shift = sum(normalized) * 0.1
offset_map = {i: round(baseline_shift * i, 3) for i in range(len(normalized))}

# Auxiliary diagnostic function (not used in final computation)
diagnose_health = lambda seq: 'stable' if len(seq) > 4 else 'critical'
status = diagnose_health(data_stream)

# Secondary unused metric
entropy_proxy = sum(1 for x in data_stream if x & 0b101010)

# Core analysis with list comprehension and bitwise logic
active_segments = [x for x in data_stream if (x >> 3) & 0b111 == 0b110]
overlap_count = len(active_segments)

# Key computation
filtration_score = analyze_pattern(data_stream, filters)

# Misleading transformation chain
temp_result = filtration_score ** 2
temp_result -= overlap_count
temp_result += len(offset_map) // 2

# Final output
print(f"Result: {filtration_score}")