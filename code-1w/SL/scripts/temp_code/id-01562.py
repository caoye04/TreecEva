def preprocess_sensors(raw_readings):
    processed = []
    offset = 273.15
    for reading in raw_readings:
        celsius = reading - offset
        normalized = (celsius + 50) / 100
        processed.append(round(normalized, 4))
    return processed

# Simulate sensor calibration drift correction
calibration_factor = 1.02
raw_temperature_reads = [303.15, 313.15, 323.15, 333.15, 343.15]
adjusted_temps = [t * calibration_factor for t in raw_temperature_reads]

def filter_outliers(values, threshold=0.9):
    return [v for v in values if v <= threshold]

# Convert to Celsius and normalize
temperature_data = preprocess_sensors(adjusted_temps)
humidity_raw = [45, 52, 58, 60, 63, 70, 40, 38]
humidity_data = [h / 100 for h in humidity_raw if h > 40]

# Extraneous helper: computes entropy (not used in final result)
def compute_entropy(seq):
    from math import log2
    freq = {}
    for x in seq:
        freq[x] = freq.get(x, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

entropy_value = compute_entropy(humidity_raw)  # Dead-end computation

# Core yield calculation
def calculate_growth_index(t, h):
    return (t * 0.7) + (h * 0.3)

def calculate_optimal_yield(temps, humids):
    indices = []
    humid_set = set(humids)
    valid_humids = [h for h in humids if h >= 0.45]

    for i, temp in enumerate(temps):
        adjusted_index = None
        if i % 2 == 0:
            base_humid = valid_humids[i % len(valid_humids)]
            adjusted_index = calculate_growth_index(temp, base_humid)
        else:
            # Use zip to pair with shifted humidity
            paired = list(zip(temps, humids[::-1]))
            shift_temp, shift_humid = paired[i % len(paired)]
            adjusted_index = calculate_growth_index(shift_temp, shift_humid)
        
        # Conditional expression for stability boost
        stability_bonus = 0.05 if temp > 0.6 else 0.02
        adjusted_index += stability_bonus
        
        # Filter using side condition
        if temp < 0.3:
            continue
            
        indices.append(adjusted_index)
    
    # Final aggregation
    total = sum(indices)
    count = len(indices)
    average_index = total / count if count > 0 else 0
    
    # Secondary distraction: unused transformation
    inverted_temps = [1 - t for t in temps]
    avg_inverted = sum(inverted_temps) / len(inverted_temps)
    
    # Actual output scaling
    yield_score = int(average_index * 1000)  # Scale to integer metric
    return yield_score

# Execution point of interest
final_yield = calculate_optimal_yield(temperature_data, humidity_data)
Result: {final_yield}