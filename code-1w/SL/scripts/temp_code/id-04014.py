from collections import defaultdict, Counter

# Simulate telemetry data from satellite subsystems
telemetry_streams = [
    [5, 3, 1, 4, 2, 5, 3],
    [9, 7, 8, 6, 7, 9, 8],
    [2, 1, 3, 2, 1, 2, 3],
    [4, 4, 4, 5, 5, 4, 4]
]

# Irrelevant: Initialize decoy system statuses
decoy_status = [False] * 10
temporary_flags = {i: (i % 3 == 0) for i in range(7)}

# Distractor: Unused transformation matrix
tf_matrix = [[i*j for j in range(5)] for i in range(5)]

# Real processing begins: extract peak magnitudes per stream
peak_magnitudes = []
for stream in telemetry_streams:
    magnitude = 0
    for val in stream:
        magnitude += val ** 2
    rms = magnitude ** 0.5
    peak_magnitudes.append(int(rms))

# Misleading intermediate: normalized peaks (not used later)
normalized_peaks = [p / sum(peak_magnitudes) for p in peak_magnitudes]

# Distractor: fake entropy calculation
entropy_sum = 0.0
for p in peak_magnitudes:
    if p > 0:
        entropy_sum -= (p/100) * ((p/100).__log__())

# Real: count frequency of base values across all streams
value_counter = Counter()
for stream in telemetry_streams:
    value_counter.update(stream)

dominant_value = value_counter.most_common(1)[0][1]  # frequency of most common value

# Distractor: unused recursive function
def useless_recurse(n):
    if n <= 1:
        return 1
    return n * useless_recurse(n - 2)

# Real: compute weighted harmonic mean of peak magnitudes (relevant)
total_inv_weight = 0.0
for mag in peak_magnitudes:
    total_inv_weight += dominant_value / mag
harmonic_mean = len(peak_magnitudes) * dominant_value / total_inv_weight if total_inv_weight else 0

# Distractor: enumerate with no side effect
event_log = []
for idx, val in enumerate(peak_magnitudes):
    event_log.append(f"Event {idx}: {val}")

# Real: simulate flow adjustment based on harmonic stability
stability_factor = int(harmonic_mean) % 4 + 1
adjusted_flow = harmonic_mean * stability_factor

# Distractor: zip unrelated lists
zipped_garbage = list(zip(decoy_status, temporary_flags.keys(), [x*2 for x in range(7)]))

# Real: calculate efficiency ratio from pattern regularity
pattern_score = 0
for stream in telemetry_streams:
    pairs = zip(stream, stream[1:])
    for a, b in pairs:
        if abs(a - b) <= 1:
            pattern_score += 1

efficiency_ratio = pattern_score / 20.0

# Critical assignment: final flux computation
final_flux = adjusted_flow * efficiency_ratio

# Distractor: unused defaultdict transformation
flow_cache = defaultdict(lambda: 0)
for i, v in enumerate(telemetry_streams[0]):
    flow_cache[f"step_{i}"] = v * final_flux

# Output target result
print(f"Target result: {final_flux}")