def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return [x ** 2 for x in filtered if x % 2 == 1]


def normalize(vector):
    length = sum([x ** 2 for x in vector]) ** 0.5
    return [round(x / length, 6) for x in vector] if length else vector


def compute_entropy(values):
    from math import log2
    total = sum(values)
    probabilities = [(v / total) for v in values if v > 0]
    return -sum(p * log2(p) for p in probabilities)


def extract_features(dataset):
    temp_result = []
    for i, row in enumerate(dataset):
        if i % 2 == 0:
            temp_result.append(sum(row) * (i + 1))
        else:
            temp_result.append(sum([x * 2 for x in row]))
    return temp_result


def validate_constraints(params):
    constraints = [len(params) > 3, params[0] < params[-1], sum(params) % 2 == 0]
    return all(constraints)


def transform_coordinates(coords):
    # Irrelevant transformation
    return [(y * 2, x // 2) for x, y in coords if x > 0 and y > 0]


def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    adjusted = [m * w for m, w in zip(metrics, weights)]
    base_score = sum(adjusted)
    
    # Red herring: entropy calculation on something irrelevant
    dummy_data = [10, 20, 30, 40]
    entropy_herring = compute_entropy(dummy_data)
    
    # Another distraction: coordinate transform with unused result
    points = [(10, 2), (8, 4), (6, 6)]
    transformed = transform_coordinates(points)
    
    # Real adjustment based on conditional pattern
    multiplier = 1
    for i, val in enumerate(metrics):
        if i % 2 == 1 and val > 5:
            multiplier += 0.1
    
    # Key computation
    raw_total = base_score * multiplier
    
    # Distractor: unused feature extraction
    features_herring = extract_features([[1, 2], [3, 4], [5, 6]])
    
    # Final adjustment based on set uniqueness
    unique_count = len(set(metrics))
    if unique_count >= 4:
        raw_total += 17
    
    # Dead code path
    if False:
        raw_total -= 999  # Never executed
    
    # Early return red herring (not taken)
    if sum(metrics) < 0:
        return -1
        
    return int(raw_total)

# Main execution block
if __name__ == '__main__':
    # Input data
    metrics = [3, 7, 5, 8, 2]
    weights = [0.1, 0.3, 0.2, 0.3, 0.1]
    
    # Irrelevant preprocessing
    signal_data = [-0.2, 1.5, -0.8, 2.1, 0.4]
    processed_signal = analyze_signal(signal_data, threshold=0.75)
    normalized_signal = normalize(processed_signal)
    
    # Critical call
    final_score = evaluate_performance(metrics, weights)
    
    # Unused variables - distractions
    config_flags = {'debug': False, 'verbose': True, 'mode': 'production'}
    backup_weights = weights[::-1]  # Reversed, never used
    validation_check = validate_constraints(weights)
    indexed_metrics = list(enumerate(metrics))
    paired_data = list(zip(metrics, normalized_signal[:len(metrics)]))
    
    # Output result
    print(f"Result: {final_score}")