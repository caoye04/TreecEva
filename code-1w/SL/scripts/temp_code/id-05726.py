import math

def preprocess_signal(raw_data, filter_bias):
    filtered = [x - filter_bias for x in raw_data if x > 0]
    return [math.log(val) if val > 0 else 0 for val in filtered]

def calculate_entropy(sequence):
    total = sum(sequence)
    probabilities = [s / total for s in sequence if s > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return entropy

def validate_calibration(matrix, offset):
    # Irrelevant precomputation (distractor)
    temp_sum = sum(sum(row) for row in matrix)
    normalization_factor = math.sqrt(temp_sum) if temp_sum != 0 else 1
    
    adjusted_matrix = [
        [(val + offset) ** 0.5 for val in row if val % 2 == 1] 
        for row in matrix
    ]
    
    # Semi-relevant transformation
    flattened = []
    for row in adjusted_matrix:
        for item in row:
            if item > 1:
                flattened.append(item)
    
    # Dead code path (distractor)
    if len(flattened) < 10:
        placeholder = [x * 2 for x in flattened]  # never used
    
    # Core logic: compute entropy and scale threshold
    if not flattened:
        entropy_metric = 0
    else:
        magnitude = sum(flattened) / len(flattened)
        entropy_metric = calculate_entropy([magnitude] * 3 + flattened[:5])
    
    # Key decision with conditional expression
    energy_threshold = entropy_metric * 1.75 if entropy_metric > 0.5 else entropy_metric * 0.85
    
    # Additional distraction
    baseline_score = sum(math.sin(x) for x in flattened[:3])
    anomaly_flag = baseline_score < -1
    
    return energy_threshold

# Main execution
signal_data = [12, 24, 15, 8, 33, 45, 7]
reference_grid = [[10, 12, 14], [18, 20, 22], [26, 28, 30]]

# Signal preprocessing (semi-relevant)
processed_signal = preprocess_signal(signal_data, filter_bias=5)

# Construct signal_matrix using modular arithmetic and slicing
mod_indices = [i % 4 for i in range(len(processed_signal))]
signal_matrix = [
    [int(math.exp(p)) + mod_indices[j] for j, p in enumerate(processed_signal)]
    for _ in range(3)
]

base_offset = len(processed_signal) % 7

# Critical statement
energy_threshold = validate_calibration(signal_matrix, base_offset)

print(f"Result: {energy_threshold}")