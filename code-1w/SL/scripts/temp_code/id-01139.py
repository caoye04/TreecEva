from collections import defaultdict

# Simulate a manufacturing process with quality checks and resource tracking
def analyze_production_efficiency():
    raw_data = ['A', 'B', 'C', 'A', 'B', 'A', 'D', 'E', 'A', 'B']
    quality_flags = [True, False, True, True, False, True, True, False, True, True]
    
    # Count occurrences of each product type
    product_counter = defaultdict(int)
    for item in raw_data:
        product_counter[item] += 1
    
    # Misleading computation: not directly used in final result
    avg_length = sum(len(item) for item in raw_data) / len(raw_data)
    normalized_scores = [len(item) * 0.75 for item in raw_data]
    
    # Relevant data initialization
    total_runs = len(raw_data)
    passed_units = sum(1 for q in quality_flags if q)
    rejected_units = total_runs - passed_units
    
    # Simulate multi-phase processing
    phase_weights = {'setup': 0.1, 'process': 0.7, 'review': 0.2}
    cycle_time = 0
    for phase, weight in phase_weights.items():
        if phase == 'setup':
            cycle_time += 3 * weight
        elif phase == 'process':
            for i in range(passed_units):
                cycle_time += weight * (1 + (i % 3) * 0.1)
        else:
            temp_time = 0
            for q in quality_flags:
                if not q:
                    temp_time += 0.5
            cycle_time += temp_time * weight

    # Resource allocation simulation (some distraction here)
    resources = {'machines': 3, 'operators': 2, 'inspector_ratio': 0.5}
    resource_count = resources['machines'] + resources['operators']
    inspector_hours = resources['operators'] * resources['inspector_ratio'] * 8
    
    # Core output calculation
    base_output = sum(product_counter[p] for p in ['A', 'B'])
    bonus_output = product_counter['C'] * 0.5
    penalty_reduction = rejected_units * 0.3
    total_output = base_output + bonus_output - penalty_reduction
    
    # Key statement
    efficiency_ratio = total_output / (cycle_time * resource_count)
    
    # Print final result
    print(f"Result: {efficiency_ratio}")
    
    return efficiency_ratio

analyze_production_efficiency()