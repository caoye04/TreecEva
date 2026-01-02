from collections import defaultdict, Counter
import math

def analyze_pattern(sequence):
    freq = Counter(sequence)
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def preprocess_input(raw_data):
    cleaned = raw_data.strip().lower()
    tokens = cleaned.split()
    word_count = len(tokens)
    char_freq = defaultdict(int)
    for c in cleaned:
        char_freq[c] += 1
    return tokens, dict(char_freq), word_count

def compute_checksum(data_list):
    checksum = 0
    for i, val in enumerate(data_list):
        if i % 2 == 0:
            checksum += val * 3
        else:
            checksum += val * 2
    return checksum % 1000

def generate_metrics(features):
    metric_set = {}
    temp_vals = []
    for k, v in features.items():
        if isinstance(v, int):
            temp_vals.append(v ** 2)
        elif isinstance(v, str):
            temp_vals.append(len(v))
    sorted_vals = sorted(temp_vals, reverse=True)
    
    # Irrelevant sorting and accumulation (distractor)
    cumulative = 0
    cumulatives = []
    for x in sorted_vals:
        cumulative += x
        cumulatives.append(cumulative)
    
    # Decoy transformation
    transformed = [x // 2 for x in sorted_vals if x > 5]
    
    metric_set['peak'] = max(sorted_vals) if sorted_vals else 0
    metric_set['spread'] = len(sorted_vals)
    metric_set['aggregate'] = sum(sorted_vals)
    metric_set['dummy_key'] = 'irrelevant_string'
    metric_set['placeholder'] = None
    return metric_set

def evaluate_performance(metrics, base):
    score = 0
    adjustment = 0
    
    # Real logic begins
    if metrics['spread'] > base['threshold']:
        adjustment += 15
    if metrics['aggregate'] < base['limit']:
        adjustment -= 10
    
    # Core calculation
    raw_score = metrics['peak'] * 2 + metrics['spread']
    
    # Misleading branch with dead-end computation
    if raw_score > 1000:
        overflow_correction = math.log(raw_score, 10)
        temp_score = raw_score / overflow_correction
        # This path is never taken due to input constraints (red herring)
    
    # Actual effective path
    score = raw_score + adjustment
    
    # Dead code block (never reached)
    redundant_calc = 0
    for i in range(100):
        redundant_calc += i * 2
        if i > 10:
            break  # Early exit, but entire block is unused
    
    return score

def main():
    # Simulated sensor data (real input)
    sensor_readings = [12, 8, 15, 7, 20, 5]
    checksum_val = compute_checksum(sensor_readings)  # Irrelevant downstream
    
    raw_text = "Dynamic System Optimization Module v2.1"
    tokens, char_map, wc = preprocess_input(raw_text)
    
    # Build feature set with mixed types
    features = {
        'version': 2,
        'module_id': 56,
        'payload': 'critical',
        'priority': 8,
        'status': 'active'
    }
    
    # Generate metrics (some fields used later)
    metric_data = generate_metrics(features)
    
    # Baseline configuration
    baseline = {
        'threshold': 4,
        'limit': 500
    }
    
    # Key execution point
    final_score = evaluate_performance(metric_data, baseline)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()