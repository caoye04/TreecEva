def analyze_metrics(data, threshold=0.75):
    # Irrelevant helper computation (distractor)
    baseline = sum(d * 0.3 for d in data if d > 0.5)
    adjustment = len([x for x in data if x < 0.4]) * 0.05
    
    # Red herring: unused transformation
    transformed = [round(d ** 0.5, 3) for d in data]
    
    # Meaningful but obscured logic
    valid_count = sum(1 for d in data if d >= threshold)
    return valid_count if valid_count > 0 else 1

# Decoy function that looks important but isn't used
def compute_efficiency(values):
    total = 0
    for v in values:
        if v > 0.6:
            total += v * 1.2
        elif v > 0.3:
            total += v * 0.8
    return total / len(values) if values else 0

# Another red herring: complex-looking but unused bitwise operation
temp_flag = 0b101010
config_mask = 0b1110001
masked_result = temp_flag & ~config_mask

# Simulated sensor readings (real input data)
sensor_readings = [0.81, 0.72, 0.88, 0.63, 0.91, 0.77, 0.85]

# Auxiliary calculation with misleading name
critical_load = sum(1 for r in sensor_readings if r > 0.7) + len(sensor_readings) // 4

# Conditional expression used idiomatically (required python feature)
scaling_factor = 1.5 if all(r > 0.6 for r in sensor_readings) else 0.9

# Complex data transformation chain (mix of relevant and irrelevant)
filtered = [r for r in sensor_readings if r > 0.65]
drift_compensated = [r - 0.02 if r < 0.8 else r for r in filtered]

# Core logic buried among distractions
primary_signals = list(filter(lambda x: x >= 0.75, drift_compensated))
secondary_weight = len(drift_compensated) - len(primary_signals)

# Key intermediate variable (but not final)
effective_yield = len(primary_signals) * scaling_factor

# Dead code path (never executed, distractor)
if False:
    effective_yield *= 0.5
    secondary_weight = 0

# Boolean logic with short-circuiting (required paradigm)
is_stable = len(primary_signals) >= 3 and (not not secondary_weight or True)
status_code = 200 if is_stable else 404

# Real computation wrapped in conditional expression (required feature)
def evaluate_performance(readings, min_qual=0.75):
    count_high = analyze_metrics(readings, min_qual)
    base_score = count_high * 100
    
    # Distractor: unused nested structure
    diagnostics = {
        'outliers': [r for r in readings if r < 0.6],
        'peak': max(readings),
        'adjusted_avg': sum(r * 1.1 for r in readings) / len(readings)
    }
    
    # Actual answer derivation (non-obvious due to context)
    penalty = 10 if len([r for r in readings if r < 0.65]) > 1 else 0
    return int(base_score - penalty) if count_high >= 3 else int(base_score * 0.7)

# Irrelevant global counter (distractor)
global_counter = 0
for i in range(len(sensor_readings)):
    global_counter += (i * 2) % 3

# Final execution point — this is what matters
final_score = evaluate_performance(sensor_readings)

# Output requirement
print(f"Result: {final_score}")