def parse_geodata(raw_input):
    coordinates = []
    temp_buffer = []
    irrelevant_sum = 0
    
    # Distractor: processing that doesn't affect final result
    for i, segment in enumerate(raw_input.split(';')):
        if len(segment) > 0:
            parts = segment.strip().split(',')
            if len(parts) == 2:
                try:
                    x = int(parts[0])
                    y = int(parts[1])
                    coordinates.append((x, y))
                    temp_buffer.append(x * y)  # Irrelevant computation
                except ValueError:
                    pass
    
    # Misleading intermediate calculation
    intermediate_value = sum(temp_buffer) if temp_buffer else 0
    irrelevant_sum = intermediate_value * 2  # Dead code path
    
    return coordinates

def filter_quadrant(points):
    filtered = []
    count_unused = 0  # Misleading counter
    
    for x, y in points:
        # Complex conditional with dead branches
        if x > 0 and y > 0:
            filtered.append((x, y))
        elif x < 0 and y < 0:
            count_unused += 1  # This path is never taken in our data
        else:
            # Distractor: complex but unused computation
            unused_metric = abs(x) ^ abs(y)
    
    return filtered

def process_coordinates(data_points):
    from itertools import chain
    
    # Slicing operations with complex indices
    if len(data_points) >= 4:
        sliced_data = data_points[1:-1:2] + data_points[::3]
    else:
        sliced_data = data_points
    
    # Irrelevant string manipulation
    debug_string = "Processing " + str(len(sliced_data)) + " points"
    
    # Core computation with bitwise operations
    result = 0
    for point in sliced_data:
        x, y = point
        # Key calculation: XOR with modular arithmetic
        result ^= (abs(x) % 16) | ((abs(y) % 16) << 4)
    
    # Final adjustment with dead code path
    if result > 1000:
        result = result // 2  # Never executed in our case
    
    return result

# Main execution
raw_coordinates = "5,12; 8,15; 3,7; 11,9; 6,4; 14,2"

# Parse and filter data
parsed_data = parse_geodata(raw_coordinates)
filtered_data = filter_quadrant(parsed_data)

# Distractor: unused computation
unused_calculation = sum(x + y for x, y in parsed_data) * 3

# Key execution point
final_output = process_coordinates(filtered_data)

print(f"Target result: {final_output}")