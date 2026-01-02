def analyze_conditions(temperature, pressure, humidity):
    # Auxiliary calculation with misleading relevance
    stability_index = (temperature * 0.3) + (pressure * 0.5) - (humidity * 0.2)
    threshold = 75 if temperature > 20 else 60
    adjustment = 1.2 if pressure > 1013 else 0.9
    
    # Distractor: complex but unused computation
    derived_metric = (stability_index ** 2) / (humidity + 1) if humidity != 0 else 0
    normalized_pressure = (pressure - 980) / 33
    
    # Real conditional logic affecting downstream flow
    is_stable = stability_index > threshold and normalized_pressure > 0
    return is_stable, adjustment


def evaluate_risk_level(sensor_readings):
    total_risk = 0
    risk_multiplier = 1.0
    
    for reading in sensor_readings:
        temp, press, humid = reading[:3]
        base_risk = 0
        
        if temp > 30:
            base_risk += 20
        elif temp < 10:
            base_risk += 15

        if press < 990 or press > 1030:
            base_risk += 25

        # Bitwise red herring: combines values but not used in final logic
        status_flag = (temp & 1) ^ (press & 1) | (humid & 1)
        debug_flag = status_flag << 2
        
        # Actual risk accumulation
        total_risk += base_risk
    
    # Conditional expression influencing final path
    risk_multiplier = 1.5 if total_risk > 50 else 1.0
    adjusted_risk = total_risk * risk_multiplier
    
    return adjusted_risk


def process_metrics(data, weights):
    # Unpacking with meaningful variables
    (temp_data, press_data, humid_data) = data
    w1, w2, w3 = weights
    
    # Intermediate transformations — some are distractions
    avg_temp = sum(temp_data) / len(temp_data)
    avg_press = sum(press_data) / len(press_data)
    avg_humid = sum(humid_data) / len(humid_data)
    
    # Complex distractor block: sorting tuples that won't be used
    sorted_pairs = sorted([(t, h) for t, h in zip(temp_data, humid_data)], key=lambda x: x[0])
    median_temp = sorted_pairs[len(sorted_pairs)//2][0]
    
    # Another red herring: bitwise masking on averages
    masked_avg = int(avg_press) & int(avg_temp) | int(avg_humid)
    dummy_shift = masked_avg >> 3
    
    # Evaluate stability using helper function
    is_system_stable, adj_factor = analyze_conditions(avg_temp, avg_press, avg_humid)
    
    # Compute primary metric components
    temp_score = abs(25 - avg_temp) * -2  # Deviation from ideal temp
    press_score = (1013 - avg_press) * 0.1
    humid_score = (50 - avg_humid) * 0.5  # Ideal humidity = 50%
    
    # Weighted aggregation
    preliminary_score = w1 * temp_score + w2 * press_score + w3 * humid_score
    
    # Use risk evaluation as modifier
    sensor_readings = list(zip(temp_data, press_data, humid_data))
    risk_penalty = evaluate_risk_level(sensor_readings)
    
    # Final score computed via conditional expression
    final_score = preliminary_score - risk_penalty if is_system_stable else (preliminary_score - risk_penalty) * adj_factor
    
    return final_score

# Input data
sensor_data = (
    [22, 24, 19, 26, 23],  # temperatures
    [1012, 1015, 1008, 1020, 1010],  # pressures
    [45, 50, 55, 40, 60]   # humidity levels
)

weights = (1.2, 0.8, 1.0)

# Execution point of interest
final_score = process_metrics(sensor_data, weights)
print(f"Target result: {final_score}")