from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def calculate_noise(x):
    return sum(i ** 0.5 for i in range(1, x + 1)) if x > 5 else 0

# Misleading transformation chain
temp_offsets = [i * 1.5 for i in range(7)]
shift_register = list(map(lambda x: (x + 2) ** 2 % 97, temp_offsets))

# Core data structure with red herring entries
event_log = [
    ('power', 120), ('power', 125), ('status', 1),
    ('debug', 440), ('power', 130), ('status', 0),
    ('calibration', 99), ('power', 135), ('status', 1)
]

# Distractor aggregation (looks important but unused in final result)
status_tracker = defaultdict(int)
power_readings = []
for event, value in event_log:
    if event == 'status':
        status_tracker[value] += 1
    elif event == 'power':
        power_readings.append(value)

# Decoy statistical summary
decoys = {
    'avg_power': sum(power_readings) / len(power_readings),
    'status_balance': status_tracker[1] - status_tracker[0],
    'peak_shift': max(shift_register) - min(shift_register)
}

# Real signal embedded in noise: extract only 'power' events above threshold
effective_powers = [val for ev, val in event_log if ev == 'power' and val > 120]

# Intermediate transformation with lambda abstraction
amplify = lambda x: x * 1.1 + 7
adjusted_levels = [int(amplify(p)) for p in effective_powers]

# Conditional filtering that mimics complex logic but is actually deterministic
filtered_results = []
for level in adjusted_levels:
    if level > 140:
        filtered_results.append(level * 2)
    elif level > 130:
        filtered_results.append(level + 25)
    else:
        filtered_results.append(level)

# Hidden accumulator: sum only every second element after index 1 (non-obvious rule)
cumulative_base = 0
for idx, val in enumerate(filtered_results):
    if idx >= 1 and (idx % 2) == 1:
        cumulative_base += val

# Bit manipulation decoy (irrelevant but looks critical)
bit_fiddling = 0
for val in filtered_results:
    bit_fiddling ^= (val << 2) | (val >> 3)

# Secondary fake checksum
dummy_hash = sum((i + 1) * v for i, v in enumerate(reversed(filtered_results))) % 1000

# Actual computation path hidden among distractors
sequence_weights = [0.5, 1.0, 1.5, 2.0]
weighted_sum = sum(w * v for w, v in zip(sequence_weights, filtered_results[:4]))

# Final processing step disguised as part of noise
def harvest_result(data):
    base = weighted_sum
    modifier = len(effective_powers) * 3
    # The real answer depends only on these two factors
    return int(base - modifier)

# Processed data is a redacted view (misleading name)
processed_data = [x for x in adjusted_levels if x != 132]

# Critical execution point
final_yield = harvest_result(processed_data)

print(f"Result: {final_yield}")