def analyze_efficiency(metrics):
    threshold = 75
    filtered = [m for m in metrics if m > threshold]
    return len(filtered) * 2

productivity = [80, 92, 67, 88, 73, 95, 85]

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return sum(x ** 0.5 for x in data if x % 2 == 0)

# Distractor variable with misleading computation
temp_adjustment = sum(1 for p in productivity if p < 80)
offset_penalty = temp_adjustment * 3.5

# Real logic begins: compute efficiency score
efficiency_score = analyze_efficiency(productivity)

# Create a set of high performers
high_performers = {p for p in productivity if p >= 85}

# Introduce a lambda for dynamic filtering (relevant)
filter_risk = lambda x: x < 90
risk_set = set(filter(filter_risk, high_performers))

# Another distractor: unused transformation
decay_factor = 0.9
projected = [val * decay_factor for val in productivity]  # Not used later

# Conditional branch that affects final outcome
if len(risk_set) > 0:
    risk_adjustment = 10
else:
    risk_adjustment = 0

# Character counting distraction (semi-relevant naming)
department_name = "Performance_Evaluation"
char_count = len([c for c in department_name if c == '_'])  # Unused

# Core calculation using multiple concepts
def evaluate_performance(eff_data, risk_group):
    base = sum(eff_data) // len(eff_data)
    penalty = len(risk_group) * 5
    return base - penalty + risk_adjustment

# Key statement
final_score = evaluate_performance(productivity, risk_set)

print(f"Result: {final_score}")