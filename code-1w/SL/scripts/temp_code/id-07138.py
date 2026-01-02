from collections import defaultdict, Counter
import math

# Simulated system metrics over time (timestamp -> readings)
raw_telemetry = {
    100: [3, 5, 2],
    105: [4, 4, 3],
    110: [6, 2, 1],
    115: [3, 3, 5],
    120: [2, 6, 4]
}

# Irrelevant auxiliary mapping - red herring
status_codes = {'OK': 200, 'WARN': 300, 'ERROR': 500, 'CRITICAL': 600}
code_weights = defaultdict(lambda: 1.0)
code_weights['WARN'] = 0.7
code_weights['ERROR'] = 0.3
code_weights['CRITICAL'] = 0.1  # Unused in logic

# Distractor: historical averages for unrelated subsystems
historical_load_avg = [0.95, 1.02, 0.87, 1.11, 0.76]
predicted_failures = {ts: round((val * 1.2) % 1, 2) for ts, val in enumerate(historical_load_avg)}

# Real data pipeline begins
aggregated_readings = []
for timestamp, values in raw_telemetry.items():
    avg_val = sum(values) / len(values)
    normalized = round(avg_val * (1 + math.sin(math.pi * timestamp / 60)), 2)
    aggregated_readings.append(normalized)

# Misleading transformation - looks important but unused later
transformed_metrics = [round(x ** 1.5, 1) for x in aggregated_readings if x > 3.0]

# Core metric computation
metric_data = defaultdict(float)
for i, val in enumerate(aggregated_readings):
    weight = math.cos(math.pi * i / 4) ** 2
    metric_data[f'window_{i}'] = round(val * weight, 3)

# Decoy function - never called
def calculate_rolling_anomaly(data, window=3):
    anomalies = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        z_scores = [(x - window_avg) for x in data[i:i+window]]
        anomalies.append(max(z_scores))
    return anomalies

# Secondary decoy: complex bit manipulation with no effect
bitmask = 0b101101
shifted_mask = (bitmask << 3) & 0xFF
inverted = ~shifted_mask & 0xFF
parity_check = bin(inverted).count('1') % 2

# Conditional distraction branch (never entered)
if len(transformed_metrics) > 10:
    adjusted_parody = parity_check * 100
else:
    dummy_calc = (inverted ^ 0xAA) >> 2
    temp_result = [dummy_calc * x for x in range(3)]  # Dead code path

# Key parameters
base_threshold = 2.85
penalty_factor = 1.7
bonus_multiplier = 0.9

# Evaluation logic with short-circuiting and conditional weighting
def evaluate_performance(metrics, threshold):
    score = 100.0
    bonus_applied = False
    penalty_applied = False

    sorted_keys = sorted(metrics.keys(), key=lambda x: int(x.split('_')[1]))
    
    for k in sorted_keys:
        value = metrics[k]
        
        # Primary logic branch
        if value > threshold:
            if not bonus_applied and value > threshold * 1.1:
                score += 15 * bonus_multiplier
                bonus_applied = True
        elif value < threshold * 0.7:
            deduction = abs(value - threshold) * penalty_factor
            score -= deduction
            penalty_applied = True

        # Hidden modular arithmetic dependency
        index = int(k.split('_')[1])
        if index % 2 == 0 and value > 2:
            score = (score * 1.05) if score < 120 else score  # Cap-aware boost

    # Final adjustment based on boolean state
    if bonus_applied and not penalty_applied:
        score = round(score * 1.1, 2)
    elif penalty_applied:
        score = round(score * 0.85, 2)
    
    return int(round(score))

# Additional red herring: unused counter analysis
reading_counter = Counter()
for vals in raw_telemetry.values():
    reading_counter.update([round(v, -1) for v in vals])  # Binning to nearest 10

# Critical execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Output result
print(f"Result: {final_score}")