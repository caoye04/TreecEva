import itertools

def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    return [y * 0.9 for y in smoothed]

samples = [0.1, 0.7, -0.8, 1.2, 0.4, -1.5, 0.9, 0.3, -0.6, 1.1]
decoy_signal = [x ** 2 for x in samples if x < 0]

# Irrelevant transformation chain
shadow_buffer = list(map(lambda x: x + 2j, samples))
offset_map = {i: val * 0.1 for i, val in enumerate(samples)}
dummy_pairs = list(zip(samples, decoy_signal[::-1]))

# Unused recursive function (red herring)
def integrate_recursive(seq, idx=0):
    if idx >= len(seq) - 1:
        return 0
    return seq[idx] + 0.5 * integrate_recursive(seq, idx + 1)

# Real processing begins
processed = analyze_signal(samples)

baseline = sum(processed) / len(processed) if processed else 0
variance = sum((x - baseline) ** 2 for x in processed) / len(processed) if processed else 0
fluctuation_index = variance * len(processed) if processed else 0

# Simulate time-series windowing
windows = [processed[i:i+2] for i in range(0, len(processed), 2) if len(processed[i:i+2]) == 2]
trend_data = []
for i, win in enumerate(windows):
    trend_data.append((i, sum(win)))

# Distractor: complex enumeration with irrelevant aggregation
decoys = []
for idx, (time, val) in enumerate(trend_data):
    temp = val * (idx + 1)
    decoys.append(temp if temp > 1 else -temp)

# Unused itertools permutation (dead code path)
permutations = list(itertools.permutations([1, 2, 3]))[:0]  # Never used

# Core metric computation buried in noise
valid_peaks = [t[1] for t in trend_data if t[1] > baseline]
anomaly_score = 0
if valid_peaks:
    peak_diffs = [abs(valid_peaks[i] - valid_peaks[i-1]) for i in range(1, len(valid_peaks))]
    if peak_diffs:
        anomaly_score = sum(peak_diffs) / len(peak_diffs) * 0.7
    else:
        anomaly_score = abs(valid_peaks[0]) * 0.3

def aggregate_metrics(metrics, base):
    total = base
    for _, val in metrics:
        total += val * 0.2
    return total * 0.8

# Key statement
final_diagnostic = aggregate_metrics(trend_data, baseline) + anomaly_score

# Output result
print(f"Result: {final_diagnostic}")