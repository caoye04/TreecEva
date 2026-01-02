def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1] if data[i-1] != 0 else 0
        trend.append('up' if change > threshold else 'down' if change < -threshold else 'stable')
    return trend

baseline = [100, 105, 98, 110, 108]
readings = [100, 115, 130, 125, 140, 142]

# Irrelevant helper: counts fluctuations above noise level
lambda_filter = lambda seq, eps: len([x for x in seq if abs(x) > eps])
noise_levels = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
high_noise_count = lambda_filter(noise_levels, 8)  # Distractor computation

# Misleading transformation - not used later
transformed = [x * 1.1 for x in baseline if x > 102]
adjusted_baseline = [x * 1.05 for x in baseline]

# Simulate sensor drift correction (partially relevant)
corrected = []
drift_rate = 0.02
for i, val in enumerate(readings):
    corrected.append(val * (1 - drift_rate * i))

# Compute moving average as new reference
window_avg = [sum(corrected[i:i+3]) / 3 for i in range(len(corrected) - 2)]

# Analyze trend on corrected data
behavior = analyze_trend(corrected, threshold=0.08)

# Count significant upward trends
upward_shifts = sum(1 for b in behavior if b == 'up')

# Auxiliary calculation: stability score
stability = len([b for b in behavior if b == 'stable'])

# Primary logic chain
if len(window_avg) > 0 and window_avg[-1] > adjusted_baseline[-1]:
    performance_boost = (window_avg[-1] - adjusted_baseline[-1]) / adjusted_baseline[-1]
else:
    performance_boost = 0

# Apply non-linear weighting based on trend consistency
consistency_factor = 1 + (upward_shifts / len(behavior)) ** 0.5 if behavior else 1

# Dead code path - never executed due to condition
redundant_flag = False
if redundant_flag:
    temp_result = [x for x in transformed if x < 120]
    backup_score = sum(temp_result)

# Final performance calculation
def calculate_performance(base, obs):
    base_mean = sum(base) / len(base)
    obs_mean = sum(obs) / len(obs)
    raw_gain = obs_mean - base_mean
    normalized_gain = raw_gain / base_mean
    return int(normalized_gain * 1000 + stability * 5 + upward_shifts * 10)

final_score = calculate_performance(baseline, readings)

# Print result
print(f"Result: {final_score}")