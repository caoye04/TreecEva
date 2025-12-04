import itertools

def transform_point(x, y, mask):
    # Distractor: unused transformation matrix
    transformation_matrix = [[2, -1], [1, 3]]
    
    # Main transformation logic
    x_rotated = (x ^ mask) + (y & 0xFF)
    y_rotated = (y | mask) - (x % 16)
    
    # Distractor: misleading intermediate calculation
    temp_sum = sum([i**2 for i in range(abs(x_rotated % 10))])
    
    # Actual coordinate calculation
    result = (x_rotated * 3) - (y_rotated * 2) + (mask >> 4)
    
    # Dead code path that never executes
    if result > 1000000:
        result = -result  # Never reached with given inputs
    
    return result

# Initial coordinates and setup
initial_x = 42
initial_y = 27
rotation_key = 0b101101

# Distractor: irrelevant coordinate processing
coordinate_pairs = list(itertools.product([initial_x, initial_y], repeat=2))
filtered_pairs = [pair for pair in coordinate_pairs if pair[0] != pair[1]]

# Process coordinates with bitwise operations
x_processed = (initial_x << 2) | 0b11
y_processed = (initial_y >> 1) ^ 0b10101

# Distractor: misleading rotation value
rotation_mask = rotation_key & 0b111111
rotation_dummy = rotation_key | 0b111000  # Never used

# Dead code: unused coordinate transformation
def unused_transform(a, b):
    return a * b + (a ^ b)

# Critical execution point
final_coordinate = transform_point(x_processed, y_processed, rotation_mask)

print(f"Result: {final_coordinate}")