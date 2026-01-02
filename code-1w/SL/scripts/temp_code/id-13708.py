import math

# Simulated sensor array data from a distributed environmental monitoring system
temperature_readings = [23.4, 25.1, 19.8, 30.2, 27.5, 22.3, 26.0, 24.8, 28.7, 31.0]
humidity_readings = [45, 52, 60, 38, 41, 56, 49, 53, 47, 39]
pressure_readings = [1013, 1015, 1012, 1008, 1010, 1016, 1014, 1011, 1009, 1007]

# Irrelevant calibration constants for unused sensors (distractors)
ph_calibration_offset = 7.0
voltage_reference = 3.3
gyro_bias_drift = 0.002

# Decoy transformation functions that are never called
def transform_coordinates(x, y):
    return (x * math.cos(math.pi/4) - y * math.sin(math.pi/4),
            x * math.sin(math.pi/4) + y * math.cos(math.pi/4))

def encrypt_timestamp(ts):
    return (ts * 257 + 17) % 10007

def deprecated_filter(old_data):
    return [x for x in old_data if x > sum(old_data) / len(old_data)]

# Auxiliary lambda for dynamic thresholding (used)
thresh_func = lambda base, factor: base * (1 + 0.1 * factor)

# Step 1: Normalize readings to z-scores (mean = 0, std = 1)
def z_score(data):
    mean_val = sum(data) / len(data)
    std_dev = math.sqrt(sum((x - mean_val)**2 for x in data) / len(data))
    return [(x - mean_val) / std_dev for x in data]

z_temp = z_score(temperature_readings)
z_humid = z_score(humidity_readings)

# Step 2: Flag anomalies using adaptive threshold (only temp used later)
anomaly_threshold = thresh_func(2.0, len(temperature_readings) // 5)
temp_anomalies = [abs(z) > anomaly_threshold for z in z_temp]
humid_anomalies = [abs(z) > 1.8 for z in z_humid]  # Unused later

# Step 3: Apply noise reduction filter (moving average)
def moving_average(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

smoothed_temps = moving_average(temperature_readings, window=2)
smoothed_humidity = moving_average(humidity_readings, window=2)  # Not used

# Step 4: Detect rising trends in temperature (consecutive increases)
rising_trend = []
for i in range(2, len(smoothed_temps)):
    trend = (smoothed_temps[i] > smoothed_temps[i-1] > smoothed_temps[i-2])
    rising_trend.append(trend)

# Step 5: Filter data based on original indices and anomaly flags
valid_indices = []
for i in range(len(temperature_readings)):
    # Only use temperature anomalies; ignore humidity ones
    if not temp_anomalies[i]:
        valid_indices.append(i)

filtered_data = [temperature_readings[i] for i in valid_indices]

# Step 6: Compute entropy of filtered temperature distribution (unused distractor)
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

entropy_value = compute_entropy(filtered_data)  # Computed but not used

# Step 7: Simulate fault-tolerant processing with fallback logic
recovery_mode = False
retry_count = 0

while retry_count < 2:
    try:
        if len(filtered_data) < 3:
            raise ValueError('Insufficient data')
        break
    except ValueError:
        filtered_data.append(25.0)
        retry_count += 1

# Step 8: Core diagnostic processor (uses modular arithmetic and case logic)
def process_readings(data):
    n = len(data)
    checksum = 0
    
    for i in range(n):
        # Modular indexing with bit manipulation twist
        idx_shift = (i ^ (i << 1)) % n  # Bitwise XOR and left shift
        raw_val = data[idx_shift]
        
        # Case conversion equivalent via arithmetic mapping
        # A=65 -> 1, B=66 -> 2, ..., Z=90 -> 26 (though no real chars here)
        # Simulating case-based logic using mod 26 as if converting char
        mapped_case = int(raw_val) % 26  # Simulates 'case' logic via mod
        
        # Key transformation: combines case logic, modular arithmetic, exponent
        contribution = (mapped_case ** 2) * math.sin(math.pi * raw_val / 180)
        checksum += contribution
    
    # Final adjustment using lambda-transformed base
    scale_factor = thresh_func(100, 3)  # returns 130.0
    intermediate = checksum * scale_factor
    
    # Destructuring assignment (tuple unpacking) - relevant
    alpha, beta = (int(intermediate), intermediate - int(intermediate))
    
    # Final diagnostic computed from integer part and fractional stability
    stability_score = abs(beta - 0.5) * 2  # maps frac to 0-1
    final_score = alpha + round(stability_score, 3)
    
    return final_score

# Step 9: Execute critical statement
target_diagnostic_hint = None
final_diagnostic = process_readings(filtered_data)

# Print result as required
print(f"Result: {final_diagnostic}")