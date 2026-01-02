def analyze_efficiency(metrics):
    adjusted = 0
    base_multiplier = 1.2
    temp_buffer = []
    for val in metrics:
        if val > 0:
            adjusted += val * base_multiplier
            temp_buffer.append(val * 0.1)  # Irrelevant accumulation
    return adjusted


def calculate_stress_level(hours_worked, breaks_taken):
    stress = 0
    if hours_worked > 8:
        stress += (hours_worked - 8) * 2
    if breaks_taken < 2:
        stress += 3
    # Dead code branch (never executed due to logic)
    if breaks_taken > 10:
        stress = 0
    return stress + 1  # Offset factor


def extract_key_indicators(log_data):
    values = []
    for line in log_data:
        cleaned = line.strip().lower()
        if 'metric' in cleaned:
            parts = cleaned.split(':')
            if len(parts) == 2 and parts[1].isdigit():
                values.append(int(parts[1]))
    return values

# Simulated system logs with mixed content
logs = [
    'System: metric: 5',
    'Info: no data',
    'Debug: metric: 0',
    'Status: metric: 10',
    'User: action complete'
]

productivity_raw = extract_key_indicators(logs)
productivity = analyze_efficiency(productivity_raw)

hours_worked = 9
breaks_taken = 1
stress_test_result = calculate_stress_level(hours_worked, breaks_taken)

risk_factor = 0
if stress_test_result > 4:
    risk_factor = 1.5
else:
    risk_factor = 1.1

redundant_check = False
intermediate_sum = 0
for i in range(len(productivity_raw)):
    intermediate_sum += productivity_raw[i] ** 2
    if intermediate_sum > 100:
        redundant_check = True
        break

scaling_constant = 2.3
final_score = 0
def evaluate_performance(efficiency, risk):
    global scaling_constant
    score = efficiency * scaling_constant
    penalty = 0
    if risk > 1.2:
        penalty = efficiency * 0.3
    result = score - penalty
    # Additional irrelevant adjustment
    if result > 50:
        result *= 0.95
    return int(result)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")