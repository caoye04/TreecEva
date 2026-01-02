def analyze_efficiency(metrics):
    weighted_sum = 0
    normalization = len(metrics) + 1e-8
    for val in metrics:
        if val < 0:
            continue
        weighted_sum += val ** 0.5
    return weighted_sum / normalization

productivity = [81, 64, 100, -25, 49, 144]
efficiency = analyze_efficiency(productivity)

risk_levels = {1: 'low', 2: 'medium', 3: 'high'}
risk_counter = {level: 0 for level in risk_levels.values()}
for i in range(1, 4):
    risk_counter[risk_levels[i]] += (i * i) % 3

baseline_adjustment = sum(risk_counter.values())
adjusted_efficiency = efficiency - baseline_adjustment

# Simulate conditional workflow with lambda and set operations
task_complexity = lambda x: x | 7 ^ 3
complexity_set = set()
for val in productivity:
    if val > 0:
        complexity_set.add(task_complexity(val % 10))

size_factor = len(complexity_set)
dummy_calc = (size_factor ** 2) // 3  # Distractor

# Risk factor determined via dictionary lookup and bitwise logic
risk_index = 2
risk_flag = (risk_index & 1) == 0
risk_factor = 1.5 if risk_flag else 0.8

# Key function combining arithmetic, boolean, and control flow logic
def evaluate_performance(prod_data, risk):
    total = 0
    count = 0
    for x in prod_data:
        if x <= 0:
            continue
        bonus = 1
        if x > 100:
            bonus = 1.2
        elif x > 50:
            bonus = 1.1
        total += (x * bonus) // 10
        count += 1
    average_bonus_score = total / max(count, 1)
    
    # Apply risk adjustment
    adjusted_score = average_bonus_score * risk
    
    # Extra distraction: unused loop over dictionary items
    temp_dict = {'a': 1, 'b': 2, 'c': 3}
    aggregate = 0
    for k, v in temp_dict.items():
        aggregate += ord(k) % v
    
    return int(adjusted_score)

intermediate_result = evaluate_performance([25, 36, 169], risk_factor)
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")