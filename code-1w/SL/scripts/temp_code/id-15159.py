import math

# Simulated sensor array data (temperature in Celsius)
sensor_readings = [23.5, 19.0, 27.3, 30.1, 18.9, 24.2, 26.8, 21.0, 29.5, 17.6]

# Irrelevant auxiliary data (distractor)
pressure_levels = [1013.25, 1009.8, 1015.4, 1020.1, 998.7, 1005.3, 1018.9, 1002.4, 1010.8, 1007.6]
humidity_data = [45, 52, 38, 33, 55, 48, 40, 50, 36, 58]

# Decoy transformation functions
def transform_pressure(p):
    return [round((x - 1000) * 0.1, 3) for x in p]

def calculate_humidity_index(h):
    return sum([x ** 0.5 for x in h if x > 40])

transformed_pressure = transform_pressure(pressure_levels)
humidity_index = calculate_humidity_index(humidity_data)

# Real processing begins here
operational_threshold = 25.0
margin_of_error = 0.7

# Misleading intermediate calculation (distractor)
extreme_count = len([x for x in sensor_readings if x > operational_threshold + 2.0])
adjusted_extremes = [x - margin_of_error for x in sensor_readings if x > operational_threshold]

# Filtering logic obscured by irrelevant list comprehensions
valid_range_readings = [x for x in sensor_readings if 18.0 <= x <= 30.0]
outliers = [x for x in sensor_readings if x < 18.0 or x > 30.0]
filtered_data = [x for x in valid_range_readings if x not in outliers]  # Redundant but confusing

# Bitwise decoy operation on floats (useless, distracts reasoning)
bit_fiddle = lambda x: int(x) ^ int(math.log(x + 1) * 10)
decoy_values = [bit_fiddle(int(x)) for x in filtered_data if x > 20.0]

# Set operations used meaningfully but with distractions
critical_set = {round(x, 1) for x in sensor_readings if x >= operational_threshold}
monitoring_set = {round(x, 1) for x in filtered_data}
overlap_region = critical_set & monitoring_set  # Actual relevant set intersection

# Higher-order function with closure (real logic)
def create_threshold_filter(base_threshold):
    def is_above(t):
        return t > base_threshold
    return is_above

threshold_func = create_threshold_filter(operational_threshold)

# Lambda used in filtering (core concept)
high_temp_filter = lambda readings, func: [r for r in readings if func(r)]
elevated_readings = high_temp_filter(filtered_data, threshold_func)

# Multiple assignment distraction
sum_filtered, count_filtered = sum(filtered_data), len(filtered_data)
avg_filtered = round(sum_filtered / count_filtered, 3) if count_filtered else 0.0

# Dead code path - never executed (red herring)
if False:
    temp_correction = [x * 0.98 for x in adjusted_extremes]
    corrected_avg = sum(temp_correction) / len(temp_correction)

# Core diagnostic logic buried in complexity
def process_readings(data, predicate):
    above_threshold = [x for x in data if predicate(x)]
    if not above_threshold:
        return 0.0
    
    # Complex transformation chain
    squared_deviations = [(x - operational_threshold) ** 2 for x in above_threshold]
    mean_squared = sum(squared_deviations) / len(squared_deviations)
    rmse_equivalent = math.sqrt(mean_squared)
    
    # Apply artificial scaling based on count
    scaling_factor = len(above_threshold) / 5.0
    adjusted_score = rmse_equivalent * scaling_factor * 100
    
    # Final manipulation using set result (cross-concept dependency)
    set_influence = len(overlap_region) * 0.5
    final_adjustment = adjusted_score + (set_influence ** 2)
    
    return round(final_adjustment, 6)

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_func)

# Output required result
print(f"Target result: {final_diagnostic}")