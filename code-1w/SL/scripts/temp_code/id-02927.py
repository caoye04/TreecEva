import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.7, 20.3, 26.8, 24.9, 21.2]
humidity_readings = [45, 52, 61, 48, 55, 59, 43, 50, 57]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1016, 1011, 1017, 1013]

# Auxiliary metadata (mostly irrelevant)
sensor_ids = ['TH01', 'TH02', 'HP03', 'BP04', 'HM05', 'LP06', 'MP07', 'XM08', 'YM09']
location_grid = [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (0,2), (1,2), (2,2)]
deployment_dates = ['2023-01-05', '2023-02-10', '2023-01-18', '2023-03-01', '2023-01-22',
                     '2023-02-28', '2023-01-09', '2023-03-15', '2023-02-05']

# Distractor: unused calibration constants
calibration_factor_a = 1.02
base_offset_x = -0.37
normalization_cap = 1024
reference_voltage = 3.3

# Real processing begins here
valid_indices = [i for i in range(len(temperature_readings)) if temperature_readings[i] > 20.0]
filtered_data = []
for idx in valid_indices:
    temp = temperature_readings[idx]
    humid = humidity_readings[idx]
    press = pressure_readings[idx]
    # Composite index using nonlinear transformation
    stability_score = (temp * 1.5) + (humid * 0.8) - (press / 100.0)
    filtered_data.append(stability_score)

# Irrelevant transformation on unused list
transformed_dates = [date.replace('-', '') for date in deployment_dates if '01' in date]
hash_sum = sum([int(d[:6]) % 100 for d in transformed_dates if d.startswith('2023')])

# Another red herring: complex but unused calculation chain
aggregate_pressure = sum(pressure_readings) / len(pressure_readings)
corrected_offsets = [abs(p - aggregate_pressure) * 0.01 for p in pressure_readings]
adjusted_values = [p - c for p, c in zip(pressure_readings, corrected_offsets)]
median_adjusted = sorted(adjusted_values)[len(adjusted_values)//2]

# Threshold map with meaningful and misleading entries
threshold_map = {
    'critical': 50.0,
    'warning_low': 30.0,
    'optimal': 38.5,
    'ignore_zone': 100.0,  # decoy threshold
    'stability_peak': 42.0
}

# Secondary filter based on character count in dummy IDs (distractor logic)
dummy_flag = any([len(sid) > 4 and sid[2].isdigit() for sid in sensor_ids])

# Actual analysis function with embedded distractions
def analyze_readings(data, thresholds):
    result = 0.0
    peak_count = 0
    total_contribution = 0.0
    
    for val in data:
        # Complex conditional branching with mixed types
        if val > thresholds['critical']:
            result += math.log(val) * 1.5
            peak_count += 1
        elif val > thresholds['optimal']:
            result += val * 0.7
        elif val > thresholds['warning_low']:
            result += val * 0.3
            if val < 35.0:
                adjustment = (35.0 - val) * 0.1
                result += adjustment
        else:
            result -= 1.0  # penalty for low values
        
        # Irrelevant internal computation
        squared_chain = val ** 2 / (1 + val)
        if squared_chain > 500:
            total_contribution += math.sqrt(squared_chain)
    
    # Meaningful final adjustment
    if peak_count > 0:
        result = result * (1.0 + 0.1 * peak_count)
    
    # Dead code branch (never reached due to logic)
    if dummy_flag and len(data) == 0:
        fallback = sum(thresholds.values()) / len(thresholds)
        return fallback
    
    return result

# Additional noise: set operations with no impact
unique_pressures = set(pressure_readings)
pressure_differences = {abs(a - b) for a in unique_pressures for b in unique_pressures if a != b}
excess_metrics = unique_pressures.union(pressure_differences).difference([1013, 1014])

# Key execution point
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")