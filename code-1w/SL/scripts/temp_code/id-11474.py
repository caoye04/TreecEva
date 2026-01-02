from collections import defaultdict

# Simulated sensor readings and calibration data
def collect_readings():
    raw_data = [15, 22, 30, 28, 18, 25]
    calibrated = []
    offset = 3
    for val in raw_data:
        adjusted = val - offset
        calibrated.append(adjusted)
    return calibrated

def analyze_trends(data):
    trends = defaultdict(int)
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends['increase'] += 1
        elif data[i] < data[i-1]:
            trends['decrease'] += 1
        else:
            trends['stable'] += 1
    return trends

def filter_outliers(data, threshold=20):
    filtered = []
    temp_sum = 0
    count = 0
    for x in data:
        temp_sum += x
        count += 1
    avg = temp_sum / count if count > 0 else 0
    deviation_scores = []
    for x in data:
        deviation_scores.append(abs(x - avg))
    for x in data:
        if abs(x - avg) <= threshold:
            filtered.append(x)
    return filtered

def calculate_final_score(readings, importance_weights):
    base_score = 0
    for reading in readings:
        if reading > 15:
            base_score += reading * importance_weights.get('high', 1.2)
        else:
            base_score += reading * importance_weights.get('low', 0.8)
    
    # Irrelevant accumulation (distractor)
    dummy_accum = 0
    for i in range(len(readings)):
        dummy_accum += i * readings[i] % 7
    
    penalty_factor = 0.9
    final_score = base_score * penalty_factor
    
    # Extra computation that doesn't affect result
    normalized = [x / sum(readings) for x in readings]
    entropy = 0
    for p in normalized:
        if p > 0:
            entropy -= p * __import__('math').log(p)
    
    return int(final_score)

# Main execution flow
sensor_log = collect_readings()
trend_summary = analyze_trends(sensor_log)
clean_data = filter_outliers(sensor_log, threshold=10)

# Weight configuration for scoring
weights = {'high': 1.5, 'low': 0.5}

# Dummy variables to increase cognitive load
buffer_cache = [0]*len(sensor_log)
shift_register = 0
for idx, val in enumerate(sensor_log):
    shift_register ^= (val << 1) + idx

# Key computational step
final_score = calculate_final_score(clean_data, weights)

print(f"Result: {final_score}")