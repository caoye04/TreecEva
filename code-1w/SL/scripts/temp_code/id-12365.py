from collections import defaultdict
import math

# Simulated user feedback ratings across multiple dimensions
dimensions = ['usability', 'performance', 'reliability', 'security']
raw_feedback = [
    {'usability': 4.2, 'performance': 3.8, 'reliability': 4.5, 'security': 4.0},
    {'usability': 4.4, 'performance': 3.9, 'reliability': 4.3, 'security': 3.7},
    {'usability': 4.1, 'performance': 4.0, 'reliability': 4.6, 'security': 4.1},
    {'usability': 4.3, 'performance': 3.7, 'reliability': 4.4, 'security': 3.9}
]

# Irrelevant distraction: unused function
def calculate_average(lst):
    return sum(lst) / len(lst)

# Misleading intermediate transformation (not used in final path)
temp_aggregates = defaultdict(list)
for entry in raw_feedback:
    for dim in dimensions:
        temp_aggregates[dim].append(entry[dim] * 0.95 + 0.1)  # adjusted but unused

# Core processing begins here
baseline_shift = 0.2
benchmark_weights = {'usability': 0.3, 'performance': 0.25, 'reliability': 0.35, 'security': 0.1}

# Compute unweighted means
means = {dim: sum(entry[dim] for entry in raw_feedback) / len(raw_feedback) for dim in dimensions}

# Apply baseline correction (distractor: some values are corrected twice?)
corrected_means = {}
for dim in dimensions:
    temp_val = means[dim] + baseline_shift
    if dim == 'security':
        temp_val -= 0.05  # minor adjustment
    corrected_means[dim] = round(temp_val, 3)

# Secondary distraction: complex lambda-based scaling (unused)
scaling_factor = lambda x: math.exp(x / 10) if x > 4 else math.log(5 + x)
scaled_distract = [scaling_factor(means[dim]) for dim in dimensions]

# Build feedback summary using list comprehension with filtering
effective_dims = [dim for dim in dimensions if corrected_means[dim] >= 4.0]
feedback_summary = {dim: corrected_means[dim] for dim in effective_dims}

# Introduce red herring variable
phantom_weight = sum([0.1 for _ in range(6)])  # evaluates to 0.6 but unused

# Another distraction: nested loop that computes nothing relevant
tracking_log = []
for i in range(2):
    for j in range(3):
        tracking_log.append(i * j + 0.01)

# Core aggregation logic (depends on feedback_summary and benchmark_weights)
def aggregate_performance(feedback, weights):
    total = 0.0
    weight_sum = 0.0
    for dim in feedback:
        if dim in weights:
            total += feedback[dim] * weights[dim]
            weight_sum += weights[dim]
    # Normalize by actual weight sum (in case not all weights applied)
    return total / weight_sum if weight_sum > 0 else 0

# Execute key computation
final_score = aggregate_performance(feedback_summary, benchmark_weights)

# Print result as required
print(f"Target result: {final_score}")