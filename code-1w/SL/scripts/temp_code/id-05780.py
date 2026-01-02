import itertools

# Simulated sensor data with noise and redundant fields
data_stream = [18, 22, 15, 30, 12, 25, 10, 8, 40, 5]
noise_filter = lambda x: x > 9

# Irrelevant preprocessing: string-based decoy transformation
decoys = ['A12', 'B22', 'C15', 'D30', 'E12']
label_prefixes = [d[0] for d in decoys]  # Useless extraction
numeric_suffixes = [int(d[1:]) for d in decoys if d[1:].isdigit()]  # Partially used but misleading

# Real processing begins: filter meaningful values
filtered_data = list(filter(noise_filter, data_stream))

# Distractor: dummy shift operations on unrelated bit patterns
temporary_bits = 0b1010101
shifted_mask = (temporary_bits << 3) & 0xFF  # Unused later
inverted_mask = ~shifted_mask & 0xFF  # Dead code path

# Transform: apply non-linear scaling using logarithmic-like growth
transformed_data = []
for val in filtered_data:
    if val % 2 == 0:
        transformed_data.append(int(val * 1.5))
    else:
        transformed_data.append(val ** 2)

# Secondary distraction: unused statistical summary
mean_val = sum(data_stream) / len(data_stream)
std_dev = (sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)) ** 0.5  # Computed but ignored

# Conditional expression chain simulating fault detection
fault_flags = [1 if v > 35 else 0 for v in transformed_data]
fault_count = sum(fault_flags)

# Core logic disguised within a generator expression
running_total = 0
counter_index = 0
for i, group in enumerate(itertools.groupby(transformed_data, key=lambda x: x // 10)):
    group_vals = list(group[1])
    if len(group_vals) >= 2:
        running_total += sum(group_vals) * (i + 1)
    else:
        running_total -= group_vals[0]

# Dummy recursive function (never called)
def recursive_sum(n):
    return n + recursive_sum(n-1) if n > 0 else 0

# Linear search for a condition that mimics calibration check
calibration_point = -1
for idx, num in enumerate(transformed_data):
    if num > 200:
        calibration_point = idx
        break

# Actual final computation
def process_sequence(seq):
    base = 0
    for i, x in enumerate(seq):
        if i % 2 == 0:
            base += x // (i + 1)
        else:
            base -= x % 7
    return base * 2

final_output = process_sequence(transformed_data)
print(f"Target result: {final_output}")