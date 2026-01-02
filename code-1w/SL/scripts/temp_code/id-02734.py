def calculate_performance(op_list, timings):
    weighted_times = list(map(lambda x: x[1] / (x[0] + 1), zip(op_list, timings)))
    avg_time = sum(weighted_times) / len(weighted_times)
    peak_utilization = max(op_list) / (sum(timings) + 1e-5)
    return round(avg_time * peak_utilization * 100, 3)

# System operation metrics
task_complexity = [3, 7, 4, 8, 5]
execution_times = [1.2, 0.9, 1.5, 0.7, 1.1]

def analyze_system_load(complexity, runtime):
    total_ops = sum(complexity)
    total_duration = sum(runtime)
    throughput = total_ops / (total_duration + 1e-5)
    return throughput

efficiency_score = 0
throughput_metric = analyze_system_load(task_complexity, execution_times)
efficiency_score = calculate_performance(task_complexity, execution_times)

print(f"Result: {efficiency_score}")