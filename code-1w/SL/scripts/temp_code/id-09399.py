import itertools

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 25.6, 30.2, 28.4, 27.9, 22.0, 20.3, 31.5]
humidity_readings = [45, 52, 60, 48, 33, 38, 41, 55, 58, 30]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1007, 1010, 1014, 1016, 1004]

# Irrelevant auxiliary arrays (distractors)
elevation_data = [120, 145, 98, 203, 88, 134, 177, 110, 165, 75]
rain_accumulation = [0.1, 0.0, 0.3, 0.0, 1.2, 0.8, 0.0, 0.0, 0.1, 2.0]
wind_speed_kmh = [12, 18, 22, 15, 30, 25, 20, 14, 19, 35]

# System calibration offsets (partially relevant, but some are decoys)
calibration_map = {
    'temp': -0.3,
    'humidity': 2.0,
    'pressure': 1.5,
    'elevation': 0.0,  # unused
    'wind': -1.1     # unused
}

# Thresholds for anomaly detection
threshold_map = {
    'high_temp': 27.0,
    'low_humidity': 40,
    'critical_pressure': 1006
}

# Apply calibration (only temp and humidity actually used later)
calibrated_temps = [t + calibration_map['temp'] for t in temperature_readings]
calibrated_humidity = [h + calibration_map['humidity'] for h in humidity_readings]
calibrated_pressure = [p + calibration_map['pressure'] for p in pressure_readings]

# Misleading transformation chain (dead path)
smoothed_wind = list(itertools.accumulate(wind_speed_kmh, lambda x, y: (x + y) / 2))
adjusted_rainfall = [r * 2.54 for r in rain_accumulation if r > 0.5]
decoded_elevation_bands = [e // 50 for e in elevation_data]

# Filter valid sensors based on operational status (simulated mask)
operational_mask = [(t < 30.0) and (h > 25) for t, h in zip(temperature_readings, humidity_readings)]
filtered_indices = [i for i, valid in enumerate(operational_mask) if valid]

# Extract only calibrated data for operational sensors
filtered_data = [
    {
        't': calibrated_temps[i],
        'h': calibrated_humidity[i],
        'p': calibrated_pressure[i]
    }
    for i in filtered_indices
]

# Auxiliary computation with misleading intermediate (not used in final result)
baseline_avg = sum(calibrated_temps) / len(calibrated_temps)
fluctuation_score = sum(abs(calibrated_temps[i] - calibrated_temps[i-1]) for i in range(1, len(calibrated_temps)))

# Complex conditional processing logic
def evaluate_stability(temp, humid, press):
    temp_flag = 1 if temp > threshold_map['high_temp'] else 0
    humid_flag = 1 if humid < threshold_map['low_humidity'] else 0
    press_flag = 1 if press < threshold_map['critical_pressure'] else 0
    
    # Composite risk index with weighted contributions
    return temp_flag * 3 + humid_flag * 2 + press_flag * 4

# Secondary decoy function (never called)
def compute_air_density(temperature, humidity, pressure):
    R = 287.05  # specific gas constant for dry air
    T = temperature + 273.15  # Kelvin
    epsilon = 0.622  # ratio of molecular weights
    vapor_pressure = 6.112 * (humidity / 100) * (17.67 * temperature) / (temperature + 243.5)
    rho = (pressure * 100) / (R * T)  # Pa instead of hPa
    return rho

# Process readings to generate diagnostic code
def process_readings(data_chunk, limits):
    diagnostics = []
    for entry in data_chunk:
        # Conditional expression usage
        status_code = evaluate_stability(entry['t'], entry['h'], entry['p']) \
            if entry['t'] > 20.0 else 0
        
        # Bit manipulation red herring (status_code modified but not ultimately decisive)
        shifted_code = (status_code << 1) & 0b1111
        adjusted_code = shifted_code ^ 0b1010
        
        # Only high-risk entries contribute to final count
        if status_code >= 5:
            diagnostics.append(adjusted_code)
    
    # Final aggregation using itertools (relevant)
    grouped = [len(list(group)) for k, group in itertools.groupby(sorted(diagnostics))]
    return sum(grouped) * 17 if grouped else -1

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result
print(f"Target result: {final_diagnostic}")