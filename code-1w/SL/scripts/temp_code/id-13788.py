from collections import defaultdict

# Simulate sensor data processing with noise filtering and state tracking
def process_sensor_readings(readings):
    total_samples = len(readings)
    valid_count = 0
    cumulative_value = 0
    noise_events = 0
    temp_buffer = []
    state_log = defaultdict(int)

    for i, val in enumerate(readings):
        # Irrelevant noise modeling (distractor)
        if abs(val - 50) > 40:
            noise_events += 1
            state_log['noise'] += 1
            continue

        # Core logic: filter and transform
        adjusted_val = val * 0.9 + 5
        if adjusted_val < 0:
            adjusted_val = 0
        
        # Track valid data
        temp_buffer.append(adjusted_val)
        cumulative_value += adjusted_val
        valid_count += 1
        state_log['processed'] += 1

    # Distractor computation: unused statistical moment
    if valid_count > 0:
        mean_val = cumulative_value / valid_count
        variance_accum = sum((x - mean_val) ** 2 for x in temp_buffer)
        unused_skewness = sum(((x - mean_val) ** 3) for x in temp_buffer)  # Dead-end calc

    # Semi-relevant transformation
    normalized_total = cumulative_value * (0.95 if noise_events > 2 else 1.0)

    return normalized_total, valid_count

# Analyze multiple sensor streams
def calculate_final_score(streams):
    global_stats = {
        'aggregated_power': 0,
        'total_valid': 0,
        'stream_bonuses': 0
    }
    
    bonus_tracker = []
    
    for idx, stream in enumerate(streams):
        processed_total, count = process_sensor_readings(stream)
        
        # Real contribution to answer
        global_stats['aggregated_power'] += processed_total * 1.1
        global_stats['total_valid'] += count
        
        # Distractor: bonus logic that doesn't affect final_score
        stream_quality = count / len(stream) if stream else 0
        if stream_quality > 0.8:
            bonus_tracker.append((idx, stream_quality))
            global_stats['stream_bonuses'] += 1  # Unused

    # Final score calculation — depends only on aggregated_power
    base_score = global_stats['aggregated_power']
    adjustment_factor = 0.98 + (global_stats['total_valid'] * 0.001)
    final_score = int(base_score * adjustment_factor)  # Key statement
    
    # Red herring: complex bitwise mix that's not used
    debug_signature = (len(bonus_tracker) << 3) ^ int(base_score % 100)
    
    return final_score

# Input data: multi-sensor readings (simulated)
sensor_streams = [
    [60, 55, 70, 80, 45, 50, 52],
    [40, 48, 53, 51, 47, 49],
    [75, 85, 42, 58, 63, 54, 46, 50],
    [30, 52, 49, 51, 56]  # Contains one outlier (30)
]

# Execute main logic
final_score = calculate_final_score(sensor_streams)
print(f"Result: {final_score}")