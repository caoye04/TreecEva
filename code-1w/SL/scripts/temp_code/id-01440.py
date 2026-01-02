def analyze_efficiency(metrics):
    adjusted_metrics = {}
    for k, v in metrics.items():
        if 'effic' in k:
            adjusted_metrics[k] = v * 1.1
        elif 'overhead' in k:
            adjusted_metrics[k] = max(v - 5, 0)
        else:
            adjusted_metrics[k] = v  
    return adjusted_metrics

metrics_data = {
    'efficiency_core': 82,
    'overhead_network': 12,
    'efficiency_cache': 76,
    'latency_base': 45,
    'overhead_cpu': 8
}

processed = analyze_efficiency(metrics_data)

productivity = 0
for key, value in processed.items():
    if 'effic' in key:
        productivity += value / 10
    elif 'latency' in key:
        productivity -= value / 20

# Simulate risk assessment with string analysis
task_sequence = "Audit,Deploy,Test,Deploy,Monitor"
task_list = task_sequence.lower().replace(' ', '').split(',')
unique_tasks = set(task_list)
duplicate_count = len(task_list) - len(unique_tasks)

risk_modifier = 1.0
if 'deploy' in unique_tasks:
    risk_modifier += 0.1
if duplicate_count > 0:
    risk_modifier += 0.05 * duplicate_count

baseline_risk = 10
risk_factor = baseline_risk * risk_modifier

# Irrelevant distraction: character frequency analysis (not used in final logic)
char_freq = {}
for task in task_list:
    for c in task:
        char_freq[c] = char_freq.get(c, 0) + 1
sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
most_common_char = sorted_chars[0][0] if sorted_chars else ''

# Another distraction: unused helper calculation
def calculate_theoretical_max(tasks):
    return len(set(tasks)) * 100 // (len(tasks) + 1) if tasks else 0

theoretical_limit = calculate_theoretical_max(task_list)

# Core evaluation logic
def evaluate_performance(efficiency, risk):
    base_score = efficiency * 10
    penalty = risk * 2.5
    bonus = 0
    if efficiency > 15:
        bonus = 8
    return base_score - penalty + bonus

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")