import math

def preprocess_signal(raw_data):
    # Distractor: Normalization that isn't used in final path
    normalized = [(x - min(raw_data)) / (max(raw_data) - min(raw_data)) for x in raw_data]
    return [x for x in raw_data if x > 0]  # Only filter positives

def transform_to_frequency(signal):
    # Apply log-magnitude transformation (relevant)
    return [math.log(x + 1e-5) for x in signal]

def sliding_window_variance(data, window_size=3):
    # Distractor function: calculated but not used in final answer
    variances = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        mean = sum(window) / window_size
        variance = sum((x - mean) ** 2 for x in window) / window_size
        variances.append(variance)
    return variances

def evaluate_complexity(profile):
    # Another distractor: computes entropy but unused
    total = sum(profile)
    probabilities = [p / total for p in profile]
    return -sum(p * math.log(p + 1e-7) for p in probabilities)

def analyze_stability(log_series, threshold):
    # Core logic: count how many slices exceed threshold
    slices = [log_series[i:i+4] for i in range(0, len(log_series), 4)]  # slicing operation
    stability_flags = []
    
    for segment in slices:
        if len(segment) < 4:
            continue
        # Compute transformed metric
        metric = (segment[0] + segment[2]) * (segment[1] - segment[3])
        stability_flags.append(abs(metric) > threshold)
    
    # Final score based on pattern of flags
    score = 0
    for i, flag in enumerate(stability_flags):
        if flag and i % 2 == 0:  # only even-indexed true flags contribute
            score += int(abs(sum(log_series[i*4:(i+1)*4])))
    
    # Introduce a red herring variable
    final_adjustment = sum(1 for f in stability_flags if not f) * 0.5  # never applied
    
    return score

# Main execution
raw_input_stream = [12, -5, 8, 14, -2, 9, 11, 3, 7, -1, 5, 6]
disruption_level = 4.2

# Preprocess and transform
filtered_signal = preprocess_signal(raw_input_stream)
log_spectrum = transform_to_frequency(filtered_signal)

# Irrelevant computations (distractors)
dynamic_variances = sliding_window_variance(log_spectrum, 3)
signal_entropy = evaluate_complexity(filtered_signal)

# Key computation with slicing and logic
threshold = disruption_level * 0.75
equilibrium_score = analyze_stability(log_spectrum, threshold)

# Print result as required
print(f"Target result: {equilibrium_score}")