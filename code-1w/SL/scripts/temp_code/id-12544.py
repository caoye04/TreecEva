def analyze_response_times(responses):
    # Irrelevant function: analyzes response times but not used in final calculation
    avg = sum(responses) / len(responses)
    variance = sum((x - avg) ** 2 for x in responses) / len(responses)
    return [x for x in responses if x < avg + variance]


def validate_calibration(data):
    # Dead code path: never called
    calibrated = [x * 0.95 for x in data]
    return all(50 < x < 100 for x in calibrated)

# Simulated user feedback levels across multiple sessions
feedback_levels = [
    [4, 5, 6],
    [7, 8, 7],
    [6, 6, 5],
    [9, 8, 9],
    [5, 4, 5]
]

# Weight matrix – only the diagonal matters; off-diagonal are red herrings
weights = [
    [0.8, 0.1, 0.1],
    [0.1, 0.9, 0.2],
    [0.0, 0.1, 0.85]
]

# Distractor variables: unused accumulators
running_total = 0
buffer_cache = []

# Irrelevant transformation: mimics useful preprocessing
processed_feedback = []
for session in feedback_levels:
    shifted = [x - 1 for x in session]  # Distractor shift
    processed_feedback.append(shifted)

# Hidden logic: only the middle element of each session is actually used
extracted_midpoints = [session[1] for session in feedback_levels]  # Key extraction

# Decoy aggregation using full arrays (never executed)
"""
full_aggregation = 0
for i in range(len(feedback_levels)):
    for j in range(len(feedback_levels[i])):
        full_aggregation += feedback_levels[i][j] * weights[i % 3][j % 3]
"""

# Real computation begins: use only midpoints and diagonal weights
weighted_sum = 0.0
normalization_factor = 0.0

for idx, value in enumerate(extracted_midpoints):
    weight = weights[idx % 3][idx % 3]  # Only diagonal elements contribute
    weighted_sum += value * weight
    normalization_factor += weight

# Secondary distractor: complex slicing that computes nothing relevant
history_log = ['A', 'B', 'C', 'D', 'E']
critical_slice = history_log[1:4:1]
duplicate_check = [x for x, _ in zip(critical_slice, extracted_midpoints)]

# Another decoy: bit manipulation with no impact
bit_flag = 0
for val in extracted_midpoints:
    bit_flag ^= (val << 2) | 0x3

# Core logic hidden among distractions: average of weighted midpoints
aggregate_performance = lambda fb, w: sum(
    fb[i] * w[i % 3][i % 3] for i in range(len(fb))
) / sum(w[i % 3][i % 3] for i in range(len(fb)))

final_score = aggregate_performance(feedback_levels, weights)

# Misleading print statements removed; only final result is output
print(f"Result: {final_score}")