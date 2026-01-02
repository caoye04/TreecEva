import math

# Simulated sensor array data with noise and calibration offsets
data_stream = [127, 255, 64, 192, 32, 224, 16, 96]
calibration_map = {i: val * 0.95 for i, val in enumerate(data_stream)}

# Irrelevant backup buffer (distractor)
backup_buffer = [x ^ 0xFF for x in data_stream][::-1]

# Apply non-uniform scaling based on position (relevant transformation)
scaled_data = [data_stream[i] * 0.8 + (i * 2.5) for i in range(len(data_stream))]

# Noise filtering using moving window average (red herring - not used later)
filtered_data = []
for i in range(2, len(scaled_data) - 2):
    window_avg = sum(scaled_data[i-2:i+3]) / 5
    filtered_data.append(window_avg)

# Key transformation: apply bitwise mask and logarithmic compression
transformed_data = [
    int((x & 0b111111) * math.log(x + 1)) if x > 30 else int(x ** 0.5)
    for i, x in enumerate(scaled_data)
]

# Decoy function that looks important but is never called
def analyze_integrity(buf):
    crc = 0
    for b in buf:
        crc ^= b << 1
        crc &= 0xFFFF
    return crc == 0x1D0F

# Threshold logic based on dynamic condition (used later)
threshold_func = lambda x: x > 45 and (x % 7 != 0)

# Auxiliary diagnostic flags (some are misleading)
anomaly_flags = [\n    transformed_data[i] < 40 for i in range(0, len(transformed_data), 2)\n]
spike_detected = any([transformed_data[i] > 120 for i in range(len(transformed_data))])
consistency_check = len(transformed_data) == len(data_stream)

# Complex conditional expression with slicing and lambda (core logic)
validation_score = (
    sum(transformed_data[1::2]) / len(transformed_data[1::2])
    if spike_detected else
    sum(transformed_data[::2]) / len(transformed_data[::2])
) if anomaly_flags.count(True) < 3 else 0

# Secondary processing with nested list comprehension and bit manipulation
processed_pairs = [
    ((a ^ b) >> 1) + (a & 0b111)
    for a, b in zip(transformed_data, transformed_data[1:] + [transformed_data[0]])
    if (a + b) % 5 == 0
]

# Dead code path - looks like fallback but is unreachable (distractor)
if validation_score < 10:
    processed_pairs = [p * 2 for p in processed_pairs]
elif len(processed_pairs) == 0:
    processed_pairs = [100]  # never executed

# Final aggregation using conditional logic and lambda filtering
effective_metrics = list(filter(
    lambda x: x != 0 and (x & (x - 1) == 0),  # keep powers of two
    [int(validation_score)] + processed_pairs
))

def process_metrics(metrics, threshold):
    base = sum(m for m in metrics if threshold(m))
    bonus = 10 if len(metrics) > 3 else 0
    penalty = 25 if base > 200 else 0
    return base + bonus - penalty

# Execution point of interest
final_diagnostic = process_metrics(transformed_data, threshold_func)

print(f"Result: {final_diagnostic}")