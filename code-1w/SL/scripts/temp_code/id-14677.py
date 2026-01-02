import math

# Simulated sensor fusion system for environmental monitoring
def acquire_data():
    raw_samples = [i * 0.77 for i in range(15)]
    offset = 3.14
    adjusted = [x + offset for x in raw_samples]
    return adjusted

# Irrelevant signal smoothing (dead path)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Decoy transformation with misleading intermediate
transform_weights = [math.sin(i * 0.5) for i in range(15)]
temp_correction = sum(transform_weights) * 0.1  # Red herring value

def apply_filter(signal):
    filtered = []
    for i, val in enumerate(signal):
        if i % 2 == 0:
            filtered.append(val * math.cos(i * 0.1))
        else:
            filtered.append(val * math.sin(i * 0.05))
    return filtered

# Unused recursive harmonic detector
def detect_harmonics(seq, depth=0):
    if depth > 3 or len(seq) < 2:
        return 0
    return seq[0] + detect_harmonics(seq[1:], depth + 1)

# Core processing chain
acquired_signals = acquire_data()
suppressed_noise = [x for i, x in enumerate(acquired_signals) if i not in [0, 1, 14]]  # Partial filter

# Real processing begins here
weighted_values = list(map(lambda x: x * 1.25 if x > 5 else x * 0.9, suppressed_noise))

# Signal binning (distractor)
bins = {f'bin_{i}': 0 for i in range(5)}
for v in weighted_values:
    idx = min(int(v // 4), 4)
    bins[f'bin_{idx}'] += 1

# Actual computation path
aggregated_metric = sum(weighted_values) / len(weighted_values)
fluctuation_index = sum(abs(weighted_values[i+1] - weighted_values[i]) for i in range(len(weighted_values)-1))
composite_score = aggregated_metric * 0.7 + fluctuation_index * 0.3

# Secondary derived values (some irrelevant)
entropy_proxy = -sum(x * math.log(abs(x)+1e-8) for x in weighted_values)  # unused
normalization_factor = math.sqrt(sum(x**2 for x in weighted_values))  # decoy

def analyze_readings(data_chunk):
    base = sum(data_chunk) / len(data_chunk)
    peaks = len([x for x in data_chunk if x > base * 1.1])
    troughs = len([x for x in data_chunk if x < base * 0.9])
    stability = 1 / (1 + abs(peaks - troughs))
    return base * stability

def process_signals(raw):
    stage1 = [x * 1.1 for x in raw]
    stage2 = [x for x in stage1 if x > 3.0]  # filtering
    final_form = [x * 0.95 for x in stage2]
    return final_form

processed_signals = process_signals(suppressed_noise)

# Key red herring assignment
theoretical_limit = math.gamma(aggregated_metric / 2)  # Misleading complex math

# Critical statement
final_diagnostic = analyze_readings(processed_signals)

# Multiple print statements to obscure focus
print(f"Fluctuation Index: {fluctuation_index:.4f}")
print(f"Composite Score: {composite_score:.4f}")
print(f"Bins distribution: {bins}")
print(f"Theoretical Limit (unused): {theoretical_limit:.4f}")
print(f"Entropy Proxy: {entropy_proxy:.4f}")
print(f"Normalization Factor (unused): {normalization_factor:.4f}")

# REQUIRED OUTPUT - DO NOT REMOVE OR MODIFY
print(f"Result: {final_diagnostic}")