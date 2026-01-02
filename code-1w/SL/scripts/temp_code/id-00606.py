import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 25.6, 24.8, 23.7]
humidity_readings = [45, 48, 50, 44, 52, 49, 47, 51, 53, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013, 1010, 1018]

# Irrelevant auxiliary arrays (distractors)
legacy_codes = ['A7', 'B3', 'C9', 'D2', 'E5', 'F8', 'G1', 'H4', 'I6', 'J9']
error_flags = [False, False, True, False, False, False, True, False, False, True]
redundant_indices = [i for i in range(len(temperature_readings)) if i % 2 == 0]

# Misleading intermediate transformations (dead path)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / mean_val * 100 for x in data]

# Unused transformation function (red herring)
def frequency_analysis(seq):
    freq_map = {}
    for item in seq:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

# Complex preprocessing with relevant and irrelevant steps
def filter_outliers(data, threshold=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Another decoy function operating on unused data
def generate_checksum(labels):
    return sum([hash(c) % 100 for s in labels for c in s])

cached_checksum = generate_checksum(legacy_codes)  # Distractor computation

# Real signal processing chain
filtered_temp = filter_outliers(temperature_readings)
filtered_humid = filter_outliers(humidity_readings)

# Simulated calibration adjustment (irrelevant but plausible)
calibration_offset = math.sin(math.pi / 6)  # Always 0.5
adjusted_temp = [t + calibration_offset for t in filtered_temp]

# Create composite tuples of processed readings (key structure)
processed_data = [(t, h) for t, h in zip(adjusted_temp, filtered_humid)]

# Dead code branch - never executed (misdirection)
if len(processed_data) > 20:
    processed_data = [(t*1.1, h*0.9) for t, h in processed_data]

# Auxiliary statistical summaries (some used, some not)
mean_temperature = sum(t for t, h in processed_data) / len(processed_data)
median_humidity = sorted([h for t, h in processed_data])[len(processed_data)//2]
variance_temp = sum((t - mean_temperature)**2 for t, h in processed_data) / len(processed_data)

# Unused statistical measures (distraction)
stdev_temp = math.sqrt(variance_temp)
max_humidity = max(h for t, h in processed_data)
min_temp = min(t for t, h in processed_data)

trend_score = 0
for i in range(1, len(temperature_readings)):
    if temperature_readings[i] > temperature_readings[i-1]:
        trend_score += 1
    elif temperature_readings[i] < temperature_readings[i-1]:
        trend_score -= 1

# Core analysis logic — depends on prior state
threshold_mask = [t > 24.0 for t, h in processed_data]
high_temp_count = sum(threshold_mask)

# Secondary condition based on humidity clustering
clustered_high_humidity = len([h for t, h in processed_data if h > 50]) >= 3

# Decoy bit manipulation (looks important, unused)
encoded_flag = (high_temp_count << 3) ^ 0xAA & 0xFF

# Final diagnostic calculation — actual answer path
def analyze_readings(data_tuples):
    temp_sum = sum(t for t, h in data_tuples)
    humid_prod = 1
    for t, h in data_tuples:
        humid_prod *= h
    # Use logarithmic scaling to avoid overflow (actual use)
    scaled_humid = math.log(humid_prod) if humid_prod > 0 else 0
    # Weighted combination
    diagnostic_value = temp_sum * 100 + int(scaled_humid)
    
    # Inject subtle correction based on count
    n = len(data_tuples)
    if n > 6:
        diagnostic_value -= 50
    else:
        diagnostic_value += 25
    
    # Additional trap: looks like it modifies, but doesn't affect final result
    temp_debug = diagnostic_value + 1000  
    temp_debug = temp_debug // 2
    temp_debug = temp_debug - 500  # Still not used
    
    return diagnostic_value

# Execution point of interest
final_diagnostic = analyze_readings(processed_data)

# Print result as required
print(f"Result: {final_diagnostic}")