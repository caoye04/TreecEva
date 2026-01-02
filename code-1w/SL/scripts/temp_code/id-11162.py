def analyze_component_health(sensor_data, thresholds):
    health_flags = {}
    for key, readings in sensor_data.items():
        avg = sum(readings) / len(readings)
        health_flags[key] = avg <= thresholds.get(key, 100)
    return health_flags

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log2
    freq = {}
    total = len(data)
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Unused transformation (dead code path)
def transform_coordinates(coords):
    transformed = []
    for x, y in coords:
        rotated_x = x * 0.707 - y * 0.707
        rotated_y = x * 0.707 + y * 0.707
        transformed.append((rotated_x, rotated_y))
    return transformed

# Complex but irrelevant signal processing mockup
def filter_noisy_signal(signal, kernel_size=3):
    filtered = [0] * len(signal)
    offset = kernel_size // 2
    for i in range(offset, len(signal) - offset):
        window = signal[i - offset : i + offset + 1]
        filtered[i] = sum(window) / len(window)
    # Edge handling (simplified)
    filtered[0] = signal[0]
    filtered[-1] = signal[-1]
    return filtered

# Core logic disguised among distractions
def calculate_weighted_sum(components, multipliers):
    temp_result = 0
    for idx, (comp, mult) in enumerate(zip(components, multipliers)):
        if idx % 2 == 0:
            temp_result += comp * mult * 1.1
        else:
            temp_result += comp * mult * 0.9
    return int(temp_result)

def recursive_combination(n, r):
    if r == 0 or r == n:
        return 1
    return recursive_combination(n - 1, r - 1) + recursive_combination(n - 1, r)

def generate_pascal_diagonal(limit):
    diagonal = []
    for i in range(limit):
        diagonal.append(recursive_combination(i + 2, 2))
    return diagonal

# Misleading statistical summary (distractor)
def get_summary_statistics(values):
    sorted_vals = sorted(values)
    mid = len(sorted_vals) // 2
    median = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return {
        'mean': round(mean, 4),
        'median': median,
        'variance': round(variance, 4)
    }

# Real computational chain buried in noise
def process_pipeline(elements):
    stage_a = [x ^ 3 for x in elements if x % 2 == 1]
    stage_b = [y << 1 for y in stage_a]
    shift_sum = sum(stage_b) >> 2
    
    # Dummy dictionary used to mislead
    debug_info = {
        'raw_elements': elements,
        'odd_filtered': [x for x in elements if x % 2 == 1],
        'post_xor': stage_a,
        'post_shift': stage_b
    }
    
    return shift_sum

def evaluate_performance(metrics, weights):
    # This zip combines relevant data but includes red herring calculations
    base_scores = []
    adjustment_factors = [0.85, 1.05, 0.95, 1.15, 0.75]  # unused in final logic
    
    for metric, weight in zip(metrics, weights):
        contribution = metric * weight
        # Some fake nonlinear scaling
        if contribution > 50:
            contribution *= 0.9
        else:
            contribution *= 1.1
        base_scores.append(contribution)
    
    # Actual answer depends only on a subset
    core_metrics = base_scores[::2]  # Take every other
    bonus = len([x for x in metrics if x > 40]) * 2
    
    # Hidden dependency on bit manipulation result
    side_channel = process_pipeline([4, 5, 6, 7, 8])
    
    primary = sum(core_metrics)
    final_score = primary + bonus + (side_channel % 17)
    
    # Dead assignment (distractor)
    final_score_debug = {
        'components': core_metrics,
        'bonus_awarded': bonus,
        'side_channel_raw': process_pipeline(list(range(3, 9)))
    }
    
    return int(final_score)

# Global configuration (some irrelevant entries)
config = {
    'timeout': 30,
    'retries': 3,
    'debug_mode': False,
    'log_level': 'INFO',
    'buffer_size': 1024
}

# Input data with plausible naming
metrics = [42, 38, 55, 29, 47]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Trigger execution
final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")