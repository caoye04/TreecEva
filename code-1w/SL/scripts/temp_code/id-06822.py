import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [45, 47, 50, 52, 58, 60, 55, 51, 49]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014]

# Irrelevant auxiliary metrics (distractor variables)
sound_levels = [32, 35, 38, 34, 36, 39, 41, 37, 33]
luminosity = [800, 820, 810, 830, 850, 870, 860, 840, 825]

# Preprocessing: Normalize temperature using z-score (used later)
mean_temp = sum(temperature_readings) / len(temperature_readings)
std_temp = (sum((x - mean_temp) ** 2 for x in temperature_readings) / len(temperature_readings)) ** 0.5
normalized_temps = [(t - mean_temp) / std_temp for t in temperature_readings]

# Bit manipulation red herring: simulate checksum (never actually used)
def calculate_checksum(data):
    chk = 0
    for val in data:
        chk ^= int(val * 10) & 0xFF
    return chk << 2

unused_checksum = calculate_checksum(humidity_readings)  # Dead code path

# Decoy function for pressure trend analysis (not part of main logic)
def analyze_pressure_trend(pressure_seq):
    trend_score = 0
    for i in range(1, len(pressure_seq)):
        if pressure_seq[i] > pressure_seq[i-1]:
            trend_score += 1
        elif pressure_seq[i] < pressure_seq[i-1]:
            trend_score -= 1
    return abs(trend_score) * 100

# Unused result (misleading intermediate)
pressure_stability_index = analyze_pressure_trend(pressure_readings)

# Real processing begins: composite index calculation
composite_index = []
for i in range(len(temperature_readings)):
    temp_factor = math.log(temperature_readings[i] + 1)
    humidity_factor = humidity_readings[i] / 100
    # Weighted combination with modular adjustment
    score = (temp_factor * 0.6 + humidity_factor * 0.4) * 100
    score = score % 95 + 5  # Modular arithmetic to keep in range
    composite_index.append(round(score, 2))

# Generate threshold map using list comprehension with filtering (key construct)
thresh_keys = ['low', 'medium', 'high']
thresh_values = [i * 15 for i in range(1, 4)]
threshold_map = {k: v for k, v in zip(thresh_keys, thresh_values)}

# Misleading transformation on luminosity (dead end)
lum_categories = ['dim', 'normal', 'bright']
lum_thresholds = [l * 0.1 for l in luminosity if l > 800]

# Process data through filtering and scaling
processed_data = [
    x * 1.08 for x in composite_index 
    if x > threshold_map['medium'] or x < threshold_map['low'] * 1.2
]

# Another decoy: hypothetical wind impact factor (irrelevant)
wind_speeds = [5.2, 6.1, 4.8, 7.3, 6.9, 5.8, 6.2, 5.5, 4.9]
wind_impact = sum([w ** 0.5 for w in wind_speeds]) / 10

# Critical function: analyzes processed readings against thresholds
def analyze_readings(data, thresholds):
    count_high = len([d for d in data if d >= thresholds['high']])
    count_low = len([d for d in data if d <= thresholds['low']])
    total_anomalies = count_high + count_low
    
    # Nested conditional with bit operation distraction
    if total_anomalies > 0:
        base_diag = 500 + (count_high << 2) - (count_low << 1)
        if count_high > count_low:
            adjustment = int(math.sin(math.pi / 6) * 100)
        else:
            adjustment = int(math.cos(math.pi / 3) * 50)
        base_diag += adjustment
        
        # Multi-level nesting with logical short-circuiting
        safety_margin = 10 if base_diag < 600 else (20 if count_high > 2 else 15)
        if base_diag >= 550 and (count_high > 1 or count_low == 0):
            base_diag -= safety_margin
        
        # Final bit flip based on parity (actual logic step)
        if total_anomalies % 2 == 1:
            base_diag = base_diag ^ 17  # XOR perturbation
    else:
        base_diag = 400
        
    return base_diag

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")