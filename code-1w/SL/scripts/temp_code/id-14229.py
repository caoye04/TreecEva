import math

# Simulated sensor data processing pipeline for environmental monitoring system
def preprocess_readings(raw_samples):
    filtered = [x for x in raw_samples if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    return normalized

# Irrelevant auxiliary function - computes entropy (not used in main logic)
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 6)

# Core trend analysis with multiple abstraction layers
def extract_trends(values):
    trends = []n    for i in range(1, len(values)):
        delta = values[i] - values[i-1]
        trend_category = 'up' if delta > 0.05 else 'down' if delta < -0.05 else 'stable'
        trends.append((delta, trend_category))
    return trends

# Higher-order transformation using lambda and list comprehension
def transform_sequence(seq, func):
    return [func(x) for x in seq]

# Data fusion algorithm with decoy control flows
def aggregate_metrics(trend_data, base_ref):
    # Real computation path
    magnitude_sum = sum(abs(item[0]) for item in trend_data)
    up_count = len([1 for item in trend_data if item[1] == 'up'])
    down_count = len([1 for item in trend_data if item[1] == 'down'])
    balance_score = (up_count - down_count) * 0.5
    
    # Dead code branch - never executed due to condition
    if len(trend_data) < 0:  # Impossible condition
        backup = 0
        for x in trend_data:
            backup += hash(str(x))
        return backup % 100
    
    # Another irrelevant intermediate calculation
    phantom_counter = 0
    for _ in range(3):
        phantom_counter += sum([i * 2 for i in range(5)])  # Always adds 20 three times → 60
    
    # Actual contribution (but obscured)
    active_components = [abs(item[0]) for item in trend_data if abs(item[0]) > 0.01]
    signal_strength = sum(active_components)
    
    # Final aggregation formula
    return (magnitude_sum * 1.5) + balance_score + (signal_strength * 0.2)

# Misleading diagnostic chain
initial_samples = [5, 12, 15, 20, 25, 30, 40, 55, 70, 85, 95, 105, 110]
processed = preprocess_readings(initial_samples)

# Unused transformed versions - red herrings
inverted_view = transform_sequence(processed, lambda x: 1 - x)
log_scaled = transform_sequence(processed, lambda x: math.log(x + 1e-5))

trend_data = extract_trends(processed)
baseline = sum(processed) / len(processed)

# Phantom metrics - computed but unused
entropy_diagnostic = compute_entropy(processed)
outlier_ratio = (len(initial_samples) - len(processed)) / len(initial_samples)

# Key computational statement
adjustment_factor = len([x for x in processed if x > 0.5]) * 0.75
final_diagnostic = aggregate_metrics(trend_data, baseline) + adjustment_factor

# Decoy print statements (only final one matters)
# print(f'Entropy: {entropy_diagnostic}')
# print(f'Phantom counter: {phantom_counter}')
# print(f'Outliers: {outlier_ratio:.3f}')
print(f'Result: {final_diagnostic}')