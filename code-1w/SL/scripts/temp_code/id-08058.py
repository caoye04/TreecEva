def analyze_signal_strength(readings):
    smoothed = []
    for i in range(2, len(readings) - 2):
        avg = sum(readings[i-2:i+3]) / 5
        smoothed.append(avg)
    return smoothed

readings_data = [12, 15, 22, 30, 45, 50, 52, 49, 40, 35, 33, 40, 55, 60, 58, 50, 45, 42, 48, 58, 65]
efficiency_scores = [x * 0.8 + 5 for x in readings_data]

# Misleading transformation (not used in final path but looks relevant)
distorted_readings = [x ** 0.5 * 1.2 for x in readings_data]
baseline_offset = sum(distorted_readings[:5]) / 5

# Slice to focus on peak performance window
peak_window = efficiency_scores[5:15]

# Simulate signal smoothing
smoothed_efficiency = analyze_signal_strength([int(x) for x in efficiency_scores])

# Log creation with redundant processing
processing_log = []
for val in smoothed_efficiency:
    if val > 40:
        category = 'HIGH'
    elif val > 30:
        category = 'MEDIUM'
    else:
        category = 'LOW'
    processing_log.append((val, category))

# Efficiency log filtered and prepared
efficiency_log = [x for x in smoothed_efficiency if x > 35]

# Red herring: unused statistical computation
temp_moment = sum([x**3 for x in efficiency_log]) / len(efficiency_log) if efficiency_log else 0
trend_deviation = max(efficiency_log) - min(efficiency_log)

threshold = 42.5

# Core optimization logic
valid_segments = 0
for score in efficiency_log:
    if score >= threshold:
        valid_segments += 1

# Secondary filter using slicing
segment_pairs = [(efficiency_log[i], efficiency_log[i+1]) for i in range(len(efficiency_log)-1)]
stable_pairs = [p for p in segment_pairs if abs(p[0] - p[1]) < 3.0]

# Final allocation strategy
if len(stable_pairs) > 0:
    avg_stability = sum([sum(p)/2 for p in stable_pairs]) / len(stable_pairs)
else:
    avg_stability = 0

# Distractor: complex but unused structure
summary_grid = [[(i, j, abs(i-j)) for j in efficiency_log[:3]] for i in efficiency_log[:3]]

# Key function call
final_bandwidth = optimize_allocation(efficiency_log, threshold)

# Helper function defined after use (adds cognitive load)
def optimize_allocation(log, thresh):
    count_above = sum(1 for x in log if x >= thresh)
    total_sum = sum(log)
    if count_above == 0:
        return 0
    base_allocation = total_sum / count_above
    adjustment_factor = 1 + (len(log) * 0.05)
    # Real answer determined here
    result = base_allocation * adjustment_factor
    return round(result, 4)

print(f"Result: {final_bandwidth}")