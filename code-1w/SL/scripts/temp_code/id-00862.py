import math

# Simulated sensor data from water treatment plant over 24 hours
temperature_readings = [22.3, 21.9, 23.4, 24.1, 25.0, 26.2, 27.5, 28.0, 27.8, 26.5, 25.3, 24.0,
                         23.8, 23.6, 23.5, 23.7, 24.2, 25.1, 26.0, 26.8, 27.2, 26.9, 25.8, 24.5]
humidity_readings = [45, 47, 48, 50, 52, 55, 58, 60, 62, 63, 65, 66, 67, 68, 70, 72, 73, 74, 75, 74, 73, 70, 68, 65]

# Historical baselines (irrelevant for current calculation but included as distractor)
historical_avg_temp = sum(temperature_readings) / len(temperature_readings)
historical_max_humidity = max(humidity_readings)
baseline_pressure = 1013.25  # kPa, not used in flow logic

# Sensor data matrix: each row is [temp, humidity, pressure] at hour t
sensor_data = [[temperature_readings[i], humidity_readings[i], baseline_pressure + i * 0.1] 
                for i in range(24)]

# Threshold configuration (only temp and pressure thresholds are relevant; humidity_threshold is a red herring)
class ThresholdConfig:
    def __init__(self):
        self.temp_threshold = 26.0      # degrees Celsius
        self.humidity_threshold = 70    # percent (not actually used)
        self.pressure_threshold = 1015.0 # kPa
        self.flow_cap = 1200            # units/hour

threshold_levels = ThresholdConfig()

# Decoy function: appears useful but never called
def analyze_humidity_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
    return trend_score

# Auxiliary transformation: applies non-linear scaling to temperature (used in final calc)
def nonlinear_temp_scale(temp):
    return temp * math.log(temp + 1) - 10

# Secondary processing: filters high-temp hours (used)
def get_high_temp_periods(data, threshold):
    periods = []
    for i, entry in enumerate(data):
        if entry[0] > threshold:
            periods.append(i)
    return periods

# Redundant validation check (never invoked)
def validate_sensor_consistency(data):
    errors = 0
    for row in data:
        if abs(row[0] - 25) < 1 and row[1] < 40:
            errors += 1
    return errors == 0

# Core calculation function with mixed operations and distractions
def calculate_optimal_flow(sensors, config):
    # Step 1: Extract nonlinear-transformed temperatures
    processed_temps = [nonlinear_temp_scale(entry[0]) for entry in sensors]
    
    # Step 2: Identify high-temperature operational periods
    critical_hours = get_high_temp_periods(sensors, config.temp_threshold)
    
    # Step 3: Compute average transformed temp during critical hours
    if critical_hours:
        critical_temps = [processed_temps[i] for i in critical_hours]
        avg_critical_temp = sum(critical_temps) / len(critical_temps)
    else:
        avg_critical_temp = processed_temps[0]
    
    # Distractor: calculate unused humidity variance during critical hours
    humidity_during_critical = [sensors[i][1] for i in critical_hours] if critical_hours else []
    if humidity_during_critical:
        mean_h = sum(humidity_during_critical) / len(humidity_during_critical)
        var_h = sum((h - mean_h) ** 2 for h in humidity_during_critical) / len(humidity_during_critical)
    else:
        var_h = 0  # This variable is never used
    
    # Step 4: Pressure deviation count (relevant)
    pressure_deviation_count = 0
    for entry in sensors:
        if entry[2] > config.pressure_threshold:
            pressure_deviation_count += 1
    
    # Step 5: Base flow adjustment using avg critical temp and deviation count
    base_flow = avg_critical_temp * 10
    
    # Step 6: Apply penalty for pressure instability
    if pressure_deviation_count > 5:
        stability_penalty = 1.5
    elif pressure_deviation_count > 0:
        stability_penalty = 1.2
    else:
        stability_penalty = 1.0
    
    # Step 7: Calculate initial optimized flow rate
    raw_flow = base_flow * (1 + math.sin(math.pi * pressure_deviation_count / 24))
    
    # Step 8: Cap flow rate based on configuration
    capped_flow = min(raw_flow, config.flow_cap)
    
    # Step 9: Final adjustment using integer division and rounding (key step)
    final_factor = (len(critical_hours) // 2) + 1
    adjusted_flow = round(capped_flow / final_factor, 2)
    
    # Irrelevant bitwise operation (dead code path - only executes if impossible condition)
    debug_flag = 0b1010
    if len(humidity_during_critical) > 100:
        debug_flag ^= 0b1111
        adjusted_flow += debug_flag << 2
    
    # The actual target result
    optimized_flow_rate = adjusted_flow * 2.5  # Final scaling
    
    return optimized_flow_rate

# Execution point of interest
optimized_flow_rate = calculate_optimal_flow(sensor_data, threshold_levels)

# Print result for evaluation
print(f"Target result: {optimized_flow_rate}")