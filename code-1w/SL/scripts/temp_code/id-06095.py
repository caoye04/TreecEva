def analyze_response_time(rt):
    if rt < 200:
        return 'optimal'
    elif rt < 500:
        return 'acceptable'
    else:
        return 'poor'

response_times = [150, 400, 600, 300, 800, 250]

categorize = lambda x: 1 if analyze_response_time(x) == 'optimal' else 0.5

# Misleading computation - not used in final result
temp_weights = [categorize(rt) * 1.5 for rt in response_times]
baseline_adjustment = sum(temp_weights) / len(temp_weights)

# Simulate feedback confidence levels based on categorized performance
def generate_feedback_confidence(times):
    confidences = []
    for t in times:
        category = analyze_response_time(t)
        if category == 'optimal':
            confidences.append(0.9)
        elif category == 'acceptable':
            confidences.append(0.6)
        else:
            confidences.append(0.3)
    return confidences

feedback_levels = generate_feedback_confidence(response_times)

# Distractor variable - appears relevant but unused in core logic
decay_factor = 0.95 ** len(feedback_levels)

# Auxiliary function with red herring parameters
def calculate_stability(values, window=3, dampen=False):
    stability = 0
    for i in range(len(values) - window + 1):
        window_avg = sum(values[i:i+window]) / window
        stability += window_avg * (0.8 if dampen else 1.0)
    return stability

stability_score = calculate_stability(feedback_levels, dampen=True)

# Core aggregation logic
normalizer = sum(1 for x in feedback_levels if x >= 0.6)

scaling_offset = len(response_times) % 7  # Semi-relevant distraction

# Actual key computation path
aggregate_performance = lambda fb_list: int(sum(fb_list) * 100) // (normalizer if normalizer else 1)

final_score = aggregate_performance(feedback_levels)

# Extraneous post-calculation step
post_adjustment = final_score * decay_factor if stability_score > 1.0 else final_score + 5

print(f"Result: {final_score}")