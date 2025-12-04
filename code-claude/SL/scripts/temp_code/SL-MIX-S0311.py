import itertools

def calculate_volume(dimensions):
    # Calculate volume of a package
    length, width, height = dimensions
    return length * width * height

def calculate_density(weight, dimensions):
    # Calculate density (not used in final calculation)
    volume = calculate_volume(dimensions)
    return weight / volume if volume > 0 else 0

def best_warehouse_configuration(inventory, constraints):
    # Find optimal warehouse capacity based on package arrangements
    
    # Extract data
    packages = inventory['packages']
    shelf_count = inventory['shelves']
    temperature_zones = inventory['temperature_zones']  # Not directly used in calculation
    
    # Space constraints
    max_height = constraints['height']
    max_width = constraints['width']
    safety_margin = constraints['safety_margin']  # Not directly used
    
    # Calculate volumes and sort packages by efficiency
    package_data = []
    for pkg in packages:
        volume = calculate_volume(pkg['dimensions'])
        weight = pkg['weight']
        priority = pkg.get('priority', 1)  # Default priority is 1
        
        # Calculate density (distractor)
        density = calculate_density(weight, pkg['dimensions'])
        
        # Calculate package efficiency score
        efficiency = volume * priority / (weight + 1)
        
        package_data.append({
            'id': pkg['id'],
            'volume': volume,
            'efficiency': efficiency
        })
    
    # Sort packages by efficiency (highest first)
    sorted_packages = sorted(package_data, key=lambda x: x['efficiency'], reverse=True)
    
    # Calculate theoretical maximum capacity
    total_volume = sum(p['volume'] for p in sorted_packages)
    
    # Apply shelf constraints
    shelf_capacity = max_height * max_width * shelf_count
    
    # Simulate different arrangements using combinations
    arrangement_options = list(itertools.combinations(range(len(sorted_packages)), min(3, len(sorted_packages))))
    
    # This is a distractor calculation
    arrangement_count = len(arrangement_options)
    arrangement_factor = min(arrangement_count / 10, 1.0)
    
    # Calculate optimal capacity
    base_capacity = min(total_volume, shelf_capacity)
    utilization_factor = 0.85  # Realistic utilization factor
    optimal_capacity = int(base_capacity * utilization_factor)
    
    # Print the result
    print(f"Result: {optimal_capacity}")
    
    return optimal_capacity

# Test data
inventory_data = {
    'packages': [
        {'id': 'A1', 'dimensions': (2, 3, 4), 'weight': 5, 'priority': 2},
        {'id': 'B2', 'dimensions': (1, 2, 2), 'weight': 3, 'priority': 1},
        {'id': 'C3', 'dimensions': (3, 4, 5), 'weight': 8, 'priority': 3},
        {'id': 'D4', 'dimensions': (2, 2, 2), 'weight': 4, 'priority': 2}
    ],
    'shelves': 5,
    'temperature_zones': ['ambient', 'refrigerated', 'frozen']
}

space_constraints = {
    'height': 10,
    'width': 12,
    'safety_margin': 0.1  # 10% safety margin
}

optimal_capacity = best_warehouse_configuration(inventory_data, space_constraints)