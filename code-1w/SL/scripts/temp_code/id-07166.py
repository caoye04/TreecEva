def calculate_density_ratio(volume, mass):
    return mass / (volume + 1e-5)


def analyze_compatibility(items, max_weight):
    compatible_count = 0
    for item in items:
        weight = item.get('weight', 0)
        if weight <= max_weight:
            compatible_count += 1
    return compatible_count


def calculate_remaining_capacity(matrix, limit):
    total_used = 0
    temp_buffer = []
    
    for row in matrix:
        row_sum = sum([x for x in row if x > 0])
        adjustment_factor = 1.0 if row_sum < limit else 0.9
        total_used += row_sum * adjustment_factor
        
        # Distractor: irrelevant transformation
        inverted = [limit - val for val in row]
        temp_buffer.append(inverted)
    
    # Real calculation
    base_capacity = 500
    degradation = 0.05 * len(matrix)
    effective_capacity = base_capacity * (1 - degradation)
    
    # Irrelevant string processing (distractor)
    status_msg = "System at {}% capacity".format(round((total_used / effective_capacity) * 100))
    status_lower = status_msg.lower()
    tokens = status_lower.split(' ')
    joined = '-'.join(tokens)
    
    # Final logic
    remaining = effective_capacity - total_used
    if remaining < 0:
        remaining = 0
        
    return int(remaining)

# Simulate sensor readings from storage units
storage_matrix = [
    [45, 30, 25, -5],
    [60, 15, 0, 40],
    [35, 50, 20, 10]
]

threshold = 100

# Unused variables and irrelevant computations (distractors)
raw_data = "TEMP:72.5,HUM:45,VOL:88"
data_parts = raw_data.split(',')
humidity_str = data_parts[1]
humidity_val = int(humidity_str.split(':')[1])

item_list = [
    {'name': 'widget_a', 'weight': 12},
    {'name': 'widget_b', 'weight': 8},
    {'name': 'widget_c', 'weight': 15}
]

max_allowed_weight = 10
compatibility_score = analyze_compatibility(item_list, max_allowed_weight)

# Core density analysis (semi-relevant but not used in final result)
density = calculate_density_ratio(125, 98)
safety_margin = 1.2 if density < 0.8 else 1.0

# Critical execution point
final_capacity = calculate_remaining_capacity(storage_matrix, threshold)

# Print result as required
print(f"Result: {final_capacity}")