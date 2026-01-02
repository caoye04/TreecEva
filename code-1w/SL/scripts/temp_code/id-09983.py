import itertools

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9]
humidity_readings = [45, 48, 52, 44, 60, 58, 50]
co2_levels = [410, 415, 420, 405, 430, 425, 418]

# Irrelevant auxiliary data (distractor)
sound_decibels = [32, 35, 30, 40, 38, 36, 33]
lux_levels = [500, 520, 480, 600, 580, 550, 510]

# Weight configurations for data fusion (some are decoys)
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'co2': 0.3,
    'fake_metric': 0.0  # Unused weight (red herring)
}

# Historical baselines (distractor, not used in final computation)
historical_avg = {
    'temp': 24.0,
    'humidity': 50,
    'co2': 416
}

# Misleading transformation functions (some unused)
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def enhance_signal(readings):
    # Applies gain that isn't actually used
    return [r * 1.05 for r in readings]

def shift_phase(data, steps=1):
    return data[-steps:] + data[:-steps]  # Unused function

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * stdev]

# Real processing pipeline
def calculate_health_index(temp, hum, co2):
    # Composite index using nonlinear transformations
    temp_factor = abs(temp - 24.0) * -1.2
    hum_factor = max(0, (50 - abs(hum - 50))) * 0.1
    co2_factor = max(0, (500 - co2)) * 0.02
    return temp_factor + hum_factor + co2_factor

# Data alignment via zip and slicing (key use of language feature)
def process_metrics(sensor_data, config):
    # Combine relevant streams with zip and slicing
    recent_window = slice(1, -1)  # Exclude first and last readings
    trimmed_temp = sensor_data[0][recent_window]
    trimmed_hum = sensor_data[1][recent_window]
    trimmed_co2 = sensor_data[2][recent_window]
    
    # Use itertools to generate all possible triplets (distractor usage)
    combos = list(itertools.combinations(range(len(trimmed_temp)), 3))
    total_combinations = len(combos)  # Distractor: computed but unused
    
    # Actual processing: compute index for each time step
    scores = []
    for t, h, c in zip(trimmed_temp, trimmed_hum, trimmed_co2):
        score = calculate_health_index(t, h, c)
        scores.append(score)
    
    # Aggregate final result
    raw_average = sum(scores) / len(scores)
    
    # Apply weights (only relevant ones used)
    weighted_result = raw_average * (config['temp'] + config['humidity'] + config['co2'])
    
    # Final nonlinear scaling
    final_value = (weighted_result ** 2) * 10
    return int(final_value)

# Dead code path (never executed)
def legacy_analysis(seq):
    if False:
        return sum(seq) // len(seq)
    else:
        return None

# Main execution block
if __name__ == "__main__":
    # Assemble input tuple (use of tuple and meaningful structure)
    data = (temperature_readings, humidity_readings, co2_levels)
    
    # Irrelevant set operations (distractor)
    unique_co2 = set(co2_levels)
    unique_co2.add(416)
    spike_detected = len(unique_co2) > len([x for x in co2_levels if x < 420])
    
    # Signal preprocessing (unused result)
    enhanced_temp = enhance_signal(temperature_readings)
    filtered_temp = filter_outliers(enhanced_temp)
    
    # Critical statement
    final_score = process_metrics(data, weights)
    
    # Output result as required
    print(f"Result: {final_score}")