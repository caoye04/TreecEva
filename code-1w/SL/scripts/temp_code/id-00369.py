from itertools import compress, cycle

def analyze_signal_pattern(raw_samples):
    # Irrelevant signal processing stub
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.5]
    return sum(filtered[:3])


def generate_reference_map(keys):
    # Dead code path - never used
    ref_map = {}
    for i, key in enumerate(keys):
        ref_map[key] = (i ** 2) % 7
    return ref_map

# Simulated sensor input data
timestamps = list(range(10, 90, 10))
sensor_a = [84, 23, 76, 15, 92, 37, 68, 41]
sensor_b = [51, 73, 29, 88, 14, 67, 35, 94]

# Misleading intermediate aggregations
avg_a = sum(sensor_a) / len(sensor_a)
avg_b = sum(sensor_b) / len(sensor_b)
mean_diff = abs(avg_a - avg_b)

# Distractor: complex-looking but unused bitwise cascade
bit_trail = 0
for val in sensor_a[:4]:
    bit_trail ^= (val << 2) | (val >> 1)

# Real processing begins here
paired_readings = list(zip(sensor_a, sensor_b))
processed_data = []

for idx, (a, b) in enumerate(paired_readings):
    if idx % 2 == 0:
        processed_data.append((a + b) * (idx + 1))
    else:
        processed_data.append(abs(a - b) // (idx + 1))

# Secondary transformation using slicing and cycling
shifted = processed_data[2:] + processed_data[:2]
mask = [i % 3 == 0 for i in range(len(shifted))]
filtered_shift = list(compress(shifted, mask))

double_cycle = list(zip(shifted, cycle(filtered_shift)))
combined_layer = [x ^ y for x, y in double_cycle if x != y]

# Checksum computation chain
running_total = 0
for i, val in enumerate(combined_layer):
    if i % 2 == 0:
        running_total += val * (i + 1)
    else:
        running_total -= val // max(i, 1)

# Final integrity calculation
baseline = sum(processed_data[::3])
correction_factor = len(filtered_shift) / 3 if filtered_shift else 0

# Critical execution point
final_checksum = compute_integrity_value(processed_data)

# Helper function defined after use (distraction via ordering)
def compute_integrity_value(data):
    temp_sum = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            temp_sum += x * 3
        else:
            temp_sum -= x * 2
    # Additional adjustment based on length parity
    if len(data) % 2:
        temp_sum += 17
    return temp_sum % 99991

# Print result for verification
print(f"Result: {final_checksum}")