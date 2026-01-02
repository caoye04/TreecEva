import math

# Simulated sensor data processing pipeline
raw_readings = [3.2, 4.7, 6.1, 2.8, 5.5, 7.3, 1.9, 4.4, 3.8, 6.6]
offset_compensation = 0.8
gain_factor = 1.4
decoy_threshold = 4.0

# Irrelevant transformation - red herring
adjusted_readings = [x + offset_compensation for x in raw_readings]

# Apply gain (meaningful but not final)
scaled_readings = [x * gain_factor for x in adjusted_readings]

# Noise filtering using moving average (distraction with partial relevance)
def apply_noise_filter(data, window=3):
    filtered = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        end = i + 1
        filtered.append(sum(data[start:end]) / (end - start))
    return filtered

smoothed_signals = apply_noise_filter(scaled_readings)

# Decoy logic: amplitude classification (unused later)
amplitude_classes = []
for val in smoothed_signals:
    if val > 6.0:
        amplitude_classes.append('HIGH')
    elif val > 4.0:
        amplitude_classes.append('MEDIUM')
    else:
        amplitude_classes.append('LOW')

# Real processing begins here: detect peaks above dynamic threshold
dynamic_baseline = sum(smoothed_signals) / len(smoothed_signals)
peak_indices = [i for i, x in enumerate(smoothed_signals) if x > dynamic_baseline and i % 2 == 0]

# Extract peak values at even positions only
peak_values = [smoothed_signals[i] for i in peak_indices]

# Misleading energy calculation (dead end)
total_energy = sum([x**2 for x in peak_values])

# Actual signal refinement: normalize and round to fixed precision
refined_peaks = [round(pv / gain_factor, 4) for pv in peak_values]

# Simulate transmission loss on every third element (but doesn't affect outcome)
transmission_mask = [True if (i+1) % 3 != 0 else False for i in range(len(refined_peaks))]
distorted_peaks = [refined_peaks[i] for i in range(len(refined_peaks)) if transmission_mask[i]]

# Filtering condition based on original domain (reverse back to raw scale)
filtered_data = []
for val in refined_peaks:
    raw_estimation = (val / 1.4) - 0.8
    if raw_estimation > 3.0:  # corresponds to meaningful signal in original units
        filtered_data.append(val)

# Core processing function
def process_signals(peaks):
    if not peaks:
        return -1
    
    # Multi-step transformation
    log_scaled = [math.log(p) for p in peaks]
    mean_log = sum(log_scaled) / len(log_scaled)
    exp_back = math.exp(mean_log)
    
    # Final adjustment
    adjustment_factor = 1 + (len(peaks) * 0.1)
    return int(round(exp_back * adjustment_factor))

# Critical execution point
final_output = process_signals(filtered_data)

print(f"Result: {final_output}")