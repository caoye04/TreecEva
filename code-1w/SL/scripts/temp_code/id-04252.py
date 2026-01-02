from itertools import compress, count
from math import log, ceil

# Simulate sensor data with noise and metadata
timestamps = list(range(100, 200))
signal_data = [x % 7 for x in timestamps]
noise_mask = [(i % 3 == 0) for i in range(len(signal_data))]

# Irrelevant transformation chain (distractor)
decoy_map = map(lambda x: (x ** 2) + 1, count(1))
decoy_filtered = [next(decoy_map) for _ in range(50)]

# Real signal processing path
filtered_signal = list(compress(signal_data, [not m for m in noise_mask]))

# Dead code path - never used (red herring)
def legacy_process(seq):
    return [seq[i] + seq[i-1] if i > 0 else seq[0] for i in range(len(seq))]

# Secondary distractor: unused accumulator
total_drift = 0
for i, val in enumerate(timestamps):
    if i % 7 == 0:
        total_drift += abs(val - sum(noise_mask))

# Core calculation setup
window_size = 5
aggregated_blocks = []

for i in range(0, len(filtered_signal) - window_size + 1, window_size):
    block = filtered_signal[i:i+window_size]
    if len(block) == window_size:
        # Apply non-linear transformation
        transformed = [log(abs(b * b - 2) + 1) for b in block]
        aggregated_blocks.append(sum(transformed))

# Misleading intermediate: looks important but unused
raw_magnitude = sum([abs(x) for x in signal_data]) / len(signal_data)

# Key variable construction
scaling_factor = 0.85
adjustment_curve = [ceil(log(k + 2)) for k in range(len(aggregated_blocks))]

# Use of enumerate and zip (required python features)
evaluated_returns = []
for idx, (ret, adj) in enumerate(zip(aggregated_blocks, adjustment_curve)):
    if idx % 2 == 0:
        evaluated_returns.append(ret * scaling_factor * adj)
    else:
        # This branch is skipped due to filtering below
        evaluated_returns.append(ret * 1.1)

# Critical filtering: only even-indexed returns are actually used
working_returns = [r for i, r in enumerate(evaluated_returns) if i % 2 == 0]

# Final computation with distraction
baseline_offset = sum([t * 0.1 for t in timestamps[:10]])  # minor offset

# Decoy function call (never executed)
def finalize_chain(data):
    return sum(data) / (len(data) + 1)

# Actual final yield calculation
if working_returns:
    mean_return = sum(working_returns) / len(working_returns)
    volatility_penalty = len(noise_mask) / 100.0
    final_yield = (mean_return - volatility_penalty) * scaling_factor * 10
else:
    final_yield = -1

# Additional red herring: complex but unused expression
synthetic_index = sum([a*b for a, b in zip(decoy_filtered[::10], adjustment_curve)]) / (log(50) + 1)

print(f"Result: {final_yield}")