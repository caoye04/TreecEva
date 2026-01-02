from collections import defaultdict, Counter
import math

# Simulated sensor array data (temperature, pressure, vibration)
sensor_logs = [
    (23.5, 101.3, 0.45), (24.1, 102.0, 0.47), (25.6, 103.1, 0.62),
    (26.8, 104.5, 0.88), (27.3, 105.2, 1.12), (28.0, 106.0, 1.35),
    (29.2, 107.4, 1.67), (30.1, 108.9, 2.05), (31.0, 110.1, 2.44),
    (32.5, 111.8, 2.95), (33.7, 113.0, 3.52), (34.8, 114.2, 4.10)
]

# Irrelevant metadata (distractor)
sensor_metadata = {
    'location': 'Reactor Chamber B7',
    'calibration_date': '2023-11-05',
    'model': 'XTR-9000',
    'firmware': 'v2.1.7'
}

# Decoy processing functions (dead code path)
def analyze_vibration_patterns(data):
    # This function is never called
    bins = defaultdict(int)
    for temp, press, vib in data:
        level = 'high' if vib > 2.0 else 'low'
        bins[level] += 1
    return dict(bins)

def compute_thermal_gradient(logs):
    # Unused function with misleading relevance
    gradients = []
    for i in range(1, len(logs)):
        delta_t = logs[i][0] - logs[i-1][0]
        gradients.append(round(delta_t, 2))
    return sum(gradients) / len(gradients)

# Real processing begins here
baseline_temp = 25.0
pressure_offset = 100.0
vibration_ceiling = 5.0

# Distractor variables (irrelevant computations)
temp_deviation_sum = 0.0
pressure_normalization_factor = 1.007
adjusted_pressures = [round(p * pressure_normalization_factor, 2) for t, p, v in sensor_logs]

# Filter logic: only readings where temp > baseline and vibration < ceiling
filtered_data = []
for reading in sensor_logs:
    temp, press, vib = reading
    if temp > baseline_temp and vib < vibration_ceiling:
        adjusted_vib = vib * 0.95  # minor correction
        corrected_reading = (temp, press, adjusted_vib)
        filtered_data.append(corrected_reading)

# Another layer of filtering using lambda (relevant)
noise_floor = 0.5
valid_readings = list(filter(lambda x: x[2] > noise_floor, filtered_data))

# Build frequency map of temperature bands (distractor)
temp_band_count = Counter()
for temp, _, _ in valid_readings:
    band = int(temp // 5) * 5
    temp_band_count[band] += 1

# Key threshold function (lambda used as required)
threshold_func = lambda x: x[0] > 30.0 and x[1] > 110.0

# Critical processing function
def process_readings(data, threshold):
    critical_count = 0
    cumulative_score = 0.0
    
    # Misleading intermediate calculation (distractor)
    phantom_integral = 0.0
    for i in range(len(data)):
        temp, press, vib = data[i]
        if i > 0:
            d_temp = temp - data[i-1][0]
            phantom_integral += d_temp * vib

    # Actual logic determining final result
    for entry in data:
        temp, press, vib = entry
        
        # Compute composite index
        stability_index = (press - pressure_offset) / (temp - baseline_temp + 1e-8)
        risk_factor = math.log(vib + 1) * 10
        
        # Early termination if condition met (control flow)
        if stability_index > 3.5:
            cumulative_score += risk_factor * 1.5
        elif temp > 33.0:
            cumulative_score += risk_factor * 1.2
        else:
            cumulative_score += risk_factor * 0.8
        
        if threshold(entry):
            critical_count += 1
    
    # Final diagnostic is a weighted combination
    # Only this line produces the actual answer
    final_value = int(cumulative_score) + (critical_count * 100)
    
    # Dead assignment (distractor)
    final_value += len(temp_band_count) * 0  # No effect
    
    return final_value

# Execution point of interest
final_diagnostic = process_readings(valid_readings, threshold_func)

# Output result as required
print(f"Target result: {final_diagnostic}")