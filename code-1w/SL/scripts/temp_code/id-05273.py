from itertools import combinations

# Simulate sensor data from a thermal regulation system
def collect_sensor_readings():
    base_temps = [22.1, 23.5, 24.0, 21.8, 25.3]
    fluctuations = [0.1 * i for i in range(5)]
    adjusted = [base_temps[i] + fluctuations[i] for i in range(len(base_temps))]
    return adjusted

# Filter out readings beyond safe operating range
def filter_anomalies(data, threshold=26.0):
    return [x for x in data if x < threshold]

# Calculate energy dispersion across sensor pairs
def compute_dispersion(valid_data):
    dispersion_pairs = list(combinations(valid_data, 2))
    total_dispersion = 0.0
    for pair in dispersion_pairs:
        total_dispersion += abs(pair[0] - pair[1])
    return total_dispersion

# Determine system stability based on fluctuation trends
def assess_stability(readings):
    trend_changes = 0
    for i in range(1, len(readings) - 1):
        prev_diff = readings[i-1] - readings[i]
        curr_diff = readings[i] - readings[i+1]
        if (prev_diff > 0 and curr_diff < 0) or (prev_diff < 0 and curr_diff > 0):
            trend_changes += 1
    # Distractor: unused calculation
    hypothetical_cycles = len(readings) ** 2 - len(readings)
    return trend_changes

# Main efficiency calculation
def calculate_efficiency(data_segment):
    if not data_segment:
        return 0.0
    
    # Primary metric: average temperature
    avg_temp = sum(data_segment) / len(data_segment)
    
    # Secondary metric: peak-to-peak variation
    ptp_variation = max(data_segment) - min(data_segment)
    
    # Tertiary: number of micro-fluctuations above threshold
    micro_events = 0
    for i in range(1, len(data_segment)):
        if abs(data_segment[i] - data_segment[i-1]) > 0.5:
            micro_events += 1
    
    # Efficiency formula (deterministic computation)
    raw_efficiency = avg_temp * 10 - ptp_variation * 5 + micro_events * 2
    
    # Normalization step (ensures deterministic result)
    normalized_efficiency = max(1.0, min(raw_efficiency, 100.0))
    
    # Distractor variables (not used in final result)
    dummy_weight = 0.75
    temp_cache = {i: normalized_efficiency / (i+1) for i in range(3)}
    adjustment_factor = len(temp_cache)  # Unused
    
    return round(normalized_efficiency, 4)

# System initialization and execution
if __name__ == '__main__':
    raw_readings = collect_sensor_readings()
    filtered_readings = filter_anomalies(raw_readings)
    dispersion_value = compute_dispersion(filtered_readings)
    stability_index = assess_stability(filtered_readings)
    processed_data = [round(x * 1.02, 3) for x in filtered_readings]  # Apply calibration
    
    # Irrelevant transformation chain (distractor)
    scaled_data = [x * 1.1 for x in processed_data]
    shifted_data = [x + 0.5 for x in scaled_data]
    aggregated_metric = sum(shifted_data) / len(shifted_data) if shifted_data else 0
    
    efficiency_score = calculate_efficiency(processed_data)
    
    # Final output
    print(f"Result: {efficiency_score}")