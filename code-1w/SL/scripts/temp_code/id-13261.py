from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor: some values are irrelevant)
sensor_inputs = [145, 128, 133, 150, 142, 138, 147, 139, 144, 141]

# Irrelevant preprocessing - red herring
calibration_offset = sum([math.sin(x * 0.01) for x in range(len(sensor_inputs))])
adjusted_readings = [x + int(calibration_offset) for x in sensor_inputs]
duplicate_counter = Counter(adjusted_readings)

# Real data pipeline starts here
raw_data_stream = [x for x in sensor_inputs if x > 130]  # filter noise

# Multiple assignment and distractor variables
total_samples, outlier_count = len(raw_data_stream), 0
stats_log = defaultdict(lambda: 0)
stats_log['processed'] = total_samples

# Decoy function - never called
def deprecated_analysis(data):
    return [d ** 0.5 for d in data if d % 2 == 0]

# Misleading intermediate transformation
shadow_copy = [x * 1.05 for x in raw_data_stream]
outlier_flags = [False] * len(shadow_copy)

for i, val in enumerate(shadow_copy):
    if val > 148:
        outlier_flags[i] = True
        outlier_count += 1

# Another decoy structure
class DataFilter:
    def __init__(self, limit):
        self.limit = limit
        self.cache = []

    def apply(self, x):
        return x < self.limit

# Unused instance - distraction
filter_instance = DataFilter(140)

# Core logic embedded within distractions
effective_values = [x for x in raw_data_stream if x >= 138]
scaling_factor = 0.97
scaled_metrics = list(map(lambda x: x * scaling_factor, effective_values))

# Conditional branching with nesting level 3
if len(scaled_metrics) > 3:
    avg_metric = sum(scaled_metrics) / len(scaled_metrics)
    if avg_metric > 135:
        deviation_scores = []
        for v in scaled_metrics:
            deviation = abs(v - avg_metric)
            if deviation > 5:
                stats_log['deviant'] += 1
            normalized_dev = deviation / avg_metric * 100
            deviation_scores.append(normalized_dev)
        
        # Real computation path
        if deviation_scores:
            max_deviation = max(deviation_scores)
            base_threshold = 12.5
            adjustment = len(deviation_scores) * 0.15
            dynamic_barrier = base_threshold - adjustment
            
            # Critical decision point
            if max_deviation < dynamic_barrier:
                health_index = int(avg_metric) + 5
            else:
                health_index = int(avg_metric) - 3
    else:
        health_index = 100  # unreachable due to data
else:
    health_index = 50  # dead code

# Secondary analysis on original data - subtle reuse
data_freq = {}
for val in sensor_inputs:
    data_freq[val] = data_freq.get(val, 0) + 1

# Complex conditional with bit manipulation red herring
flag_state = 0b1010
mask_applied = flag_state & 0b1100
shifted_flag = mask_applied >> 2

# Distractor: unused recursive function
def trace_path(node, depth=0):
    if depth > 2:
        return 1
    return trace_path(node+1, depth+1) + node

# Threshold configuration (only this matters at end)
thresholds = {
    'critical': 140,
    'warning': 130,
    'decay_rate': 0.95
}

# Real but obscured final processing
health_data = {
    'readings': effective_values,
    'index': health_index,
    'deviations': deviation_scores if 'deviation_scores' in locals() else []
}

# Function that looks generic but contains key logic
def analyze_metrics(data, config):
    base = data['index']
    readings = data['readings']
    n = len(readings)
    
    # Summation with modular arithmetic twist
    checksum = 0
    for i, r in enumerate(readings):
        checksum += (r * (i + 1)) % 17
    
    # Final transformation
    adjusted_base = base * config['decay_rate']
    final_score = adjusted_base + (checksum % n if n > 0 else 0)
    
    # Tiebreaker logic
    if final_score % 1 == 0:
        final_score += 0.75  # force decimal result
    
    return round(final_score, 6)

# Execution point of interest
final_diagnostic = analyze_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")