from itertools import combinations

# Simulate sensor array readings over time with noise filtering
time_series_data = [102, 98, 115, 93, 120, 88, 118, 95]
noise_threshold = 10
smoothed_readings = []
running_avg = 0

for i in range(len(time_series_data)):
    running_avg += time_series_data[i]
    if i == 0:
        smoothed_readings.append(time_series_data[i])
    else:
        diff = abs(time_series_data[i] - time_series_data[i-1])
        if diff > noise_threshold:
            corrected = (time_series_data[i] + time_series_data[i-1]) / 2
            smoothed_readings.append(round(corrected))
        else:
            smoothed_readings.append(time_series_data[i])

# Identify stable subsequences using sliding window
window_size = 3
stable_windows = []
variance_log = []

for start in range(len(smoothed_readings) - window_size + 1):
    window = smoothed_readings[start:start+window_size]
    mean_val = sum(window) / window_size
    variance = sum((x - mean_val) ** 2 for x in window) / window_size
    variance_log.append(variance)
    if variance < 60:
        stable_windows.append(window)

# Compute potential output yields from stable configurations
yield_multipliers = {'low': 0.8, 'medium': 1.1, 'high': 1.4}
base_yield = 25
net_outputs = []

for window in stable_windows:
    key_product = 1
    for val in window:
        key_product *= (val % 10)
    
    # Irrelevant transformation: digit sum path (not used in final yield)
    digit_sum = sum(int(d) for d in str(key_product))
    temp_adjustment = digit_sum * 0.5 if digit_sum > 10 else digit_sum * 0.3
    
    # Actual yield computation path
    magnitude_score = sum(window) / len(window)
    if magnitude_score < 100:
        category = 'low'
    elif magnitude_score < 110:
        category = 'medium'
    else:
        category = 'high'
    
    raw_output = base_yield * yield_multipliers[category]
    efficiency_factor = len([x for x in window if x > 100]) / len(window)
    net_yield = raw_output * (1 + efficiency_factor)
    net_outputs.append(round(net_yield, 2))

# Secondary analysis - unused but plausible-looking computation
pairwise_peaks = list(combinations([int(x) for x in smoothed_readings[::2]], 2))
peak_scores = [a * b for a, b in pairwise_peaks if a > b]
overall_peak_index = sum(peak_scores) / 1000 if peak_scores else 0

# Final integration step
final_yield = max(net_outputs)
Result: {final_yield}