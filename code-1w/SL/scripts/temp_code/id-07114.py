import math

# Simulated sensor data processing with diagnostic logic
def preprocess_sensor_readings(raw_readings):
    filtered = []
    noise_floor = 0.05
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)

# Irrelevant helper: computes statistical dispersion (not used in final path)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Signal compression using quantization and run-length encoding simulation
def compress_signal(readings):
    quanta = [int(x * 10) for x in readings]
    compressed = []
    count = 1
    for i in range(1, len(quanta)):
        if quanta[i] == quanta[i-1]:
            count += 1
        else:
            compressed.append((quanta[i-1], count))
            count = 1
    if quanta:
        compressed.append((quanta[-1], count))
    return compressed

# Auxiliary function: generates entropy approximation (distractor)
def estimate_entropy(seq):
    freq_map = {}
    for item in seq:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(seq)
    entropy = -sum((count / total) * math.log2(count / total) for count in freq_map.values())
    return round(entropy, 4)

# Core analysis: identifies anomalies based on set membership and magnitude decay
def analyze_signal(compressed_blocks, critical_levels):
    spike_magnitudes = []
    decay_trend = []
    
    # Extract unique signal levels present
    observed_levels = set(block[0] for block in compressed_blocks)
    
    # Determine which critical thresholds were crossed
    triggered = observed_levels & critical_levels  # Set intersection: key operation
    
    for level, duration in compressed_blocks:
        if level in triggered:
            spike_magnitudes.append(level)
            if len(decay_trend) > 0 and level < decay_trend[-1]:
                decay_trend.append(level)
            elif len(decay_trend) == 0:
                decay_trend.append(level)
    
    # Compute weighted diagnostic score
    base_score = sum(spike_magnitudes)
    trend_bonus = 0
    if len(decay_trend) == len(spike_magnitudes) and decay_trend == sorted(spike_magnitudes, reverse=True):
        trend_bonus = 15
    
    # Dead code path: early exit never taken due to data constraints (red herring)
    if len(spike_magnitudes) == 0:
        return -999  # unreachable with current input
    
    # Final computation
    diagnostic_value = base_score * 10 + trend_bonus
    
    # Unused intermediate variables (distractors)
    avg_duration = sum(block[1] for block in compressed_blocks) / len(compressed_blocks)
    peak_level = max(observed_levels)
    spurious_flag = False
    
    return int(diagnostic_value)

# Simulated raw data from multi-axis sensor array
raw_sensor_data = [
    0.02, 0.03, 0.15, 0.15, 0.15, 0.23, 0.23, 0.19, 0.12, 0.07,
    0.31, 0.31, 0.31, 0.31, 0.25, 0.25, 0.18, 0.41, 0.41, 0.33
]

# Preprocess and compress signal
cleaned = preprocess_sensor_readings(raw_sensor_data)
compressed_data = compress_signal(cleaned)

# Define critical thresholds as set
threshold_set = {3, 4, 7, 15, 23, 31, 41}

# Spurious entropy calculation (irrelevant to final result)
entropy_metric = estimate_entropy([block[0] for block in compressed_data])

# Key execution point
final_diagnostic = analyze_signal(compressed_data, threshold_set)

# Output result
print(f"Result: {final_diagnostic}")