from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant readings
data_stream = [
    (1, 15), (2, 22), (3, 18), (4, 25), (5, 30), (6, 35), (7, 28), (8, 20), (9, 17), (10, 23),
    (11, 40), (12, 38), (13, 33), (14, 29), (15, 27)
]

# Irrelevant mapping - decoy for signal processing
signal_map = {i: (val % 7) for i, val in data_stream}

# Real processing: extract timestamps and values
timestamps = [entry[0] for entry in data_stream]
sensor_values = [entry[1] for entry in data_stream]

# Dead code path: frequency analysis of timestamps (unused)
timestamp_freq = Counter(timestamps)

# Distractor: moving average with irrelevant window
window_size = 3
moving_avg = [
    sum(sensor_values[i:i+window_size]) / window_size
    for i in range(len(sensor_values) - window_size + 1)
] if window_size <= len(sensor_values) else sensor_values

# Unused transformation: reverse cumulative sum
rev_cumsum = []
cumulative = 0
for v in reversed(sensor_values):
    cumulative += v
    rev_cumsum.append(cumulative)
rev_cumsum.reverse()

# Begin relevant logic: detect rising edges (consecutive increases)
rising_edges = 0
for i in range(1, len(sensor_values)):
    if sensor_values[i] > sensor_values[i-1]:
        rising_edges += 1

# Bit manipulation red herring: encode timestamp parity
parity_code = 0
for t in timestamps:
    parity_code ^= (t & 1) << (t % 5)

# Real computation: find local maxima (peaks)
peaks = []
for i in range(1, len(sensor_values)-1):
    if sensor_values[i-1] < sensor_values[i] > sensor_values[i+1]:
        peaks.append(sensor_values[i])

# Secondary metric: total fluctuation (sum of absolute differences)
fluctuation = 0
for i in range(1, len(sensor_values)):
    fluctuation += abs(sensor_values[i] - sensor_values[i-1])

# Distractor dictionary with unused diagnostics
diagnostics = defaultdict(int)
diagnostics['max_value'] = max(sensor_values)
diagnostics['min_value'] = min(sensor_values)
diagnostics['range'] = diagnostics['max_value'] - diagnostics['min_value']
diagnostics['median_guess'] = sorted(sensor_values)[len(sensor_values)//2]

diagnostics['rising_rate'] = rising_edges / len(sensor_values)

diagnostics['noise_estimate'] = fluctuation / sum(sensor_values)

# String-based decoy: encode peak count in hex string
peak_count_hex = hex(len(peaks))[2:]

# Slicing distraction: analyze only middle third
mid_start = len(sensor_values) // 3
mid_end = 2 * len(sensor_values) // 3
middle_segment = sensor_values[mid_start:mid_end]

# Unused combinatorics: possible pairs in middle segment
pair_count = 0
for i in range(len(middle_segment)):
    for j in range(i+1, len(middle_segment)):
        if middle_segment[i] + middle_segment[j] > 50:
            pair_count += 1

# Actual signal: weighted importance based on peak magnitude and fluctuation
aggregate_score = sum(peaks) * 2 - fluctuation // 10

# Correction factor derived from timestamp divisibility pattern
correction_factor = sum(1 for t in timestamps if t % 4 == 0)

correction_factor += len([v for v in sensor_values if v > 25]) // 5

# Critical assignment
final_diagnostic = aggregate_score + correction_factor

# Output the result as required
print(f"Result: {final_diagnostic}")