from collections import defaultdict, Counter
import math

# Simulated sensor data processing with performance evaluation
sensor_readings = [145, 267, 145, 89, 267, 89, 89, 301, 145, 267]
baseline_threshold = 150
calibration_factor = 0.87

# Irrelevant auxiliary mapping (distractor)
type_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
mode_registry = defaultdict(int)
for reading in sensor_readings:
    mode_registry[reading % 4] += 1

# Misleading preprocessing path (dead code - never used)
elevated_flags = []
for idx, val in enumerate(sensor_readings):
    if val > baseline_threshold:
        elevated_flags.append((idx, val * calibration_factor))

# Actual signal filtering logic
filtered_signals = [x for x in sensor_readings if x < baseline_threshold]
suppressed_count = len([x for x in sensor_readings if x >= baseline_threshold])

# Generate frequency stats (partially relevant)
freq_stats = Counter(sensor_readings)
dominant_value = freq_stats.most_common(1)[0][1]  # max frequency count

# Auxiliary transformation chain
normalized = [round(math.log(x + 1) * 1.2, 2) for x in filtered_signals]
shifted_norm = [n + 0.5 for i, n in enumerate(normalized) if i % 2 == 0]

# Fake risk scoring (red herring - looks important but unused)
risk_scores = {}
for val in set(sensor_readings):
    z_score = (val - 200) / 50
    risk_scores[val] = round(1 / (1 + math.exp(-z_score)), 3)

# Decoy function that appears central but is never called
def legacy_calibrate(data, factor=1.1):
    return [int(x * factor) for x in data if x % 2 == 1]

# Real metric computation begins
metric_weights = {
    'consistency': 0.4,
    'stability': 0.3,
    'efficiency': 0.2,
    'rarity': 0.1
}

raw_outcomes = {
    'mode_frequency': sum(1 for x in freq_stats.values() if x == dominant_value),
    'suppression_rate': suppressed_count / len(sensor_readings),
    'signal_clarity': len(filtered_signals) / (len(sensor_readings) + 1e-8),
    'entropy': sum(-freq / len(sensor_readings) * math.log(freq / len(sensor_readings)) 
                  for freq in freq_stats.values())
}

# Secondary decoy structure (unused weighted average)
fake_aggregate = 0
weight_sum = 0
for k, v in raw_outcomes.items():
    fake_weight = abs(hash(k)) % 10 + 1
    fake_aggregate += v * fake_weight
    weight_sum += fake_weight
fake_aggregate /= weight_sum if weight_sum else 1

# Real evaluation function
def evaluate_performance(weights, outcomes):
    # Intermediate derived metrics
    adjusted_entropy = outcomes['entropy'] * 100
    normalized_rarity = outcomes['mode_frequency'] * outcomes['signal_clarity']
    
    # Hidden logic: only three metrics are actually used
    components = [
        weights['consistency'] * adjusted_entropy,
        weights['stability'] * (1 - outcomes['suppression_rate']) * 100,
        weights['rarity'] * normalized_rarity * 10
    ]
    
    # Critical distraction: commented alternate formula
    # final = sum(weights[k] * outcomes[k] * 10 for k in outcomes) 
    
    base_score = sum(components)
    
    # Apply hidden correction based on dominant pattern
    if dominant_value >= 3:
        base_score *= 1.1
    
    # Final nonlinear scaling
    return int(math.floor(base_score))

# Trigger key computation
temp_debug = [math.sin(x) for x in range(5)]  # irrelevant trigonometric trace
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Output target result
print(f"Result: {final_score}")