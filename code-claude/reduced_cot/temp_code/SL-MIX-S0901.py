def calculate_treasure(treasure_map, path):
    # Calculate the value of treasure based on map coordinates and path
    value = sum([treasure_map[i] for i in path if i < len(treasure_map)])
    return value

def decode_ancient_map(encrypted_data):
    # This function decodes the ancient treasure map data
    result = []
    for code in encrypted_data:
        # Apply special decoding algorithm
        decoded = ((code ^ 0xAB) + 7) % 100
        result.append(decoded)
    return result

def find_optimal_path(map_data, start_point=0):
    # Find the optimal path through the treasure map
    path = [start_point]
    visited = set([start_point])
    
    # Calculate prime factors - used for navigation
    def get_prime_factors(n):
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
        return factors
    
    # Navigation logic
    current = start_point
    for _ in range(4):  # We can only move 4 times due to oxygen constraints
        if current % 2 == 0:
            next_pos = (current * 3) % len(map_data)
        else:
            next_pos = (current // 2) if current > 0 else 0
        
        # Check for underwater caves (dead end)
        if next_pos in visited:
            # Use alternative navigation
            primes = get_prime_factors(current + 10)
            if primes:
                next_pos = (current + primes[0]) % len(map_data)
        
        path.append(next_pos)
        visited.add(next_pos)
        current = next_pos
    
    return path

# Encrypted ancient treasure map data
encrypted_map = [123, 87, 142, 109, 165, 178, 203, 111, 89, 76]

# Decoding the map
decoded_map = decode_ancient_map(encrypted_map)

# Calculate potential routes for comparison
historical_routes = [
    [2, 5, 1, 8, 3],  # Captain Blackbeard's route
    [0, 3, 6, 9, 4],   # Admiral Nelson's path
    [1, 4, 7, 2, 8]    # Pirate Queen Anne's strategy
]

# Evaluate historical routes
route_values = []
for route in historical_routes:
    # Calculate hypothetical oxygen consumption
    oxygen = sum([i % 3 + 1 for i in route])
    
    # Calculate potential treasure value
    potential_value = calculate_treasure(decoded_map, route)
    
    # Adjust for oxygen risk
    adjusted_value = potential_value - (oxygen * 2)
    route_values.append(adjusted_value)

# Find our optimal path
optimal_path = find_optimal_path(decoded_map)

# Calculate final treasure value
treasure_value = calculate_treasure(decoded_map, optimal_path)

# Check if we beat historical records
if treasure_value > max(route_values):
    print(f"New record! Beating historical best by {treasure_value - max(route_values)}")
else:
    print(f"Historical routes were better by {max(route_values) - treasure_value}")

print(f"Result: {treasure_value}")