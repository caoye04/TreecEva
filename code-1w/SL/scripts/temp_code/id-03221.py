import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9, 24.8, 23.0]
humidity_readings = [45, 52, 58, 47, 60, 63, 50, 55, 59, 49]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1008, 1014, 1016, 1011, 1017]

# Irrelevant calibration coefficients (distractor)
alpha, beta, gamma = 0.987, 1.024, 0.893
calibration_map = {i: round((i * alpha + beta) ** gamma, 3) for i in range(10)}

# Misleading preprocessing: normalization (not actually used in final path)
normalized_temps = [round((t - min(temperature_readings)) / (max(temperature_readings) - min(temperature_readings)), 3) for t in temperature_readings]

# Data fusion function that looks important but returns dummy values (dead code path)
def fuse_sensors(temp, humid, press):
    return sum([t*h/p for t, h, p in zip(temp[:3], humid[:3], press[:3])])  # Unused

# Decoy statistical analysis with red-herring output
def analyze_trends(data_list):
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    return {'mean': mean_val, 'variance': variance, 'peak_noise': max(data_list) % 7}

trend_report = analyze_trends(pressure_readings)  # Distractor variable

# Conditional filtering based on empirical thresholds (key relevant logic)
valid_temp_range = lambda t: 20.0 <= t <= 25.5
valid_humid_range = lambda h: 45 <= h <= 60

# Combined sensor validity check using lambda and conditionals
is_valid_reading = lambda t, h: valid_temp_range(t) and valid_humid_range(h)

# Apply filtering across paired readings
filtered_data = []
for i in range(len(temperature_readings)):
    temp = temperature_readings[i]
    humid = humidity_readings[i]
    if is_valid_reading(temp, humid):
        # Compute composite index only for valid entries
        index = round(temp * (humid / 100) * math.log(temp + 1), 2)
        filtered_data.append(index)

# Irrelevant string-based identifier generation (distractor)
sensor_id_base = "ENV-STAT-7X"
checksum_str = ''.join(str(int(d*10) % 10) for d in temperature_readings[:5])
sensor_tag = (sensor_id_base + '-' + checksum_str).lower()
formatted_tag = sensor_tag.replace('x', '9').upper()  # Dead transformation

# Auxiliary function to count high-risk conditions (unused)
def count_critical_conditions(data):
    return len([x for x in data if x > 25.0])

critical_count = count_critical_conditions(temperature_readings)  # Red herring

# Core processing function with embedded logic chain
def process_readings(indices):
    if not indices:
        return -999.0
    
    # Step 1: Baseline shift
    shifted = [val - 10 for val in indices]
    
    # Step 2: Apply adaptive gain using conditional expression
    amplified = [s * (1.5 if s > 5 else 1.2) for s in shifted]
    
    # Step 3: Accumulate with alternating signs (pattern-based summation)
    accumulated = 0
    for j, val in enumerate(amplified):
        accumulated += val if j % 2 == 0 else -val
    
    # Step 4: Scale by ratio of valid readings to total
    coverage_ratio = len(indices) / len(temperature_readings)
    adjusted = accumulated * coverage_ratio
    
    # Step 5: Final non-linear correction using exponentiation
    corrected = adjusted * (1 + math.exp(-len(indices)/10))
    
    return round(corrected, 6)

# Key execution point
final_diagnostic = process_readings(filtered_data)

# Output result as required
print(f"Result: {final_diagnostic}")