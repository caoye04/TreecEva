from collections import defaultdict

# Simulate sensor data processing with performance scoring
def analyze_readings(data_stream):
    readings_count = defaultdict(int)
    anomalies = []
    total_power = 0
    normalization_factor = 1.5

    for i, reading in enumerate(data_stream):
        readings_count[reading % 4] += 1
        
        if reading > 100:
            anomalies.append(i)
        
        # Irrelevant transformation
        temp_offset = (reading * 0.1) ** 0.5
        total_power += reading ** 2

    # Distractor computation - not used later
    avg_power = total_power / len(data_stream) if data_stream else 0
    spike_rate = len(anomalies) / len(data_stream)

    return readings_count, spike_rate


def calculate_performance(flags, stats):
    base_score = 0
    penalty = 0
    
    # Complex conditional logic with red herrings
    for key, value in stats.items():
        if key in flags and flags[key]:
            base_score += value * 10
        elif key == 0:
            base_score += 5
        else:
            penalty += 2

    # Extra computation that looks important but isn't fully impactful
    adjustment = len(flags) - len(stats)
    if adjustment > 0:
        base_score += adjustment * 3

    return base_score - penalty

# Main execution
sensor_data = [12, 45, 67, 89, 105, 23, 44, 76, 98, 110]
processed_counts, rate = analyze_readings(sensor_data)

# Misleading intermediate transformations
bonus_flags = {0: True, 1: False, 2: True, 3: False}
scaling_vector = [1.1, 0.9, 1.2]  # Unused dead weight
offset_correction = sum([x for x in scaling_vector]) / 3  # Distractor

metrics = {}
for k, v in processed_counts.items():
    if k % 2 == 0:
        metrics[k] = v + 1
    else:
        metrics[k] = v

# Key statement
final_score = calculate_performance(bonus_flags, metrics)

# Additional irrelevant tracking
status_log = []
for idx, val in enumerate(zip(sensor_data, [x*2 for x in sensor_data])):
    status_log.append(f"Sample {idx}: {val[0]} -> {val[1]}")

print(f"Result: {final_score}")