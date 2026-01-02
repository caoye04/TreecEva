from collections import defaultdict, Counter
import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.4, 24.1, 22.8, 25.0, 26.7, 23.9, 24.4, 25.1]
humidity_readings = [55, 60, 62, 58, 70, 65, 59, 63]
co2_levels = [410, 415, 420, 418, 430, 425, 412, 419]

# Irrelevant auxiliary data (distractor)
power_cycles = [1, 0, 1, 1, 0, 1, 1, 1]
uptime_hours = [1023, 891, 1102, 988, 765, 1001, 954, 1030]

# Misleading preprocessing (dead path)
def normalize_values(data):
    mean = sum(data) / len(data)
    return [round((x - mean) / mean * 100, 2) for x in data]

normalized_temp = normalize_values(temperature_readings)  # Not used later

# Core processing function with red herrings
def calculate_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Decoy function that looks important but is unused
def analyze_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 1
    return trend_score

# Real aggregation logic
aggregated_readings = []
for i in range(len(temperature_readings)):
    score = 0
    # Temperature impact (weighted)
    if 22 <= temperature_readings[i] <= 25:
        score += 30
    elif 25 < temperature_readings[i] <= 27:
        score += 20
    else:
        score += 10
    
    # Humidity impact
    if 55 <= humidity_readings[i] <= 65:
        score += 25
    else:
        score += 15
    
    # CO2 impact
    if co2_levels[i] < 415:
        score += 30
    elif co2_levels[i] < 425:
        score += 20
    else:
        score += 10
        
    aggregated_readings.append(score)

# Additional irrelevant transformation (distraction)
deviation_from_avg = [round(x - sum(aggregated_readings)/len(aggregated_readings), 2) for x in aggregated_readings]

# Create composite dataset with multiple fields
aggregate_data = []
for i in range(len(aggregated_readings)):
    entry = {
        'station_id': i + 1000,
        'base_score': aggregated_readings[i],
        'temp_raw': temperature_readings[i],
        'humidity_raw': humidity_readings[i],
        'co2_raw': co2_levels[i],
        'anomaly_flag': False
    }
    
    # Inject anomaly based on obscure rule (not actually used)
    if temperature_readings[i] > 26 and co2_levels[i] > 420:
        entry['anomaly_flag'] = True
        
    aggregate_data.append(entry)

# Thresholds for diagnostic classification (critical)
thresh_a = 65
thresh_b = 55
thresh_c = 45
thresholds = (thresh_a, thresh_b, thresh_c)

# Secondary decoy structure (unused)
status_map = defaultdict(lambda: 'UNKNOWN')
for i in range(8):
    if aggregated_readings[i] >= 70:
        status_map[i] = 'OPTIMAL'
    elif aggregated_readings[i] >= 55:
        status_map[i] = 'STABLE'
    else:
        status_map[i] = 'CAUTION'

# Real diagnostic processor
entropy_metric = calculate_entropy([x['base_score'] for x in aggregate_data])

def process_metrics(data_list, threshold_tuple):
    a, b, c = threshold_tuple
    total_diagnostic = 0
    
    # Simulate multi-step reasoning
    high_count = 0
    mid_count = 0
    
    for record in data_list:
        val = record['base_score']
        if val >= a:
            high_count += 1
        elif val >= b:
            mid_count += 1
    
    # Complex weighting
    weight_factor = 1.75
    if high_count >= 3:
        weight_factor += 0.25
    if mid_count >= 4:
        weight_factor += 0.15
    
    # Main computation chain
    raw_sum = sum(item['base_score'] for item in data_list)
    adjustment = round(math.sqrt(high_count * 100), 2)
    
    # Hidden key step: XOR-based obfuscation of logic
    intermediate = (raw_sum ^ 1337) + int(adjustment * 100)
    intermediate = intermediate ^ 42  # Reverse earlier XOR effect partially
    
    # Final integration with entropy (real dependency)
    scaled_entropy = int(entropy_metric * 1000)  # Use precomputed entropy
    final_value = (intermediate // 3) + scaled_entropy
    
    # Dead conditional branch (misleading)
    if len(data_list) == 10:
        final_value *= 0.9
    
    # Critical assignment
    final_diagnostic = final_value - 884  # Net offset to bring into reasonable range
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(aggregate_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")