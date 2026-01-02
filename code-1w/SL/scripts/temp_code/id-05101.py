import itertools

def analyze_response_time(base, load_factor):
    # Irrelevant computation: simulates system load but only used once
    temp_load = sum([load_factor ** i for i in range(3)])
    adjusted = base * (1 + load_factor / 10)
    return round(adjusted, 2)

# Misleading data structure with unused entries
diagnostic_log = {
    'version': '2.1.0',
    'errors_seen': [],
    'metadata': {'calibration': 987, 'bias_shift': 0.045}
}

# Simulate user feedback cycles with varying quality
feedback_qualities = [0.85, 0.91, 0.76, 0.94, 0.88]
response_times = [1.2, 0.9, 1.5, 0.7, 1.1]

# Distractor: complex-looking but unused list comprehension
_ = [f"{chr(97+i)}_{j*2}" for i, j in enumerate(range(5))]

# State tracker for consistency checks (semi-relevant)
stability_counter = 0
consistency_threshold = 0.85

# Apply conditional logic to assess performance streaks
streak_active = False
max_streak = 0
current_streak = 0

for q in feedback_qualities:
    if q >= consistency_threshold:
        current_streak += 1
        streak_active = True
    else:
        if streak_active:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
            streak_active = False

if streak_active:
    max_streak = max(max_streak, current_streak)

# Compute time-weighted performance using lambda and zip
weighted_analyzer = lambda times, qualities: [
    t * q if q >= 0.8 else t * q * 0.5 
    for t, q in zip(times, qualities)
]

adjusted_times = weighted_analyzer(response_times, feedback_qualities)

# Use itertools to create sliding window (relevant only for average)
time_windows = list(itertools.pairwise(adjusted_times))

# Compute average of second elements in each pair (arbitrary aggregation)
avg_windowed = sum(window[1] for window in time_windows) / len(time_windows)

# Simulate recursive depth check (distractor with minor side effect)
def validate_depth(node, depth=0):
    if depth >= 3 or not isinstance(node, dict):
        return depth
    if 'children' in node:
        return max(validate_depth(child, depth + 1) for child in node['children'])
    return depth

mock_tree = {
    'id': 'root',
    'children': [{'id': 'A'}, {'id': 'B', 'children': [{'id': 'C'}]}]
}

tree_depth = validate_depth(mock_tree)  # Not directly used

# Core calculation: aggregate performance based on response time analysis
baseline_scores = [analyze_response_time(rt, fq) for rt, fq in zip(response_times, feedback_qualities)]

# Final scoring logic
aggregation_factor = 1.2 if max_streak >= 2 else 0.9

# Introduce conditional expression affecting final result
penalty = 1.0
if any(t > 1.3 for t in adjusted_times):
    penalty = 0.85

# Key statement
final_score = aggregation_factor * penalty * sum(baseline_scores)

# Print result as required
print(f"Target result: {final_score}")