import math

# Simulate sensor data processing with noise filtering and efficiency calculation
def collect_sensor_data():
    raw_values = [i * 2 + (-1)**i * 3 for i in range(1, 11)]
    filtered = [x for x in raw_values if x > 0]
    return filtered

# Noise reduction using moving average (dummy function to add interference)
def smooth_signal(signal):
    window = 3
    smoothed = []
    for i in range(len(signal) - window + 1):
        avg = sum(signal[i:i+window]) / window
        smoothed.append(round(avg, 2))
    # Misleading: this value is not used later
    baseline_drift = sum(smoothed) / len(smoothed) if smoothed else 0
    return smoothed

# Core transformation function using lambda
transform_data = lambda x: x ** 0.5 if x >= 4 else x * 1.5

def analyze_patterns(dataset):
    pattern_scores = []
    for val in dataset:
        if val % 2 == 0:
            score = int(math.log(val + 1, 2))
        else:
            score = val // 3
        pattern_scores.append(score)
    
    # Intermediate aggregate not directly used in final result
    avg_pattern = sum(pattern_scores) / len(pattern_scores) if pattern_scores else 0
    peak = max(pattern_scores) if pattern_scores else 0
    
    # Introduce irrelevant control flow
    anomaly_count = 0
    for s in pattern_scores:
        if s < 0:
            anomaly_count += 1
    # Dead code path (never executed due to data constraints)
    if anomaly_count > 100:
        pattern_scores = [0] * len(pattern_scores)
        
    return pattern_scores

# Main processing pipeline
def process_metrics(raw):
    transformed = [transform_data(x) for x in raw]
    
    # Extra computation on transformed data
    squared_sum = sum([t**2 for t in transformed])
    mean_val = sum(transformed) / len(transformed) if transformed else 0
    variance_proxy = sum([(t - mean_val)**2 for t in transformed]) / len(transformed) if transformed else 0
    
    # Efficiency logic based on conditional thresholds
    efficiency_components = []
    for t in transformed:
        if t > 4.0:
            comp = t * 0.8
        elif t > 2.0:
            comp = t * 1.1
        else:
            comp = t * 1.5
        efficiency_components.append(comp)
    
    # Distractor variables
    temp_buffer = [math.sin(c) for c in efficiency_components]
    total_sin_energy = sum(temp_buffer)
    normalized_energy = total_sin_energy / len(temp_buffer) if temp_buffer else 0
    
    # Final efficiency score calculation (this is the actual answer)
    efficiency_score = int(sum(efficiency_components) // 1)  # integer division
    
    # Additional unrelated tracking
    outlier_flags = [1 if ec > 10 else 0 for ec in efficiency_components]
    flag_sum = sum(outlier_flags)
    
    # Return dict to simulate real-world output structure
    final_output = {
        "efficiency_score": efficiency_score,
        "components": efficiency_components,
        "diagnostics": {
            "baseline_drift": normalized_energy,
            "flag_count": flag_sum
        }
    }
    
    return final_output

# Execution sequence
data_points = collect_sensor_data()
smoothed_data = smooth_signal(data_points)
analysis_results = analyze_patterns(data_points)
final_output = process_metrics(data_points)

# Extract target variable
Result: {final_output['efficiency_score']}