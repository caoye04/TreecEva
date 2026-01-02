def preprocess_data(raw):
    # Irrelevant preprocessing steps (distractors)
    cleaned = [x for x in raw if x > 0]
    smoothed = [sum(cleaned[i:i+3]) / 3 for i in range(len(cleaned) - 2)]
    normalized = [x / max(smoothed) for x in smoothed]  # Not actually used
    return cleaned

# Misleading auxiliary functions
def compute_entropy(arr):
    from math import log
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    total = len(arr)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return entropy  # Unused result

def validate_sequence(seq):
    if len(seq) < 5:
        return False
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True  # Dead logic path

def transform_values(data, factor=1.5):
    # Complex-looking but irrelevant transformation
    transformed = []
    for idx, val in enumerate(data):
        temp = val * factor
        if idx % 2 == 0:
            temp += 2
        else:
            temp -= 1
        transformed.append(int(temp ** 0.5))
    return transformed  # Not used in final computation

def filter_outliers(arr, threshold=2):
    mean_val = sum(arr) / len(arr)
    std_val = (sum((x - mean_val) ** 2 for x in arr) / len(arr)) ** 0.5
    filtered = [x for x in arr if abs(x - mean_val) <= threshold * std_val]
    return filtered  # Distractor: looks important but unused

def calculate_final_score(data, weights):
    # Core logic embedded within distractions
    base_scores = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            base_scores.append(val * weights[i % len(weights)])
        else:
            base_scores.append(val + weights[i % len(weights)])
    
    # Actual key computation
    adjusted = [x for x in base_scores if x > 5]  # Filter
    exponent_shift = len(adjusted) % 4  # Used later
    
    # Real contribution to answer
    running_total = 0
    for j, score in enumerate(adjusted):
        if j % 3 == 0:
            running_total += score * 2
        elif j % 3 == 1:
            running_total -= score // 2
        else:
            running_total ^= (score % 7)  # Bitwise distraction with real effect
    
    # Final adjustment using modular arithmetic and length
    multiplier = (exponent_shift + 1) if len(adjusted) > 3 else 1
    final_part = running_total * multiplier
    
    # Red herring: complex unused structure
    stats_summary = {
        'max': max(base_scores),
        'min': min(base_scores),
        'range': max(base_scores) - min(base_scores),
        'median_guess': sorted(base_scores)[len(base_scores)//2]
    }
    
    # This is the actual answer variable
    final_score = final_part - 17  # Deterministic, depends on prior logic
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data with meaningful names
    sensor_readings = [3, 8, -1, 6, 4, 9, 2, 7, 5]
    calibration_weights = [2, 3, 1, 4]
    
    # Irrelevant variables and operations
    outlier_flags = [x < 0 or x > 10 for x in sensor_readings]
    temporal_gaps = [sensor_readings[i+1] - sensor_readings[i] for i in range(len(sensor_readings)-1)]
    gap_analysis = {i: gap for i, gap in enumerate(temporal_gaps) if gap > 1}
    
    # Multiple layers of processing (only some matter)
    processed_data = preprocess_data(sensor_readings)
    entropy_metric = compute_entropy(processed_data)
    is_valid = validate_sequence(processed_data)
    tweaked_data = transform_values(processed_data, factor=2.0)
    clean_data = filter_outliers(tweaked_data, threshold=1.8)
    
    # The real computation path
    final_score = calculate_final_score(processed_data, calibration_weights)
    
    # Output requirement
    print(f"Result: {final_score}")