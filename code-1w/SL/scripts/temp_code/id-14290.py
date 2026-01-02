from collections import defaultdict, Counter
import math

# Sensor calibration and diagnostic simulation

def calibrate_sensor(raw_values, baseline=5.0):
    """Apply non-linear calibration to raw sensor data."""
    calibrated = []
    for val in raw_values:
        adjusted = (val * 1.08) - baseline + 0.3 * math.sin(val)
        calibrated.append(round(adjusted, 4))
    return calibrated


def filter_anomalies(data):
    """Remove statistical outliers using interquartile range."""
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data) // 4]
    q3 = sorted_data[3 * len(sorted_data) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    
    # Irrelevant distractor: counting digit frequencies in floats
    digit_count = defaultdict(int)
    for num in data:
        str_num = str(abs(int(num * 100))))
        for d in str_num:
            digit_count[int(d)] += 1
    
    # Dead code path: never used
    if sum(digit_count.values()) > 100:
        anomaly_score = 0
        for k, v in digit_count.items():
            anomaly_score += k * v % 7
    
    return filtered


def analyze_readings(samples):
    """Compute final diagnostic index from cleaned sensor data."""
    # Compute moving average over window size 3
    moving_averages = []
    for i in range(len(samples) - 2):
        avg = round(sum(samples[i:i+3]) / 3, 4)
        moving_averages.append(avg)
    
    # Distractor: frequency analysis of rounded values
    freq_counter = Counter([round(x, 2) for x in samples])
    mode_value = max(freq_counter, key=freq_counter.get)
    mode_count = freq_counter[mode_value]
    
    # Unused recursive function (decoy)
    def _recursive_transform(n, depth=0):
        if depth >= 3 or n < 1:
            return 1
        return n * _recursive_transform(n - 2, depth + 1)
    
    # Actual computation path
    total_energy = sum(x ** 2 for x in moving_averages)
    stability_factor = len(moving_averages) / (len(samples) + 1e-8)
    
    # Complex formula combining multiple metrics
    diagnostic_index = (total_energy * stability_factor * 100)
    
    # More distractions: bit manipulation on irrelevant data
    bit_analysis = 0
    for i, val in enumerate(samples):
        shifted = int(abs(val * 10)) << 2
        xor_val = shifted ^ (i % 256)
        bit_analysis += bin(xor_val).count('1')
    
    # Final result has no relation to bit_analysis, but it's distracting
    return int(diagnostic_index)

# Simulated raw sensor inputs (real-world source)
raw_sensor_data = [4.2, 6.8, 7.1, 5.5, 3.9, 12.3, 5.7, 6.2, 4.8, 5.1, 15.6, 5.9, 6.4, 4.6, 5.3]

# Step 1: Calibration
baseline_offset = 5.0
calibrated_samples = calibrate_sensor(raw_sensor_data, baseline_offset)

# Misleading intermediate check (not part of main logic)
temp_deviation = sum(abs(x - baseline_offset) for x in calibrated_samples) / len(calibrated_samples)
flag_high_noise = temp_deviation > 2.0  # unused flag

# Step 2: Filtering anomalies
cleaned_readings = filter_anomalies(calibrated_samples)

# Step 3: Final diagnostic analysis
final_diagnostic = analyze_readings(cleaned_readings)

print(f"Result: {final_diagnostic}")