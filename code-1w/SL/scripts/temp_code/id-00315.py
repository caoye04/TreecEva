import math

# Simulated sensor data processing pipeline
# Some variables are red herrings or used in dead code paths

def analyze_signal(strength):
    if strength < 0:
        return abs(strength) * 0.5
    else:
        return strength ** 0.7

# Irrelevant helper that's never called
analyze_noise = lambda n: sum([i % 3 for i in range(n)]) if n > 10 else 0

def process_metrics(raw):
    normalized = []
    peak = 0
    total = 0
    for val in raw:
        if val > peak:
            peak = val
        total += val
    avg = total / len(raw)
    for val in raw:
        normalized.append((val - avg) / (peak if peak != 0 else 1))
    return normalized

# Unused function – misleading but plausible
validate_input = lambda x: all(isinstance(i, (int, float)) and i >= 0 for i in x)

def compute_risk_factor(values):
    risk = 0
    for v in values:
        if v > 0.5:
            risk += 0.2
        elif v < -0.5:
            risk -= 0.1
    return max(0, risk)

def evaluate_performance(data):
    # Core logic embedded with distractions
    base_score = 0
    adjustments = []
    
    # Real computation begins
    for item in data:
        signal_val = analyze_signal(item)
        if signal_val > 3.0:
            base_score += 2
        elif signal_val > 1.5:
            base_score += 1
        adjustments.append(signal_val * 0.3)
    
    # Distractor: complex-looking but unused accumulation
    temp_accum = 0
    for a in adjustments:
        temp_accum += math.sin(a) ** 2 + math.cos(a) ** 2  # Always 1
    
    # Dead code path – condition never true in this context
    if len(adjustments) > 100:
        fallback = sum(adjustments) / len(adjustments)
        base_score = int(fallback)

    # Real adjustment
    modifier = len(list(filter(lambda x: x > 0.9, process_metrics(data))))
    base_score += modifier

    # Another red herring variable
    outlier_count = sum(1 for d in data if d < 0)
    if outlier_count > 5:
        base_score -= 2

    return base_score

# Simulated input data – deterministic
sensor_readings = [2, -4, 5, 3, 1, 7, 2, 3, 6]

# Irrelevant transformation
transformed = [x * 1.1 for x in sensor_readings if x > 0]

# Key execution point
metric_data = [r * 1.5 for r in sensor_readings]
final_score = evaluate_performance(metric_data)

# Ensure output is printed as required
print(f"Result: {final_score}")