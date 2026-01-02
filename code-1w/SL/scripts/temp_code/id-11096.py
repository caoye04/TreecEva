from collections import defaultdict
import math

# Simulate system health metrics over time
def collect_metrics(days):
    data = defaultdict(list)
    for i in range(days):
        data['cpu'].append((i * 2.5) % 100)
        data['memory'].append(70 + (i % 5) * 3)
        data['disk_io'].append((i * 1.8) % 80)
    return data

def analyze_trend(values):
    trend = sum(values[-10:]) / 10 if len(values) > 10 else sum(values) / len(values)
    return round(trend, 2)

def normalize(val, max_val=100):
    return val / max_val

def compute_volatility(series):
    mean_val = sum(series) / len(series)
    variance = sum((x - mean_val) ** 2 for x in series) / len(series)
    return math.sqrt(variance)

def apply_correction(x, method='linear'):
    # Irrelevant correction function (dead path)
    return x * 1.1 if method == 'linear' else x * 0.9

def filter_outliers(data_list, threshold=2):
    # Unused function - red herring
    mean_val = sum(data_list) / len(data_list)
    std_dev = math.sqrt(sum((x - mean_val) ** 2 for x in data_list) / len(data_list))
    return [x for x in data_list if abs(x - mean_val) <= threshold * std_dev]

def assess_risk_level(value, category):
    # Misleading risk logic (not used in final calculation)
    if category == 'cpu' and value > 85:
        return 'critical'
    elif value > 70:
        return 'warning'
    else:
        return 'normal'

# Core logic with distractors
baseline = {
    'cpu': 65.0,
    'memory': 72.0,
    'disk_io': 45.0,
    'network': 30.0  # Unused field
}

metrics = collect_metrics(14)

# Distractor: irrelevant transformations
transformed = {}
for k, v in metrics.items():
    transformed[k] = [normalize(x) for x in v]

volatilities = {}
for k, v in metrics.items():
    volatilities[k] = compute_volatility(v)

# Fake aggregation path (dead end)
aggregated = 0
for key in ['cpu', 'memory', 'disk_io']:
    aggregated += analyze_trend(transformed[key])
aggregated /= 3

# Real computation begins here — hidden among noise
adjusted_metrics = {}
for key in baseline.keys():
    if key in metrics:
        recent_avg = analyze_trend(metrics[key])
        adjustment_factor = 1 + (recent_avg - baseline[key]) / 100
        adjusted_metrics[key] = recent_avg * adjustment_factor

# Conditional expression chain (core relevance)
performance_ratio = (
    (adjusted_metrics['cpu'] / baseline['cpu']) if baseline['cpu'] != 0 else 1
) * (
    (adjusted_metrics['memory'] / baseline['memory']) if baseline['memory'] != 0 else 1
) * (
    (adjusted_metrics['disk_io'] / baseline['disk_io']) if baseline['disk_io'] != 0 else 1
)

scaling_factor = 100 if performance_ratio >= 1 else 80

# Critical intermediate (misleading name)
raw_score = performance_ratio * scaling_factor

# Secondary adjustment using conditional logic
penalty = 0
if raw_score > 95:
    penalty = 5
elif raw_score < 70:
    penalty = 10
else:
    penalty = 2

interim_result = raw_score - penalty

# Final evaluation with tuple unpacking distraction
factors = (interim_result, 0.95)
adjusted_raw, decay = factors

# Actual final score computation
final_score = int(adjusted_raw * decay)

# Output required format
print(f"Result: {final_score}")