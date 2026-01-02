from collections import defaultdict

# System resource simulation with capacity thresholds
def simulate_workload():
    node_load = [12, 18, 25, 9, 30, 14]
    threshold = 20
    excess_log = defaultdict(int)
    residual_capacity = 100
    
    for load in node_load:
        if load > threshold:
            overload = load - threshold
            excess_log['overloaded_nodes'] += 1
            excess_log['total_excess'] += overload
            residual_capacity -= overload
            if residual_capacity < 10:
                break
        else:
            residual_capacity -= load // 2
    
    print(f"Result: {residual_capacity}")

simulate_workload()