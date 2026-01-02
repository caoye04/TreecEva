from collections import defaultdict
import math

# Irrelevant utility function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

def analyze_trend(data):
    # Distractor: computes trend but not used in final result
    if len(data) < 2:
        return 0
    return sum(data[i+1] - data[i] for i in range(len(data)-1)) / (len(data) - 1)

def calculate_entropy(values):
    # Dead code path — looks relevant but unused
    freq = defaultdict(int)
    for v in values:
        freq[v] += 1
    probabilities = [count / len(values) for count in freq.values()]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def filter_outliers(seq, threshold=1.5):
    # Computes IQR but ultimately irrelevant
    sorted_seq = sorted(seq)
    q1 = sorted_seq[len(sorted_seq) // 4]
    q3 = sorted_seq[3 * len(sorted_seq) // 4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [x for x in seq if lower <= x <= upper]

# Core logic disguised among distractions
def apply_weighting(series, weights):
    return sum(a * b for a, b in zip(series, weights))

def evaluate_performance(metrics, base):
    # Key logic embedded within noise
    temp_results = []
    adjustments = [0.9, 1.1, 0.8, 1.2]
    
    # Red herring: complex transformation
    transformed = list(map(lambda x: round(x ** 0.5 * 1.05, 4), metrics))
    
    # Real computation hidden in middle
    raw_total = sum(metrics) * 0.75
    
    # Fake multi-step adjustment
    for i, val in enumerate(transformed):
        if i % 2 == 0:
            temp_results.append(val * adjustments[i % 4])
        else:
            temp_results.append(val * 0.95)
    
    # Decoy aggregation
    fake_score = sum(temp_results) / len(temp_results)
    
    # Actual answer computation
    deviation = sum(abs(m - base) for m in metrics)
    penalty = math.floor(deviation / 10) * 0.5
    final_score = raw_total - penalty  # <-- Critical assignment point
    
    # Unused conditional branch (dead code)
    if final_score > 100:
        final_score = 100
    elif final_score < 0:
        final_score = 0
        
    return final_score

# Simulated input data
baseline = 20
metrics = [18, 22, 19, 25, 17, 21]

# Distractor variables
config = defaultdict(lambda: 'N/A')
config['version'] = '2.1'
config['mode'] = 'diagnostic'

aux_data = [math.sin(i * 0.5) for i in range(10)]
trend_value = analyze_trend(aux_data)  # Misleading intermediate

# Weighting that looks important but isn't used in final score
custom_weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.2]
weighted_sum = apply_weighting(metrics, custom_weights)

# Outlier filtering on non-outliers (distraction)
cleaned_metrics = filter_outliers(metrics, 2.0)

# Actual target execution point
final_score = evaluate_performance(metrics, baseline)

# Print required output
print(f"Result: {final_score}")