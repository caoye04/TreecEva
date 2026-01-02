def analyze_trend(data, threshold=5):
    trend_flags = []
    cumulative = 0
    temp_offset = 0

    for i, value in enumerate(data):
        if value > threshold:
            trend_flags.append(1)
            cumulative += (i + 1) * value
        else:
            trend_flags.append(0)
            temp_offset += i
    
    # Irrelevant transformation
    reversed_flags = trend_flags[::-1]
    ignored_sum = sum(reversed_flags[:3]) if len(reversed_flags) > 3 else 0

    return cumulative - temp_offset


def detect_peaks(values):
    peaks = [i for i in range(1, len(values)-1) if values[i-1] < values[i] > values[i+1]]
    peakiness = sum(values[i] for i in peaks)
    return peakiness


def calculate_performance(records):
    base_metric = 0
    adjustment_factor = 0
    noise_counter = 0

    # Extract time-series observations
    observations_only = [r[1] for r in records]
    timestamps = [r[0] for r in records]
    
    # Red herring computation
    delta_times = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_interval = sum(delta_times) / len(delta_times) if delta_times else 0
    
    # Real logic begins
    base_metric = analyze_trend(observations_only, threshold=4)
    
    for idx, (ts, val) in enumerate(zip(timestamps, observations_only)):
        if val % 2 == 0 and ts % 2 == 1:
            adjustment_factor += (idx + 1) * (val // 2)
        elif val > 5:
            noise_counter += 1  # unused later

    secondary_boost = detect_peaks(observations_only)
    
    # Distractor: complex-looking but unused bitwise combination
    magic_key = 0
    for x in observations_only:
        magic_key ^= (x << 1) | 1
        magic_key &= 255
    
    final_score = base_metric + adjustment_factor + secondary_boost // 2
    
    return final_score

# Main execution
observations = [(1, 6), (2, 3), (3, 8), (4, 2), (5, 9), (6, 4), (7, 7)]
final_score = calculate_performance(observations)
print(f"Result: {final_score}")