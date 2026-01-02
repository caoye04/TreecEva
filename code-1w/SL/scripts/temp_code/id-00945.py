import math

# Simulated sensor data processing with performance evaluation

def preprocess(data_stream):
    cleaned = []
    noise_floor = 0.05
    for val in data_stream:
        if abs(val) > noise_floor:
            cleaned.append(round(val ** 2, 4))
    return cleaned

# Irrelevant helper - decoy function (dead path)
def analyze_trend(sequence):
    trend_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_score += 0.1
    return trend_score  # never used

# Misleading transformation chain
def transform_features(raw_features):
    transformed = []
    for x in raw_features:
        temp_val = math.log(abs(x) + 1)
        shifted = temp_val * 1.5 if temp_val < 1 else temp_val * 0.8
        transformed.append(shifted)
    # Dead end: this normalization isn't actually used later
    normalized = [t / max(transformed) for t in transformed]
    return transformed  # returns unnormalized

# Core evaluation logic
def compute_weighted_sum(metrics, weights):
    if len(metrics) != len(weights):
        raise ValueError("Mismatched dimensions")
    total = 0.0
    for m, w in zip(metrics, weights):
        total += m * w
    return total

# Red herring: complex but unused data structure
class PerformanceBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [0.0] * capacity
        self.index = 0
    
    def append(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.capacity
    
    def get_average(self):
        return sum(self.buffer) / len(self.buffer)

# Unused instance - distraction
data_buffer = PerformanceBuffer(100)

# Actual metric processor
def evaluate_metric(value, baseline, method='rms'):
    diff = abs(value - baseline)
    if method == 'rms':
        return math.sqrt(diff)
    elif method == 'linear':
        return diff * 0.5
    else:
        return diff

# Main scoring function
def evaluate_performance(weight_vector, result_vector):
    # Step 1: Preprocess raw results
    processed_results = preprocess(result_vector)
    
    # Step 2: Transform features (but we only use part of it)
    features = transform_features(processed_results)
    
    # Step 3: Compute derived metrics using slicing and enumerate
    derived_metrics = []
    for i, feat in enumerate(features):
        if i % 2 == 0:
            derived_metrics.append(feat * 0.7)
        else:
            derived_metrics.append(feat * 1.3)
    
    # Step 4: Apply evaluation on selected metrics using fixed baseline
    evaluated = []
    for dm in derived_metrics[::2]:  # every other element
        score = evaluate_metric(dm, baseline=0.5, method='rms')
        evaluated.append(score)
    
    # Step 5: Normalize weights (ensure sum to 1.0)
    weight_sum = sum(weight_vector)
    normalized_weights = [w / weight_sum for w in weight_vector]
    
    # Step 6: Truncate metrics to match weight vector length
    truncated_metrics = evaluated[:len(normalized_weights)]
    
    # Step 7: Compute final weighted score
    final_raw = compute_weighted_sum(truncated_metrics, normalized_weights)
    
    # Step 8: Post-process with rounding
    final_score = round(final_raw * 1000)  # Scale up for precision
    
    return final_score

# Simulated input data
raw_sensor_data = [0.12, -0.03, 0.45, 0.67, -0.21, 0.89, 0.04, -0.11]
metric_weights = [0.2, 0.3, 0.5]

# Dead variables - red herrings
baseline_threshold = 0.01
calibration_sequence = [x * 0.1 for x in range(10)]
temp_analysis = analyze_trend(calibration_sequence)

# Key execution point
raw_results = [x * 1.2 for x in raw_sensor_data]
final_score = evaluate_performance(metric_weights, raw_results)

print(f"Target result: {final_score}")