def analyze_efficiency(metrics):
    adjusted = [m * 1.5 for m in metrics if m > 20]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [15, 25, 30, 40, 10]

# Irrelevant metric tracking (distractor)
temp_tracker = []
for val in productivity:
    temp_tracker.append(val ** 2 + 3 * val - 1)

baseline = 25
offset = 0
if len(productivity) % 2 == 0:
    offset += 5
else:
    offset -= 2

# Simulate conditional tuning (semi-relevant)
correction_factor = 1.1 if sum(productivity) / len(productivity) > baseline else 0.9

# Apply correction and compute efficiency index
efficiency_index = analyze_efficiency(productivity) * correction_factor

# Risk assessment module
risk_levels = {'low': 1, 'med': 2, 'high': 3}
risk_history = ['low', 'med', 'low', 'high']
risk_count = {k: risk_history.count(k) for k in risk_levels}
risk_factor = risk_count['med'] * risk_levels['med'] + risk_count['high'] * risk_levels['high']

# Dummy state tracking (dead code path)
current_state = 'active'
state_log = []
if current_state == 'inactive':
    state_log.append('reset')

# Core evaluation logic
penalty = 0
for i, p in enumerate(productivity):
    if p < baseline:
        penalty += (baseline - p) // 5

# Secondary adjustment based on bitwise pattern analysis (moderately relevant)
signal = efficiency_index ^ risk_factor
if signal & 1:
    penalty += 1

# Final performance scoring
final_score = 0
def evaluate_performance(prod, risk):
    base = sum(p // 5 for p in prod)
    adjustment = base // risk if risk else 0
    return base - adjustment - penalty

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")