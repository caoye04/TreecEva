import math

# Simulated sensor data processing with diagnostic evaluation
def preprocess_readings(raw_readings):
    processed = {}
    temp_cache = []
    for k, v in raw_readings.items():
        if 'sensor' in k:
            cleaned = [x for x in v if x > 0]
            avg = sum(cleaned) / len(cleaned) if cleaned else 0
            processed[k] = round(avg, 3)
            temp_cache.append(avg)  # red herring: never used again
    return processed

# Irrelevant helper that looks important
def calculate_entropy(data_dict):
    total = sum(data_dict.values())
    entropy = 0
    for val in data_dict.values():
        if val > 0 and total > 0:
            prob = val / total
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

# Distractor function - appears in call chain but unused path
def legacy_normalization(vec):
    norm = math.sqrt(sum(x**2 for x in vec))
    return [x/norm for x in vec] if norm else vec

# Core transformation with string-based key routing
def transform_sensors(sensor_dict, mode='advanced'):
    result = {}
    keys = list(sensor_dict.keys())
    shifted = keys[-2:] + keys[:-2]  # scramble order

    for i, k in enumerate(keys):
        base_val = sensor_dict[k]
        # Apply transformation based on key name properties
        if k.endswith('2') or k.endswith('4'):
            transformed = base_val ** 1.5
        elif len(k) % 2 == 0:
            transformed = base_val * math.pi
        else:
            transformed = base_val + math.e
        
        new_key = shifted[i].replace('sensor', 'node').upper()
        result[new_key] = round(transformed, 5)
        
    # Dead code branch - only activates with invalid mode (never happens)
    if mode not in ['basic', 'intermediate', 'advanced']:
        fallback = {k: v + 1000 for k, v in result.items()}
        return fallback
        
    return result

# Diagnostic analyzer with early returns and control flow distractions
def analyze_pattern(data_map, settings):
    critical_threshold = settings['threshold']
    activation_log = []
    score_chain = []
    
    # Initialize with dummy aggregation
    aggregate = 0
    for val in data_map.values():
        aggregate += val * 0.1
    
    # Redundant normalization step (looks like it matters)
    normalized_agg = aggregate / (len(data_map) or 1)
    adjustment_factor = settings.get('factor', 1.0)
    
    # Primary logic hidden among multiple checks
    for key, value in data_map.items():
        if 'NODE_A' in key:  # only NODE_B* keys matter
            continue
            
        # Real condition chain begins here
        if 'NODE_B' in key:
            if value > critical_threshold:
                activation_log.append(True)
                bits = int(value / 10) & 7  # bit masking operation
                score_chain.append(bits ** 2)
            else:
                activation_log.append(False)
                
        # Fake pattern detector
        if key.count('_') > 2:
            score_chain.append(-999)  # dead insertion path

    # Early exit decoy
    if len(activation_log) == 0:
        return -42  # unreachable due to data setup

    # Actual answer derivation
    if len(score_chain) >= 2:
        first_moment = score_chain[0] * 2
        second_moment = score_chain[1] + 5
        combined = first_moment + second_moment
        final_score = int(combined * adjustment_factor)
        return final_score
        
    return 0

# Unused recursive function - distractor for complexity
def recursively_refine(data, depth=0):
    if depth >= 3 or not data:
        return data
    new_data = {k: v / 2 for k, v in data.items() if v > 1}
    return recursively_refine(new_data, depth + 1)

# Main execution flow
if __name__ == '__main__':
    # Initial dataset
    readings = {
        'sensor1': [12.5, 13.1, 11.9],
        'sensor2': [8.7, 9.2, 8.8],
        'sensor3': [15.0, 14.8, 15.2],
        'sensor4': [7.6, 7.9, 7.7]
    }
    
    # Configuration with misleading fields
    system_config = {
        'mode': 'advanced',
        'threshold': 25.0,
        'factor': 3.0,
        'debug': False,
        'timeout': 30,
        'retries': 2,
        'buffer_size': 1024
    }
    
    # Step 1: Preprocess raw inputs
    clean_data = preprocess_readings(readings)
    
    # Step 2: Compute irrelevant entropy metric
    entropy_value = calculate_entropy(clean_data)  # looks important
    
    # Step 3: Transform sensor layout
    transformed_data = transform_sensors(clean_data, system_config['mode'])
    
    # Step 4: Analyze final pattern
    final_diagnostic = analyze_pattern(transformed_data, system_config)
    
    # Output target result
    print(f"Result: {final_diagnostic}")