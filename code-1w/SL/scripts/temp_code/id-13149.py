import itertools

def analyze_trend(data):
    trend_changes = 0
    prev = data[0]
    for curr in data[1:]:
        if (curr > prev) != (data[0] > data[-1]):  # artificial pattern check
            trend_changes += 1
        prev = curr
    return trend_changes

def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

def calculate_performance(base, values):
    # Irrelevant transformation (distractor)
    normalized = [v / base for v in values]
    filtered = [v for v in normalized if v > 0.5]
    
    # Real computation begins
    log_vals = [len(str(int(v * 100))) for v in filtered]  # digit count after scaling
    total_impact = sum(log_vals)
    
    # Secondary path: counting sequences
    grouped = [len(list(group)) for k, group in itertools.groupby(log_vals)]
    sequence_penalty = sum(g for g in grouped if g > 1)  # punish repeated digit lengths
    
    # Dummy variables and red herrings
    peak_magnitude = max(values) * base
    stability_factor = len(values) - analyze_trend(values)
    dummy_shift = (peak_magnitude % 10) * stability_factor
    
    # Actual scoring logic
    raw_score = total_impact * base
    adjustment = sequence_penalty * 2
    final_score = raw_score - adjustment + dummy_shift * 0  # dummy_shift has no effect
    
    return int(final_score)

# Input data
baseline = 7
readings = [12.5, 18.3, 9.1, 14.7, 14.7, 6.2, 19.0, 19.0, 19.0]

# Signal smoothing (unused but plausible)
smoothed_readings = smooth_signal([r * 2 for r in readings])
denoised_avg = sum(smoothed_readings) / len(smoothed_readings)

# Key execution point
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")