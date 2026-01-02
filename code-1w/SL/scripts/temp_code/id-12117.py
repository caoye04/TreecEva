from collections import defaultdict, Counter

# Simulated sensor network data with noise and redundant metrics
def collect_sensor_metrics():
    raw_readings = [
        (1007, 'temp', 23.5), (1008, 'humid', 65), (1009, 'press', 1013.25),
        (1010, 'temp', 24.1), (1011, 'humid', 67), (1012, 'co2', 415),
        (1013, 'temp', 19.8), (1014, 'pm25', 12), (1015, 'press', 1012.9),
        (1016, 'temp', 22.7), (1017, 'co2', 395), (1018, 'humid', 70)
    ]
    return raw_readings

# Irrelevant preprocessing: formats timestamps for unused audit log
def generate_audit_stamps(base_id, count):
    stamps = []
    for i in range(count):
        tick = (base_id * 17 + i * 3) % 97
        stamps.append(f"LOG-{tick:03d}")
    return stamps  # Never used in main logic

# Distractor function: analyzes outlier frequency but not connected to final result
def analyze_outlier_frequency(data_list):
    counts = defaultdict(int)
    for _, typ, val in data_list:
        if val < 20 or val > 50:
            counts[typ] += 1
    return dict(counts)  # Computed but unused

# Core filtering: extract temperature readings above baseline
def extract_relevant_stream(raw_entries, mode='temp'):
    stream = []
    for sid, sensor_type, value in raw_entries:
        if sensor_type == mode:
            adjusted_val = value + 0.25  # Calibration offset
            normalized_id = (sid % 100) * 10
            stream.append((normalized_id, adjusted_val))
    return stream

# Misleading transformation: computes rolling average but discarded
def compute_rolling_average(values, window=2):
    averages = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        avg = sum(values[start:i+1]) / (i - start + 1)
        averages.append(round(avg, 2))
    return averages  # Calculated but ignored

# Real processing path begins here
threshold_map = {'temp': 22.0, 'humid': 60.0, 'press': 1010.0}

# Extract only temperature entries with calibration
raw_data = collect_sensor_metrics()
distractor_outliers = analyze_outlier_frequency(raw_data)  # Dead-end analysis

filtered_pairs = extract_relevant_stream(raw_data, 'temp')
baseline_temp_readings = [val for _, val in filtered_pairs]

# Red herring: timestamp generation unrelated to output
timestamp_log = generate_audit_stamps(1000, len(raw_data))
rolling_temps = compute_rolling_average(baseline_temp_readings)  # Computed, then ignored

# Decoy statistical summary using string methods on numeric placeholders
def create_summary_distractor(data):
    as_strings = [str(round(x, 1)) for x in data]
    joined = ','.join(as_strings)
    token_count = joined.count('2') + joined.count('.')
    return token_count * 1.5  # Meaningless metric

summary_noise = create_summary_distractor(baseline_temp_readings)

# Actual logic: map site ID to calibrated temp, apply threshold mask
def process_readings(temp_data, thresholds):
    result_set = defaultdict(float)
    high_temp_sites = []
    
    for site_code, t_val in temp_data:
        if t_val > thresholds['temp']:
            high_temp_sites.append(site_code)
    
    # Secondary filter based on site code pattern (bit manipulation red herring)
    valid_sites = []
    for code in high_temp_sites:
        if (code & 3) == 0:  # Divisible by 4?
            valid_sites.append(code)
    
    # Final computation: sum of valid site codes minus count of all high temps
    site_sum = sum(valid_sites)
    trigger_count = len(high_temp_sites)
    adjustment_factor = len(threshold_map)  # Always 3
    
    # Real answer formation
    diagnostic_score = site_sum - trigger_count * adjustment_factor
    return int(diagnostic_score)

# Critical execution point
final_diagnostic = process_readings(filtered_pairs, threshold_map)
print(f"Result: {final_diagnostic}")