def analyze_efficiency(metrics):
    base_efficiency = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = len(metrics) ** 0.5
    return base_efficiency / adjustment if adjustment != 0 else 0

metrics_data = [0.8, 0.95, 0.78, 1.02, 0.88]

# Irrelevant transformation (distractor)
transformed_data = ''.join([chr(int(m * 100) + 65) for m in metrics_data])

# Dummy variables and unused computations (interference)
baseline_threshold = 0.85
exceeded_count = sum(1 for m in metrics_data if m > baseline_threshold)
penalty_factor = exceeded_count * 0.05 if exceeded_count > 2 else 0

# Simulate environmental conditions (dead computation path)
environment_log = []
for hour in range(24):
    if hour % 6 == 0:
        env_value = (hour + 1) * 0.3
        environment_log.append(f'T{hour}:{env_value:.2f}')

# Core logic begins
productivity = analyze_efficiency(metrics_data)

# Secondary metric with partial relevance
risk_levels = [abs(m - 0.9) for m in metrics_data]
risk_factor = max(risk_levels) * 10

# Additional distraction: string processing red herring
status_flags = ['HIGH' if r > 0.1 else 'LOW' for r in risk_levels]
alert_count = status_flags.count('HIGH')

# Critical function with multiple reasoning steps
config_mode = 'STANDARD'
if risk_factor > 1.0:
    config_mode = 'SAFE_MODE'
    risk_factor *= 0.8
else:
    config_mode = 'OPTIMIZED'
    productivity *= 1.1

# Final evaluation with combined arithmetic and logic
def evaluate_performance(eff, risk):
    if eff < 1.0:
        return 0
    score = (eff * 100) - (risk * 5)
    if score > 90:
        bonus = 10
        # Nested conditional with limited impact
        if risk < 0.5:
            bonus += 5
        score += bonus
    return round(score, 2)

final_score = evaluate_performance(productivity, risk_factor)
print(f'Result: {final_score}')