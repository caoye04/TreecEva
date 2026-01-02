import math

# Simulated sensor array diagnostics with noise filtering and anomaly detection
def collect_sensor_data():
    raw_readings = [23.4, 19.1, 25.6, 20.3, 100.5, 22.7, -5.2, 24.1, 21.0, 18.9]
    calibration_offset = 1.2
    adjusted = [x + calibration_offset for x in raw_readings]
    return adjusted

def remove_outliers(data, limit=30.0):
    cleaned = []
    temp_log = []
    for val in data:
        if val < 0:  # Flag negative values but don't include
            temp_log.append(f'Invalid reading: {val}')
        elif val > limit:
            continue  # Skip outliers above limit
        else:
            cleaned.append(val)
    return cleaned

def compute_rolling_average(values, window=2):
    averages = []
    for i in range(len(values) - window + 1):
        avg = sum(values[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages

def generate_checksum(sequence):
    # Irrelevant function - decoy for data integrity focus
    checksum = 0
    for num in sequence:
        checksum ^= int(num * 10) % 256
    return checksum

def evaluate_stability_metrics(rolling_avgs):
    variance_proxy = 0.0
    for i in range(1, len(rolling_avgs)):
        variance_proxy += (rolling_avgs[i] - rolling_avgs[i-1]) ** 2
    stability_score = math.sqrt(variance_proxy) if variance_proxy > 0 else 0.0
    return stability_score

def determine_operational_state(score, bounds=(1.5, 4.0)):
    if score < bounds[0]:
        return 'STABLE'
    elif score > bounds[1]:
        return 'UNSTABLE'
    else:
        return 'MONITOR'

# Unused helper - dead code path
def deprecated_normalization(vec):
    max_val = max(vec)
    return [v / max_val for v in vec]

# Key set operations for interference and relevance
baseline_range = {20, 21, 22, 23, 24, 25}
tolerance_band = {19, 20, 21, 22, 23, 24, 25, 26}
threshold_set = baseline_range & tolerance_band  # Intersection: relevant
excluded_zones = tolerance_band - baseline_range  # Red herring

all_data = collect_sensor_data()
filtered_data = remove_outliers(all_data)

# Compute derived metrics (some used, some not)
rolling_averages = compute_rolling_average(filtered_data)
checksum_value = generate_checksum(filtered_data)  # Computed but unused
stability_metric = evaluate_stability_metrics(rolling_averages)

# Simulate secondary diagnostic chain (distractor)
phantom_readings = [x * 0.95 for x in filtered_data if x > 22]
dummy_aggregate = sum(phantom_readings) / len(phantom_readings) if phantom_readings else 0

# Control flow with nested logic and distractors
status_flag = ''
if len(filtered_data) >= 5:
    if stability_metric < 2.0:
        status_flag = 'GREEN'
        temp_cache = [math.floor(x) for x in filtered_data]
        unique_floors = set(temp_cache)
        overlap_count = len(unique_floors & threshold_set)
    elif stability_metric > 5.0:
        status_flag = 'RED'
    else:
        status_flag = 'YELLOW'
else:
    status_flag = 'ERROR'

# Main analysis function with critical execution point
def analyze_readings(readings, valid_set):
    base_sum = sum(int(x) for x in readings)
    count_in_range = 0
    for val in readings:
        if int(val) in valid_set:
            count_in_range += 1
    adjustment_factor = 1.0
    if count_in_range >= 4:
        adjustment_factor = 0.85
    elif count_in_range == 0:
        adjustment_factor = 1.5
    else:
        adjustment_factor = 1.1
    
    # Introduce bit manipulation red herring
    magic_seed = 0b101010
    for r in readings:
        magic_seed ^= int(r) & 0b1111
    
    # Final computation - only this matters
    weighted_total = base_sum * adjustment_factor
    diagnostic_code = int(weighted_total) ^ 0xAB  # Bitwise XOR with hex constant
    return diagnostic_code

# Execute main logic
final_diagnostic = analyze_readings(filtered_data, threshold_set)

# Print result as required
print(f"Result: {final_diagnostic}")