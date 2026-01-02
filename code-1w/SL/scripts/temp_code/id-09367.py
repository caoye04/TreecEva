import math

# Irrelevant helper function (dead code path)
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log2(x)
    return entropy

# Misleading intermediate processing
def preprocess_signal(signal):
    filtered = [x for x in signal if x % 2 == 0]
    normalized = [x / max(filtered) for x in filtered] if filtered else [0]
    return [round(x, 3) for x in normalized]

# Another decoy function with complex but unused logic
def analyze_pattern(seq):
    if not seq:
        return 0
    trend = 0
    for i in range(1, len(seq)):
        trend += (seq[i] - seq[i-1]) ** 2
    return int(math.sqrt(trend)) if trend > 0 else 0

# Core scientific transformation with distractors
def transform_readings(readings):
    # Distractor variables
    temp_buffer = []
    correction_factor = 1.0
    baseline_shift = sum(readings) / len(readings) if readings else 0
    
    # Actual relevant computation begins
    adjusted = [x - baseline_shift for x in readings]
    squared_devs = [x * x for x in adjusted]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    std_dev = math.sqrt(variance)
    
    # Normalize using standard deviation (key step)
    z_scores = [x / std_dev if std_dev != 0 else 0 for x in adjusted]
    
    # Apply non-linear compression (important)
    compressed = [math.tanh(x) for x in z_scores]
    
    # Distractor: unused transformation
    freq_domain = []
    for i in range(len(compressed)):
        freq_domain.append(compressed[i] * math.cos(i * math.pi / 4))
    
    return compressed  # Only compressed is used later

# Main aggregation with conditional logic and red herrings
def aggregate_trials(trials):
    all_results = []n    outlier_threshold = 2.5
    total_weight = 0.0
    weight_sum = 0.0
    
    for idx, trial in enumerate(trials):
        # Irrelevant classification
        trial_type = "A" if idx % 3 == 0 else "B" if idx % 3 == 1 else "C"
        
        # Actual processing
        processed = transform_readings(trial)
        valid_points = [x for x in processed if abs(x) < outlier_threshold]
        
        # Weighting logic (only weight_sum matters)
        weight = len(trial) ** 0.5
        weight_sum += weight
        
        mean_response = sum(valid_points) / len(valid_points) if valid_points else 0
        all_results.append(mean_response)
    
    # Final aggregation
    final_mean = sum(all_results) / len(all_results) if all_results else 0
    return final_mean, weight_sum  # Only final_mean is used

# Harvest function that combines everything
def harvest_results(experiments):
    cumulative = 0.0
    experiment_count = 0
    
    for exp in experiments:
        # Distractor set operations
        unique_values = set()
        for series in exp:
            unique_values.update([round(x, 1) for x in series])
        
        # Real work
        if exp:  # Check non-empty
            _, weighted_total = aggregate_trials(exp)
            adjustment = math.log(weighted_total + 1) if weighted_total > 0 else 0
            primary_result, _ = aggregate_trials(exp)  # Re-run to simulate expensive op
            cumulative += primary_result * adjustment
            experiment_count += 1
    
    # Final scaling based on count and average
    scale_factor = experiment_count ** 0.5 if experiment_count > 0 else 0
    final_yield = cumulative * scale_factor
    
    # Decoy output
    diagnostics = {
        "runs": experiment_count,
        "yield": final_yield,
        "hash": sum([int(abs(final_yield) * 10**i) % 10 for i in range(6)])
    }
    
    return final_yield  # This is the answer

# Simulated experimental dataset (structured but complex)
experiment_data = [
    [
        [12.5, 15.3, 14.1, 13.7, 16.2],
        [11.8, 14.0, 13.5, 15.9],
        [13.1, 14.7, 15.2, 13.9, 14.3, 15.0]
    ],
    [
        [8.9, 10.1, 9.5],
        [9.2, 11.3, 10.7, 9.8, 10.5],
        [10.0, 9.7, 10.3]
    ],
    [
        [16.5, 17.2, 15.8, 16.9, 17.5, 16.1],
        [17.0, 16.3, 15.9]
    ]
]

# Trigger execution
final_yield = harvest_results(experiment_data)
print(f"Target result: {final_yield}")