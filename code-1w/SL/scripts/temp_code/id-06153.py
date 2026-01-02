def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 50]
    return sum(adjusted) / len(metrics) if metrics else 0

productivity = [85, 90, 78, 92, 88]
overhead = [p % 10 for p in productivity]
dummy_calc = sum(x**2 for x in overhead if x > 5)

baseline = 80
risk_factor = 0.0
for i, val in enumerate(productivity):
    deviation = val - baseline
    if deviation < 0:
        risk_factor += 0.05 * abs(deviation)
    elif deviation > 10:
        risk_factor -= 0.02 * deviation

# Simulate auxiliary data processing with zip and string methods
labels = ['Q1', 'Q2', 'Q3', 'Q4']
status = [str(val).zfill(3) + '_OK' for val in productivity]
combined = list(zip(labels, status))
filtered_status = [s for s in status if 'OK' in s]

# Use lambda to compute dynamic weights
weight_func = lambda x: 1.05 if x > 85 else 0.95
weights = list(map(weight_func, productivity))
weighted_productivity = sum(p * w for p, w in zip(productivity, weights))

# Secondary metric (not directly used but adds interference)
phantom_metric = sum(1 for s in filtered_status if s.startswith('0'))

# Core logic hidden among distractions
def evaluate_performance(efforts, penalty):
    base = sum(efforts) / len(efforts)
    adjustment = analyze_efficiency(efforts)
    return int(base + adjustment - penalty * 10)

intermediate_result = evaluate_performance(productivity, 0)
final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")