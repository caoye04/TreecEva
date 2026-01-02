from itertools import groupby

def analyze_transitions(sequence):
    transitions = 0
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            transitions += 1
    return transitions

# Simulate sensor state changes over time
sensor_log = '111100001111000011110000'
state_changes = analyze_transitions(sensor_log)

# Extract runs of consecutive states
consecutive_runs = [len(list(group)) for key, group in groupby(sensor_log)]
long_runs = sum(1 for run in consecutive_runs if run >= 4)
short_runs = sum(1 for run in consecutive_runs if run < 4)

# Background process: calculate entropy (unused distractor)
import math
total_bits = len(sensor_log)
ones_count = sensor_log.count('1')
zeros_count = sensor_log.count('0')
if ones_count and zeros_count:
    entropy = -(ones_count/total_bits) * math.log2(ones_count/total_bits) \
              -(zeros_count/total_bits) * math.log2(zeros_count/total_bits)
else:
    entropy = 0.0

# Secondary metric: position-weighted score (semi-relevant but not used directly)
weighted_score = 0
for idx, val in enumerate(sensor_log[:12]):
    if val == '1':
        weighted_score += idx * 0.5

# Misleading intermediate calculation
baseline_offset = sum(consecutive_runs[::2]) - sum(consecutive_runs[1::2])
adjustment_factor = abs(baseline_offset) % 7

# Core evaluation logic
metric_data = [
    state_changes * 2,
    long_runs * 5,
    short_runs * -3,
    len(consecutive_runs) + adjustment_factor
]

base_threshold = 10

# Key function that determines final result
def evaluate_performance(metrics, threshold):
    total = 0
    penalties = 0
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            if val > threshold:
                total += val // 2
        else:
            total += val
            if val < 0:
                penalties += 1
    # Final adjustment based on penalty count
    return total - (penalties * 2)

final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")