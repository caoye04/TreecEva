def analyze_trends(data_stream):
    trend_marks = []
    for i, value in enumerate(data_stream):
        if i == 0:
            trend_marks.append(0)
        else:
            diff = value - data_stream[i-1]
            trend_marks.append(1 if diff > 0 else (-1 if diff < 0 else 0))
    return trend_marks

# Simulate sensor stability check (irrelevant to final result but adds cognitive load)
def assess_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 5

# Core evaluation logic
def evaluate_performance(feedbacks, weights):
    weighted_sum = 0
    normalization = 0
    
    # Misleading unpacking and zip usage
    for idx, (fb, wt) in enumerate(zip(feedbacks, weights)):
        adjusted = fb * wt
        if idx % 2 == 0:
            adjusted += 1  # artificial bias that affects only even indices
        weighted_sum += adjusted
        normalization += wt + (1 if idx % 2 == 0 else 0)
    
    score = weighted_sum / normalization if normalization != 0 else 0
    
    # Dead code path - never executed due to input constraints
    if score > 100:
        score = 99.9
    
    return score

# Irrelevant auxiliary computation
def generate_synthetic_data(n):
    return [i * 0.5 + (i % 3) for i in range(n)]

# Distractor: unused complex structure
class PerformanceLog:
    def __init__(self):
        self.entries = []
        self.timestamp = 0

# Main execution
if __name__ == "__main__":
    # Input data
    feedback_sequence = [4, 7, 6, 8, 5]
    benchmark_weights = [1, 2, 1, 3, 2]
    
    # Unused but plausible-looking preprocessing
    trends = analyze_trends(feedback_sequence)
    stable = assess_stability(feedback_sequence)
    
    # Generate unused synthetic data (distractor)
    dummy_data = generate_synthetic_data(10)
    
    # Key computation
    final_score = evaluate_performance(feedback_sequence, benchmark_weights)
    
    # Print required result
    print(f"Result: {final_score}")