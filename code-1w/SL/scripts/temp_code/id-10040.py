from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring system
def collect_readings():
    readings = [23.4, 24.1, 19.5, 25.0, 22.8, 20.3, 26.7, 21.9, 18.2, 24.5]
    return [r + 0.1 for r in readings]  # calibration adjustment

def analyze_trends(data):
    trend_stats = defaultdict(int)
    above_threshold = 0
    total_change = 0.0
    
    for i in range(1, len(data)):
        if data[i] > 22.0:
            trend_stats['high_count'] += 1
        if data[i] > data[i-1]:
            trend_stats['rising'] += 1
        else:
            trend_stats['falling'] += 1
        total_change += abs(data[i] - data[i-1])
    
    trend_stats['avg_fluctuation'] = round(total_change / (len(data) - 1), 2)
    return trend_stats

def compute_baseline(ref_data):
    mean_val = sum(ref_data) / len(ref_data)
    variance = sum((x - mean_val) ** 2 for x in ref_data) / len(ref_data)
    std_dev = math.sqrt(variance)
    return {'mean': mean_val, 'std_dev': std_dev}

def filter_outliers(raw_data, limit=2.0):
    baseline = compute_baseline(raw_data)
    filtered = [x for x in raw_data if abs(x - baseline['mean']) <= limit * baseline['std_dev']]
    return filtered  # some values may be removed

def derive_index(values):
    index_map = {}
    for idx, val in enumerate(values):
        shifted = int((val - min(values)) * 10)
        index_map[f'item_{idx}'] = shifted << 1  # bit shift for scaling
    return index_map

def generate_summary(features):
    summary_vector = []
    for k, v in features.items():
        if 'count' in k:
            summary_vector.append(v * 2)
        elif 'fluctuation' in k:
            summary_vector.append(int(v * 100))
        else:
            summary_vector.append(v % 7)
    return summary_vector

def validate_consistency(signal):
    checksum = 0
    for val in signal:
        checksum ^= int(val)  # bitwise XOR accumulation
    return checksum == 0

def normalize_weights(weights):
    total = sum(weights)
    return [round(w / total, 3) for w in weights]

def evaluate_stability(logs):
    stability_flags = []
    for entry in logs:
        flag = (entry > 20.0) and (entry < 25.0)
        stability_flags.append(flag)
    return Counter(stability_flags)[True]  # count stable readings

def aggregate_performance(metrics, offset):
    base = offset
    modifier = 1
    if metrics['vector'][0] > 10:
        modifier += 0.5
    if metrics['vector'][1] < 50:
        modifier -= 0.2
    
    # Core calculation path
    raw_score = sum(metrics['vector']) * modifier
    final_score = int(raw_score + base)  # key assignment point
    
    # Irrelevant transformations below (dead code paths)
    temp_result = math.log(final_score + 1) if final_score > 0 else 0
    normalized = [x / final_score for x in metrics['vector']] if final_score != 0 else []
    encoded = ''.join([chr(int(x * 10) % 26 + 97) for x in normalized[:3]]) if normalized else ''
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    raw_readings = collect_readings()
    
    # Step 2: Filter out anomalous values
    clean_readings = filter_outliers(raw_readings, limit=1.8)
    
    # Step 3: Analyze temporal trends
    trends = analyze_trends(clean_readings)
    
    # Step 4: Compute statistical baseline
    stats = compute_baseline(clean_readings)
    
    # Step 5: Derive positional indices
    indices = derive_index(clean_readings)
    
    # Step 6: Generate feature vector
    features = generate_summary(trends)
    
    # Step 7: Evaluate system stability
    stable_count = evaluate_stability(clean_readings)
    
    # Step 8: Validate data stream (checksum check - unused result)
    is_valid = validate_consistency(clean_readings)
    
    # Step 9: Normalize derived weights (irrelevant to final score)
    dummy_weights = [len(indices), trends['rising'], trends['falling'], stable_count]
    scaled_weights = normalize_weights(dummy_weights)
    
    # Step 10: Prepare metric bundle
    performance_metrics = {
        'trend': trends,
        'stats': stats,
        'indices': indices,
        'vector': features  # used in aggregation
    }
    
    # Step 11: Set base offset using modular arithmetic
    base_offset = (stable_count * 17) % 97
    
    # Step 12: Aggregate final performance score
    final_score = aggregate_performance(performance_metrics, base_offset)
    
    # Output result
    print(f"Result: {final_score}")