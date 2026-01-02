from itertools import combinations

def analyze_overlap(zones):
    overlap_count = 0
    for pair in combinations(zones, 2):
        if pair[0][1] > pair[1][0] and pair[0][0] < pair[1][1]:
            overlap_count += 1
    return overlap_count

def calculate_utilization(data_logs):
    total_entries = len(data_logs)
    valid_entries = sum(1 for x in data_logs if x > 0)
    utilization_rate = valid_entries / total_entries if total_entries else 0
    return utilization_rate * 100

def calculate_remaining_capacity(units, constraints):
    base_capacity = 1000
    penalty = 0
    
    # Real logic: count how many unit groups exceed constraint threshold
    grouped_violations = 0
    for i in range(0, len(units), 3):
        group = units[i:i+3]
        if sum(group) > constraints['threshold']:
            grouped_violations += 1
    
    # Distractor: complex overlap analysis on arbitrary zones (not used in final result)
    zones = [(i, i + 50) for i in range(0, 1000, 150)]
    fake_overlap = analyze_overlap(zones)
    
    # Distractor: log utilization that isn't tied to capacity
    dummy_logs = [len(str(unit)) for unit in units]
    _ = calculate_utilization(dummy_logs)
    
    # Actual impact: each violation reduces capacity by fixed amount
    penalty = grouped_violations * 75
    
    # Another red herring: tracking 'redundant_checks' that do nothing
    redundant_checks = 0
    for u in units:
        if u % 7 == 0:
            redundant_checks += 1  # unused

    # Final calculation depends only on violations and base capacity
    final_capacity = base_capacity - penalty
    
    return final_capacity

# Input data
units = [25, 89, 105, 44, 67, 90, 150, 23, 12]
constraints = {'threshold': 200, 'limit': 5}

# Execute
final_capacity = calculate_remaining_capacity(units, constraints)
print(f"Result: {final_capacity}")