import itertools

# Realistic domain: System performance evaluation with multiple metrics

def analyze_throughput(data_points):
    if len(data_points) < 2:
        return 0
    return sum(abs(a - b) for a, b in zip(data_points, data_points[1:]))

def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * log2(p) for p in probabilities)

def filter_outliers(seq, threshold=1.5):
    if len(seq) == 0:
        return seq
    q1, q3 = sorted(seq)[len(seq)//4], sorted(seq)[-len(seq)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [x for x in seq if lower <= x <= upper]

def extract_diagonals(matrix):
    # Irrelevant function - decoy
    size = len(matrix)
    diag1 = [matrix[i][i] for i in range(size)]
    diag2 = [matrix[i][size-i-1] for i in range(size)]
    return diag1, diag2

def accumulate_segments(series):
    # Another red herring - not used in final computation
    segments = []
    current = []
    for val in series:
        if val < 0:
            if current:
                segments.append(current)
                current = []
        else:
            current.append(val)
    if current:
        segments.append(current)
    return [sum(seg) for seg in segments]

def detect_cycles(sequence):
    # Unused complex logic - distraction
    seen = {}
    for i, val in enumerate(sequence):
        if val in seen:
            return sequence[seen[val]:i]
        seen[val] = i
    return None

def bitwise_flag_check(num):
    # Used in one conditional - subtle but relevant
    return (num & (num - 1)) == 0  # power of two check

def evaluate_performance(metrics, weights):
    # Core logic begins here
    adjusted = {}
    temp_store = []

    # Distractor: unused intermediate
    redundant_calc = [x ** 0.5 for x in weights.values()]

    for k, v in metrics.items():
        if isinstance(v, list) and len(v) > 0:
            base_val = sum(v) / len(v)
        elif isinstance(v, (int, float)):
            base_val = v
        else:
            base_val = 0

        adjustment = 1.0
        if k == 'latency':
            adjustment = 0.8 if base_val < 50 else 0.6
        elif k == 'throughput':
            adjustment = 1.2 if base_val > 1000 else 1.0
        elif k == 'entropy':
            adjustment = 1.1 if base_val > 3.0 else 0.9

        # Relevant flag-based adjustment
        weight_key = f"{k}_weight"
        raw_weight = weights.get(weight_key, 1.0)
        if bitwise_flag_check(int(raw_weight * 10)):
            adjustment *= 1.05

        adjusted[k] = base_val * adjustment

    # Construct weighted score
    final_components = []
    for key in ['latency', 'throughput', 'entropy']:
        comp_key = f"{key}_weight"
        score_contrib = adjusted.get(key, 0) * weights.get(comp_key, 0)
        final_components.append(score_contrib)

    aggregate = sum(final_components)

    # Critical distractor: looks important but unused
    shadow_copy = adjusted.copy()
    shadow_copy['checksum'] = aggregate * 1.07
    shadow_copy['valid'] = True

    # Final transformation
    multiplier = weights.get('scale_factor', 1)
    offset = weights.get('offset', 0)
    result = aggregate * multiplier + offset

    # This variable is printed and asked about
    final_score = int(round(result))

    # Dead code path - never reached due to logic above
    if len(redundant_calc) > 100:
        fallback = compute_entropy(redundant_calc)
        final_score = int(fallback)

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data
    metrics = {
        'latency': [45, 52, 38, 61],
        'throughput': [1200, 1100, 1300],
        'entropy': [2.8, 3.1, 3.3, 2.9],
        'jitter': [5, 7, 6]  # Unused metric
    }

    weights = {
        'latency_weight': 0.3,
        'throughput_weight': 0.5,
        'entropy_weight': 0.2,
        'scale_factor': 2.0,
        'offset': 10,
        'debug_flag': 9  # irrelevant
    }

    # Distractor variables
    system_log = set(['init', 'ready', 'active', 'idle'])
    active_modes = {'performance', 'balanced', 'power_saving'}
    overlap = system_log & active_modes

    # Unused data structure
    time_series_data = list(itertools.accumulate([1, -1, 2, -2, 3, -3, 4]))
    cycle_detect = detect_cycles(time_series_data)

    # Dictionary operation - irrelevant
    config_map = {k: f"cfg_{v}" for k, v in weights.items()}
    config_map.pop('debug_flag', None)

    # Key execution point
    final_score = evaluate_performance(metrics, weights)

    # Output result as required
    print(f"Result: {final_score}")