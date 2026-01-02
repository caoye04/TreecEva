import math

# Simulated sensor array data (irrelevant in part)
sensor_offsets = [0.1, -0.3, 0.4, 0.05]
baseline_adjustment = sum([abs(x) for x in sensor_offsets]) / len(sensor_offsets)

def deprecated_normalizer(data):
    # Obsolete function - never called
    return [x / max(data) for x in data]

def moving_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        end = i + 1
        window_avg = sum(values[start:end]) / (end - start)
        smoothed.append(round(window_avg, 2))
    return smoothed

# Core health metrics from biomedical sensors
raw_readings = [78, 85, 90, 92, 88, 84, 80, 76, 73, 70]

# Irrelevant transformation chain
transform_chain = lambda x: x ** 0.5
interim_signal = [transform_chain(val + 10) for val in raw_readings]
denoised_signal = moving_average(interim_signal)

# Red herring: fake classification using set operations (unused)
abnormal_set = {78, 85, 92, 70}
critical_set = {92, 70}
dubious_flags = abnormal_set & critical_set  # {70, 92}
false_alarm_risk = len(dubious_flags) > 1 and max(raw_readings) >= 90

# Real processing begins here
filtered_readings = [val for val in raw_readings if val > 75]

# Compute statistical descriptors (some are distractions)
mean_val = sum(filtered_readings) / len(filtered_readings)
variance_proxy = sum([(x - mean_val) ** 2 for x in filtered_readings]) / len(filtered_readings)
std_dev = math.sqrt(variance_proxy)
median_val = sorted(filtered_readings)[len(filtered_readings) // 2]

# Threshold logic based on adaptive criterion
steep_drop_count = 0
for i in range(1, len(filtered_readings)):
    if filtered_readings[i] < filtered_readings[i-1] - 3:
        steep_drop_count += 1

# Decoy counter: tracks drops but isn't used in final logic
decoys_triggered = 0
if steep_drop_count >= 2:
    decoys_triggered += 1
if std_dev > 5.0:
    decoys_triggered += 1

# Actual threshold function used in processing
threshold_func = lambda x: x < (mean_val - 1.1 * std_dev)

# Health state categorization with distractor logic
state_map = {}
for idx, val in enumerate(filtered_readings):
    if val >= mean_val + std_dev:
        state_map[idx] = 'high'
    elif threshold_func(val):
        state_map[idx] = 'low'
    else:
        state_map[idx] = 'normal'

# Auxiliary unused diagnostic (red herring)
entropy_estimate = 0.0
if 'low' in state_map.values() or 'high' in state_map.values():
    counts = {k: list(state_map.values()).count(k) for k in set(state_map.values())}
    entropy_estimate = -sum((cnt / len(state_map)) * math.log2(cnt / len(state_map)) 
                          for cnt in counts.values())

# Core accumulation logic: count sustained declines
sustained_decline_streak = 0
temp_streak = 0
for i in range(1, len(filtered_readings)):
    if filtered_readings[i] < filtered_readings[i-1]:
        temp_streak += 1
        sustained_decline_streak = max(sustained_decline_streak, temp_streak)
    else:
        temp_streak = 0

# Secondary metric: recovery signal
recovery_signal = 0
for i in range(2, len(filtered_readings)):
    if (filtered_readings[i] > filtered_readings[i-1] > filtered_readings[i-2]):
        recovery_signal += 1

# Main data structure used in final computation
health_data = {
    'readings': filtered_readings,
    'streak': sustained_decline_streak,
    'recoveries': recovery_signal,
    'states': state_map,
    'baseline': mean_val,
    'noise_floor': baseline_adjustment,  # Unused
    'entropy': entropy_estimate      # Unused
}

# Critical processing function
def process_metrics(data, threshold_logic):
    readings = data['readings']
    streak = data['streak']
    recoveries = data['recoveries']
    states = data['states']
    base = data['baseline']
    
    # Count how many values fall below dynamic threshold
    low_count = sum(1 for v in readings if threshold_logic(v))
    
    # Complex interaction between streaks and recoveries
    if streak >= 3 and low_count >= 2:
        risk_mod = 3
    elif streak >= 2 and recoveries <= 1:
        risk_mod = 2
    else:
        risk_mod = 1
    
    # Final diagnostic score: combination of multiple factors
    severity_index = 0
    for i, val in enumerate(readings):
        if i in states and states[i] == 'low':
            severity_index += (base - val) * risk_mod
    
    # Additional adjustment based on recovery pattern
    if recoveries >= 2 and low_count <= 1:
        severity_index *= 0.5  # Improvement reduces severity
    
    # Final nonlinear transformation
    diagnostic_score = int((severity_index ** 1.1) + (streak * 1.5) - (recoveries * 0.8))
    
    return diagnostic_score

# Execute main logic
final_diagnostic = process_metrics(health_data, threshold_func)

# Print result as required
print(f"Result: {final_diagnostic}")