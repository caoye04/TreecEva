import math

# Simulated sensor data processing with interference
raw_readings = [i * 0.7 for i in range(100)]
offset_calibration = 12.8
scaling_factor = 2.1

# Irrelevant signal smoothing (dead path)
avg_filtered = [sum(raw_readings[i:i+3]) / 3 for i in range(len(raw_readings) - 2)]
temp_buffer = [x + offset_calibration for x in avg_filtered if x > 15]

# Actual processing begins here — but masked by noise above
threshold = 42
primary_signal = [x * scaling_factor for x in raw_readings]
masked_signal = [x for x in primary_signal if x < threshold]

# Bit manipulation decoy (irrelevant)
decoys = []
for i in range(5):
    val = (i << 3) ^ 7
    decoys.append(val)

# Conditional filtering with red herring variables
limit_check = lambda x: x >= 20
flagged = [x for x in masked_signal if limit_check(x)]

# Spurious statistical distraction
mean_val = sum(flagged) / len(flagged) if flagged else 0
deceptive_median = sorted(flagged)[len(flagged)//2] if flagged else 0

# Core logic disguised among distractions
sequence_mask = [(i, x) for i, x in enumerate(flagged) if i % 2 == 0]
processed_magnitudes = [round(math.log(x) ** 2, 4) for i, x in sequence_mask]

# Modular arithmetic mixed with string-based indexing trick (unused)
fake_checksum = 0
reference_tags = ['A', 'B', 'C', 'D', 'E']
for x in processed_magnitudes:
    fake_checksum += int(x) % 5
    fake_checksum %= 10

token_map = {i: reference_tags[fake_checksum % 5] for i in range(3)}  # unused structure

# Real transformation chain
def transform_entry(val):
    if val < 3:
        return val ** 3
    elif val < 6:
        return val * 1.5
    else:
        return val - 2.3

# Distractor: recursive function that is never called
def recursive_denoise(data, depth):
    if depth == 0 or len(data) < 2:
        return data
    return recursive_denoise([0.5 * (data[i] + data[i+1]) for i in range(len(data)-1)], depth-1)

# Critical computation hidden in list comprehension and conditional expression
adjusted_levels = [transform_entry(p) for p in processed_magnitudes if p > 1.8]

# Misleading intermediate aggregation
phantom_total = sum([x for x in adjusted_levels if x < 5]) * 1.1

# Key assignment embedded in complex control flow
final_output = 0
for idx, level in enumerate(adjusted_levels):
    modifier = 1.1 if idx % 3 == 0 else (0.95 if idx % 3 == 1 else 1.05)
    cumulative = level * modifier
    final_output += cumulative

# Redundant print statements as noise
# print(f'Debug: phantom={phantom_total}, mean={mean_val}, median={deceptive_median}')
# print(f'Decoys: {decoys}, Tags: {token_map}')

# Answer is determined here
final_output = process_signals(filtered_data) if 'filtered_data' in locals() else final_output

# Function definitions at the end to obscure flow
def process_signals(data_list):
    base = sum(data_list)
    penalty = len(data_list) * 0.2
    bonus = math.sqrt(base) if base > 10 else 0
    return round(base + bonus - penalty, 4)

# Reassignment of filtered_data late in flow
filtered_data = [x * 1.05 for x in adjusted_levels if x > 2.0]

# Final re-evaluation of final_output using correct data
final_output = process_signals(filtered_data)

print(f"Target result: {final_output}")