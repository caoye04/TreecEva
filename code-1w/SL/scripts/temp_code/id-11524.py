import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.7, 23.9, 25.8]
humidity_readings = [45, 48, 50, 44, 52, 49, 47, 51]
co2_levels = [400, 410, 415, 398, 420, 405, 395, 412]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 1.002
CALIBRATION_OFFSET_B = -0.05
REFERENCE_VOLTAGE = 3.3
MAX_SENSOR_INPUT = 1023

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    return [x / max(data) for x in data]  # Unused function

def compute_thermal_index(temp, humidity):
    # Heat index approximation (not used in final calculation)
    return temp + 0.5 * (humidity - 50)

# Decoy transformation using string methods (irrelevant)
sensor_labels = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8']
label_status = [label.lower().replace('t', 'sensor_') for label in sensor_labels]
status_summary = ''.join(label_status).upper().strip('SENSOR_')

# Actual relevant processing begins here
filtered_temps = [t for t in temperature_readings if 23 <= t <= 26]  # Filter valid range

# Compute moving average over 3-point window
moving_avg = []
for i in range(1, len(filtered_temps)-1):
    avg = (filtered_temps[i-1] + filtered_temps[i] + filtered_temps[i+1]) / 3
    moving_avg.append(avg)

# Apply correction based on CO2 trend (only first few elements used)
co2_trend = sum(co2_levels[i+1] > co2_levels[i] for i in range(len(co2_levels)-1))
temp_correction = 0.1 if co2_trend > 4 else -0.1

corrected_temps = [t + temp_correction for t in filtered_temps]

# Calculate volatility index using bit manipulation (relevant)
def calculate_volatility(data):
    diffs = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    squared_diffs = [d**2 for d in diffs]
    mean_sq = sum(squared_diffs) / len(squared_diffs)
    volatility = math.sqrt(mean_sq)
    # Encode volatility level using bit shifting (actual use)
    level = int(volatility * 10)
    encoded = (level << 2) | (level >> 1)  # Bitwise mix
    return encoded

volatility_code = calculate_volatility(corrected_temps)

# Simulate redundant system check (distractor)
system_flags = {"active": True, "redundant": False, "override": None}
if system_flags["active"] and not system_flags["redundant"]:
    override_sequence = [i**2 for i in range(5) if i % 2 == 0]
    checksum = sum(override_sequence) ^ 255  # Unused result

# Data transformation pipeline
processed_data = {
    "samples": len(corrected_temps),
    "baseline": sum(corrected_temps) / len(corrected_temps),
    "flags": volatility_code & 0xFF,  # Use lower byte
    "mode": "diagnostic"
}

# Secondary irrelevant computation (misleading intermediate)
def predict_outlier(data):
    mean = sum(data) / len(data)
    deviations = [abs(x - mean) for x in data]
    threshold = 1.5 * mean
n    outliers = [x for x in data if abs(x - mean) > threshold]
    return len(outliers) > 0

outlier_prediction = predict_outlier(humidity_readings)  # Dead end

# Core analysis logic
config_mask = 0b1101
adjustment_factor = 1.75

# Final diagnostic depends on multiple cross-concept steps
def analyze_readings(data_dict):
    sample_count = data_dict["samples"]
    base_value = data_dict["baseline"]
    flag_signal = data_dict["flags"]
    
    # Complex interaction of arithmetic, bitwise, and logical ops
    intermediate = (base_value * adjustment_factor) + (flag_signal ^ config_mask)
    
    # Additional logic layer
    if sample_count >= 4:
        intermediate -= 2.5
    else:
        intermediate += 5.0
    
    # Final transformation with string method red herring
    metadata_tag = f"D{sample_count}".zfill(3).replace('D', 'DIAG_')
    tag_value = len(metadata_tag)  # Minor contribution
    
    final_score = intermediate + tag_value
    
    return int(round(final_score))

final_diagnostic = analyze_readings(processed_data)
print(f"Target result: {final_diagnostic}")