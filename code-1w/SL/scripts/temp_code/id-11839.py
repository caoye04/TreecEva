from collections import defaultdict, Counter

# Simulated sensor data ingestion pipeline
def collect_sensor_data():
    raw_streams = [
        'temp:72;hum:45;press:30.1;err:0;temp:75;hum:44',
        'temp:68;hum:50;press:29.9;vib:3;err:1',
        'temp:74;hum:47;press:30.3;vib:1;err:0',
        'temp:70;hum:55;press:30.0;err:0;vib:2'
    ]
    readings = []
    for stream in raw_streams:
        segments = stream.split(';')
        temp_reading = None
        hum_reading = None
        for seg in segments:
            if seg.startswith('temp:'):
                temp_reading = float(seg.split(':')[1])
            elif seg.startswith('hum:'):
                hum_reading = float(seg.split(':')[1])
        if temp_reading is not None and hum_reading is not None:
            readings.append((temp_reading, hum_reading))
    return readings

def analyze_correlation(data):
    # Irrelevant correlation analysis (distraction)
    if len(data) < 2:
        return 0.0
    temp_sum = sum(d[0] for d in data)
    hum_sum = sum(d[1] for d in data)
    mean_temp = temp_sum / len(data)
    mean_hum = hum_sum / len(data)
    numerator = sum((d[0] - mean_temp) * (d[1] - mean_hum) for d in data)
    denom_temp = sum((d[0] - mean_temp)**2 for d in data)
    denom_hum = sum((d[1] - mean_hum)**2 for d in data)
    if denom_temp == 0 or denom_hum == 0:
        return 0.0
    return round(numerator / ((denom_temp * denom_hum) ** 0.5), 4)

def compute_rolling_average(values, window=2):
    # Unused rolling average function (dead code path)
    if len(values) < window:
        return []
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def filter_outliers(data, limit=5):
    # Outlier filtering based on temperature variance
    if len(data) == 0:
        return []
    temps = [d[0] for d in data]
    mean_temp = sum(temps) / len(temps)
    variances = [(t - mean_temp) ** 2 for t in temps]
    std_dev = (sum(variances) / len(variances)) ** 0.5
    filtered = [d for d in data if abs(d[0] - mean_temp) <= 2 * std_dev]
    return filtered

def generate_threshold_map(config_level=3):
    # Generate threshold logic map (partially relevant)
    base_map = defaultdict(lambda: (70.0, 50.0))  # (temp_threshold, hum_threshold)
    adjustments = {
        1: (2.0, 3.0),
        2: (4.0, 5.0),
        3: (6.0, 7.0)
    }
    adj = adjustments.get(config_level, (5.0, 5.0))
    base_map['A'] = (70.0 - adj[0], 50.0 + adj[1])
    base_map['B'] = (70.0 + adj[0], 50.0 - adj[1])
    return base_map

def calculate_entropy(data):
    # Information-theoretic distraction
    labels = ['high' if d[0] > 72 else 'low' for d in data]
    counts = Counter(labels)
    total = len(labels)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def process_readings(data, thresholds):
    # Core processing with key logic
    category_count = defaultdict(int)
    for temp, hum in data:
        if temp > thresholds['A'][0] and hum < thresholds['A'][1]:
            category_count['A'] += 1
        elif temp < thresholds['B'][0] and hum > thresholds['B'][1]:
            category_count['B'] += 1
        else:
            category_count['neutral'] += 1
    
    # Decoy transformation chain
    transformed = []
    for i, (t, h) in enumerate(data):
        idx_mod = (i * 3) % 7
        transformed.append((t + idx_mod, h * (idx_mod + 1)))
    
    # Red herring checksum
    checksum = 0
    for val in transformed:
        checksum ^= int(val[0])
        checksum = (checksum * 31) % 10007

    # Actual diagnostic logic
    a_count = category_count['A']
    b_count = category_count['B']
    n_count = category_count['neutral']
    balance_score = abs(a_count - b_count)
    total_valid = a_count + b_count + n_count
    
    if total_valid == 0:
        base_diagnostic = 0
    else:
        base_diagnostic = (a_count * 17 + b_count * 13 + n_count * 5) // max(1, balance_score + 1)
    
    # Final interference: irrelevant bit manipulation
    decoy_bits = 0
    for i in range(8):
        decoy_bits |= (1 << i) if i % 3 == 0 else 0
    decoy_bits ^= 255
    
    final_diagnostic = base_diagnostic + (decoy_bits & 0)  # Neutralized but looks active
    return final_diagnostic

# Main execution sequence
data_source = collect_sensor_data()
correlation_index = analyze_correlation(data_source)
entropy_metric = calculate_entropy(data_source)
filtered_data = filter_outliers(data_source)
threshold_map = generate_threshold_map(config_level=3)
# Rolling average not used (dead code distraction)
unused_averages = compute_rolling_average([d[0] for d in data_source], window=3)
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Target result: {final_diagnostic}")