import math

# Simulated sensor data processing system for environmental monitoring
def fetch_raw_readings():
    return [14.2, 18.7, 22.5, 19.3, 25.1, 20.4, 17.8, 23.6]

def clean_data(raw):
    cleaned = []
    threshold = 15.0
    offset = 0.5
    temp_offset = 0.0  # distractor
    for val in raw:
        if val > threshold:
            cleaned.append(val - offset)
    return cleaned

def transform_scale(data):
    scaled = []
    max_val = max(data)
    scale_factor = 100 / max_val
    for x in data:
        scaled.append(x * scale_factor)
    return scaled

def generate_checksum(values):
    # Irrelevant function - decoy
    checksum = 0
    for v in values:
        checksum += int(v) % 7
    return checksum * 3

def filter_outliers(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    lower, upper = mean - 1.5 * std_dev, mean + 1.5 * std_dev
    filtered = [x for x in data if lower <= x <= upper]  # list comprehension
    
    # Dead code path (never executed due to prior logic)
    if len(filtered) == 0:
        fallback = [0.0] * 5
        for i in range(len(fallback)):
            fallback[i] += 1.1
        return fallback
        
    return filtered

def compute_entropy(data):
    # Distractor: not used in final computation
    total = sum(data)
    probs = [(x / total) for x in data]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def rolling_average(data, window=3):
    avgs = []
    for i in range(len(data) - window + 1):
        avgs.append(sum(data[i:i+window]) / window)
    return avgs

def extract_flags(readings):
    # Another red herring
    flags = set()
    for r in readings:
        if r > 90:
            flags.add('HIGH')
        elif r < 30:
            flags.add('LOW')
    return flags.union({'BASELINE'})  # set operation

def normalize_strings(names):
    # Completely irrelevant string processing
    return [name.strip().upper() for name in names]  # list comprehension

def analyze_readings(logs):
    # Core logic begins
    base_score = 0
    for reading in logs:
        if reading > 85:
            base_score += 5
        elif reading > 75:
            base_score += 3
        else:
            base_score += 1
    
    adjustment = len(logs) % 4  # minor tweak
    base_score -= adjustment
    
    # Key transformation
    if base_score > 20:
        base_score = base_score // 2
    
    secondary_weight = 0
    for i, val in enumerate(logs):
        if i % 2 == 0 and val > 70:
            secondary_weight += 2
    
    final_risk = base_score + secondary_weight
    
    # Final mapping
    mapping_key = (final_risk % 6) + 1
    lookup = {1: 12, 2: 18, 3: 27, 4: 36, 5: 45, 6: 54}
    return lookup[mapping_key]

# Main execution flow with distractions
sensor_names = ['S1', 'S2', 'S3', 'S4', 'S5']
formatted_names = normalize_strings(sensor_names)
cached_values = {name: 0 for name in formatted_names}  # unused dict

raw_log_data = fetch_raw_readings()
processed_logs = clean_data(raw_log_data)
processed_logs = transform_scale(processed_logs)
processed_logs = filter_outliers(processed_logs)

# Generate unused metrics
diagnostic_checksum = generate_checksum(processed_logs)
data_entropy = compute_entropy(processed_logs)
rolling_trend = rolling_average(processed_logs)
flag_set = extract_flags(processed_logs)

# Critical statement
final_diagnostic = analyze_readings(processed_logs)

Result: {final_diagnostic}