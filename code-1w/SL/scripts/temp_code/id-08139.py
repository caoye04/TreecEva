import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 25.3, 22.7, 26.0, 25.8, 24.6, 23.9, 27.1, 26.3]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 53, 49, 47]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014, 1016, 1018]

# Irrelevant calibration constants for unused sensors
gyro_bias = 0.0037
accel_noise_floor = 0.012
magnetic_declination = 12.4

# Distractor: Unused transformation function
def transform_coordinates(x, y):
    return (x * math.cos(math.radians(magnetic_declination)) -
            y * math.sin(math.radians(magnetic_declination))), \
           (x * math.sin(math.radians(magnetic_declination)) +
            y * math.cos(math.radians(magnetic_declination)))

# Decoy data processing path
def legacy_filter(data):
    smoothed = []
    for i in range(len(data)):
        if i == 0 or i == len(data) - 1:
            smoothed.append(data[i])
        else:
            smoothed.append(sum(data[i-1:i+2]) / 3)
    return smoothed  # Never actually called

# Real processing begins here
raw_magnitude = [math.sqrt(t**2 + h**2) for t, h in zip(temperature_readings, humidity_readings)]

# Apply moving average filter (real preprocessing)
def apply_digital_filter(signal, window=3):
    filtered = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        filtered.append(sum(signal[start:i+1]) / (i - start + 1))
    return filtered

processed_magnitude = apply_digital_filter(raw_magnitude)

# Compute dynamic threshold based on statistical analysis
data_mean = sum(processed_magnitude) / len(processed_magnitude)
data_variance = sum((x - data_mean) ** 2 for x in processed_magnitude) / len(processed_magnitude)
adaptive_factor = math.sqrt(data_variance) / data_mean
threshold = data_mean + (1.8 * math.sqrt(data_variance))

# Secondary distraction: Power spectral density estimation (unused)
def estimate_psd(signal):
    n = len(signal)
    psd = [0] * (n // 2)
    for k in range(n // 2):
        real = sum(signal[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        imag = sum(signal[i] * math.sin(2 * math.pi * k * i / n) for i in range(n))
        psd[k] = real**2 + imag**2
    return psd

# Another red herring: Unused recursive peak detector
def find_peaks_recursive(data, idx=0, peaks=None):
    if peaks is None:
        peaks = []
    if idx >= len(data):
        return peaks
    if (idx == 0 or data[idx] > data[idx-1]) and (idx == len(data)-1 or data[idx] > data[idx+1]):
        peaks.append(idx)
    return find_peaks_recursive(data, idx + 1, peaks)

# Construct composite dataset with irrelevant fields
class DataPacket:
    def __init__(self, mag, temp, hum, press, timestamp):
        self.magnitude = mag
        self.temperature = temp
        self.humidity = hum
        self.pressure = press
        self.timestamp = timestamp
        self.checksum = int(sum([mag*100, temp, hum, press % 100]) % 256)

packets = [DataPacket(mag, temp, hum, press, i*300) for i, (mag, temp, hum, press) in 
           enumerate(zip(processed_magnitude, temperature_readings, 
                        humidity_readings, pressure_readings))]

# Extract relevant field for actual computation
processed_data = [p.magnitude for p in packets]

# Core analysis logic with early termination condition
def analyze_readings(readings, limit):
    anomaly_count = 0
    cumulative_deviation = 0.0
    max_consecutive_anomalies = 0
    current_streak = 0
    
    for reading in readings:
        if reading > limit:
            anomaly_count += 1
            cumulative_deviation += (reading - limit)
            current_streak += 1
            if current_streak > max_consecutive_anomalies:
                max_consecutive_anomalies = current_streak
        else:
            current_streak = 0
            
        # Early exit condition - misleading as it's rarely triggered
        if cumulative_deviation > 100.0:
            break
    
    # Final diagnostic combines multiple factors
    severity_score = (anomaly_count * 10) + \ 
                     int(cumulative_deviation * 5) + \ 
                     (max_consecutive_anomalies * 7)
    
    # Final transformation
    normalized_severity = int(math.floor(severity_score / 2.3))
    
    return normalized_severity

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")