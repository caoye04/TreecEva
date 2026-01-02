from itertools import compress

def analyze_efficiency(metrics):
    baseline = sum(metrics) / len(metrics)
    adjusted = [x for x in metrics if x > baseline]
    efficiency = sum(adjusted) / len(adjusted) if adjusted else 0
    return efficiency

def calculate_stress_level(workload, threshold=80):
    stress = 0
    for task in workload:
        if task > threshold:
            stress += (task - threshold) * 1.5
        elif task < threshold / 2:
            stress -= 5  # counterintuitive, but models adapt
    return max(stress, 0)

def evaluate_performance(output, risk):
    performance = 0
    scaling_factor = 1.2 if output > 60 else 0.8
    
    # Simulate conditional bonus logic
    bonus = 10 if output >= 70 and risk < 40 else (5 if output > 50 else 0)
    
    # Distractor: complex-looking but unused calculation
    shadow_risk = sum([r**2 for r in range(1, int(risk)+1)]) % 100
    phantom_score = (output * 0.3 + risk * 0.1) / (scaling_factor + 0.1)
    
    performance = output * scaling_factor - risk * 0.5 + bonus
    
    # Additional red herring: state tracking that isn't used
    audit_log = []
    audit_log.append(f'Final performance calc: {performance}')
    
    return int(performance)

# Main execution block
if __name__ == "__main__":
    # Input data
    daily_tasks = [75, 82, 90, 60, 45, 88, 73]
    productivity = analyze_efficiency(daily_tasks)
    
    # Irrelevant transformation
    normalized_tasks = [min(max(t, 0), 100) for t in daily_tasks]
    filtered_tasks = list(filter(lambda x: x > 50, normalized_tasks))
    
    # Unused set operations for distraction
    unique_workloads = set(daily_tasks)
    peak_loads = set([x for x in unique_workloads if x > 80])
    low_loads = set(range(30, 50))
    overlap = peak_loads & low_loads  # empty, but looks meaningful
    
    # Compute stress (semi-relevant, but not directly used in final answer)
    stress_level = calculate_stress_level(daily_tasks, threshold=75)
    
    # Risk factor derived from stress, but with cap
    risk_factor = min(stress_level * 2, 50)
    
    # Key statement
    final_score = evaluate_performance(productivity, risk_factor)
    
    # Print result as required
    print(f"Target result: {final_score}")