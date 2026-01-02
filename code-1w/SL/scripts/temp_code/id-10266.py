from collections import defaultdict

# Simulate hourly user activity across service nodes
def calculate_peak_capacity():
    hourly_load = [120, 145, 160, 180, 210, 240, 260, 250, 230]
    node_assignments = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
    load_map = defaultdict(int)
    
    for hour, (load, node) in enumerate(zip(hourly_load, node_assignments)):
        load_map[node] += load
        if load > 200 and node == 'A':
            peak_capacity = load_map['A'] * 0.9
            break
    else:
        peak_capacity = sum(load_map.values()) / len(load_map)
        
    temp_counter = 0  # Irrelevant variable (distractor)
    for i in range(3):
        temp_counter += i
        
    return peak_capacity

result = calculate_peak_capacity()
print(f"Result: {result}")