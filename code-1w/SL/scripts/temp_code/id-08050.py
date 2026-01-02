import itertools

# Simulated sensor data processing pipeline for environmental monitoring system
def collect_sensor_data():
    return [23.4, 19.5, 27.3, 21.8, 30.1, 18.7, 24.9]

def filter_outliers(data, threshold=25.0):
    # Irrelevant filtering for high values (distractor)
    return [x for x in data if x < threshold]

def normalize readings(reading_list):
    min_val, max_val = min(reading_list), max(reading_list)
    return [(r - min_val) / (max_val - min_val) for r in reading_list]

def generate_combinations(values):
    # Distractor: generates combinations but not used in final path
    return list(itertools.combinations(values, 2))

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def assess_stability(variance, tolerance=0.1):
    # Misleading stability check (not actually used)
    return "stable" if variance < tolerance else "unstable"

def compute_entropy(normalized):
    import math
    return -sum(p * math.log2(p) for p in normalized if p > 0)

def extract_features(data_stream):
    filtered = filter_outliers(data_stream, 100)  # Deliberately non-restrictive threshold (red herring)
    normalized = normalize_readings(filtered)
    
    # Dead code path - never accessed
    if len(normalized) > 10:
        backup = [x * 1.1 for x in normalized]
        return backup
    
    entropy = compute_entropy(normalized)
    variance = calculate_variance(normalized)
    peak_ratio = max(normalized) / (sum(normalized) / len(normalized))
    
    # Decoy metric calculation
    pair_combinations = generate_combinations(normalized)
    combo_count = len(pair_combinations)
    
    return {
        'entropy': entropy,
        'variance': variance,
        'peak_ratio': peak_ratio,
        'size': len(normalized)
    }

# Unused function - decoy for signal processing
def apply_fourier_transform(signal):
    result = []
    for k in range(len(signal)):
        comp = sum(signal[n] * complex(0, -2 * 3.14159 * k * n / len(signal)) for n in range(len(signal)))
        result.append(abs(comp))
    return result

def evaluate_performance(metrics, weights):
    score = 0
    # Only three metrics are actually weighted; others ignored (key insight)
    relevant_keys = ['entropy', 'peak_ratio', 'size']
    for i, key in enumerate(relevant_keys):
        score += metrics[key] * weights[i]
    return int(score * 100)  # Discretization step

# Main execution flow
if __name__ == "__main__":
    raw_data = collect_sensor_data()
    
    # Multiple distractor variables
    temp_snapshot = raw_data[::2]
    average_temp = sum(raw_data) / len(raw_data)
    high_freq_spikes = [t for t in raw_data if t > 25]
    
    processed_metrics = extract_features(raw_data)
    
    # Red herring: unused alternative weight sets
    alt_weights_a = [0.5, 0.3, 0.2]
    alt_weights_b = [0.1, 0.6, 0.3]
    debug_trace = set()
    
    primary_weights = [0.4, 0.35, 0.25]  # Actual weights used
    
    # Critical assignment point
    final_score = evaluate_performance(processed_metrics, primary_weights)
    
    # Additional misleading computation
    synthetic_index = (processed_metrics['variance'] + 0.1) * 1000
    
    Result: {final_score}