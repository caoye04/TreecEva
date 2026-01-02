import math

# Simulated sensor data from a distributed monitoring system
temperature_readings = [23.4, 24.1, 22.9, 25.6, 26.7, 24.3, 23.9]
humidity_readings = [45, 47, 50, 52, 48, 44, 46]
pressure_readings = [1013, 1011, 1009, 1014, 1015, 1010, 1008]

# Auxiliary irrelevant arrays (distractors)
sound_levels = [32, 35, 30, 33, 36, 31, 34]  # Unused in logic
light_intensity = [450, 480, 500, 470, 460, 490, 510]  # Dead code path

# System state flags (some are decoys)
system_state = {
    'active_nodes': 8,
    'overload_threshold': 7,
    'node_health': [True, True, True, False, True, True, True, True],
    'maintenance_mode': False,
    'last_sync_cycle': 127,
    'debug_flag': True,  # Misleading flag
    'version': '2.1.5'
}

# Historical logs with string metadata (mixing types for distraction)
log_headers = ['ERR', 'INFO', 'WARN', 'DEBUG', 'CRIT', 'INFO', 'WARN']
log_timestamps = ['2023-07-10T08:23:01', '2023-07-10T08:24:15', '2023-07-10T08:25:33', 
                    '2023-07-10T08:26:41', '2023-07-10T08:27:09', '2023-07-10T08:28:12', '2023-07-10T08:29:30']
log_severity_codes = [1, 0, 2, 0, 3, 0, 2]

# Distractor function - appears relevant but unused
def analyze_light_trend(data):
    trend = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend += 1
    return trend * 0.5

# Another red herring function dealing with sound
def calculate_noise_rms(levels):
    squared = [x ** 2 for x in levels]
    mean_sq = sum(squared) / len(squared)
    return math.sqrt(mean_sq)

# Core processing pipeline

def extract_diagnostic_patterns(readings):
    n = len(readings)
    if n == 0:
        return 0.0
    avg = sum(readings) / n
    variance = sum((x - avg) ** 2 for x in readings) / n
    std_dev = math.sqrt(variance)
    return avg + std_dev  # Composite metric


def evaluate_node_stability(state):
    healthy_count = sum(state['node_health'])
    total_nodes = len(state['node_health'])
    ratio = healthy_count / total_nodes
    if state['active_nodes'] > state['overload_threshold']:
        ratio *= 1.1
    return min(ratio, 1.0)


def filter_critical_logs(log_data):
    # log_data is list of severity codes
    critical_indices = [i for i, code in enumerate(log_data) if code >= 3]
    return critical_indices


def parse_log_metadata(timestamps, headers):
    # Extract hour from each timestamp using slicing
    hours = [ts[11:13] for ts in timestamps]
    hour_counts = {}
    for h in hours:
        hour_counts[h] = hour_counts.get(h, 0) + 1
    peak_hour = max(hour_counts, key=hour_counts.get)
    return int(peak_hour)


def aggregate_environmental_metrics(temp, hum, pres):
    # Normalize and combine multiple sensor streams
    norm_temp = sum(temp) / len(temp)
    norm_hum = sum(hum) / len(hum)
    norm_pres = sum(pres) / len(pres)
    
    # Apply arbitrary weighting (simulates calibration)
    weighted_score = (norm_temp * 0.4) + (norm_hum * 0.1) + (norm_pres * 0.001)
    return weighted_score


def generate_diagnostic_hash(state, size=8):
    # Create a pseudo-hash using system state (not actually used in final result)
    seed_str = str(state['active_nodes']) + state['version']
    hash_val = 0
    for c in seed_str:
        hash_val = (hash_val * 31 + ord(c)) % 1000000
    return hash_val % (10 ** size)


def process_metrics(log_data, system_status):
    # Step 1: Compute environmental stability index
    env_index = aggregate_environmental_metrics(
        temperature_readings, humidity_readings, pressure_readings
    )
    
    # Step 2: Assess hardware reliability
    node_stability = evaluate_node_stability(system_status)
    
    # Step 3: Extract anomaly patterns from logs
    critical_log_positions = filter_critical_logs(log_data)
    anomaly_count = len(critical_log_positions)
    
    # Step 4: Derive temporal pattern from log metadata (irrelevant to final answer)
    peak_activity_hour = parse_log_metadata(log_timestamps, log_headers)
    
    # Step 5: Compute diagnostic trend from temperature (red herring computation)
    temp_pattern = extract_diagnostic_patterns(temperature_readings)
    
    # Step 6: Construct fake health signature (dead end)
    health_signature = set()
    for i, val in enumerate(humidity_readings):
        if val > 45:
            health_signature.add(f'H{i}')
    signature_length = len(health_signature)
    
    # Step 7: Compute secondary noise metric (completely irrelevant)
    noise_metric = calculate_noise_rms(sound_levels)
    
    # Step 8: Generate unused cryptographic checksum
    checksum = 0
    for h in log_headers:
        checksum += sum(ord(c) for c in h)
    checksum %= 97
    
    # Step 9: Main calculation chain
    base_score = env_index * 100
    adjusted_score = base_score * node_stability
    
    # Step 10: Apply penalty for anomalies
    if anomaly_count > 0:
        adjusted_score -= (anomaly_count * 25.5)
    
    # Step 11: Add arbitrary offset based on system mode (but mode is false)
    if system_status['maintenance_mode']:
        adjusted_score -= 100
    else:
        adjusted_score += 12.75
    
    # Step 12: Final adjustment using bit manipulation (key step)
    int_part = int(adjusted_score)
    fractional = adjusted_score - int_part
    # XOR upper bits to simulate error correction
    manipulated = (int_part ^ 0b110101) & 0xFFFF  # Mask to 16 bits
    final_value = manipulated + fractional
    
    return final_value

# Irrelevant preprocessing (distractor)
processed_light = [x * 0.85 for x in light_intensity if x > 450]
filtered_logs = [h for h, t in zip(log_headers, log_severity_codes) if t >= 1]

# Key execution point
final_diagnostic = process_metrics(log_severity_codes, system_state)

# Output result
print(f"Result: {final_diagnostic}")