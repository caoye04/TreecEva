import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_stream(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 300]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]
    inverted = [100 - val for val in normalized][:len(normalized)//2]  # distractor: unused
    return normalized

# Irrelevant transformation chain
def encrypt_sequence(seq):
    encrypted = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            encrypted.append(int(val * 1.7) ^ 255)
        else:
            encrypted.append(int(val + 3.14))
    return encrypted  # never used

# Core pattern analysis with decoy logic
def evaluate_symmetry(signal):
    mid = len(signal) // 2
    left, right = signal[:mid], signal[-mid:][::-1]
    differences = [abs(a - b) for a, b in zip(left, right)]
    avg_diff = sum(differences) / len(differences) if differences else 0
    return avg_diff < 5.0

# Distractor function: looks important but unused in final path
def compute_entropy(data):
    from math import log
    freqs = {}
    for x in data:
        freqs[x] = freqs.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log(count/total) for count in freqs.values())
    return entropy

# Data windowing with enumerate misuse as distraction
def segment_signal(data, size=4):
    segments = []
    for i in range(0, len(data) - size + 1, size//2):
        window = data[i:i+size]
        tagged = [f'{i+j}:{val}' for j, val in enumerate(window)]  # creates strings
        numeric = [float(v.split(':')[1]) for v in tagged]
        segments.append(numeric)
    return segments

# Real processing function buried among distractions
def transform_readings(readings):
    # Apply moving average
    smoothed = []
    for i in range(2, len(readings)):
        smoothed.append(sum(readings[i-2:i+2]) / 4)
    # Amplify every third element
    amplified = [
        val * 1.5 if (i+1) % 3 == 0 else val
        for i, val in enumerate(smoothed)
    ]
    # Normalize again to 0-100 scale
    min_val, max_val = min(amplified), max(amplified)
    return [(v - min_val) / (max_val - min_val) * 100 for v in amplified]

# Critical analysis function that determines final result
def analyze_pattern(data, config):
    # Extract control parameters from config
    threshold_a = config['alpha']
    threshold_b = config['beta']
    limit = config['limit']
    
    # Compute rolling features
    cumulative = list(itertools.accumulate(data))
    trends = [cumulative[i+1] - cumulative[i] for i in range(len(cumulative)-1)]
    
    # Filter based on dynamic condition
    significant = [t for t in trends if abs(t) > threshold_a]
    
    # Count trend reversals
    reversals = 0
    for i in range(2, len(significant)):
        current, prev = significant[i], significant[i-1]
        if (current > 0 and prev < 0) or (current < 0 and prev > 0):
            reversals += 1
    
    # Secondary filter using threshold_b
    strong_reversals = [s for s in significant if abs(s) > threshold_b]
    
    # Key computation: harmonic weighting
    weighted_sum = 0.0
    for i, val in enumerate(strong_reversals, 1):
        weighted_sum += val / i  # harmonic decay
    
    # Final decision logic
    if reversals >= limit:
        base_score = 8542
    else:
        base_score = 4217
    
    # Apply correction factor from weighted sum
    correction = int(abs(weighted_sum) * 100) % 97
    return base_score + correction

# Main execution flow
if __name__ == '__main__':
    # Raw input data
    sensor_input = [12, 45, 67, 23, 89, 34, 78, 56, 91, 11, 37, 68, 43, 77, 52]
    
    # Preprocess
    cleaned = preprocess_sensor_stream(sensor_input)
    
    # Distractor transformations
    cipher = encrypt_sequence(cleaned)  # dead end
    entropy_value = compute_entropy(cleaned)  # irrelevant metric
    
    # Real transformation path
    transformed_data = transform_readings(cleaned)
    
    # Segment for visual analysis (unused)
    chunks = segment_signal(transformed_data, 4)
    
    # Configuration with misleading keys
    system_params = {
        'alpha': 12.5,
        'beta': 18.3,
        'limit': 3,
        'debug_mode': True,
        'buffer_size': 256,
        'timeout_ms': 500
    }
    
    # Threshold configuration (critical)
    thresholds = {
        'alpha': 12.5,
        'beta': 18.3,
        'limit': 3
    }
    
    # Analyze symmetry (distractor call)
    is_symmetric = evaluate_symmetry(transformed_data)
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    print(f"Result: {final_diagnostic}")