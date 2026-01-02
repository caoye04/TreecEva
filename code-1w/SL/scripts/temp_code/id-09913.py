import math

# Simulated sensor array diagnostics with embedded logic chain

def preprocess_readings(raw_samples):
    cleaned = []
    outlier_count = 0  # distractor: not used in final logic
    for sample in raw_samples:
        if -100 < sample < 1000:  # valid range filter
            if sample > 500:
                adjusted = sample * 0.95 + 10
            else:
                adjusted = sample * 1.02
            cleaned.append(round(adjusted))
        else:
            outlier_count += 1
    return cleaned

# Irrelevant transformation - dead path
def deprecated_normalize(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

# Core analysis function with key logic
def analyze_readings(data, config):
    base_reference = config['ref']
    mode_flag = config['mode']  # distractor: influences nothing
    result = 0
    history = []  # misleading accumulation
    
    for i, val in enumerate(data):
        if i % 3 == 0 and val > base_reference:
            transformed = int(math.log(val, 2)) if val > 1 else 0
            history.append(transformed)
            result += transformed ** 2
        elif i % 4 == 2:
            result -= val % 7
    
    # Critical computation path
    secondary_weight = sum([i for i in history if i > 2])  # list comprehension
    tertiary_factor = len(set(history))  # set usage
    
    # Final diagnostic calculation
    final_score = result + secondary_weight * tertiary_factor
    
    # Decoy assignment - looks important but unused
    calibration_state = {'status': 'nominal', 'level': final_score // 10}
    
    return final_score

# Auxiliary function - never called
def compute_entropy(seq):
    freq = {}
    for x in seq:
        freq[x] = freq.get(x, 0) + 1
    return -sum((count/len(seq)) * math.log2(count/len(seq)) for count in freq.values())

# Main execution flow
if __name__ == "__main__":
    # Simulated input data
    sensor_log = [23, 450, 670, 12, 89, 901, 44, 111, 333, 77, 999]
    
    # Distractor variables
    baseline_metrics = {'mean': 200, 'peak': 999, 'samples': 11}
    temporal_weights = [0.1, 0.3, 0.6]
    aggregation_mode = 'weighted'
    
    # Actual processing pipeline
    processed = preprocess_readings(sensor_log)
    
    # More red herring code
    derived_features = []
    for v in processed:
        if v < 100:
            derived_features.append(v ** 0.5)
        elif v < 400:
            continue  # early skip - irrelevant
        else:
            derived_features.append(math.sin(v))
    
    # Key configuration map
    threshold_map = {
        'ref': 85,
        'mode': 'legacy',
        'version': '2.1'
    }
    
    # Filtering operation with side effect lookalike
    filtered_data = [x for x in processed if x > 40]  # list comprehension
    
    # Critical statement
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")