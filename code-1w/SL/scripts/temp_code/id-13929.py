from itertools import compress

def analyze_efficiency(logs):
    total_ops = sum(logs)
    avg_op_time = total_ops / len(logs) if logs else 0
    efficiency = total_ops / (avg_op_time + 1)
    return efficiency

def calculate_risk(monitoring_data):
    anomalies = [x > 85 for x in monitoring_data]
    high_risk_count = sum(anomalies)
    risk_factor = high_risk_count * 1.75
    temp_adjustment = sum([x * 0.1 for x in monitoring_data])  # Distractor
    return risk_factor

def evaluate_performance(productivity, risk):
    base_score = productivity * 2.5
    penalty = risk * 1.2 if risk > 20 else 0
    bonus = 10 if productivity > 100 else 0  # Not triggered
    final_score = base_score - penalty + bonus
    intermediate_debug = base_score + penalty  # Irrelevant tracking
    return final_score

def main():
    # Simulated system telemetry
    cpu_load = [78, 82, 80, 91, 76, 84, 89]
    task_throughput = [15, 20, 18, 25, 22, 19, 24]
    memory_usage = [65, 70, 72, 88, 60, 75, 85]  # Partially used

    # Core metrics
    productivity = analyze_efficiency(task_throughput)
    
    # Misleading preprocessing
    filtered_memory = list(compress(memory_usage, (x > 70 for x in cpu_load)))
    shadow_metric = sum(x**2 for x in filtered_memory) / 100  # Dead-end computation

    # Risk assessment
    risk_factor = calculate_risk(cpu_load)
    
    # Final evaluation
    final_score = evaluate_performance(productivity, risk_factor)
    
    # Red herring: unused diagnostic
    diagnostics = {"peak_load": max(cpu_load), "stability": len(cpu_load) - sum(x > 85 for x in cpu_load)}
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()