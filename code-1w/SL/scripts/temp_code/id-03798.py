from itertools import compress, count

# Simulate environmental sensor readings over time
temperature_readings = [22, 24, 19, 25, 27, 23, 20, 26, 28, 24]
humidity_readings = [50, 55, 60, 62, 58, 54, 61, 59, 56, 53]
co2_levels = [400, 410, 395, 420, 430, 415, 390, 425, 440, 405]

# Auxiliary data (distractor)
sensor_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010']
calibration_offsets = [0.1, -0.2, 0.05, 0.15, -0.1, 0.0, 0.2, -0.05, 0.1, -0.15]

# Distractor: unrelated statistical tracking
running_averages = []
for i in range(1, len(temperature_readings) + 1):
    avg = sum(temperature_readings[:i]) / i
    running_averages.append(round(avg, 2))

# Threshold function based on adaptive conditions
threshold_func = lambda t, h: t > 23 and h < 60

# Secondary helper (semi-relevant but not directly used in final logic)
def filter_stable_ranges(data, window=3):
    stable_flags = []
    for i in range(len(data) - window + 1):
        window_vals = data[i:i+window]
        if max(window_vals) - min(window_vals) <= 2:
            stable_flags.append(True)
        else:
            stable_flags.append(False)
    return list(compress(count(1), stable_flags))

# Main yield calculation logic
def calculate_optimal_yield(data_list, condition):
    # Data structure transformation
    records = [
        {'temp': t, 'humid': h, 'co2': c} 
        for t, h, c in zip(data_list[0], data_list[1], data_list[2])
    ]
    
    # State tracking variables
    valid_periods = 0
    cumulative_score = 0
    peak_bonus = 0
    
    # Primary evaluation loop (key logic)
    for idx, record in enumerate(records):
        temp = record['temp']
        humid = record['humid']
        co2 = record['co2']
        
        # Irrelevant transformation (distractor)
        adjusted_co2 = co2 * (1 + calibration_offsets[idx] / 100) if idx < len(calibration_offsets) else co2
        
        # Core condition check
        if condition(temp, humid):
            valid_periods += 1
            base_yield = temp * 1.5 - humid * 0.8
            
            # Bonus logic
            if co2 > 420:
                peak_bonus += 1
            
            cumulative_score += base_yield

    # Final computation with distractor-influenced path
    adjustment_factor = 0.9 if len(running_averages) > 5 else 1.0  # semi-relevant
    bonus_multiplier = 1 + (peak_bonus * 0.1)  # depends on CO2 spikes
    
    # Actual answer computation
    final_yield_value = (cumulative_score * adjustment_factor * bonus_multiplier) + valid_periods
    
    # Dead code path (distractor)
    if False:
        fallback = sum(co2_levels) / len(co2_levels)
        final_yield_value = fallback  
    
    return int(round(final_yield_value))

# Execute main logic
sensor_data = [temperature_readings, humidity_readings, co2_levels]
final_yield = calculate_optimal_yield(sensor_data, threshold_func)

# Print result
print(f"Result: {final_yield}")