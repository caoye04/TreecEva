from collections import defaultdict
import math

# Simulated sensor data aggregation (distractor: not all used)
sensor_readings = [14.2, 18.7, 22.1, 19.5, 25.3, 20.4, 17.8, 23.6]

# Irrelevant preprocessing path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / mean_val for x in data]

# Unused transformation chain
temp_scaled = [math.log(x) ** 2 for x in sensor_readings if x > 15]
weight_map = defaultdict(lambda: 1.0)
for i, val in enumerate(temp_scaled):
    weight_map[i] = val * 0.3 if i % 2 == 0 else val * 0.1

# Real processing begins here — but obscured by noise above
raw_sequence = [8, 3, 12, 7, 14, 5]
mask_pattern = 0b1101

eval_marks = []
for x in raw_sequence:
    # Bitwise masking to derive diagnostic class
    masked = x ^ mask_pattern
    if masked & 0b1000:
        eval_marks.append(masked + 2)
    else:
        eval_marks.append(masked - 1)

# Secondary transformation with red herring variables
shifted_scores = []
decoys = []
baseline_shift = 9
for idx, val in enumerate(eval_marks):
    if idx % 3 == 0:
        shifted_scores.append(val * 2)
    elif idx == 1:
        decoys.append(val)  # unused branch
    else:
        shifted_scores.append(val + 3)

# Core logic buried among distractions
aggregation_key = sum(shifted_scores) % 7

# Fake alternate path (never taken due to fixed input)
if aggregation_key > 10:
    health_signature = math.floor(aggregation_key / 2)
elif aggregation_key < 0:
    health_signature = -aggregation_key
else:
    health_signature = aggregation_key * 5  # This path is taken

# Another layer of irrelevant computation
useless_histogram = defaultdict(int)
for x in [aggregation_key * i - 2 for i in range(5)]:
    useless_histogram[abs(x) % 4] += 1

# Decoy function that looks important but isn't called
def calculate_robustness_index(seq, factor=1.5):
    cnt = Counter(seq)
    return sum(k * v for k, v in cnt.items()) * factor

# Actual final calculation hidden after distractions
baseline_offset = len(useless_histogram.keys())

# Critical statement
final_diagnostic = process_metrics(health_signature, baseline_offset)

# Implementation of required function
def process_metrics(hs, bo):
    temp = hs + (bo * 2)
    temp = temp ^ 0b1010  # bitwise interference
    if temp % 2 == 0:
        temp = int(math.sqrt(temp ** 2 / 2))
    else:
        temp = temp * 3 + 1
    return temp + sum([i for i in range(bo)])

# Print result as required
Result: {final_diagnostic}