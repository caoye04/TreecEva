import itertools

# Simulated system telemetry data
technical_metrics = [0.88, 0.92, 0.76, 0.94, 0.81]
user_engagement = [120, 150, 98, 200, 132]
resource_utilization = [78, 85, 65, 90, 73]

def normalize(series):
    min_val, max_val = min(series), max(series)
    if max_val == min_val:
        return [0.5 for _ in series]
    return [(x - min_val) / (max_val - min_val) for x in series]

def rolling_average(series, window=3):
    smoothed = []
    for i in range(len(series)):
        start = max(0, i - window + 1)
        smoothed.append(sum(series[start:i+1]) / (i - start + 1))
    return smoothed

def calculate_entropy(weights):
    # Irrelevant function - decoy
    import math
    return -sum(w * math.log2(w) for w in weights if w > 0)

def assess_risk_factor(data):
    # Dead code path - never used
    threshold = 0.85
    high_risk_count = sum(1 for x in data if x > threshold)
    return 'HIGH' if high_risk_count > 2 else 'LOW'

def generate_combinations(values):
    # Distractor: creates combinations but unused
    return list(itertools.combinations(values, 2))

def filter_outliers(series, threshold=1.5):
    median_val = sorted(series)[len(series)//2]
    mad = sorted([abs(x - median_val) for x in series])[len(series)//2]
    if mad == 0:
        return series
    return [x for x in series if abs(x - median_val) <= threshold * mad]

def compute_correlation(x, y):
    # Another irrelevant computation
    x_norm = normalize(x)
    y_norm = normalize(y)
    return sum(a * b for a, b in zip(x_norm, y_norm)) / len(x)

def apply_weights(values, importance):
    return [v * w for v, w in zip(values, importance)]

def aggregate_score(components, multipliers):
    weighted = apply_weights(components, multipliers)
    return sum(weighted) / sum(multipliers)

def validate_integrity(checksums):
    # Unused validation logic
    base = checksums[0]
    return all(abs(c - base) < 0.1 for c in checksums)

def process_metrics(performance_data, impact_weights):
    # Core logic begins
    norm_perf = normalize(performance_data)
    filtered = filter_outliers(norm_perf, threshold=2.0)
    
    # Simulate missing data recovery
    if len(filtered) < len(norm_perf):
        recovered = [x if x in filtered else 0.5 for x in norm_perf]
    else:
        recovered = filtered[:len(norm_perf)]
    
    # Apply transformation
    adjusted = [x ** 2 for x in recovered]
    
    # Weighted aggregation
    final_component = aggregate_score(adjusted, impact_weights)
    
    # Secondary adjustment based on distribution shape
    entropy_distractor = calculate_entropy(impact_weights)  # Computed but not used
    correlation_noise = compute_correlation(adjusted, impact_weights)  # Also unused
    
    # Final nonlinear scaling
    result = int((final_component * 10000) // 10) * 10  # Scale and snap to tens
    
    return result

# Irrelevant dataset
dummy_logs = [
    {'id': 101, 'level': 'INFO', 'size': 234},
    {'id': 102, 'level': 'DEBUG', 'size': 89},
    {'id': 103, 'level': 'WARN', 'size': 412}
]

# Unused combination set
combo_pool = generate_combinations(user_engagement)

# Main data pipeline setup
data = technical_metrics  # The actual input source
weights = [0.1, 0.3, 0.1, 0.4, 0.1]  # Importance weights

# Spurious correlation check
corr_check = compute_correlation(technical_metrics, resource_utilization)

# Trigger processing
temp_results = {}
for idx, val in enumerate(data):
    temp_results[f'entry_{idx}'] = val * weights[idx]

# Critical execution point
final_score = process_metrics(data, weights)

# Print result as required
print(f"Target result: {final_score}")