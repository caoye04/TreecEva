def analyze_signal(samples, threshold=0.75):
    normalized = [s / max(samples) for s in samples]
    filtered = [s for s in normalized if s > threshold]
    return len(filtered) * 100 / len(normalized) if filtered else 0.0


def transform_coordinates(coords):
    # Irrelevant geometric transformation (distractor)
    transformed = []
    for x, y in coords:
        rotated_x = x * 0.707 - y * 0.707
        rotated_y = x * 0.707 + y * 0.707
        transformed.append((rotated_x, rotated_y))
    magnitude = sum((x**2 + y**2)**0.5 for x, y in transformed)
    return magnitude

# Simulated sensor data (real input)
sensor_readings = [1024, 384, 512, 896, 256, 768, 640, 128, 896, 512]

# Decoy data structures and operations
fake_dataset = [(i, i*2) for i in range(10)]
temp_analysis = {f'key_{i}': i*15 for i in range(5)}
useless_buffer = bytearray(b'\x00' * 50)

# Real processing begins
baseline_adjusted = [val - 128 for val in sensor_readings if val > 200]
efficiency_ratios = [1.0 / (1 + (val / 512)) for val in baseline_adjusted]

# Bit manipulation chain (mixed paradigm distractor)
crypto_mask = 0b110101
masked_values = []
for idx, val in enumerate(baseline_adjusted):
    masked = (val ^ (idx * 3)) & crypto_mask
    masked_values.append(masked)

# Main diagnostic computation chain
compression_factor = len(sensor_readings) / len(baseline_adjusted) if baseline_adjusted else 0
drift_compensation = sum(1 for a, b in zip(baseline_adjusted, baseline_adjusted[1:]) if b < a)

# Secondary analysis with enumerate (required feature)
outlier_indices = []
for i, val in enumerate(baseline_adjusted):
    if val > 700 and i % 2 == 0:
        outlier_indices.append(i)

# Simulated hardware flags (irrelevant state tracking)
hw_status_flags = [1, 0, 1, 1, 0]
active_channels = sum(hw_status_flags)
latency_offset = active_channels * 1.25

# Core metric calculation
signal_quality = analyze_signal(sensor_readings, threshold=0.6)
consistency_score = len(outlier_indices) * 10

# Data structure mixing: tuple unpacking and zip (required features)
processing_chain = list(zip(enumerate(efficiency_ratios), masked_values))
diagnostics = []
for (idx, ratio), mask in processing_chain:
    if idx % 2 == 0:
        diagnostics.append(ratio * 50 + mask)
    else:
        diagnostics.append(ratio * 30 - mask)

# Final aggregation logic
sum_diagnostics = sum(d for d in diagnostics if d > 10)
weighted_drift = drift_compensation * 17

# Critical statement
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Supporting function (defined late to obscure flow)
def aggregate_metrics(chain, metrics):
    base = sum(metrics) / len(metrics) if metrics else 0
    penalty = len([c for c in chain if isinstance(c, tuple) and c[0][0] % 3 == 0]) * 2.5
    bonus = transform_coordinates([(1, 1), (2, 2), (3, 3)]) * 0.1  # Distractor call
    return (base - penalty + bonus) * compression_factor

# Print result for verification
Result: {final_diagnostic}