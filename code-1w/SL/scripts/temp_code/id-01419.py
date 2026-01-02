import math

def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return [x ** 0.5 for x in sequence if x % 2 == 0]

def compute_entropy(data):
    # Distractor function: looks important but unused
    total = sum(data)
    probs = [d / total for d in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

def evaluate_stability(readings):
    # Unused but plausible-sounding analysis
    moving_avg = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 5 and len(moving_avg) > 0

def extract_features(dataset):
    # Red herring transformation
    features = []
    for i, val in enumerate(dataset):
        if i % 3 == 0:
            features.append(val * 1.5)
    return features

def process_metrics(data):
    # Core logic buried among distractions
    raw_values = [x['value'] for x in data]
    weights = [0.1, 0.2, 0.3, 0.4][:len(raw_values)]
    
    # Apply weighted sum with slicing distraction
    base_score = sum(raw_values[i] * weights[i] for i in range(len(raw_values)))
    
    # Additional transformations
    offset = len([x for x in raw_values if x > 50])  # list comprehension distractor
    adjustment = math.floor(base_score / 10) if base_score > 100 else 5
    
    # Key intermediate result (misleading)
    temp_result = base_score + offset * adjustment
    
    # Real computation path
    segment_a = raw_values[:3]
    segment_b = raw_values[3:]
    
    # Actual formula for final score
    correction_factor = 1 if sum(segment_a) > 120 else 0.8
    secondary_metric = sum(x**2 for x in segment_b) // (len(segment_b) or 1)
    
    # Final calculation
    final_score = int((base_score * correction_factor) + (secondary_metric * 0.1) - adjustment)
    
    # Print to ensure observable output
    return final_score

# Simulated dataset
assessment_data = [
    {'id': 'A7', 'value': 45, 'type': 'primary'},
    {'id': 'B2', 'value': 52, 'type': 'primary'},
    {'id': 'C9', 'value': 61, 'type': 'primary'},
    {'id': 'D3', 'value': 12, 'type': 'secondary'},
    {'id': 'E8', 'value': 18, 'type': 'secondary'}
]

# Unused variables - red herrings
baseline_ref = 42.5
scaling_vector = [1.01, 0.99, 1.03, 0.97]
calibration_flag = True
auxiliary_cache = {}

# Decoy operations
if calibration_flag:
    baseline_ref *= 1.1

for i in range(2):
    scaling_vector = [v * 0.95 for v in scaling_vector]

# Main execution
final_score = process_metrics(assessment_data)
print(f"Result: {final_score}")