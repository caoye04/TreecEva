import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 48, 52, 44, 55, 50, 47]
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016, 1011]

# Auxiliary irrelevant data (distractor)
sound_levels = [32, 35, 40, 33, 38, 36, 34]  # Decoy sensor data
light_intensity = [800, 850, 900, 820, 870, 830, 860]  # Not used in calculation

# Weight configuration for relevant metrics (used in actual logic)
weights = {
    'temp': 0.4,
    'humidity': 0.35,
    'pressure': 0.25
}

# Irrelevant transformation functions (dead code path)
def transform_sound(data):
    return [math.log(x + 1) for x in data]

def normalize_light(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Core processing function with distractions
def calculate_baseline(readings):
    # This function is not actually used (red herring)
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return avg + math.sqrt(variance)

def filter_outliers(data, threshold=1.5):
    # Interquartile range filtering (unused but plausible)
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Main processing pipeline
def aggregate_data(temps, humidity, pressure):
    # Compute normalized indices
    norm_temps = [(t - 20) / 10 for t in temps]  # Normalize around baseline
    norm_humidity = [h / 100 for h in humidity]
    norm_pressure = [(p - 1000) / 50 for p in pressure]
    
    # Create composite dictionary structure (relevant)
    records = []
    for i in range(len(temps)):
        record = {
            'index': i,
            'temp_norm': norm_temps[i],
            'humidity_norm': norm_humidity[i],
            'pressure_norm': norm_pressure[i],
            'combined_factor': norm_temps[i] * 0.6 + norm_humidity[i] * 0.4,  # intermediate
            'stability_metric': abs(norm_temps[i] - norm_pressure[i])  # distraction
        }
        records.append(record)
    
    # Extract key values for final computation
    factors = [r['combined_factor'] for r in records]
    stability_scores = [1 / (1 + r['stability_metric']) for r in records]  # not used
    
    # Final weighted average preparation
    primary_mean = sum(factors) / len(factors)
    return {'factors': factors, 'baseline': primary_mean}

# Misleading secondary analysis (distractor)
def analyze_trends(data_list):
    trends = []
    for data in data_list:
        trend = 0
        for i in range(1, len(data)):
            trend += (data[i] - data[i-1]) > 0  # count increasing steps
        trends.append(trend / (len(data) - 1))
    return trends

# Real final processing function
def process_metrics(raw_data, weight_map):
    # Reconstruct structured data
    temp_avg = sum(raw_data[0]) / len(raw_data[0])
    humid_avg = sum(raw_data[1]) / len(raw_data[1])
    press_avg = sum(raw_data[2]) / len(raw_data[2])
    
    # Normalize inputs
    n_temp = (temp_avg - 20) / 10
    n_humid = humid_avg / 100
    n_press = (press_avg - 1000) / 50
    
    # Apply weights from dictionary
    weighted_sum = (
        n_temp * weight_map['temp'] + 
        n_humid * weight_map['humidity'] + 
        n_press * weight_map['pressure']
    )
    
    # Additional correction based on data consistency (bit manipulation red herring)
    consistency_flag = 0
    for t in raw_data[0]:
        consistency_flag ^= int(t * 10)  # XOR chain - unused
    
    # Final nonlinear transformation
    final_value = math.exp(weighted_sum) * 1000  # Scale to larger integer
    
    # Dead logic branch (never executed - misleading)
    if len(raw_data[0]) < 5:
        fallback = 0
        for i, t in enumerate(raw_data[0]):
            fallback += t * (i + 1)
        final_value = fallback
    
    return int(final_value)

# Orchestration block
if __name__ == "__main__":
    # Process the core environmental data
    processed_batch = aggregate_data(temperature_readings, humidity_readings, pressure_readings)
    
    # Unused transformations (distractions)
    sound_features = transform_sound(sound_levels)
    light_normalized = normalize_light(light_intensity)
    trend_analysis = analyze_trends([temperature_readings, humidity_readings])
    
    # Actual critical computation
    data_input = [temperature_readings, humidity_readings, pressure_readings]
    final_score = process_metrics(data_input, weights)
    
    # Print result as required
    print(f"Result: {final_score}")