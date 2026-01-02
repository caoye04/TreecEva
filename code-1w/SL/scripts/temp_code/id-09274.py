import math

def preprocess_inputs(raw):
    # Irrelevant preprocessing (dead path)
    if len(raw) == 0:
        return [0]
    cleaned = [x for x in raw if x > 0]
    normalized = [math.log(x + 1) for x in cleaned]
    return normalized

def compute_bias_factor(values):
    # Misleading statistical distraction
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return math.sqrt(variance) if variance > 0.5 else 0.5

def evaluate_threshold(signal, limit=100):
    # Unused function with red herring logic
    if any(s > limit for s in signal):
        return sum(s ** 0.5 for s in signal if s > 0)
    return 0

def filter_anomalies(dataset):
    # Complex but irrelevant filtering
    anomalies = []
    for i, val in enumerate(dataset):
        if i > 0 and abs(val - dataset[i-1]) > 3 * compute_bias_factor(dataset):
            anomalies.append(i)
    return [v for i, v in enumerate(dataset) if i not in anomalies]

def aggregate_performance(data, config):
    # Core logic embedded in distractions
    base_scores = []
    for entry in data:
        score = 0
        # Real contribution: weighted sum of transformed features
        if entry['active']:
            raw_value = entry['reading'] ^ entry['checksum']  # Bitwise XOR relevant
            adjusted = raw_value * config['gain']
            if adjusted > 50:
                adjusted -= config['decay']
            score += adjusted
        base_scores.append(score)
    
    # Distractor: complex list comprehension with partial relevance
    filtered_scores = [s for s in base_scores if s > 10]
    if len(filtered_scores) < 3:
        filtered_scores.append(15)
    
    # Actual answer computation buried here
    total = sum(filtered_scores)
    penalty = len(data) % 7 * config['penalty_factor']
    final_score = int(total - penalty)  # Key assignment point
    
    # Dead code branches below
    if final_score < 0:
        final_score = abs(final_score) ^ 10
    elif final_score > 1000:
        temp = math.ceil(final_score / 3)
        for _ in range(2):
            temp = int(temp * 0.9)
        final_score = temp

    return final_score

# Simulated sensor readings with metadata
logged_data = [
    {'reading': 23, 'checksum': 18, 'active': True},
    {'reading': 45, 'checksum': 27, 'active': True},
    {'reading': 12, 'checksum': 10, 'active': False},
    {'reading': 67, 'checksum': 61, 'active': True},
    {'reading': 33, 'checksum': 35, 'active': True}
]

# Configuration map with decoy keys
weights = {
    'gain': 2,
    'decay': 8,
    'penalty_factor': 3,
    'smoothing': 0.95,
    'threshold_cap': 200,
    'buffer_size': 5
}

# Irrelevant intermediate processing
raw_inputs = [d['reading'] for d in logged_data]
cleaned_inputs = preprocess_inputs(raw_inputs)
bias_correction = compute_bias_factor(cleaned_inputs)
signal_test = evaluate_threshold(cleaned_inputs)
pruned_data = filter_anomalies(cleaned_inputs)

# Critical execution point
final_score = aggregate_performance(logged_data, weights)

# Output result
print(f"Result: {final_score}")