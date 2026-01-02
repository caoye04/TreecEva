import math

def analyze_performance(timestamps, base_freq=1.8):
    time_diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_interval = sum(time_diffs) / len(time_diffs) if time_diffs else 0
    peak_freq = base_freq * (1.2 if avg_interval < 0.05 else 1.0)
    jitter = sum(abs(diff - avg_interval) for diff in time_diffs)
    return avg_interval, peak_freq, jitter

# Simulate sensor data log with redundant preprocessing
data_log = [0.0, 0.02, 0.045, 0.068, 0.09, 0.111, 0.133]

scaling_factor = 1.45
offset_correction = 0.002
smoothed_log = [t + offset_correction for t in data_log]
delta_noise = [abs(smoothed_log[i+1] - smoothed_log[i]) for i in range(len(smoothed_log)-1)]
noise_floor = sum(delta_noise) / len(delta_noise)

# Irrelevant audio simulation block (dead computation path)
audio_bandwidth = 44100
harmonic_series = [audio_bandwidth / (2**n) for n in range(1, 5)]
audio_envelope = lambda x: x * 0.8 if x > 0.5 else x * 1.2
processed_audio = [audio_envelope(h) for h in harmonic_series]

# Core processing function with conditional logic
def process_metrics(log_data):
    raw_intervals = [log_data[i+1] - log_data[i] for i in range(len(log_data)-1)]
    valid_intervals = [ival for ival in raw_intervals if ival > 0.01]
    
    # Compute multiple metrics including distractors
    total_duration = log_data[-1] - log_data[0]
    interval_variance = sum((x - sum(valid_intervals)/len(valid_intervals))**2 for x in valid_intervals) / len(valid_intervals) if valid_intervals else 0
    compression_ratio = len(log_data) / (sum(valid_intervals) + 1e-8)
    
    # Secondary analysis with nested conditionals
    stress_factor = 0
    if len(valid_intervals) > 4:
        if max(valid_intervals) > 0.05:
            stress_factor += 1.5
        if min(valid_intervals) < 0.03:
            stress_factor += 0.8
    
    # Efficiency model using lambda and conditional expression
    efficiency_curve = lambda x: x * 1.5 if x < 0.05 else x * 0.9
    adjusted_intervals = [efficiency_curve(iv) for iv in valid_intervals]
    base_efficiency = sum(adjusted_intervals) / len(adjusted_intervals) if adjusted_intervals else 0
    
    # Final scoring with distractor-weighted terms
    noise_penalty = noise_floor * 100  # Unused but calculated
    temp_bias = scaling_factor * 0.1   # Misleading variable
    efficiency_score = (base_efficiency * 1000) - (stress_factor * 50) + (compression_ratio * 2)  # Key result
    
    # Red herring post-processing
    normalized_score = efficiency_score / (efficiency_score + 1) if efficiency_score > 0 else 0
    saturation_level = 'high' if normalized_score > 0.7 else 'low'
    
    return {
        'score': efficiency_score,
        'normalized': normalized_score,
        'saturation': saturation_level
    }

# Execute main logic
result_container = analyze_performance(data_log)
final_output = process_metrics(data_log)
efficiency_score = final_output['score']
print(f"Result: {efficiency_score}")