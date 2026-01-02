from itertools import combinations, cycle

# Simulated sensor readings with noise and metadata
data_stream = [15, 23, -7, 42, 8, 19, -3, 31, 12, 4, 0, 64, -15, 22]
noise_pattern = [1, -1, 2]
timestamps = list(range(1000, 1000 + len(data_stream)))

# Irrelevant transformations (distractors)
doubled = [x * 2 for x in data_stream if x > 10]
shifted_noise = [(x + y) % 256 for x, y in zip(data_stream[::3], cycle(noise_pattern))]

# Key data processing chain
smoothed = []
for i in range(2, len(data_stream)):
    smoothed.append(sum(data_stream[i-2:i+1]) / 3)

even_windows = list(combinations([x for x in smoothed if x > 10], 2))
threshold_pairs = [pair for pair in even_windows if abs(pair[0] - pair[1]) < 5]

# Decoy statistical analysis
mean_val = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)
median_like = sorted(smoothed)[len(smoothed)//2]

# Actual relevant logic path
outlier_mask = [abs(x - mean_val) > 15 for x in data_stream]
cleaned = [data_stream[i] for i in range(len(data_stream)) if not outlier_mask[i]]
transformed = [x // 2 if x > 0 else x for x in cleaned]
filtered_values = [x for x in transformed if x in smoothed or x % 4 == 0]

# Dead code path - looks important but unused
aggregated = []
for size in range(2, 4):
    for window in zip(*[cleaned[i:] for i in range(size)]):
        aggregated.append(sum(window) // len(window))

# Secondary decoy: complex but irrelevant frequency map
freq_map = {}
for val in data_stream:
    bin_key = bin(val & 0b111).count('1')
    freq_map[bin_key] = freq_map.get(bin_key, 0) + 1

# Critical assignment
filtered_sum = sum(filtered_values)

# Unrelated visualization prep (dead end)
plot_points = []
for t, v in zip(timestamps, data_stream):
    if v % 3 == 0:
        plot_points.append((t, v ** 0.5))

print(f"Result: {filtered_sum}")