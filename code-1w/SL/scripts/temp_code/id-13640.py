def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [85, 90, 78, 65, 92, 88]

# Irrelevant transformation (distractor)
decay_curve = [(p ** 0.95) for p in productivity]
baseline_avg = sum(decay_curve) / len(decay_curve)

# Simulate risk exposure using set operations
event_codes = {1, 2, 3, 4, 5}
triggered_events = {2, 4}
risk_factors = {e ** 2 for e in triggered_events}  # {4, 16}
risk_set = risk_factors.union({sum(risk_factors)})  # {4, 16, 20}

# Dummy state tracker (dead code path)
current_state = {'phase': 'analysis', 'status': 0}
if len(risk_set) > 5:
    current_state['status'] = 1
else:
    current_state['status'] = current_state.get('status')

# Core evaluation logic
efficiency_rating = analyze_efficiency(productivity)
penalty = len(risk_set) * 2
raw_score = efficiency_rating - penalty

# Secondary adjustment with lambda (irrelevant to final score)
adjustment_factor = lambda x: x * 0.9 if x > 10 else x * 1.1
temp_correction = adjustment_factor(raw_score // 3)

# Key computation step
def evaluate_performance(perf_data, risks):
    base = sum(perf_data) / len(perf_data)
    risk_penalty = sum(risks) / len(risks)
    return int(base - risk_penalty + 5)

final_score = evaluate_performance(productivity, risk_set)

# Extraneous post-processing (distractor)
outlier_check = [p for p in productivity if abs(p - final_score) > 30]
sorted_risks = sorted(list(risk_set), reverse=True)

print(f"Result: {final_score}")