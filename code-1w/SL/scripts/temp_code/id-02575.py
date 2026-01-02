def analyze_response_times(responses):
    avg_time = sum(responses) / len(responses)
    threshold = 0.5 * avg_time
    fast_count = sum(1 for t in responses if t < threshold)
    return fast_count > len(responses) * 0.3

# Simulated user interaction data
timing_data = [1.2, 0.8, 1.5, 0.4, 1.1, 0.9]

class EngagementTracker:
    def __init__(self, baseline):
        self.baseline = baseline
        self.adjustment = 0.1
    
    def update(self, value):
        return value * (1 + self.adjustment) if value > self.baseline else value

tracker = EngagementTracker(baseline=1.0)
adjusted_metrics = [tracker.update(t) for t in timing_data]

# Irrelevant distraction: buffer calculation
decay_factor = 0.9
buffer_zone = [t * decay_factor for t in adjusted_metrics]
smoothed = sum(buffer_zone) / len(buffer_zone)  # unused

# Core logic begins
feedback_levels = [0.6, 0.8, 0.75, 0.92, 0.68]
weights = [1, 2, 1, 3, 2]

# Misleading pre-processing
normalization_sum = sum(weights)
normalized_weights = [w / normalization_sum for w in weights]

# Distractor: conditional expression with side effect-like appearance
status_flag = 'high' if sum(feedback_levels) / len(feedback_levels) > 0.75 else 'medium'
scale_factor = 1.2 if status_flag == 'high' else 1.0  # not actually used later

# Real computation interleaved with noise
aggregate_performance = lambda levels, wts: sum(l * w for l, w in zip(levels, wts))

data_pairs = list(zip(feedback_levels, weights))
reversed_pairs = [(w, l) for l, w in data_pairs]  # unused

# Key execution point
final_score = aggregate_performance(feedback_levels, weights)

# More red herring: set operations on irrelevant derived data
distinct_levels = set(feedback_levels)
distinct_weights = set(weights)
overlap_check = distinct_levels & distinct_weights  # empty, irrelevant

# Final output
print(f"Result: {final_score}")