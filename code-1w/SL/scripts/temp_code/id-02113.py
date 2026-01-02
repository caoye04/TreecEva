def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = 0
    if len(metrics) > 5:
        adjustment += 10
    else:
        adjustment -= 5
    
    # Distractor: irrelevant computation
    temp_normalization = [x / (sum(metrics) + 1e-5) for x in metrics]
    normalized_sum = sum(temp_normalization)

    return base_efficiency + adjustment


def detect_anomalies(values):
    anomalies = 0
    for v in values:
        if v < 0 or v > 100:
            anomalies += 1
    # Dead code path (never executed due to logic)
    if False:
        anomalies = -1
    return anomalies

# Simulated productivity metrics over 7 days
productivity = [85, 90, 78, 92, 88, 76, 95]

# Irrelevant intermediate transformation
shifted_metrics = [x - 70 for x in productivity]
dummy_aggregate = sum(shifted_metrics) * 0.1

# Compute efficiency score
efficiency = analyze_efficiency(productivity)

# Simulate risk factors based on volatility
volatility = sum(abs(productivity[i] - productivity[i-1]) for i in range(1, len(productivity)))

# Distractor: unused risk analysis
risk_indicators = set()
if volatility > 50:
    risk_indicators.add('HIGH_VOLATILITY')
if max(productivity) - min(productivity) > 25:
    risk_indicators.add('WIDE_SPREAD')
risk_flag_count = len(risk_indicators)

# Real risk factor used later
risk_factor = 1.0
if volatility > 40:
    risk_factor *= 0.85
if detect_anomalies(productivity) > 0:
    risk_factor *= 0.9

# Another distractor variable
projected_trend = (productivity[-1] - productivity[0]) / len(productivity)

# Core evaluation logic
scaling_factor = 0.1 if efficiency > 400 else 0.2
penalty = 15 if len([p for p in productivity if p < 80]) >= 3 else 0

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Definition provided after usage (tests execution order understanding)
def evaluate_performance(perf_data, risk_multiplier):
    raw_total = sum(perf_data)
    weighted_total = raw_total * risk_multiplier
    consistency_bonus = 20 if all(p >= 75 for p in perf_data) else 0
    return int((weighted_total * scaling_factor) - penalty + consistency_bonus)

print(f"Result: {final_score}")