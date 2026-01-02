import math

# Simulated sensor array data processing with diagnostic analysis
def collect_sensor_data():
    raw_signals = [127, 255, 193, 64, 87, 212, 144, 95, 113, 77]
    noise_floor = 65
    filtered = [x for x in raw_signals if x > noise_floor]
    return filtered

# Irrelevant helper - dead path
def deprecated_normalization(data):
    max_val = max(data)
    return [round(x / max_val, 3) for x in data]

# Signal transformation using slicing and windowing
def window_transform(signal_seq):
    window_size = 3
    transformed = []
    for i in range(0, len(signal_seq) - window_size + 1):
        window = signal_seq[i:i+window_size]
        avg = sum(window) / window_size
        rms = math.sqrt(sum([x**2 for x in window]) / window_size)
        transformed.append(round(rms - avg, 2))
    # Extended tail padding (distractor)
    transformed += [transformed[-1]] * 2
    return transformed

# Data enrichment with irrelevant metrics
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((freq/total) * math.log2(freq/total) for freq in counts.values())
    return round(entropy, 4)

# Decoy function - looks important but unused in final chain
def validate_calibration(seq):
    checksum = 0
    for i, val in enumerate(seq):
        checksum ^= (val + i) % 256
    return checksum == 42

# Real processing begins here
sensor_readings = collect_sensor_data()
processed_signal = window_transform(sensor_readings)

# Extraneous intermediate calculations (distractors)
mean_level = sum(processed_signal) / len(processed_signal)
variance = sum((x - mean_level)**2 for x in processed_signal) / len(processed_signal)
peak_magnitude = max(abs(x) for x in processed_signal)

# Set operations to identify anomalies (relevant)
positive_set = {x for x in processed_signal if x > 0}
negative_set = {x for x in processed_signal if x < 0}
anomaly_boundaries = positive_set.symmetric_difference(negative_set)

# Lambda-based dynamic threshold (used later)
threshold_func = lambda x: x > (mean_level * 1.15) if x > 0 else x < (mean_level * 0.85)

# Red herring: complex bit manipulation on unrelated index
bit_analysis = 0
for i in range(len(processed_signal)):
    bit_analysis ^= int(processed_signal[i]) & 0xF
bit_flags = [(bit_analysis >> i) & 1 for i in range(4)]

# Simulate historical comparison (unused legacy)
historical_baseline = [0.88, 1.02, 0.91, 1.18, 0.77]
drift_score = sum(abs(a - b) for a, b in zip(processed_signal[:5], historical_baseline))

# Core logic: detect significant deviations
high_impact = list(filter(threshold_func, processed_signal))
impact_sum = sum(abs(x) for x in high_impact)

# Diagnostic classification using accumulation and set logic
def analyze_readings(readings, thresholder):
    above_threshold = list(filter(thresholder, readings))
    if not above_threshold:
        return 0
    
    # Use of slicing to analyze trend direction
    recent_trend = readings[-5:]
    increasing_periods = sum(1 for i in range(1, len(recent_trend)) if recent_trend[i] > recent_trend[i-1])
    
    # Accumulate weighted significance
    weight_map = map(lambda x: abs(x) * 1.5 if x > 0 else abs(x) * 0.8, above_threshold)
    total_weight = sum(weight_map)
    
    # Final computation combining multiple factors
    base_score = total_weight * len(above_threshold)
    trend_factor = increasing_periods / 4 if len(recent_trend) >= 5 else 0.5
    return int(base_score * trend_factor)

# Critical execution point
final_diagnostic = analyze_readings(processed_data=processed_signal, threshold_func=threshold_func)
print(f"Result: {final_diagnostic}")