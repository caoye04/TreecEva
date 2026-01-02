def analyze_signal(data, threshold=0.5):
    """Irrelevant function analyzing signal strength."""
    count = 0
    for val in data:
        if val > threshold:
            count += 1
    return count


def transform_coordinates(coords):
    """Decoy transformation with no impact on result."""
    transformed = []
    for i, (x, y) in enumerate(coords):
        angle = 3.14159 / 4
        x_new = x * __import__('math').cos(angle) - y * __import__('math').sin(angle)
        y_new = x * __import__('math').sin(angle) + y * __import__('math').cos(angle)
        transformed.append((x_new + i, y_new - i))
    return transformed


def compute_entropy(sequence):
    """Misleading entropy computation - unused in final logic."""
    from collections import Counter
    freqs = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for freq in freqs.values():
        p = freq / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 6)


def filter_outliers(values, factor=1.5):
    """Dead code path - never called but looks important."""
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]


def merge_dicts(d1, d2):
    """Unused utility - distractor."""
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

# Irrelevant global variables
temp_buffer = [0] * 10
config_flags = {'debug': False, 'strict_mode': True}
system_log = []

# Real input data
metrics = {
    'latency': 0.82,
    'throughput': 1250,
    'consistency': 0.94,
    'availability': 0.995,
    'scalability': 4.7
}

weights = {
    'latency': 0.2,
    'throughput': 0.25,
    'consistency': 0.2,
    'availability': 0.15,
    'scalability': 0.2
}

# Unused intermediate calculations
baseline = sum(metrics.values()) / len(metrics)
adjusted_metrics = {k: v * 1.05 for k, v in metrics.items() if k != 'latency'}

# Simulated time-series decoy
time_series = [0.1, 0.3, 0.4, 0.8, 0.82]
correlation_matrix = [[i * j for j in range(4)] for i in range(4)]

# Critical function that actually determines result
def evaluate_performance(met, wgt):
    score = 0.0
    bonus = 0.0
    penalty = 0.0

    # Normalize throughput to 0-1 scale (hypothetical max = 2000)
    norm_throughput = min(met['throughput'] / 2000, 1.0)

    # Apply weighted scoring using dictionary iteration and enumerate
    components = list(wgt.keys())
    for idx, key in enumerate(components):
        weight = wgt[key]
        raw_value = met[key]

        if key == 'throughput':
            effective_value = norm_throughput
        elif key == 'scalability':
            # Convert 1-5 scale to 0-1
            effective_value = raw_value / 5.0
        else:
            effective_value = raw_value

        contribution = effective_value * weight
        score += contribution

        # Bonus logic for high performers
        if effective_value > 0.9 and idx % 2 == 0:
            bonus += 0.02

        # Penalty for latency above threshold
        if key == 'latency' and raw_value > 0.8:
            penalty += 0.05

    final = score + bonus - penalty

    # Additional adjustment based on zip and conditional checks
    adjustments = [0.01, -0.02, 0.03, 0.0, 0.01]
    for m_key, adj in zip(components, adjustments):
        if met[m_key] > 0.9 and wgt[m_key] > 0.15:
            final += adj

    return round(final, 6)

# Dead assignment - misleading
interim_result = analyze_signal(time_series, 0.5)

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Print required output
print(f"Result: {final_score}")