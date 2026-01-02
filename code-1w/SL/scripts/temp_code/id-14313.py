from collections import defaultdict, Counter
import itertools

# Simulated system performance metrics over time
timestamps = [100, 200, 300, 400, 500]
raw_data = [120, 140, 130, 160, 180]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A', 'B', 'C']
buffer_cache = {k: [] for k in legacy_codes}

# Real metric processing
def normalize(values):
    mean_val = sum(values) / len(values)
    return [v - mean_val for v in values]

def rolling_average(data, window=2):
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

def detect_spikes(anomalies, threshold):
    count = 0
    for a in anomalies:
        if abs(a) > threshold:
            count += 1
    return count

# Unused decoy function (dead code path)
def deprecated_analysis(x):
    temp = 0
    for i in range(len(x)):
        temp += x[i] * (i % 3)
    return temp // 2

# More irrelevant computations
offset_table = defaultdict(int)
for t in timestamps:
    offset_table[t] += (t % 7) * 2

# Core logic disguised among distractions
baseline = {'alpha': 135, 'beta': 145, 'gamma': 155}
metrics = {}

# Populate metrics with derived features
norm_data = normalize(raw_data)
roll_data = rolling_average(raw_data, 2)
spike_count = detect_spikes(norm_data, 15.0)

metrics['mean_deviation'] = sum(abs(x) for x in norm_data) / len(norm_data)
metrics['growth_trend'] = raw_data[-1] - raw_data[0]
metrics['volatility'] = sum(abs(roll_data[i+1] - roll_data[i]) for i in range(len(roll_data)-1))
metrics['anomalies'] = spike_count

# Fake correlation map (distractor)
correlation_matrix = {}
for pair in itertools.combinations(['latency', 'throughput', 'jitter'], 2):
    correlation_matrix[pair] = 0.5

# Secondary fake structure
event_log = [{'type': 'INFO', 'code': 200} for _ in range(5)]
for entry in event_log:
    entry['processed'] = False

# Critical function with embedded logic
weight_map = {'mean_deviation': -0.3, 'growth_trend': 0.5, 'volatility': -0.2, 'anomalies': -1.0}

def evaluate_performance(metrs, base):
    score = 0.0
    # Conditional weighting based on baseline thresholds
    if metrs['growth_trend'] >= 50:
        score += 10
    else:
        score -= 5
    
    # Accumulate weighted contributions
    for key, weight in weight_map.items():
        if key in metrs:
            score += metrs[key] * weight
    
    # Additional rule-based adjustment (non-linear)
    if metrs['anomalies'] == 0:
        score += 3.5
    elif metrs['anomalies'] > 2:
        score -= 7
    
    # Red herring: unused transformation
    transformed = [x ** 0.5 for x in raw_data if x > 0]
    avg_transform = sum(transformed) / len(transformed)
    dummy_impact = avg_transform * 0.01  # Not used
    
    return round(score, 4)

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Target result: {final_score}")