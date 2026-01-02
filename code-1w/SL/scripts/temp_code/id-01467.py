from collections import defaultdict
from itertools import combinations

# Simulate sensor data aggregation and threshold analysis for environmental monitoring
raw_readings = [14, 28, 19, 35, 22, 17, 24, 31]
weights = [0.8, 1.2, 0.9, 1.5, 1.1, 0.7, 1.3, 1.0]

# Apply weighted transformation to sensor readings
data_stream = [r * w for r, w in zip(raw_readings, weights)]

# Misleading normalization (not used in final calculation)
normalized = [x / sum(data_stream) for x in data_stream]
scaling_factor = sum(normalized)  # Red herring: always equals 1.0

# Group readings into flow windows using modulo patterns
flow_data = defaultdict(float)
for i, val in enumerate(data_stream):
    bucket = i % 3
    flow_data[bucket] += val

# Define dynamic thresholds based on powers and logarithmic scaling
base_threshold = 2 ** 4
log_adjustment = int(10 * __import__('math').log(base_threshold))
thresholds = {k: base_threshold + log_adjustment * (k + 1) for k in range(3)}

# Spurious secondary structure (dead code path)
flagged_buckets = []
for b in flow_data:
    if flow_data[b] > thresholds[b] * 1.1:  # Not actually used
        flagged_buckets.append(b)

# Auxiliary computation with partial relevance
combination_peaks = []
for combo in combinations(flow_data.keys(), 2):
    combined_flow = flow_data[combo[0]] + flow_data[combo[1]]
    peak_estimate = combined_flow % 25
    combination_peaks.append(peak_estimate)

# Core logic disguised among distractions
def calculate_equilibrium(flows, limits):
    score = 0
    for key in flows:
        if flows[key] >= limits[key]:
            residual = int(flows[key] - limits[key])
            score += residual % 7
        else:
            deficit = int(limits[key] - flows[key])
            score -= deficit % 5
    return abs(score) + 5  # Final adjustment

# Critical execution point
equilibrium_score = calculate_equilibrium(flow_data, thresholds)

# Additional red herring: unused statistical check
mean_peak = sum(combination_peaks) / len(combination_peaks) if combination_peaks else 0
variance_check = (mean_peak - 5.0) ** 2 < 1.5  # Distractor

# Print result as required
Result: {equilibrium_score}