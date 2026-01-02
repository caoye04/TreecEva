import math

# Simulated sensor array data (temperature in Celsius)
sensor_readings = [23.5, 19.0, 27.3, 30.1, 18.9, 22.4, 25.6, 28.7, 17.2, 24.8]

# Irrelevant auxiliary data (distractor)
pressure_levels = [1013, 1009, 1015, 1020, 1005, 1018, 1012, 1007, 1022, 1010]
humidity_data = {i: val * 1.3 for i, val in enumerate(pressure_levels)}

# Threshold constants
temp_threshold = 25.0
min_valid_count = 4

# Misleading intermediate calculation (dead path)
baseline_avg = sum(sensor_readings[:3]) / 3
adjusted_baseline = baseline_avg * 1.05 if baseline_avg < 25 else baseline_avg * 0.95

# Data filtering based on threshold
valid_readings = list(filter(lambda x: x >= temp_threshold, sensor_readings))

# Distractor: unused function (decoy)
def analyze_pressure(volatility_window):
    return [abs(pressure_levels[i] - pressure_levels[i-1]) for i in range(1, len(pressure_levels))]

# Another distractor: complex but unused transformation
rolling_humidity = []
for i in range(len(humidity_data)):
    if i % 3 == 0:
        rolling_humidity.append(humidity_data[i] * 0.8)
    elif i % 3 == 1:
        rolling_humidity.append(humidity_data[i] * 1.1)
    else:
        rolling_humidity.append(humidity_data[i] * 0.95)

# Conditional expression to mask valid count check
effective_count = len(valid_readings) if len(valid_readings) >= min_valid_count else min_valid_count

# Secondary filter: exclude outliers above 29.0 (additional logic step)
filtered_data = [temp for temp in valid_readings if temp <= 29.0]

# Unused recursive red herring
def recursive_variance(data, depth=0):
    if depth >= 2 or len(data) < 2:
        return 0.0
    mean_val = sum(data) / len(data)
    variances = [(x - mean_val) ** 2 for x in data]
    return recursive_variance([math.sqrt(v) for v in variances], depth + 1)

# Real processing function with embedded logic chain
def process_readings(data):
    if not data:
        return -999.0
    
    # Step 1: base average
    avg_temp = sum(data) / len(data)
    
    # Step 2: apply elevation correction (fictional, but realistic-sounding)
    corrected_avg = avg_temp + 1.8
    
    # Step 3: safety margin deduction based on data spread
    deviation = max(data) - min(data)
    margin_deduction = deviation * 0.3
    
    # Step 4: conditional boost if more than 3 readings
    boost = 2.5 if len(data) > 3 else 0
    
    # Step 5: final adjustment using logarithmic scaling (advanced math)
    adjusted_result = (corrected_avg - margin_deduction + boost)
    if adjusted_result > 0:
        adjusted_result = adjusted_result * math.log(adjusted_result + 1) / (math.log(adjusted_result + 1) - 0.2)
    
    return round(adjusted_result, 4)

# Critical execution point
final_diagnostic = process_readings(filtered_data)

# Print result as required
print(f"Result: {final_diagnostic}")