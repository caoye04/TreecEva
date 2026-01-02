from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing pipeline with diagnostic analysis
raw_readings = [3, 5, 2, 8, 5, 9, 2, 7, 4, 6, 5, 1, 8, 3, 7]

timestamp_groups = defaultdict(list)
for i, val in enumerate(raw_readings):
    timestamp_groups[i // 3].append(val)

# Irrelevant aggregation: spatial coherence (unused later)
spatial_coherence = sum(len(group) for group in timestamp_groups.values() if len(group) > 2)

# Transform readings into fluctuation patterns
fluctuations = [abs(raw_readings[i] - raw_readings[i-1]) for i in range(1, len(raw_readings))]

# Misleading statistical trap: harmonic mean (not used in final path)
def harmonic_mean(xs):
    if 0 in xs:
        return 0
    return len(xs) / sum(1/x for x in xs)

reversed_readings = raw_readings[::-1]
mean_reversed = sum(reversed_readings) / len(reversed_readings)

# Decoy function: entropy calculation (never called)
calculate_entropy = lambda data: sum(-x/sum(data)*__import__('math').log2(x/sum(data)) for x in data if x > 0)

# Signal normalization via moving average
window_size = 3
smoothed = [sum(raw_readings[i:i+window_size]) / window_size 
             for i in range(len(raw_readings) - window_size + 1)]

# Extract peaks above dynamic threshold
threshold = sum(smoothed) / len(smoothed)
peaks = [x for x in smoothed if x > threshold]

# Destructuring assignment - extract key segments
early_peaks, *mid_peaks, late_peaks = [[p for p in peaks if p < 6], 
                                       [p for p in peaks if 6 <= p <= 7], 
                                       [p for p in peaks if p > 7]]

# Complex transformation: amplitude-weighted timing
weighted_timing = sum(i * val for i, val in enumerate(raw_readings) if val in peaks)

# Simulate phase shift interference (red herring)
shifted_cycle = list(itertools.islice(itertools.cycle([1, -1]), len(fluctuations)))
interference_score = sum(f * s for f, s in zip(fluctuations, shifted_cycle))

# Actual relevant transformation chain
baseline = sum(p % 3 for p in peaks if p > threshold) * 2

transformed_data = []
for i, val in enumerate(smoothed):
    if i % 2 == 0:
        transformed_data.append((val ** 2) // (i + 1))
    else:
        transformed_data.append(int(__import__('math').sqrt(val * 2)))

# Dead code path: buffer alignment check (never executed)
if False:
    alignment_buffer = [transformed_data[i] ^ transformed_data[-i-1] for i in range(len(transformed_data)//2)]
    baseline += sum(alignment_buffer)

# Core metric aggregation function
def aggregate_metrics(metrics, offset):
    count_large = sum(1 for m in metrics if m > 7)
    total_small = sum(m for m in metrics if m < 4)
    return (count_large * offset) - total_small

# Anomaly detection using fluctuation frequency
freq_dist = Counter(fluctuations)
dominant_fluctuation = freq_dist.most_common(1)[0][1]
anomaly_score = dominant_fluctuation ** 2

# Critical execution point
final_diagnostic = aggregate_metrics(transformed_data, baseline) + anomaly_score

print(f"Result: {final_diagnostic}")