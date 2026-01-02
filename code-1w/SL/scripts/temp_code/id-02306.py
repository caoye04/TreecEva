import math

# Simulated cognitive assessment data with multiple metrics
def generate_assessment_data():
    base_metrics = [78, 85, 92, 64, 71, 88, 95, 73]
    noise_offset = [math.sin(i * 0.5) for i in range(8)]
    return [base_metrics[i] + noise_offset[i] for i in range(8)]

# Misleading auxiliary function (dead code path)
def calculate_aggregate_v1(data):
    total = 0
    for x in data:
        if x > 80:
            total += x * 1.2
        else:
            total += x * 0.8
    return total / len(data)

# Another decoy function with complex but unused logic
def analyze_trends(seq):
    trends = []
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            trends.append(1)
        elif seq[i] < seq[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return sum(trends) % 7

# Real processing function buried among distractions
def process_results(raw_scores, importance_weights):
    normalized = [max(0, min(100, score)) for score in raw_scores]
    
    # Apply non-linear transformation to dampen extremes
    transformed = []
    for val in normalized:
        if val >= 85:
            transformed.append(40 + 60 * math.sqrt((val - 85) / 15))
        elif val <= 60:
            transformed.append(10 + 50 * (val / 60))
        else:
            transformed.append(10 + 30 * ((val - 60) / 25))
    
    # Irrelevant intermediate calculation (distractor)
    outlier_count = 0
    for v in raw_scores:
        if abs(v - sum(raw_scores)/len(raw_scores)) > 20:
            outlier_count += 1
    adjustment_factor = math.log(1 + outlier_count)  # Unused
    
    # Core weighted computation
    weighted_sum = 0
    weight_sum = 0
    
    # Use enumerate and zip as required
    for i, (score, weight) in enumerate(zip(transformed, importance_weights)):
        if i % 2 == 0:
            # Even indices get extra smoothing
            smoothed_weight = weight * (0.9 + 0.1 * math.cos(i))
            weighted_sum += score * smoothed_weight
            weight_sum += smoothed_weight
        else:
            weighted_sum += score * weight
            weight_sum += weight
    
    preliminary_score = weighted_sum / weight_sum
    
    # Final nonlinear calibration using slicing of transformed data
    segment_a = transformed[:4]
    segment_b = transformed[4:]
    balance_metric = abs(sum(segment_a) - sum(segment_b)) / 8
    
    # Key final adjustment (uses slicing and mathematical operations)
    final_adjustment = 1 - (balance_metric / 100)
    return int(preliminary_score * final_adjustment)

# Irrelevant global variables (distractors)
MAX_ITERATIONS = 1000
temp_buffer = [0]*16
scaling_mode = "adaptive"
reference_baseline = 76.543

# Weight configuration (looks configurable but fixed for determinism)
weights_config = [1.2, 0.9, 1.4, 0.8, 1.1, 1.0, 1.3, 0.7]

# Main execution flow
if __name__ == "__main__":
    # Generate data
    assessment_data = generate_assessment_data()
    
    # Dead code: trend analysis not used in final computation
    trend_index = analyze_trends(assessment_data)
    aggregate_v1 = calculate_aggregate_v1(assessment_data)
    
    # Critical statement
    final_score = process_results(assessment_data, weights_config)
    
    # Print result as required
    print(f"Result: {final_score}")