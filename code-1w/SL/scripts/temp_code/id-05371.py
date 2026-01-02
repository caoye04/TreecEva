def analyze_trends(values, window_size=3):
    trends = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        avg = sum(window) / window_size
        trend = 'up' if window[-1] > window[0] else 'down' if window[-1] < window[0] else 'stable'
        trends.append((avg, trend))
    return trends

# Simulated sensor readings over time
sensor_data = [104.5, 105.0, 106.8, 98.2, 97.1, 96.9, 101.3, 102.7, 103.0]

# Irrelevant transformation - distractor
transformed = [round(x * 1.01 + 0.5) for x in sensor_data]
dropped = [t for t in transformed if t > 100]

# Analyze movement patterns (used later)
movements = []
for i, (curr, prev) in enumerate(zip(sensor_data[1:], sensor_data[:-1])):
    change = curr - prev
    direction = 'positive' if change > 0 else 'negative' if change < 0 else 'none'
    movements.append({'step': i+1, 'delta': change, 'dir': direction})

# Threshold logic for anomaly detection (partially relevant)
anomaly_flags = []
critical_threshold = 102.5
warning_threshold = 97.5
for val in sensor_data:
    if val > critical_threshold:
        flag = 'CRITICAL'
    elif val < warning_threshold:
        flag = 'WARNING'
    else:
        flag = 'NORMAL'
    anomaly_flags.append(flag)

# Secondary processing: group consecutive similar flags
flag_groups = []
current_group = {'type': anomaly_flags[0], 'count': 1}
for f in anomaly_flags[1:]:
    if f == current_group['type']:
        current_group['count'] += 1
    else:
        flag_groups.append(current_group.copy())
        current_group = {'type': f, 'count': 1}
flag_groups.append(current_group)

# Count how many times CRITICAL appears in groups (distractor)
critical_count = sum(1 for g in flag_groups if g['type'] == 'CRITICAL')

# Core calculation function
def calculate_stability_index(data):
    diffs = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    avg_diff = sum(diffs) / len(diffs)
    stability = 100 / (1 + avg_diff)  # higher stability when changes are small
    return round(stability, 2)

# Another helper - computes volatility score
def compute_volatility(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean)**2 for x in data) / len(data)
    return round(variance ** 0.5, 3)

# Volatility is computed but only partially used
volatility_score = compute_volatility(sensor_data)

# Main scoring logic
thresholds = {
    'high': 102.0,
    'low': 97.0
}

def calculate_final_score(raw_data, limits):
    high_lim = limits['high']
    low_lim = limits['low']
    
    # Step 1: count out-of-bound readings
    oob_count = 0
    for val in raw_data:
        if val > high_lim or val < low_lim:
            oob_count += 1
    
    # Step 2: calculate base penalty
    base_penalty = oob_count * 5
    
    # Step 3: assess trend continuity using enumerate and zip
    upward_runs = 0
    for i, (curr, next_val) in enumerate(zip(raw_data[:-1], raw_data[1:])):
        if next_val > curr:
            # Check if this is part of a longer upward sequence
            run_length = 1
            j = i
            while j < len(raw_data) - 1 and raw_data[j+1] > raw_data[j]:
                run_length += 1
                j += 1
            if run_length >= 2:
                upward_runs += 1
    
    # Bonus for sustained upward trends toward optimal zone
    trend_bonus = upward_runs * 3 if upward_runs >= 2 else 0
    
    # Step 4: stability contribution
    stability_index = calculate_stability_index(raw_data)
    stability_contribution = int(stability_index / 2)  # max ~50
    
    # Final score computation
    initial_score = 100
    final_adjustment = initial_score - base_penalty + trend_bonus + stability_contribution
    
    # Dead code branch - red herring
    if volatility_score > 5.0:
        final_adjustment *= 0.9  # not triggered
    
    return int(final_adjustment)

# Execute main logic
data = sensor_data
trend_analysis = analyze_trends(data)
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")