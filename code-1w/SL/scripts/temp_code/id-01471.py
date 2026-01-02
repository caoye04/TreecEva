from collections import defaultdict

# Simulate sensor data readings over time with some noise
data = [102, 95, 110, 98, 100, 103, 97, 101, 105, 96, 108, 99]

# Irrelevant baseline metrics (distractor)
baseline_avg = sum(range(90, 100)) / 10
offset_correction = 0.75
adjusted_readings = [x - offset_correction for x in data if x > 90]  # Partial filtering

# Thresholds for different severity levels (used later)
thresholds = {
    'warning_low': 98,
    'warning_high': 102,
    'critical_low': 95,
    'critical_high': 105
}

# Track occurrences per category (semi-relevant)
counts = defaultdict(int)
for val in data:
    if val < thresholds['warning_low']:
        counts['low'] += 1
    elif val > thresholds['warning_high']:
        counts['high'] += 1
    else:
        counts['normal'] += 1

# Compute moving average for smoothing (distractor computation)
window_size = 3
smoothed = []
for i in range(len(data) - window_size + 1):
    smoothed.append(sum(data[i:i+window_size]) / window_size)

# Auxiliary function to compute stability index (not used in final score)
def compute_stability_index(values):
    diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
    return sum(diffs) / len(diffs)

# Another unused helper — adds cognitive load
def apply_filter(sequence, mode='low_pass'):
    factor = 0.9 if mode == 'low_pass' else 0.1
    result = [sequence[0]]
    for x in sequence[1:]:
        result.append(result[-1] * factor + x * (1 - factor))
    return result

# Core scoring logic
def calculate_final_score(readings, limits):
    score = 0
    warning_range = list(range(limits['warning_low'], limits['warning_high'] + 1))
    
    # Assign points based on proximity to ideal (100)
    for reading in readings:
        if reading == 100:
            score += 10
        elif reading in warning_range:
            score += 5
        elif abs(reading - 100) <= 10:
            score += 3
        else:
            score -= 2  # penalty for extreme values
    
    # Apply multiplier based on critical threshold breaches
    critical_breaches = 0
    for r in readings:
        if r < limits['critical_low'] or r > limits['critical_high']:
            critical_breaches += 1
    
    multiplier = 0.9 if critical_breaches > 2 else 1.0
    
    # Final adjustment using slice-based pattern check (last 5 readings)
    recent_trend = readings[-5:]
    improving = all(recent_trend[i] <= recent_trend[i+1] for i in range(len(recent_trend)-1))
    if improving and len(recent_trend) >= 2:
        score = int(score * 1.1)
    
    return int(score * multiplier)

# Execute main calculation
final_score = calculate_final_score(data, thresholds)

# Print result as required
print(f"Target result: {final_score}")