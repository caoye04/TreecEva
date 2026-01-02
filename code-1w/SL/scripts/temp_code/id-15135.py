import itertools

def collect_sensor_metrics():
    # Simulated raw sensor data (temperature in millidegrees)
    raw_readings = [23450, 24120, 22980, 25670, 26100, 24880, 23990]
    baseline = 24000
    tolerance = 1500

    # Irrelevant transformation: convert to hex strings (distractor)
    hex_values = [hex(x) for x in raw_readings]

    # Relevant filtering: find anomalies
    anomalies = []
    for reading in raw_readings:
        if abs(reading - baseline) > tolerance:
            anomalies.append(reading)

    # Dead code path: never executed due to logic (red herring)
    if len(anomalies) == 100:
        anomalies = [x * 2 for x in anomalies]

    return raw_readings, anomalies

def preprocess_signal(signal_list):
    # Apply moving average filter (relevant)
    smoothed = []
    window_size = 3
    for i in range(len(signal_list)):
        if i < window_size - 1:
            smoothed.append(signal_list[i])
        else:
            avg = sum(signal_list[i - window_size + 1:i + 1]) // window_size
            smoothed.append(avg)
    
    # Distractor: unused transformation
    inverted = list(map(lambda x: ~x, signal_list))

    # Another distractor: itertools permutation with no side effects
    _ = list(itertools.permutations([1, 2], 2))

    return smoothed

def evaluate_thresholds(data):
    # Determine threshold bands (partially relevant)
    high_band = []
    mid_band = []
    low_band = []

    for val in data:
        if val > 25000:
            high_band.append(val)
        elif val > 24000:
            mid_band.append(val)
        else:
            low_band.append(val)
    
    # Misleading statistic: not used later
    avg_high = sum(high_band) / len(high_band) if high_band else 0

    # Return only the counts (actual interface contract)
    return len(low_band), len(mid_band), len(high_band)

def generate_report_summary(metrics):
    # Use itertools.chain to flatten (relevant usage)
    flat = list(itertools.chain.from_iterable([[x] for x in metrics]))
    total = sum(flat)
    report_code = total * 2 if total > 100000 else total // 2
    
    # Unused string manipulation (distractor)
    debug_tag = "REPORT_" + "_".join(str(report_code)).replace("5", "X")

    return report_code

def analyze_readings(clean_data):
    # Core diagnostic logic
    trend = 0
    for i in range(1, len(clean_data)):
        if clean_data[i] > clean_data[i-1]:
            trend += 1
        elif clean_data[i] < clean_data[i-1]:
            trend -= 1

    # Secondary check: sustained rise
    sustained_rise = 0
    for i in range(3, len(clean_data)):
        if (clean_data[i] >= clean_data[i-1] and 
            clean_data[i-1] >= clean_data[i-2] and 
            clean_data[i-2] >= clean_data[i-3]):
            sustained_rise += 1

    # Final computation
    base_score = trend * 17
    modifier = sustained_rise * 5
    final_diagnostic = base_score + modifier

    # Red herring: complex but unused bitwise logic
    decoy_flag = (base_score ^ modifier) & 0xFF
    if decoy_flag > 100:
        decoy_flag = decoy_flag << 2

    return final_diagnostic

# Main execution flow
raw_data, detected_outliers = collect_sensor_metrics()
processed_data = preprocess_signal(raw_data)
band_counts = evaluate_thresholds(processed_data)
summary_code = generate_report_summary(band_counts)
final_diagnostic = analyze_readings(processed_data)
print(f"Target result: {final_diagnostic}")