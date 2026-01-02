from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant readings
data_stream = [
    (1, 'A', 105), (2, 'B', 110), (3, 'A', 95), (4, 'C', 120), (5, 'B', 115),
    (6, 'A', 100), (7, 'D', 130), (8, 'C', 125), (9, 'B', 108), (10, 'A', 90),
    (11, 'E', 140), (12, 'D', 135), (13, 'C', 118), (14, 'B', 112), (15, 'A', 97)
]

# Irrelevant mapping - distractor
type_map = {'A': 'Type1', 'B': 'Type2', 'C': 'Type3', 'D': 'Type4', 'E': 'Type5'}

# Noise threshold filter - partially relevant but overcomplicated
def is_valid_reading(value, min_val=90, max_val=135):
    return min_val <= value <= max_val

# Decoy function - never called
def analyze_trend(data):
    return sum(x[2] for x in data) / len(data)

# Another decoy: complex but unused statistical transform
def entropy_score(values):
    from math import log
    freq = Counter(values)
    total = len(values)
    return -sum((count/total) * log(count/total) for count in freq.values())

# Signal grouping with distraction logic
grouped = defaultdict(list)
for seq, typ, val in data_stream:
    if is_valid_reading(val):
        grouped[typ].append(val)

# Misleading aggregation - looks important but unused later
total_energy = 0
for k in grouped:
    total_energy += sum(v**1.1 for v in grouped[k])

# Extract only type 'A' and 'B' signals - actual relevant filtering
filtered_data = []
for seq, typ, val in data_stream:
    if typ in ['A', 'B'] and is_valid_reading(val):
        filtered_data.append(val)

# Red herring: string-based analysis on numeric context (never used)
diagnostic_tag = "SIGMON-2023"
if diagnostic_tag.startswith("SIG") and diagnostic_tag.endswith("2023"):
    debug_mode = True
else:
    debug_mode = False

# Core processing function with conditional expression
def process_signals(values):
    base = sum(values)
    # Apply conditional offset based on parity and length
    adjustment = 10 if len(values) % 2 == 0 else -5
    # Bit manipulation twist: use XOR to scramble then unscramble logic
    magic_key = 0b1101
    masked_base = base ^ magic_key
    unmasked_base = masked_base ^ magic_key  # Restores original
    # Final transform with tuple unpacking and set deduplication
    unique_vals = list(set(values))
    sorted_vals = sorted(unique_vals, reverse=True)
    # Simulate weighted importance: top two values get extra weight
    if len(sorted_vals) >= 2:
        weighted_boost = (sorted_vals[0] // 10) + (sorted_vals[1] // 10)
    else:
        weighted_boost = 0
    # Distractor loop: modifies local scope only
    temp = 0
    for _ in range(3):
        temp += 7
        continue  # Early break red herring
        temp = 999  # Dead code
    # Actual output computation
    result = unmasked_base + adjustment + weighted_boost
    return result

# Key execution point
final_output = process_signals(filtered_data)
print(f"Result: {final_output}")