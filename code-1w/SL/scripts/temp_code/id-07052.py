import math

# Simulated sensor data with noise and metadata
raw_signals = [0.7, 1.2, -0.3, 4.5, 2.1, -1.0, 3.3, 0.0, -2.4, 5.6]

timestamps = [1623456780 + i*60 for i in range(10)]
quality_flags = [True, True, False, True, True, False, True, True, True, True]

# Irrelevant calibration constants (distractor)
calibration_factor_a = 0.987
reference_offset_x = 1.023
baseline_noise_level = 0.05

# Signal preprocessing pipeline
filtered_data = [x for x, flag in zip(raw_signals, quality_flags) if flag]
smoothed_data = [math.sin(x) * math.cos(x) for x in filtered_data]

# Misleading transformation branch (dead path)
if len(smoothed_data) > 20:
    enhanced_signal = [x * 2 for x in smoothed_data]
else:
    temp_buffer = [abs(x) ** 0.5 for x in smoothed_data if x != 0]
    enhanced_signal = [math.log(y + 1) for y in temp_buffer]  # Not actually used later

# Primary data transformation with decoy intermediate steps
transformation_matrix = [math.exp(-i * 0.1) for i in range(len(smoothed_data))]
transformed_data = [a * b for a, b in zip(smoothed_data, transformation_matrix)]

# Dummy diagnostic functions that look important but aren't used
def compute_entropy(signal_list):
    return -sum(p * math.log(abs(p)) for p in signal_list if p != 0)

def normalize_signal(signal):
    norm = sum(abs(x) for x in signal)
    return [x / norm for x in signal] if norm else signal

# Real processing begins here — subtle due to distractions above
event_peaks = [x for x in transformed_data if x > 0.5]
peak_count = len(event_peaks)

# Decoy statistical analysis (irrelevant computations)
mean_value = sum(transformed_data) / len(transformed_data) if transformed_data else 0
variance = sum((x - mean_value)**2 for x in transformed_data) / len(transformed_data) if transformed_data else 0
deviation_flag = variance > 0.1

# Control flow with red herring condition
threshold = 0.6
activation_log = []
for val in transformed_data:
    if val > threshold:
        activation_log.append(True)
    elif val < -threshold:
        activation_log.append(False)
    else:
        continue  # Skips neutral values

# Another misleading aggregate
active_ratio = len(activation_log) / len(transformed_data) if transformed_data else 0

# Core logic hidden among distractors: pattern periodicity check
def analyze_pattern(data, thresh):
    significant = [i for i, x in enumerate(data) if x > thresh]
    if len(significant) < 2:
        return 0
    intervals = [significant[i+1] - significant[i] for i in range(len(significant)-1)]
    avg_interval = sum(intervals) / len(intervals)
    consistency = all(abs(x - avg_interval) < 1.5 for x in intervals)
    return int(avg_interval * 100) if consistency else sum(intervals)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Result: {final_diagnostic}")