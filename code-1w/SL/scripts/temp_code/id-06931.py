import itertools

# Simulate multi-stage signal processing with financial weighting
raw_signals = [0.5, 1.2, -0.3, 4.1, 2.7, -1.8, 3.0]
filtered = [x for x in raw_signals if abs(x) > 0.4]
weights = [round(1 / (1 + x**2), 4) for x in filtered]

# Irrelevant transformation chain (distractor)
dummy_map = list(map(lambda x: x * 0.95, weights))
decoys = [w * 1.1 for w in dummy_map if w < 0.5]
decoys.append(sum(decoys) / len(decoys)) if decoys else None

# Real computation begins: weighted sequence analysis
cumulative = 0
weighted_sequence = []
for i, w in enumerate(weights):
    cumulative += w * (i + 1)
    weighted_sequence.append(round(cumulative, 4))

# Secondary irrelevant path: bit manipulation red herring
bit_flags = 0
for val in raw_signals[:3]:
    bit_flags ^= int(abs(val) * 10) & 0xFF
status_mask = bit_flags | 0x0A
flag_check = (status_mask >> 4) & 1

# Control flow distraction with early exit that isn't taken
temporary_holdings = []
for w in weights:
    adj = w * 1.05
    if adj > 1.0:
        temporary_holdings.append(adj)
        break
    temporary_holdings.append(adj)

# Actual relevant logic: transform and slice
expanded = [weighted_sequence[0]]
for j in range(1, len(weighted_sequence)):
    diff = weighted_sequence[j] - weighted_sequence[j-1]
    expanded.append(round(diff * 2.1, 4))

# Introduce slicing and list comprehension distractors
sliced_view = expanded[1::2]
aggregated_slice = sum([x for x in sliced_view if x > 0.5])

# Core calculation hidden among noise
base_anchor = sum(weights) * 0.7
adjustment_log = [round((w - base_anchor)**2, 4) for w in weights]
final_shift = sum(adjustment_log) / len(adjustment_log)

# Multiple assignments with unpacking distraction
a, b = 10, 20
b, a = a + 1, b - 1
c, d = (a * 2, b // 2) if flag_check else (0, 0)

# Key data structure transformation
running_total = 0
transform_chain = []
for x in itertools.accumulate(expanded):
    running_total += x * 0.85
    transform_chain.append(round(running_total, 4))

# Decoy container operations
history_buffer = [[], [], []]
for idx, val in enumerate(transform_chain):
    history_buffer[idx % 3].append(val)

# Real final computation embedded late
correction_factor = 1 - (final_shift * 0.1)
final_weights = [w * correction_factor for w in transform_chain]

# Critical execution point — this is the answer anchor
threshold_balance = final_weights[-1] * correction_factor

print(f"Result: {threshold_balance}")