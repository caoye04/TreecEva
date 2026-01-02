from collections import defaultdict, Counter

# Simulated system telemetry data
def collect_telemetry():
    signals = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    response_times = [120, 300, 150, 90, 450, 200, 180, 210, 500, 320]
    errors = [0, 1, 0, 0, 1, 0, 0, 0, 2, 1]
    return signals, response_times, errors

signals, rt_data, err_log = collect_telemetry()

# Irrelevant preprocessing: normalize signals (not used later)
normalized_signals = [x * 0.5 + 0.1 for x in signals if x > -1]

# Compute engagement from active signals
total_engagement = sum(1 for s in signals if s == 1)
active_duration = sum(rt_data) / len(rt_data) if rt_data else 0

# Misleading metric: error rate (calculated but not used in final logic)
error_rate = sum(err_log) / len(err_log) if len(err_log) > 0 else 0
error_flags = [e > 0 for e in err_log]
temp_correction_factor = 1.05 if any(error_flags) else 1.0

# Latency classification based on thresholds
latency_bins = defaultdict(int)
for rt in rt_data:
    if rt < 100:
        latency_bins['low'] += 1
    elif rt < 300:
        latency_bins['medium'] += 1
    else:
        latency_bins['high'] += 1

# Auxiliary analysis: frequency count of response time categories
freq_count = Counter(latency_bins)
adjusted_freq = {k: v * 0.9 for k, v in freq_count.items()}  # Distractor calculation

# Determine primary latency tier
primary_tier = max(latency_bins, key=lambda x: latency_bins[x])

def process_metrics(engagement, latency_profile):
    base_score = engagement * 10
    
    # Apply latency penalty
    if latency_profile == 'high':
        penalty = 25
    elif latency_profile == 'medium':
        penalty = 10
    else:
        penalty = 0
        
    # Conditional adjustment using ternary-like expression
    multiplier = 1.2 if engagement >= 6 else 0.8
    intermediate = base_score - penalty
    final = intermediate * multiplier
    
    # Dead code branch: never executed due to logic above
    if False and engagement == 0:
        final = -1
        
    return int(final)

# Key statement
final_score = process_metrics(total_engagement, primary_tier)

# Output result
print(f"Result: {final_score}")