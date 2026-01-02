from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
raw_data = [85, 90, 78, 92, 88, 76, 95, 89]
weights = {'precision': 0.4, 'recall': 0.3, 'latency': 0.2, 'throughput': 0.1}

# Irrelevant auxiliary calculation (distractor)
dummy_counter = defaultdict(int)
for val in raw_data:
    if val > 85:
        dummy_counter['high'] += 1
    else:
        dummy_counter['low'] += 1

# Misleading transformation (dead path)
adjusted_latency = []
for x in raw_data:
    temp_val = x * 0.95
    if temp_val < 80:
        adjusted_latency.append(temp_val + 5)
    # This branch does not contribute to final result

# Core metric processing
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) * 100 for v in values]

normalized_metrics = normalize(raw_data)

# Simulate multi-dimensional results (some fields unused)
raw_results = {
    'precision': normalized_metrics[0],
    'recall': normalized_metrics[1],
    'latency': normalized_metrics[2],
    'throughput': normalized_metrics[3],
    'reliability': 91.5,  # Unused field
    'availability': 99.0   # Unused field
}

metric_weights = weights  # Redundant assignment for distraction

# Secondary distractor: unused helper function
def calculate_ema(data, alpha=0.3):
    ema = [data[0]]
    for i in range(1, len(data)):
        ema.append(alpha * data[i] + (1 - alpha) * ema[-1])
    return ema

# Another red herring: complex but irrelevant set operation
observed = set(raw_data)
expected = {75, 80, 85, 90, 95}
missing = expected - observed
impact_factor = len(missing) * 0.5 if missing else 0.0

# Key computation chain
effective_scores = {}
for key in metric_weights:
    if key in raw_results:
        effective_scores[key] = raw_results[key] * 0.01  # Convert to ratio

# Weighted aggregation with conditional adjustment
base_score = 0.0
for k, w in metric_weights.items():
    base_score += effective_scores[k] * w

# Apply non-linear adjustment based on threshold logic
if base_score >= 0.85:
    bonus = 0.08
elif base_score >= 0.75:
    bonus = 0.05
else:
    bonus = 0.02

penalty = 0.0
if impact_factor > 0:
    penalty = 0.03

adjusted_score = base_score + bonus - penalty

# Final scaling and rounding
final_score = round(adjusted_score * 1000)  # Scale to integer metric

# Output result as required
print(f"Result: {final_score}")