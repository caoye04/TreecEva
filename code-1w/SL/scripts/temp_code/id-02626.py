import math

# Simulated sensor data from a distributed environmental monitoring system
def generate_sensor_readings():
    base_values = [2.1, 3.5, 4.8, 5.2, 6.7, 7.3, 8.0, 9.1]
    noise_offsets = [(-1) ** i * 0.1 * i for i in range(8)]
    return [base_values[i] + noise_offsets[i] for i in range(8)]

# Irrelevant auxiliary function - simulates battery levels (distractor)
def calculate_battery_health(sensors):
    return [100 - (i * 2.3) % 7 for i in range(len(sensors))]

# Signal preprocessing with multiple transformation layers
def filter_outliers(data, limit=5.0):
    filtered = []
    temp_log = []
    for val in data:
        if abs(val - limit) > 3.5:
            temp_log.append(f'Flagged: {val}')
        else:
            filtered.append(round(val, 2))
    return filtered

# Complex mapping of thresholds based on zone sensitivity
def build_threshold_map(zones):
    zone_names = ['forest', 'urban', 'coastal', 'desert']
    base_thresholds = [x * 1.7 for x in range(4)]
    # Misleading dictionary construction (only values used later)
    full_map = {zone_names[i]: {'min': base_thresholds[i], 'max': base_thresholds[i] * 2} for i in range(4)}
    return {k: v['min'] for k, v in full_map.items()}

# Data normalization using z-score (but only mean is actually used)
def normalize_dataset(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance) if variance > 0 else 1.0
    normalized = [(x - mean_val) / std_dev for x in data]
    return normalized, mean_val, std_dev  # Only mean_val is used downstream

# Bit manipulation to encode data quality flags (mostly unused)
def compute_data_signature(dataset):
    sig = 0
    for i, val in enumerate(dataset):
        if val > 0:
            sig ^= int(val) << (i % 5)
        else:
            sig |= i
    return sig % 1000  # Decoy metric

# Core analysis function combining boolean logic and arithmetic
def evaluate_condition(value, zone, thresholds):
    t = thresholds.get(zone, 0.0)
    condition_score = 0
    if value > t:
        condition_score += 5
        if value > t * 1.8:
            condition_score += 3
    elif value < t * 0.5:
        condition_score -= 4
    return condition_score > 0  # Returns True if significant deviation

# Main processing pipeline
sensor_data = generate_sensor_readings()
battery_levels = calculate_battery_health(sensor_data)  # Dead path - not used

# Normalize and filter
cleaned_data, avg_val, _ = normalize_dataset(sensor_data)
filtered_data = filter_outliers(cleaned_data, limit=avg_val)

# Generate complex structure with red herring fields
data_packets = []
for idx, val in enumerate(filtered_data):
    packet = {
        'id': idx,
        'raw': sensor_data[idx] if idx < len(sensor_data) else 0,
        'norm': val,
        'flag': (idx % 3 == 0),
        'zone': ['forest', 'urban', 'coastal', 'desert'][idx % 4],
        'quality': compute_data_signature([val])  # Unused field
    }
    data_packets.append(packet)

# Extract relevant sequences using list comprehension and zip
processed_data = [p['norm'] for p in data_packets if p['flag']]
zone_sequence = [p['zone'] for p in data_packets if p['flag']]
temp_pairing = list(zip(processed_data, zone_sequence))

# Build actual threshold map
threshold_map = build_threshold_map(['forest', 'urban', 'coastal', 'desert'])

# Secondary filtering based on spurious correlation (irrelevant)
def find_anomalies_by_position(data_list):
    anomalies = []
    for i, (val, zone) in enumerate(temp_pairing):
        if i % 5 == 0 and val > 2.0:
            anomalies.append((i, val))
    return anomalies

spurious_alerts = find_anomalies_by_position(temp_pairing)  # Not used

# Critical diagnostic function with nested logic
def analyze_signal(values, th_map):
    results = []
    for i, val in enumerate(values):
        # Cycling through zones repeatedly
        zone = ['urban', 'coastal', 'desert', 'forest'][(i * 2) % 4]
        thresh = th_map[zone]
        # Multi-step evaluation with intermediate decoy variables
        baseline = thresh * 1.1
        deviation = abs(val - baseline)
        significance = deviation / (baseline + 0.1)
        weight = 1.0 if significance > 0.5 else 0.5
        score = deviation * weight
        # Final boolean decision with short-circuit logic
        is_elevated = (score > 0.75) or (significance > 0.6 and val > 1.5)
        results.append(1 if is_elevated else 0)
    
    # Aggregate result through weighted sum
    total = 0
    for j, res in enumerate(results):
        factor = 2 if j % 3 == 0 else 1
        total += res * factor
    
    # Final adjustment using enumerate pattern
    for idx, val in enumerate(processed_data):
        if idx % 4 == 0 and val > 0:
            total += int(val) % 3  # Minor deterministic tweak

    return total

# Execute key statement
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")