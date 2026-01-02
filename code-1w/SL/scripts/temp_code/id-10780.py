import itertools

def analyze_response_time(raw_logs):
    # Irrelevant function: processes logs but not used in final computation
    processed = [x * 1.05 for x in raw_logs if x > 0]
    return sum(processed) // len(processed) if processed else 0

def generate_placeholder_metrics(n):
    # Dead code path — never called
    return [i ** 2 for i in range(n) if i % 3 == 0]

def filter_anomalies(data_stream):
    # Distractor: looks important but unused
    return [x for x in data_stream if 10 <= x <= 100]

def compute_baseline(reference_window):
    # Unused baseline calculation (red herring)
    moving_avg = sum(reference_window) / len(reference_window)
    deviation = sum(abs(x - moving_avg) for x in reference_window)
    return moving_avg, deviation

def evaluate_threshold(value, thresholds):
    # Decoy logic: appears in multiple places but not impactful
    for t in sorted(thresholds, reverse=True):
        if value > t:
            return t
    return 0

def aggregate_performance(feedback, metrics):
    # Core logic embedded with distractions
    
    # Irrelevant set operations (distractors)
    temp_set_a = {x for x in metrics if x % 2 == 0}
    temp_set_b = {x + 10 for x in metrics if x % 4 == 0}
    unused_intersection = temp_set_a & temp_set_b
    
    # Real logic begins
    base_points = sum(feedback)
    bonus_multiplier = 1
    
    # Conditional nesting with misleading branches
    if len(feedback) > 3:
        bonus_multiplier += 0.1
        if sum(metrics) > 100:
            bonus_multiplier += 0.15
            for k in range(3):
                if k in feedback:
                    bonus_multiplier += 0.05
                    break
        else:
            bonus_multiplier *= 0.9  # Dead branch due to data
    
    # List comprehension with filtering (core step)
    refined_metrics = [m for m in metrics if m in feedback]
    
    # Accumulation via itertools (required feature)
    cumulative_shift = 0
    for pair in itertools.pairwise(sorted(refined_metrics)):
        cumulative_shift += pair[1] - pair[0]
    
    # Bit manipulation decoy
    encoded_value = 0
    for m in metrics:
        encoded_value ^= (m << 2) | (m >> 1)  # Unused result
    
    # Final score calculation
    adjustment = len(unused_intersection) * 0.5  # Looks relevant but minimal impact
    final_score = base_points * bonus_multiplier + cumulative_shift - adjustment
    
    return int(final_score)

# Simulated input data
user_feedback = [4, 5, 6, 7]
system_metrics = [2, 4, 5, 6, 8, 10, 12]

# Placeholder variables to distract
baseline_data = [15, 20, 25, 30]
threshold_levels = [1, 5, 10, 25]
anomaly_stream = [5, 150, 200, 8]

# Key execution point
final_score = aggregate_performance(user_feedback, system_metrics)

# Output result
print(f"Result: {final_score}")