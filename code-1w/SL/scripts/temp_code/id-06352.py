def analyze_response_time(raw_logs, threshold=0.15):
    """ Irrelevant function analyzing response times (dead end). """
    anomalies = []
    for entry in raw_logs:
        if entry > threshold:
            anomalies.append(entry * 2.5)
    return [x for x in anomalies if x < 1.0]


def preprocess_metrics(data_stream):
    """ Misleading preprocessing that isn't used in final calculation. """
    cleaned = []
    offset = 0.001
    for val in data_stream:
        cleaned.append(round(val + offset, 4))
    return cleaned

# Unused global constants (red herring)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30.0
ACTIVE_MODE = False

# Core data structures
feedback_levels = [4.2, 3.8, 4.5, 4.0, 3.7, 4.3, 4.1]
benchmark_weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.1, 0.1]

# Distractor variables with plausible but unused computations
baseline_shift = sum(feedback_levels) / len(feedback_levels) - 3.5
adjusted_weights = [w * 1.1 for w in benchmark_weights]
dummy_matrix = [[i * j for j in range(3)] for i in range(3)]

# Simulated metadata (irrelevant)
system_profile = {
    'version': 'v2.3',
    'calibration': 'Q4_2023',
    'active_filters': ['noise', 'outlier']
}

# Real logic buried among distractions
def validate_consistency(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    total = 0
    for a, b in zip(arr1, arr2):
        total += a * b
    return total < 2.0


def compute_entropy(values):
    """ Dead-end mathematical transformation not used. """
    import math
    n = len(values)
    if n == 0:
        return 0.0
    mean_val = sum(values) / n
    variance = sum((x - mean_val) ** 2 for x in values) / n
    return round(math.log(variance + 1e-8), 6) if variance > 0 else 0.0


def aggregate_performance(scores, weights):
    # Key computation nested within multiple checks and distractors
    if not scores or not weights:
        return 0.0

    if len(scores) != len(weights):
        temp_weights = [1 / len(scores)] * len(scores)
    else:
        temp_weights = weights

    weighted_sum = 0.0
    max_score = max(scores)
    min_score = min(scores)
    score_range = max_score - min_score

    # Additional irrelevant normalization
    normalized_scores = []
    for s in scores:
        norm = (s - min_score) / (score_range + 1e-6) if score_range > 0 else 0.5
        normalized_scores.append(norm)

    # Actual aggregation using original scores and weights
    for idx, (score, weight) in enumerate(zip(scores, temp_weights)):
        if score >= 4.0:  # High performance bonus simulation
            weight *= 1.1
        elif score < 3.8:
            weight *= 0.9
        weighted_sum += score * weight

    # Final adjustment based on consistency heuristic
    consistency_flag = True
    for i in range(1, len(scores)):
        if abs(scores[i] - scores[i-1]) > 0.6:
            consistency_flag = False
            break

    if consistency_flag:
        weighted_sum *= 1.05

    return round(weighted_sum, 6)

# Secondary irrelevant list processing
aux_data = ['metric_a', 'metric_b', 'metric_c']
enumerated_tags = [f'{i}_{tag.upper()}' for i, tag in enumerate(aux_data)]

# Critical execution point buried in script-style flow
temp_result = analyze_response_time([0.12, 0.18, 0.14, 0.22])
preprocessed = preprocess_metrics([1.1, 2.2, 3.3])
entropy_value = compute_entropy(feedback_levels)

# This is the key statement
final_score = aggregate_performance(feedback_levels, benchmark_weights)

# Print required output
print(f"Target result: {final_score}")