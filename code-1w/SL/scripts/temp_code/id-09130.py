import math

# Simulated sensor array data from a distributed environmental monitoring system
def fetch_sensor_data():
    raw_values = [23.4, 18.9, 25.1, 20.3, 27.8, 22.5, 19.7, 24.0, 26.2, 21.8]
    timestamps = [1634567890, 1634567950, 1634568010, 1634568070, 1634568130,
                   1634568190, 1634568250, 1634568310, 1634568370, 1634568430]
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'OK', 'OK', 'WARNING', 'OK', 'OK', 'OK']
    return list(zip(raw_values, timestamps, statuses))

# Legacy function - not used in current flow (red herring)
def legacy_calibrate(x):
    return x * 0.98 + 1.2

# Irrelevant transformation for hypothetical humidity compensation
def apply_humidity_bias(reading, humidity_level=45):
    factor = 1 + (humidity_level - 40) / 1000
    return reading * factor

# Signal processing pipeline
def denoise_signal(signal_list):
    # Apply moving average filter (window size = 3)
    smoothed = []
    for i in range(len(signal_list)):
        if i == 0:
            smoothed.append(signal_list[i])
        elif i == len(signal_list) - 1:
            smoothed.append(signal_list[i])
        else:
            avg = (signal_list[i-1] + signal_list[i] + signal_list[i+1]) / 3
            smoothed.append(round(avg, 2))
    return smoothed

# Advanced validation with checksum (unused path)
def generate_checksum(data_seq):
    chk = 0
    for val in data_seq:
        chk ^= int(val * 10) % 256
    return chk

# String-based status classifier (distractor using string methods)
def classify_status_list(statuses):
    result_flags = []
    for s in statuses:
        s_clean = s.strip().upper()
        if 'ERR' in s_clean:
            result_flags.append(-1)
        elif 'WARN' in s_clean:
            result_flags.append(0)
        else:
            result_flags.append(1)
    return result_flags

# Core signal processor - filters and normalizes valid readings
def process_valid_readings(sensor_data):
    valid_readings = []
    log_entries = []
    
    for value, ts, status in sensor_data:
        entry = f"{ts}: {value:.1f} ({status})"
        log_entries.append(entry)
        
        if 'ERROR' in status or 'ERR' in status.upper():
            continue
        if value < 19.0 or value > 27.5:
            continue
        adjusted = value * 1.02  # Minor calibration
        valid_readings.append(adjusted)
    
    # Use string method to count critical logs (distractor)
    critical_count = sum(1 for e in log_entries if 'ERROR' in e or 'WARN' in e)
    summary = '; '.join(log_entries)
    token_count = len(summary.split())
    
    return valid_readings

# Signal transformer: applies frequency-domain approximation (overkill but plausible)
def transform_to_frequency_domain(signal_seq):
    N = len(signal_seq)
    transformed = []
    for k in range(N // 2 + 1):
        real = sum(signal_seq[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(-signal_seq[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = math.sqrt(real**2 + imag**2) / N
        transformed.append(magnitude)
    return transformed

# Analyze power distribution in frequency bands (mostly irrelevant)
def analyze_frequency_bands(freq_data):
    low_band = sum(f for f in freq_data[:3])
    mid_band = sum(f for f in freq_data[3:6])
    high_band = sum(f for f in freq_data[6:])
    dominance = 'low' if low_band > max(mid_band, high_band) else 'mid' if mid_band > high_band else 'high'
    coherence = math.exp(-abs(low_band - high_band))
    return {'dominance': dominance, 'coherence': coherence, 'raw_sum': sum(freq_data)}

# Primary analysis function that computes diagnostic score
def analyze_readings(clean_signal):
    if len(clean_signal) == 0:
        return 0.0
    
    # Apply denoising
    filtered = denoise_signal(clean_signal)
    
    # Compute statistical moments
    mean_val = sum(filtered) / len(filtered)
    variance = sum((x - mean_val)**2 for x in filtered) / len(filtered)
    std_dev = math.sqrt(variance)
    
    # Detect trends using slope between first and last quartiles
    q1_idx = len(filtered) // 4
    q3_idx = 3 * len(filtered) // 4
    trend_slope = (filtered[q3_idx] - filtered[q1_idx]) / (q3_idx - q1_idx + 1)
    
    # Apply complex weighting formula (actual answer source)
    stability_score = 100 * math.exp(-std_dev / 5.0)
    trend_penalty = 10 * abs(trend_slope)
    length_bonus = min(5, len(filtered))  # Max bonus of 5
    
    # Final computation
    raw_diagnostic = stability_score - trend_penalty + length_bonus
    
    # Dead code branch - never executed due to filtering above
    if any(x < 0 for x in clean_signal):
        raw_diagnostic *= 0.5
    
    # Format result using string operation (distraction)
    diagnostic_str = f"DIAG-{raw_diagnostic:.4f}-END"
    digits = [c for c in diagnostic_str if c.isdigit() or c == '.']
    decimal_part = ''.join(digits).split('.')[-1][:6]
    precision_offset = int(decimal_part) % 97
    
    final_score = raw_diagnostic + (precision_offset * 0.001)
    
    return round(final_score, 4)

# Unused recursive combinatorics function (decoy)
def count_subsequences(arr, threshold=20.0):
    if len(arr) <= 1:
        return 1 if (arr and arr[0] > threshold) else 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    cross_count = sum(1 for x in left for y in right if x + y > threshold)
    return count_subsequences(left, threshold) + count_subsequences(right, threshold) + cross_count

# Main execution sequence
if __name__ == "__main__":
    # Step 1: Retrieve raw sensor data
    sensor_input = fetch_sensor_data()
    
    # Step 2: Extract and process only valid signals
    processed_signals = process_valid_readings(sensor_input)
    
    # Step 3: Transform into frequency domain (irrelevant for final result)
    freq_components = transform_to_frequency_domain(processed_signals)
    freq_analysis = analyze_frequency_bands(freq_components)
    
    # Step 4: Perform final diagnostic analysis
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result
    print(f"Result: {final_diagnostic}")