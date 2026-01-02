import math

# Simulated sensor data processing system for environmental monitoring
def collect_readings():
    raw_readings = [3.2, 4.5, 6.7, 2.1, 5.8, 7.3, 4.0, 6.1]
    offset = 0.9
    adjusted = [r + offset for r in raw_readings]
    return adjusted

def filter_outliers(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    threshold = 1.8 * std_dev
    filtered = [x for x in data if abs(x - mean) <= threshold]
    return filtered

def compute_entropy(values):
    total = sum(values)
    probabilities = [(v / total) for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 6)

def transform_sequence(seq):
    # Irrelevant transformation path (dead code)
    transformed = [int(x * 10) % 7 for x in seq]
    lookup = {i: chr(97 + (i * 3) % 26) for i in range(7)}
    mapped = ''.join([lookup[t] for t in transformed])
    reversed_mapped = mapped[::-1]
    score = sum(ord(c) for c in reversed_mapped)  # Misleading intermediate result
    return score  # Not used in main logic

def generate_checksum(data):
    # Decoy function with complex but irrelevant logic
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= int(val * 100)
        checksum = (checksum * 31) % 997
    return checksum

def normalize_readings(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

def calculate_robustness_index(norm_data):
    # Robustness based on variance and distribution
    mean_norm = sum(norm_data) / len(norm_data)
    variance = sum((x - mean_norm) ** 2 for x in norm_data) / len(norm_data)
    index = (1 - variance) * 100
    return int(index)

def temporal_trend_analysis(data_list):
    # Another red herring: computes trend but not used
    diffs = [data_list[i+1] - data_list[i] for i in range(len(data_list)-1)]
    positive_trend = sum(1 for d in diffs if d > 0)
    negative_trend = sum(1 for d in diffs if d < 0)
    net_bias = positive_trend - negative_trend
    return net_bias * 10

def aggregate_indicators(filtered, normalized):
    # Combines multiple metrics into a diagnostic vector
    avg_filtered = sum(filtered) / len(filtered)
    entropy = compute_entropy(filtered)
    peak_concentration = max(normalized)
    spread_metric = max(filtered) - min(filtered)
    return [avg_filtered, entropy, peak_concentration, spread_metric]

def analyze_metrics(metrics_vector):
    base_score = metrics_vector[0] * 100
    entropy_weight = 1 - (metrics_vector[1] / 3.0)  # Assume max entropy ~3
    concentration_factor = metrics_vector[2] ** 2
    adjustment = (metrics_vector[3] * 50) * entropy_weight
    final_score = base_score * concentration_factor + adjustment
    
    # Apply non-linear correction using lambda
    corrector = lambda x: math.tanh(x / 1000) * x
    refined = corrector(final_score)
    
    # String-based flag generation (irrelevant but plausible)
    category = 'HIGH' if refined > 800 else 'MODERATE' if refined > 500 else 'LOW'
    flag_code = f'DX-{category[0]}-{int(refined % 89)+11}'
    flag_length = len(flag_code.replace('-', ''))
    
    # Final diagnostic includes string method distraction
    description = f"Diagnostic output level {refined:.2f} - Status: {flag_code.lower()}"
    token_count = len(description.split())
    hash_value = sum(ord(c) for c in description if c.isalpha()) % 1000
    
    # Actual answer derivation (non-obvious due to distractions)
    final_diagnostic = int(refined - hash_value + flag_length * 2)
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    readings = collect_readings()
    cleaned = filter_outliers(readings)
    processed_data = normalize_readings(cleaned)
    
    # Irrelevant side computations (distractors)
    dummy_transform = transform_sequence(cleaned)
    security_hash = generate_checksum(cleaned)
    trend_bias = temporal_trend_analysis(cleaned)
    
    indicators = aggregate_indicators(cleaned, processed_data)
    final_diagnostic = analyze_metrics(indicators)
    
    # Critical print statement
    print(f'Result: {final_diagnostic}')