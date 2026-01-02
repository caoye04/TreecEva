from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamps = list(range(100, 200, 3))
raw_readings = [t * 0.7 + ((t % 11) - 5) for t in timestamps]

# Misleading auxiliary computation (distractor)
baseline_offset = sum([abs(r % 4) for r in raw_readings[:20]]) / len(raw_readings[:20])
adjusted_readings = [r - baseline_offset for r in raw_readings]

# Filter out anomalous spikes using sliding window (relevant)
def detect_anomalies(data, window_size=5, threshold=1.5):
    anomalies = []
    for i in range(window_size, len(data)):
        window = data[i - window_size:i]
        mean_val = sum(window) / len(window)
        if abs(data[i] - mean_val) > threshold * (max(window) - min(window)):
            anomalies.append(i)
    return anomalies

anomaly_indices = detect_anomalies(adjusted_readings)
cleaned_readings = [v for i, v in enumerate(adjusted_readings) if i not in anomaly_indices]

# Segment data into blocks (semi-relevant)
block_size = 7
segmented_blocks = [cleaned_readings[i:i+block_size] for i in range(0, len(cleaned_readings), block_size)]
residual_data = cleaned_readings[len(segmented_blocks) * block_size:]  # Unused (distractor)

# Compute block statistics (some used later)
block_averages = [sum(block) / len(block) for block in segmented_blocks if len(block) > 0]
block_variances = [sum((x - sum(block)/len(block))**2 for x in block) / len(block) for block in segmented_blocks]

# Weighting scheme based on stability (relevant)
stability_scores = [1.0 / (1.0 + var) for var in block_variances]
weighted_sum = sum(avg * weight for avg, weight in zip(block_averages, stability_scores))
weight_total = sum(stability_scores)
normalized_score = weighted_sum / weight_total if weight_total > 0 else 0

# Secondary processing: trend analysis (distractor)
def compute_trend_strength(series):
    diffs = [series[i+1] - series[i] for i in range(len(series)-1)]
    positive_count = len([d for d in diffs if d > 0])
    return positive_count / len(diffs) if diffs else 0

trend_score = compute_trend_strength([sum(block) for block in segmented_blocks])
penalty_factor = 0.95 if trend_score < 0.4 else 1.0  # Rarely applies (misleading)

# Simulate calibration adjustment (distractor)
calibration_map = defaultdict(float)
for idx, val in enumerate(block_averages):
    calibration_map[f'cal_{idx % 5}'] += val * 0.01

# Core transformation pipeline
processed_data = [normalized_score * 1.25]
processed_data.append(normalized_score * 0.8)
processed_data.append(normalized_score * 1.1)

# Final scoring logic
def calculate_final_score(scores):
    base = sum(scores)
    bonus = 10 if len(scores) >= 3 else 5
    # Apply entropy-like dispersion penalty
    mean_score = base / len(scores)
    variance = sum((s - mean_score) ** 2 for s in scores) / len(scores)
    penalty = 15 * (variance / (1 + variance))  # Saturating penalty
    return int(base + bonus - penalty)  # Deterministic integer output

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")