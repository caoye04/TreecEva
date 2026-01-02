from collections import defaultdict, Counter
import math

# Simulated sensor data for a health monitoring system
def generate_sensor_data():
    return [58 + (i * 2) % 17 for i in range(15)]

def analyze_rhythm(pattern):
    # Irrelevant rhythm analysis (red herring)
    rhythm_score = 0
    for i in range(1, len(pattern)):
        if pattern[i] > pattern[i-1]:
            rhythm_score += 1
    return rhythm_score * 0.7

def compute_entropy(values):
    # Another distraction: entropy calculation not used in final result
    freq = Counter(values)
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

def validate_readings(readings):
    # Dead code path - never actually called
    if all(x > 40 for x in readings):
        return True
    return False

def filter_anomalies(data, limit=70):
    # Misleading filtering operation
    return [x for x in data if x < limit]

def calculate_baseline(signal):
    # Decoy function that computes but isn't used
    return sum(signal[:5]) / 5

def extract_features(dataset):
    # Extracts multiple features, some irrelevant
    stats = defaultdict(float)
    stats['peak'] = max(dataset)
    stats['trough'] = min(dataset)
    stats['range'] = stats['peak'] - stats['trough']
    stats['midpoint'] = (stats['peak'] + stats['trough']) / 2
    stats['slope'] = (dataset[-1] - dataset[0]) / len(dataset)
    return stats

def evaluate_stability(metrics, config):
    # Complex conditional logic with red herrings
    stability = 0
    if metrics['range'] < config.get('max_variance', 30):
        stability += 10
    if abs(metrics['slope']) < 0.5:
        stability += 5
    if metrics['midpoint'] > 60:
        stability += 7
    return stability * config.get('weight', 1.0)

def process_metrics(data, criteria):
    # Core processing with embedded distractions
    
    # Step 1: Extract meaningful features
    features = extract_features(data)
    
    # Step 2: Compute auxiliary values (some irrelevant)
    temp_log = [math.log(x) for x in data if x > 0]
    avg_log = sum(temp_log) / len(temp_log)
    
    # Step 3: Apply threshold logic
    above_threshold = list(filter(lambda x: x > criteria['critical_level'], data))
    
    # Step 4: Count occurrences using Counter (partially relevant)
    counts = Counter(data)
    frequent_values = [k for k, v in counts.items() if v > 1]
    
    # Step 5: Evaluate system stability (used in final calculation)
    config = {'weight': 1.2, 'max_variance': 25}
    stability_index = evaluate_stability(features, config)
    
    # Step 6: Simulate fallback mechanism (dead branch)
    fallback_mode = False
    if len(above_threshold) == 0 and stability_index > 20:
        fallback_mode = True
    else:
        pass  # Placeholder for future expansion
    
    # Step 7: Calculate weighted diagnostic score
    base_score = features['peak'] * 0.3
    trend_modifier = 1 + (features['slope'] / 10)
    
    # Step 8: Final computation chain
    raw_diagnostic = base_score * trend_modifier
    adjustment = stability_index * 0.6
    final_diagnostic = int(raw_diagnostic + adjustment)
    
    # Print intermediate decoys to mislead reasoning
    debug_info = {
        'anomaly_count': len([x for x in data if x < 50]),
        'entropy': compute_entropy(data),
        'rhythm': analyze_rhythm(data)
    }
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Generate real data
    health_data = generate_sensor_data()
    
    # Define decision thresholds
    thresholds = {
        'critical_level': 70,
        'warning_base': 60
    }
    
    # Call target function
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output the required result
    print(f"Target result: {final_diagnostic}")