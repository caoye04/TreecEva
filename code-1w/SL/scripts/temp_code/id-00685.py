from collections import defaultdict

# Simulate manufacturing process with quality tracking
def analyze_production_cycle():
    batch_data = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
    defect_rates = {i: (100 - val) * 0.01 for i, val in enumerate(batch_data)}
    
    # Irrelevant temperature tracking (distractor)
    temperature_log = defaultdict(list)
    for hour in range(5):
        temperature_log['sensor_A'].append(22.5 + hour * 0.3)
        temperature_log['sensor_B'].append(23.1 + hour * 0.2)
    
    total_output = sum(batch_data)
    avg_output = total_output / len(batch_data)
    
    # Dead code path - never accessed (distractor)
    if False:
        placeholder = 0
        for _ in range(3):
            placeholder += 1

    cycle_time = 4.5  # hours per cycle
    setup_time = 1.2
    cleanup_time = 0.8
    total_time = cycle_time + setup_time + cleanup_time  # unused

    resource_count = 3
    
    # Secondary metric not used in final calculation
    utilization_rate = (cycle_time / (cycle_time + setup_time)) * 100
    
    efficiency_score = total_output / (cycle_time * resource_count)
    
    # Additional irrelevant computation
    projected_weekly = efficiency_score * 8 * 5
    
    return efficiency_score

result = analyze_production_cycle()
print(f"Result: {result}")