def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = 0
    if len(metrics) > 3:
        adjustment += 5
    else:
        adjustment -= 2
    
    temp_debug = [x ** 0.5 for x in metrics if x > 10]  # Irrelevant computation
    scaling_factor = len(temp_debug) or 1
    adjusted = base_efficiency * (1 + adjustment / 10) / scaling_factor
    return int(adjusted)


def track_progress(history):
    peak = max(history)
    avg = sum(history) / len(history)
    volatility = sum(abs(history[i] - history[i-1]) for i in range(1, len(history)))
    return {'peak': peak, 'average': avg, 'jumps': volatility}

# Simulate system health assessment
health_metrics = [8, 12, 15, 7, 20]
system_risk = 0
for val in health_metrics:
    if val < 10:
        system_risk += 3
    elif val > 18:
        system_risk += 1

productivity = [90, 85, 92, 78, 88]
overhead_cost = sum(p // 10 for p in productivity) * 0.5  # Distractor

risk_factor = system_risk / len(health_metrics)

# Auxiliary debug trace - not used in final result
diagnostic_log = []
for i, p in enumerate(productivity):
    status = 'HIGH' if p > 85 else 'LOW'
    diagnostic_log.append(f"Day {i}: {status}")

processed_diagnostic = [entry.replace('HIGH', 'OPTIMAL') for entry in diagnostic_log]  # Dead code path

interim_result = analyze_efficiency(productivity)

snapshot = track_progress(productivity)
baseline = snapshot['average']

effective_rate = interim_result / baseline if baseline else 0

# Core logic hidden among distractions
def evaluate_performance(perf_data, risk):
    raw_total = sum(perf_data)
    penalty = raw_total * (risk / 10)
    bonus = 10 if len(perf_data) >= 5 else 5
    
    # Complex conditional expression combining multiple factors
    multiplier = 1.2 if raw_total > 400 and risk < 2 else (0.8 if risk > 3 else 1.0)
    
    temp_val = (raw_total - penalty + bonus) * multiplier
    
    # More red herring variables
    projected = temp_val * 1.1
    buffer_adjustment = projected * 0.05
    final_calc = temp_val - buffer_adjustment  # This line doesn't affect anything
    
    return int(temp_val)  # Actual return value

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")