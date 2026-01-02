import itertools

# Simulated sensor data processing pipeline for environmental monitoring system
def collect_metrics(base_signal, noise_level=0.1):
    return [(base_signal[i] + (i * noise_level)) for i in range(len(base_signal))]

# Irrelevant helper: Computes harmonic mean (not used in final calculation)
def harmonic_mean(data):
    if 0 in data:
        return 0
    return len(data) / sum(1/x for x in data)

# Distraction function: Processes unrelated telemetry (dead code path)
def process_telemetry(stream):
    checksum = 0
    for val in stream:
        checksum ^= int(val * 100) % 255
    return checksum

# Core transformation: Applies exponential smoothing
def smooth_data(series, alpha=0.3):
    smoothed = [series[0]]
    for i in range(1, len(series)):
        smoothed.append(alpha * series[i] + (1 - alpha) * smoothed[i-1])
    return smoothed

# Misleading aggregation: Includes unused statistical measures
def aggregate_stats(measurements):
    avg = sum(measurements) / len(measurements)
    variance = sum((x - avg) ** 2 for x in measurements) / len(measurements)
    peak = max(measurements)
    # Following lines are red herrings
    normalized_peak = peak / (variance + 1e-5)
    entropy_like = -sum((x/sum(measurements)) * ((x+1e-5)/(sum(measurements)+1e-5)) for x in measurements)
    return {'average': avg, 'variance': variance, 'peak': peak, 'distorted': normalized_peak}

# Key evaluation logic with distractors
def evaluate_performance(raw_data):
    # Apply smoothing - relevant
    filtered = smooth_data(raw_data)
    
    # Generate sliding windows - relevant for next step
    windows = list(itertools.windowed(filtered, n=3))
    
    # Filter valid windows (non-decreasing) - relevant
    valid_windows = [w for w in windows if w[0] <= w[1] <= w[2]]
    
    # Compute window scores using lambda - relevant
    score_fn = lambda win: (win[2] - win[0]) * 100
    window_scores = [score_fn(w) for w in valid_windows]
    
    # Dead branch: never executed due to condition (distractor)
    debug_mode = False
    if debug_mode and len(window_scores) > 10:
        fallback = harmonic_mean(window_scores)
        return fallback
    
    # Unused intermediate calculations (misdirection)
    total_energy = sum(x**2 for x in filtered)
    fluctuation_index = sum(abs(filtered[i+1] - filtered[i]) for i in range(len(filtered)-1))
    pseudo_entropy = -sum((x/total_energy)*fluctuation_index for x in filtered if x > 0)
    
    # Critical computation path
    if not window_scores:
        primary_metric = 0
    else:
        primary_metric = sum(window_scores) / len(window_scores)
    
    # Secondary metric with slicing distraction
    trend_segment = filtered[-5:]  # Last 5 points
    early_segment = filtered[:5]   # First 5 points
    # The following line looks important but isn't used
    phantom_trend = [trend_segment[i] - trend_segment[i-1] for i in range(1, len(trend_segment))]
    
    # Actual contribution: simple average difference
    segment_diff = sum(trend_segment) / len(trend_segment) - sum(early_segment) / len(early_segment)
    
    # Final combination - only primary_metric is actually used
    final_weighted = 0.8 * primary_metric + 0.2 * segment_diff
    
    # Distractor: complex expression that evaluates but isn't returned
    complexity_proxy = len([x for x in filtered if x > sum(filtered)/len(filtered)])
    stability_ratio = (len(filtered) - complexity_proxy) / len(filtered) if filtered else 1
    
    # ACTUAL RETURN VALUE
    return final_weighted

# Simulated input data
baseline = [1.2, 1.4, 1.3, 1.7, 1.9, 2.1, 2.0, 2.4, 2.6, 2.7]
noise_factor = 0.05
metric_data = collect_metrics(baseline, noise_factor)

# Unused variables (red herrings)
data_copy = metric_data[:]
duplicate_stream = [x * 2 for x in metric_data]
scaling_factor = 1.0
offset_correction = 0.05

# Dead code block with misleading comment
# "Optimize data" - actually does nothing meaningful
temp_buffer = []
for val in metric_data:
    if val > 1.5:
        temp_buffer.append(val * 0.95)

# Key execution point
temp_result = process_telemetry(metric_data)  # Unused result
evaluation_snapshot = aggregate_stats(metric_data)  # Partially used stats
final_score = evaluate_performance(metric_data)

print(f"Result: {final_score}")