def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1] * (1 + threshold):
            trend.append('surge')
        elif data[i] < data[i-1] * (1 - threshold):
            trend.append('drop')
        else:
            trend.append('stable')
    return trend

# Irrelevant helper function (distractor)
def normalize(values):
    max_val = max(values)
    return [v / max_val for v in values]

# Another decoy function with misleading purpose
def compute_entropy(seq):
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Core logic disguised among noise
baseline = [0.8, 1.2, 0.9, 1.5, 1.1]
metrics = [1.1, 1.3, 0.7, 1.6, 1.05]
correlation_matrix = [[0 for _ in range(5)] for _ in range(5)]

# Unused but plausible-looking intermediate calculations
temporal_weights = list(map(lambda x: x ** 0.5, baseline))
weighted_metrics = [m * w for m, w in zip(metrics, temporal_weights)]

# Fake data transformation chain
def transform(signal):
    shifted = signal[1:] + [signal[0]]
    return [abs(s - 1.0) for s in shifted]

transformed = transform(weighted_metrics)
slice_window = transformed[::2][:3]

# Real evaluation logic buried under distractions
def evaluate_performance(measures, reference):
    length = min(len(measures), len(reference))
    deviations = []
    adjustment_factor = 1.0
    
    # Hidden key calculation path
    for i in range(length):
        dev = abs(measures[i] - reference[i])
        deviations.append(dev)
        
        # Conditional mutation of factor based on red herring condition
        if dev > 0.3 and i % 2 == 0:
            adjustment_factor *= 0.9
        elif i in [1, 3]:
            adjustment_factor += 0.05  # Misleading increment
    
    # Actual core computation
    avg_dev = sum(deviations) / length
    raw_score = 100 * (1 - avg_dev)
    
    # Final adjustment using correct path (others are dead ends)
    if avg_dev < 0.25:
        final_bonus = 15
    elif avg_dev < 0.4:
        final_bonus = 5
    else:
        final_bonus = -10
    
    result = raw_score + final_bonus
    
    # Dead code branch — never reached due to logic above
    if adjustment_factor > 2.0:
        result *= adjustment_factor  # Decoy operation
    
    return int(round(result))

# Simulated analysis (unused)
trends = analyze_trend(metrics, 0.1)
entropy_value = compute_entropy(trends)

# Key execution point
final_score = evaluate_performance(metrics, baseline)

# Print required output
print(f"Result: {final_score}")