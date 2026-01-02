def analyze_temperature_data(raw_readings):
    # Irrelevant transformation: normalize readings (not used in final logic)
    normalized = [round((x - 32) * 5/9, 2) for x in raw_readings]
    
    # Filter valid high-precision measurements
    valid_readings = [r for r in raw_readings if r >= 0 and r % 1 == 0]
    
    # Misleading statistical computation
    avg_temp = sum(valid_readings) / len(valid_readings) if valid_readings else 0
    temp_variance = sum((x - avg_temp) ** 2 for x in valid_readings) / len(valid_readings) if valid_readings else 0

    # Distraction: simulate calibration offset (unused)
    calibration_map = {i: round(avg_temp * 0.05 * i, 3) for i in range(5)}
    adjustment_factor = sum(calibration_map.values()) * 0.1

    # Process readings: convert to integer ranks based on thresholds
    ranked = []
    for val in valid_readings:
        if val > 75:
            ranked.append(3)
        elif val > 60:
            ranked.append(2)
        else:
            ranked.append(1)
    
    # Use set to deduplicate rank patterns (concept: set operations)
    unique_ranks = set(ranked)
    rank_frequency = {r: ranked.count(r) for r in unique_ranks}  # dict comprehension

    # Simulate multi-stage quality scoring
    base_score = 0
    for r in ranked:
        if r == 3:
            base_score += 15
        elif r == 2:
            base_score += 8
        else:
            base_score += 3

    # Extra distraction: sort frequency keys unnecessarily
    sorted_ranks = sorted(rank_frequency.keys())
    decay_penalty = 0
    for i, rk in enumerate(sorted_ranks):
        decay_penalty += rk * 0.5 * (i + 1)

    # Final adjustment using only base_score and fixed logic
    stability_bonus = len(unique_ranks) * 2
    final_assessment = base_score + stability_bonus - int(decay_penalty)

    return final_assessment


def calculate_final_score(data):
    # Additional irrelevant preprocessing
    processed = [x.upper() for x in data if isinstance(x, str)]
    char_count = sum(len(s) for s in processed)
    
    # Dummy control flow with dead end
    threshold = 10
    if char_count > threshold:
        scaling = 1.0
    else:
        scaling = 1.0  # same result either way

    # Actual contribution: constant offset
    return 42 + len(processed)

# Main execution
sensor_inputs = [68, 70, 77, 62, 85, 55, 73, -5, 70.5, 88]
data_labels = ['A', 'B', 'C', 'D']

# Key processing step
processed_data = analyze_temperature_data(sensor_inputs)

# Statement of interest
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")