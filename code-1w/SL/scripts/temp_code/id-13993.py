import math

def analyze_pattern(sequence):
    temp_peaks = []
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            temp_peaks.append(i)
    return temp_peaks

# Simulate sensor data drift (irrelevant for final result)
sensor_drift_compensation = lambda x: [val * 1.02 + 0.5 for val in x]
data_raw = [12, 15, 10, 20, 18, 25, 16, 22, 14]
data_adjusted = sensor_drift_compensation(data_raw)

# Misleading transformation: looks important but unused later
distorted_data = [math.sin(x / 5) * 100 for x in data_raw]

# Core processing pipeline
def compute_stability_index(values):
    diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
    avg_change = sum(diffs) / len(diffs)
    variance = sum((d - avg_change) ** 2 for d in diffs) / len(diffs)
    return round(math.sqrt(variance), 4)

baseline_threshold = 8.5
event_markers = analyze_pattern(data_raw)

# Secondary metric with distractor variables
amplitude_fluctuations = []
for j in event_markers:
    prev_val = data_raw[j-1]
    next_val = data_raw[j+1]
    fluctuation = abs(prev_val - next_val)
    amplitude_fluctuations.append(fluctuation)

# Unused diagnostic stats (distractors)
total_energy = sum(x**2 for x in data_raw)
peak_count_analysis = len(event_markers) * 2.5

# Actual logic contributing to answer
raw_sum = sum(data_raw)
adjusted_sum = sum(data_adjusted)
consistency_factor = compute_stability_index(data_raw)

# Key intermediate calculation
normalization_constant = 1000 / (raw_sum + 1)
weighted_base = raw_sum * normalization_constant

# Final metrics
reliability_ratio = len(event_markers) / (consistency_factor + 1)

# Efficiency score formula (this is the target variable)
efficiency_score = weighted_base - (reliability_ratio * 10)

# Additional red herring function
def debug_print_summary():
    print(f"Debug: total_energy={total_energy}")
    print(f"Debug: peak_count_analysis={peak_count_analysis}")

# This call does nothing impactful
debug_print_summary()

# Critical execution point
final_output = efficiency_score

print(f"Result: {final_output}")