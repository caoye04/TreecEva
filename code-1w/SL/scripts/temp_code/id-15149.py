def analyze_response_time(base_time, load_factor):
    adjusted_time = base_time * (1 + load_factor / 100)
    penalty = 0
    if adjusted_time > 2.0:
        penalty = (adjusted_time - 2.0) * 10
    return adjusted_time, penalty


def evaluate_stability(rtt_list):
    avg_rtt = sum(rtt_list) / len(rtt_list)
    variance = sum((x - avg_rtt) ** 2 for x in rtt_list) / len(rtt_list)
    stability_score = 100 - (variance * 50)
    return max(stability_score, 0)

# Simulated system performance metrics
timing_samples = [1.2, 1.5, 1.3, 1.8, 2.1, 1.4]
load_index = 15

# Irrelevant intermediate calculation (distractor)
theoretical_capacity = len(timing_samples) * 1000 // (sum(timing_samples) + 1)
buffer_zone = [x * 0.95 for x in timing_samples if x < 1.7]

# Primary metric processing
response_time, time_penalty = analyze_response_time(sum(timing_samples) / len(timing_samples), load_index)
stability_metric = evaluate_stability(timing_samples)

# Feedback calibration using lambda and list comprehension (python idiom)
calibration_curve = lambda x: x ** 0.5 if x > 0 else 0
feedback_levels = [calibration_curve(stability_metric), calibration_curve(100 - time_penalty * 2), response_time * 10]

# Misleading redundant computation (dead logic path)
consistency_flag = False
temp_weights = []
for val in feedback_levels:
    if val > 50:
        consistency_flag = True
        temp_weights.append(1.2)
    else:
        temp_weights.append(0.8)

# Core aggregation logic
weight_adjuster = lambda w: w * 1.1 if w > 1.0 else w
adjusted_weights = [weight_adjuster(w) for w in temp_weights]  # Unused distraction

# Actual final score computation
normalized_feedback = [min(f, 60) for f in feedback_levels]
raw_aggregate = sum(normalized_feedback)
scale_factor = 0.75 if response_time < 1.6 else 0.65

final_score = aggregate_performance(feedback_levels)

# Separate function to increase nesting and logic dependency
def aggregate_performance(inputs):
    filtered_inputs = [x for x in inputs if x >= 0]
    if len(filtered_inputs) == 0:
        return 0
    
    # Additional distraction: unused tracking variables
    running_total = 0
    peak_value = max(filtered_inputs)
    decay_sequence = [peak_value / (i + 1) for i in range(5)]
    
    # Real computation buried among distractions
    meaningful_sum = sum(x * 0.8 for x in filtered_inputs)
    adjustment = 10 if len(filtered_inputs) >= 2 else 5
    
    result = meaningful_sum + adjustment
    
    # Final red herring operation (no effect)
    shadow_copy = [result / 2 for _ in range(3)]
    
    return int(result)

print(f"Result: {final_score}")