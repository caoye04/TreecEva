import math

def preprocess_data(raw):
    # Irrelevant preprocessing steps (dead code path)
    cleaned = [x for x in raw if x > 0]
    temp_offset = sum(cleaned) / len(cleaned) if cleaned else 0
    adjusted = [x - temp_offset for x in cleaned]
    return [abs(x) for x in adjusted]


def transform_features(values):
    # Distractor function: looks important but unused
    transformed = []
    for v in values:
        if v == 0:
            transformed.append(1)
        else:
            transformed.append(math.log(abs(v)) * math.sin(v))
    return transformed


def filter_outliers(seq, threshold=2.5):
    mean_val = sum(seq) / len(seq)
    std_dev = (sum((x - mean_val) ** 2 for x in seq) / len(seq)) ** 0.5
    # This function is called but its result is ignored — red herring
    return [x for x in seq if abs(x - mean_val) / std_dev < threshold]


def compute_weighted_sum(elements, factors):
    # Relevant function: computes weighted sum used later
    total = 0
    for i in range(len(elements)):
        total += elements[i] * factors[i % len(factors)]
    return total


def calculate_entropy(values):
    # Misleading intermediate computation (not part of final answer)
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    probs = [count / len(values) for count in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 6)


def calculate_final_score(dataset, config):
    # Core logic begins here — nested and interwoven with noise
    
    # Step 1: Extract specific slices
    segment_a = dataset[::2]
    segment_b = dataset[1::2]
    
    # Step 2: Compute derived metrics (some irrelevant)
    avg_a = sum(segment_a) / len(segment_a)
    avg_b = sum(segment_b) / len(segment_b)
    diff_metric = abs(avg_a - avg_b) * 1.5  # Not actually used
    
    # Step 3: Apply weighting using config (critical step)
    weighted_total = compute_weighted_sum(dataset, config)
    
    # Step 4: Normalize based on dynamic scale
    magnitude_factor = math.sqrt(sum(x**2 for x in dataset))
    normalized_score = weighted_total / magnitude_factor if magnitude_factor != 0 else 0
    
    # Step 5: Adjust using constant shift (hidden in logic chain)
    shift_value = len([x for x in config if x > 1])  # Count of weights > 1
    adjusted_score = normalized_score + shift_value
    
    # Step 6: Final nonlinear transformation
    if adjusted_score >= 0:
        final = math.tanh(adjusted_score) * 100
    else:
        final = -math.log(1 + abs(adjusted_score)) * 50
    
    return round(final, 6)

# Main execution block
if __name__ == "__main__":
    
    # Input data (real signal embedded in noise)
    raw_input = [-3, 7, 2, -8, 5, 12, -1, 4]
    weights = [0.5, 2.0, 1.5, 0.8, 3.0]  # Used in calculation
    
    # Dead variables — look meaningful but unused
    baseline_metrics = {"offset": 0.25, "tolerance": 1.7, "damping": 0.9}
    calibration_sequence = [math.cos(i * 0.1) for i in range(10)]
    
    # Trigger distractor functions
    filtered_data = filter_outliers(raw_input, threshold=3.0)  # Result ignored
    entropy_value = calculate_entropy(raw_input)  # Computed but unused
    
    # Actual relevant processing starts here
    processed = preprocess_data(raw_input)  # Actually used
    
    # Introduce more noise: unused transformations
    feature_space = []
    for val in processed:
        if val > 3:
            feature_space.append(val ** 0.5)
        else:
            feature_space.append(val ** 2)
    
    # Key statement
    final_score = calculate_final_score(processed, weights)
    
    # Output target result
    print(f"Result: {final_score}")