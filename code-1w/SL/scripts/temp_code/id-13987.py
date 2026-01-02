def analyze_efficiency(values):
    weighted_sum = sum(x * (i + 1) for i, x in enumerate(values))
    normalization = max(values) if values else 1
    return weighted_sum / normalization if normalization != 0 else 0

productivity = [85, 90, 78, 92, 88]
risk_factor = [0.1, 0.3, 0.2, 0.5, 0.4]

def calculate_stress_index(seq):
    stress = 0
    for val in seq:
        if val > 80:
            stress += 1
    return stress

temp_debug = [x ** 2 for x in productivity if x < 85]
baseline = sum(productivity) / len(productivity)
adjusted_risk = list(map(lambda r: r * 1.5 if r > 0.3 else r, risk_factor))

# Simulate workload distribution across teams
team_load = 0
for i in range(len(productivity)):
    team_load += productivity[i] * (1 - adjusted_risk[i])

# Irrelevant aggregation for distraction
distraction_total = 0
for x in risk_factor:
    distraction_total += x ** 3

consistency_metric = analyze_efficiency(productivity)
threshold = 85 if consistency_metric > 40 else 75

performance_bonus = 0
if baseline >= threshold:
    performance_bonus = 10
else:
    performance_bonus = 5

# Key evaluation function with lambda and conditional logic
evaluate_performance = lambda prod, risk: (
    sum(p * (1 - r) for p, r in zip(prod, risk)) + performance_bonus
)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")