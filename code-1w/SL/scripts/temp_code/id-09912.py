import math

# Simulated sensor data processing with diagnostic analysis
def analyze_readings(raw_stream, threshold=0.75):
    normalized = [x / max(raw_stream) for x in raw_stream]
    spikes = [i for i, v in enumerate(normalized) if v > threshold]
    return spikes

# Irrelevant helper: computes geometric mean (not used in final path)
def geo_mean(data):
    product = 1
    for x in data:
        product *= x
    return product ** (1 / len(data))

# Core transformation pipeline
def extract_features(signal):
    # Apply windowed slicing and frequency approximation
    windows = [signal[i:i+4] for i in range(0, len(signal)-2, 3)]
    freq_components = []
    for win in windows:
        component = sum(w * (i+1) for i, w in enumerate(win))
        freq_components.append(component)
    
    # Misleading intermediate: harmonic adjustment (unused)
    adjusted = []
    for f in freq_components:
        if f != 0:
            adjusted.append(len(freq_components) / sum(1/freq_components))
    
    return freq_components

# Primary metric aggregator
def aggregate_metrics(trends, base):
    # Use dictionary to map trend indices to strength scores
    score_map = {i: round(abs(t - base[i % len(base)]) * 100) for i, t in enumerate(trends)}
    
    # Augment with zip-based correlation tracking (some values irrelevant)
    correlations = {}
    for idx, (a, b) in enumerate(zip(trends[1:], base[:-1])):
        corr = (a - b) ** 2
        correlations[f'c_{idx}'] = corr
    
    # Real computation path
    total_score = sum(score_map.values())
    penalty = sum(1 for c in correlations.values() if c > 50)
    return total_score - (penalty * 15)

# Dead function: looks important but unused
def validate_calibration(seq):
    checksum = 0
    for i, val in enumerate(seq):
        checksum ^= (val + i) % 256
    return format(checksum, 'b').count('1')

# --- Main Execution ---
sensor_log = [104, 182, 93, 201, 144, 88, 199, 134, 90]

# Distractor: unused processed forms
spike_indices = analyze_readings(sensor_log)
dummy_geo = geo_mean(sensor_log[::2])

# Key data structures with mixed relevance
baseline_ref = [100, 180, 95, 200, 140]
trend_data = extract_features(sensor_log)

# Outlier buffer computed from slice statistics (only this part matters)
slice_peak = max(sensor_log[2:6])
slice_floor = min(sensor_log[2:6])
outlier_ratio = (slice_peak - slice_floor) / slice_floor
outlier_buffer = int(math.log(outlier_ratio * 100 + 1))

# Critical statement
final_diagnostic = aggregate_metrics(trend_data, baseline_ref) // outlier_buffer

# Final output
print(f"Result: {final_diagnostic}")