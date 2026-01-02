def analyze_efficiency(output, overhead):
    if output <= 0:
        return 0
    efficiency = (output - overhead) / output
    return efficiency if efficiency > 0 else 0.0


def validate_string_input(s):
    # Irrelevant string validation function (distractor)
    if not isinstance(s, str):
        return False
    cleaned = s.strip().lower()
    return cleaned.startswith('proc') and cleaned.endswith('ed')


def calculate_base_metric(data_points):
    total = 0
    for x in data_points:
        if x % 2 == 0 and x > 10:
            total += x // 2
    return total

# Simulated monitoring system variables
process_log = 'processed_batch_42'
validation_result = validate_string_input(process_log)  # Distractor variable

baseline_data = [12, 15, 24, 7, 30, 18]
base_metric = calculate_base_metric(baseline_data)
efficiency_ratio = analyze_efficiency(sum(baseline_data), len(baseline_data) * 2)

# Intermediate irrelevant computation
phantom_value = 0
for i in range(3):
    for j in range(2):
        phantom_value += (i + j) ** 2  # Dead-end calculation

productivity = base_metric * efficiency_ratio
risk_factor = 1

if efficiency_ratio < 0.6:
    risk_factor += 1
elif len(baseline_data) > 5:
    risk_factor += 0.5  # Triggered: baseline_data has 6 elements

# Core logic with key assignment
adjusted_productivity = productivity + (efficiency_ratio * 10)
penalty = 0
if str(risk_factor).endswith('5'):
    penalty = 2.5

final_score = evaluate_performance(productivity, risk_factor)

# Mock function to simulate realistic context
def evaluate_performance(prod, risk):
    normalized = prod / (1 + risk)
    if normalized > 100:
        return int(normalized // 2)
    bonus = 5 if prod > 40 else 0
    return int(normalized + bonus)

# Misleading late-stage operation (does not affect final_score)
dummy_tracker = []
for k in range(int(efficiency_ratio * 10)):
    dummy_tracker.append(k * base_metric // (k + 1))

print(f"Result: {final_score}")