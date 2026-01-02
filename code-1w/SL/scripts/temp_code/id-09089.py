from itertools import accumulate, cycle
import math

# Simulated sensor data stream with noise
data_stream = [18, 23, 27, 36, 41, 54, 63, 69, 72, 81, 90, 93, 100]

# Irrelevant transformation: time-based weighting (unused later)
time_weights = [round(0.5 * (1 + math.cos(i)), 3) for i in range(len(data_stream))]
weighted_values = [a * b for a, b in zip(data_stream, time_weights)]

# Noise filter threshold (distractor - not actually used in final logic)
threshold = sum(weighted_values) / len(weighted_values)

# Real processing begins: clean and transform
def clean_signal(seq):
    # Remove outliers above 95 (misleading - not actually impactful here)
    filtered = [x for x in seq if x <= 95]
    shifted = [x - 10 for x in filtered]  # Offset to normalize
    return [x for x in shifted if x > 0]  # Remove non-positive

processed = clean_signal(data_stream)

# Distractor: complex unused transformation chain
binned = dict()
for val in processed:
    key = val // 10
    binned.setdefault(key, []).append(val)

sorted_bins = {k: sorted(v) for k, v in binned.items()}
flat_sorted = [item for sublist in sorted_bins.values() for item in sublist]

# Another red herring: attempt to smooth with moving average (never used)
def moving_avg(lst, window=3):
    return [sum(lst[i:i+window]) / window for i in range(len(lst) - window + 1)]

smoothed = moving_avg(flat_sorted)

# Real computation path: find every third element in accumulated sum that is divisible by 4
acc = list(accumulate(processed, initial=0))[1:]

candidates = []
cycle_pattern = cycle([1, 2, 3])
for val in acc:
    if val % 4 == 0 and next(cycle_pattern) == 1:
        candidates.append(val)

# Secondary filter: only those present in original processed or acc
valid_candidates = [c for c in candidates if c in processed or c in acc]

# Checksum base: use only values divisible by 3 from processed
# This is the actual critical line
checksum = finalize(sum(filter(lambda x: x % 3 == 0, processed)))

# Dummy function to create illusion of complexity
def finalize(x):
    # Apply bit manipulation noise
    x ^= 255
    x += 1000
    # Extra operations to mislead
    temp = x * 2
    temp -= 500
    temp |= 1024
    # But only x is returned
    return x

# Unused recursive function (dead code path)
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)

# Unused data structure: graph representation of jumps (decoy)
jumps = [(processed[i], processed[i+1]) for i in range(len(processed)-1) if processed[i+1] - processed[i] > 5]
graph = {}
for src, dst in jumps:
    graph.setdefault(src, []).append(dst)

# Print result as required
Result: {checksum}